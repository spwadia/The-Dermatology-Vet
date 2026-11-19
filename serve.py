#!/usr/bin/env python3
"""
The Dermatology Vet: web server (Python 3.9+, standard library only).

  * Serves the static site: the .html pages and assets/ only. Source files,
    .env and anything else in the folder are never served.
  * POST /api/enquiry receives the three website forms (appointment,
    tele-consult, referral) and emails them through SendGrid.

Run:   python3 serve.py [port]
Config: environment variables, or a .env file next to this script
        (copy .env.example to .env). See README, "Forms and email".
"""
import base64
import html
import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from email import policy
from email.parser import BytesParser
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, unquote, urlsplit

ROOT = os.path.dirname(os.path.abspath(__file__))


# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------
def load_env_file(path):
    """Minimal .env reader: KEY=value lines; real environment variables win."""
    if not os.path.isfile(path):
        return
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            key, value = key.strip(), value.strip().strip('"').strip("'")
            os.environ.setdefault(key, value)


load_env_file(os.path.join(ROOT, ".env"))


def env(key, default=""):
    return os.environ.get(key, default).strip()


def recipients(key):
    return [a.strip() for a in env(key).split(",") if a.strip()]


SENDGRID_API_KEY = env("SENDGRID_API_KEY")
MAIL_FROM = env("MAIL_FROM")
MAIL_FROM_NAME = env("MAIL_FROM_NAME", "The Dermatology Vet Website")
TRUST_PROXY = env("TRUST_PROXY") in ("1", "true", "yes")

MAX_BODY = 14 * 1024 * 1024          # whole request, including attachments
MAX_FILES = 10
MAX_FILE_BYTES = 10 * 1024 * 1024    # attachments in total
RATE_LIMIT = (5, 600)                # 5 sent forms per IP per 10 minutes (failed attempts don't count)

IST = timezone(timedelta(hours=5, minutes=30))
EMAIL_RE = re.compile(r"^[^@\s<>,;\"]+@[^@\s<>,;\"]+\.[A-Za-z]{2,}$")
PHONE_RE = re.compile(r"^[0-9+()\-. ]{7,20}$")

ATTACHMENT_TYPES = {
    ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp",
    ".heic": "image/heic", ".heif": "image/heif", ".pdf": "application/pdf",
}

# Each form: who receives it, its fields in display order, and the email subject.
# (field name, label, required, max length)
FORMS = {
    "appointment": {
        "title": "Appointment request",
        "source": "the Contact page (Request an appointment)",
        "to_env": "MAIL_TO_APPOINTMENT",
        "name_field": "name",
        "fields": [
            ("name", "Name", True, 120),
            ("phone", "Phone", True, 20),
            ("email", "Email", True, 200),
            ("where", "How they would like to be seen", False, 80),
            ("species", "Species", False, 40),
            ("vet", "Their own vet's practice", False, 200),
            ("problem", "The problem and how long it has been going on", True, 5000),
        ],
        "subject": lambda d: "Appointment request: {} ({}, {})".format(
            d["name"], d.get("species") or "species not given", d.get("where") or "clinic"),
    },
    "teleconsult": {
        "title": "Tele-consult request",
        "source": "the Services page (Request a Tele-Consult)",
        "to_env": "MAIL_TO_TELECONSULT",
        "name_field": "name",
        "fields": [
            ("name", "Name", True, 120),
            ("phone", "Phone", True, 20),
            ("email", "Email", True, 200),
            ("city", "City", False, 80),
            ("species", "Species", False, 40),
            ("who", "They are", False, 60),
            ("problem", "The problem and how long it has been going on", True, 5000),
            ("treatment", "What has already been tried", False, 5000),
        ],
        "subject": lambda d: "Tele-consult request: {} ({}{})".format(
            d["name"], d.get("species") or "species not given",
            ", " + d["city"] if d.get("city") else ""),
    },
    "referral": {
        "title": "Case referral (TDV Connect)",
        "source": "TDV Connect (Send a case)",
        "to_env": "MAIL_TO_REFERRAL",
        "name_field": "vet",
        "files": True,
        "fields": [
            ("vet", "Referring vet", True, 120),
            ("practice", "Practice and city", True, 200),
            ("email", "Email", True, 200),
            ("phone", "Phone", False, 20),
            ("type", "What they need", False, 80),
            ("species", "Species", False, 40),
            ("case", "The case", True, 8000),
        ],
        "subject": lambda d: "Case referral: {}, {} ({})".format(
            d["vet"], d["practice"], d.get("species") or "species not given"),
    },
}

THANKS = {
    "appointment": "Thank you. Your appointment request has been sent. We will get back to you soon.",
    "teleconsult": "Thank you. Your tele-consult request has been sent. We will get back to you soon.",
    "referral": "Thank you. Your case has been sent to our dermatology team.",
}


# --------------------------------------------------------------------------
# Request parsing and validation
# --------------------------------------------------------------------------
class FormError(Exception):
    def __init__(self, message, status=400):
        super().__init__(message)
        self.status = status


def one_line(value):
    return re.sub(r"[\r\n\t]+", " ", value).strip()


def parse_body(content_type, body):
    """Return (fields: dict[str, str], files: list[(filename, mime, bytes)])."""
    fields, files = {}, []
    ctype = (content_type or "").lower()
    if ctype.startswith("multipart/form-data"):
        msg = BytesParser(policy=policy.HTTP).parsebytes(
            b"Content-Type: " + content_type.encode("latin-1") + b"\r\n\r\n" + body)
        if not msg.is_multipart():
            raise FormError("The form could not be read.")
        for part in msg.iter_parts():
            name = part.get_param("name", header="content-disposition")
            if not name:
                continue
            filename = part.get_filename()
            payload = part.get_payload(decode=True) or b""
            if filename is not None:
                if payload:
                    files.append((filename, part.get_content_type(), payload))
            else:
                fields[name] = payload.decode("utf-8", "replace")
    elif ctype.startswith("application/x-www-form-urlencoded"):
        for key, values in parse_qs(body.decode("utf-8", "replace"), keep_blank_values=True).items():
            fields[key] = values[0]
    else:
        raise FormError("Unsupported form encoding.", 415)
    return fields, files


def validate(form_id, fields, files):
    spec = FORMS.get(form_id)
    if not spec:
        raise FormError("Unknown form.")
    data, missing = {}, []
    for key, label, required, max_len in spec["fields"]:
        value = (fields.get(key) or "").strip()
        if len(value) > max_len:
            raise FormError("{} is too long.".format(label))
        if required and not value:
            missing.append(label.lower())
        data[key] = value
    if missing:
        raise FormError("Please fill in: {}.".format(", ".join(missing)))
    if not EMAIL_RE.match(data["email"]):
        raise FormError("Please enter a valid email address.")
    if data.get("phone") and not PHONE_RE.match(data["phone"]):
        raise FormError("Please enter a valid phone number.")

    attachments = []
    if files and not spec.get("files"):
        raise FormError("This form does not take attachments.")
    if len(files) > MAX_FILES:
        raise FormError("Please attach up to {} files.".format(MAX_FILES))
    total = 0
    for filename, _mime, content in files:
        clean = re.sub(r"[^\w.\- ()]+", "_", os.path.basename(filename.replace("\\", "/")))[:120] or "file"
        ext = os.path.splitext(clean)[1].lower()
        if ext not in ATTACHMENT_TYPES:
            raise FormError("{}: only JPG, PNG, HEIC, WebP or PDF files can be attached.".format(clean))
        total += len(content)
        attachments.append((clean, ATTACHMENT_TYPES[ext], content))
    if total > MAX_FILE_BYTES:
        raise FormError("The attachments come to more than 10 MB. Please send fewer or smaller files.")
    return spec, data, attachments


# --------------------------------------------------------------------------
# Email
# --------------------------------------------------------------------------
def build_email(form_id, spec, data, attachments):
    stamp = datetime.now(IST).strftime("%d %b %Y, %H:%M IST")
    rows_text, rows_html = [], []
    for key, label, _req, _max in spec["fields"]:
        value = data.get(key) or "-"
        rows_text.append("{}:\n{}\n".format(label, value))
        rows_html.append(
            '<tr><th align="left" valign="top" style="padding:6px 14px 6px 0;color:#555;'
            'font-weight:600;white-space:nowrap">{}</th><td style="padding:6px 0">{}</td></tr>'.format(
                html.escape(label), html.escape(value).replace("\n", "<br>")))
    if attachments:
        names = ", ".join(a[0] for a in attachments)
        rows_text.append("Attachments:\n{}\n".format(names))
        rows_html.append('<tr><th align="left" style="padding:6px 14px 6px 0;color:#555">Attachments</th>'
                         "<td>{}</td></tr>".format(html.escape(names)))

    footer = "Sent from {} on thedermatology.vet, {}. Reply to this email to answer {} directly.".format(
        spec["source"], stamp, data[spec["name_field"]])
    text = "{}\n\n{}\n--\n{}\n".format(spec["title"], "\n".join(rows_text), footer)
    body_html = (
        '<div style="font-family:Arial,sans-serif;font-size:15px;color:#141414">'
        '<h2 style="font-size:18px;margin:0 0 14px">{}</h2>'
        '<table cellspacing="0" cellpadding="0" style="border-collapse:collapse">{}</table>'
        '<p style="color:#777;font-size:13px;margin-top:22px">{}</p></div>').format(
            html.escape(spec["title"]), "".join(rows_html), html.escape(footer))

    message = {
        "personalizations": [{"to": [{"email": a} for a in recipients(spec["to_env"])]}],
        "from": {"email": MAIL_FROM, "name": MAIL_FROM_NAME},
        "reply_to": {"email": data["email"], "name": one_line(data[spec["name_field"]])},
        "subject": "[TDV website] " + one_line(spec["subject"](data))[:180],
        "content": [{"type": "text/plain", "value": text}, {"type": "text/html", "value": body_html}],
        "categories": ["tdv-website", form_id],
    }
    if attachments:
        message["attachments"] = [
            {"content": base64.b64encode(content).decode("ascii"), "filename": name,
             "type": mime, "disposition": "attachment"}
            for name, mime, content in attachments]
    return message


def config_problem(form_id):
    if not recipients(FORMS[form_id]["to_env"]):
        return "{} is not set".format(FORMS[form_id]["to_env"])
    if not SENDGRID_API_KEY:
        return "SENDGRID_API_KEY is not set"
    if not MAIL_FROM:
        return "MAIL_FROM is not set"
    return ""


def send_email(message):
    req = urllib.request.Request(
        "https://api.sendgrid.com/v3/mail/send",
        data=json.dumps(message).encode("utf-8"),
        headers={"Authorization": "Bearer " + SENDGRID_API_KEY, "Content-Type": "application/json"},
        method="POST")
    try:
        with urllib.request.urlopen(req, timeout=25) as res:
            if res.status != 202:
                raise RuntimeError("SendGrid returned HTTP {}".format(res.status))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:600]
        raise RuntimeError("SendGrid returned HTTP {}: {}".format(e.code, detail))


# --------------------------------------------------------------------------
# Rate limiting (in memory, per client IP)
# --------------------------------------------------------------------------
_hits, _hits_lock = {}, threading.Lock()


def allow(ip):
    limit, window = RATE_LIMIT
    now = time.time()
    with _hits_lock:
        recent = [t for t in _hits.get(ip, []) if now - t < window]
        if recent:
            _hits[ip] = recent
        else:
            _hits.pop(ip, None)
        return len(recent) < limit


def record(ip):
    with _hits_lock:
        _hits.setdefault(ip, []).append(time.time())


# --------------------------------------------------------------------------
# HTTP handler
# --------------------------------------------------------------------------
STATIC_OK = re.compile(r"^/(?:[a-z0-9-]+\.html|robots\.txt|sitemap\.xml|assets/(?:[A-Za-z0-9_-][A-Za-z0-9_.-]*/)*[A-Za-z0-9_-][A-Za-z0-9_.-]*)$")


class Handler(SimpleHTTPRequestHandler):
    server_version = "TDV"
    sys_version = ""

    def end_headers(self):
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.send_header("X-Frame-Options", "SAMEORIGIN")
        super().end_headers()

    # ---- static files: allow-list only ----
    def _static_allowed(self):
        path = unquote(urlsplit(self.path).path)
        if path == "/":
            return True
        return bool(STATIC_OK.match(path)) and ".." not in path

    def do_GET(self):
        if not self._static_allowed():
            self.send_error(404)
            return
        super().do_GET()

    def do_HEAD(self):
        if not self._static_allowed():
            self.send_error(404)
            return
        super().do_HEAD()

    # ---- forms ----
    def client_ip(self):
        if TRUST_PROXY:
            forwarded = self.headers.get("X-Forwarded-For", "")
            if forwarded:
                return forwarded.split(",")[0].strip()
        return self.client_address[0]

    def wants_json(self):
        return "application/json" in (self.headers.get("Accept") or "")

    def reply(self, status, ok, text):
        if self.wants_json():
            body = json.dumps({"ok": ok, ("message" if ok else "error"): text}).encode("utf-8")
            ctype = "application/json; charset=utf-8"
        else:  # browser without JavaScript: a plain page with a way back
            body = ("<!DOCTYPE html><meta charset='utf-8'><meta name='viewport' content='width=device-width'>"
                    "<title>The Dermatology Vet</title><body style='font-family:Arial,sans-serif;max-width:640px;"
                    "margin:60px auto;padding:0 20px'><p>{}</p><p><a href='javascript:history.back()'>Go back</a>"
                    " &middot; <a href='/'>Home</a></p></body>").format(html.escape(text)).encode("utf-8")
            ctype = "text/html; charset=utf-8"
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if urlsplit(self.path).path != "/api/enquiry":
            self.send_error(404)
            return
        try:
            length = int(self.headers.get("Content-Length") or 0)
        except ValueError:
            length = 0
        if length <= 0:
            self.reply(411, False, "The form arrived empty. Please try again.")
            return
        if length > MAX_BODY:
            self.close_connection = True
            self.reply(413, False, "The attachments are too large. Please keep them under 10 MB in total.")
            return
        body = self.rfile.read(length)

        form_id = "?"
        try:
            fields, files = parse_body(self.headers.get("Content-Type"), body)
            form_id = (fields.get("form") or "").strip()
            if fields.get("website"):  # honeypot filled in: a bot. Pretend it worked.
                self.log_message("honeypot hit on %s form", form_id or "?")
                self.reply(200, True, THANKS.get(form_id, "Thank you."))
                return
            if not allow(self.client_ip()):
                raise FormError("Too many requests from this connection. Please wait a few minutes "
                                "and try again, or email us at hello@thedermatology.vet.", 429)
            spec, data, attachments = validate(form_id, fields, files)
            problem = config_problem(form_id)
            if problem:
                self.log_error("email not configured: %s", problem)
                raise FormError("Sorry, the form is not available right now. Please email us at "
                                "hello@thedermatology.vet.", 503)
            send_email(build_email(form_id, spec, data, attachments))
            record(self.client_ip())
        except FormError as e:
            self.reply(e.status, False, str(e))
            return
        except Exception as e:  # SendGrid or network failure
            self.log_error("sending %s form failed: %s", form_id, e)
            self.reply(502, False, "Sorry, your request could not be sent. Please try again, or email "
                                   "us at hello@thedermatology.vet.")
            return
        self.log_message("%s form sent (%d attachment(s))", form_id, len(attachments))
        self.reply(200, True, THANKS[form_id])


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else int(env("PORT", "4173"))
    host = env("HOST", "127.0.0.1")
    httpd = ThreadingHTTPServer((host, port), partial(Handler, directory=ROOT))
    mode = "sending via SendGrid" if SENDGRID_API_KEY else "SENDGRID_API_KEY not set: forms will fail"
    print("Serving %s on http://%s:%d  [%s]" % (ROOT, host, port, mode), flush=True)
    for form_id, spec in FORMS.items():
        print("  %-12s -> %s" % (form_id, ", ".join(recipients(spec["to_env"])) or "(not set)"), flush=True)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
