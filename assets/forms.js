/* Sends the appointment, tele-consult and referral forms to /api/enquiry
   (served by serve.py) and shows the result under the button. */
(function () {
  "use strict";

  var MAX_FILES = 10;
  var MAX_BYTES = 10 * 1024 * 1024;

  function setStatus(el, text, kind) {
    el.textContent = text;
    el.className = "form-status" + (kind ? " " + kind : "");
  }

  function checkFiles(form) {
    var input = form.querySelector('input[type="file"]');
    if (!input || !input.files) return "";
    if (input.files.length > MAX_FILES) return "Please attach up to " + MAX_FILES + " files.";
    var total = 0;
    for (var i = 0; i < input.files.length; i++) total += input.files[i].size;
    if (total > MAX_BYTES) return "The attachments come to more than 10 MB. Please send fewer or smaller files.";
    return "";
  }

  function onSubmit(e) {
    var form = e.currentTarget;
    if (!window.fetch || !window.FormData) return; // let the browser post the form normally
    e.preventDefault();

    var status = form.querySelector(".form-status");
    var button = form.querySelector('button[type="submit"]');

    var fileError = checkFiles(form);
    if (fileError) { setStatus(status, fileError, "err"); return; }

    button.disabled = true;
    setStatus(status, "Sending…", "");

    fetch(form.getAttribute("action"), {
      method: "POST",
      body: new FormData(form),
      headers: { "Accept": "application/json" }
    })
      .then(function (res) {
        return res.json().catch(function () { return { ok: false }; }).then(function (data) {
          return { okStatus: res.ok, data: data };
        });
      })
      .then(function (r) {
        if (r.okStatus && r.data.ok) {
          form.reset();
          setStatus(status, r.data.message || "Thank you. Your request has been sent and we will get back to you soon.", "ok");
        } else {
          setStatus(status, (r.data && r.data.error) ||
            "Sorry, your request could not be sent. Please try again, or email us at hello@thedermatology.vet.", "err");
        }
      })
      .catch(function () {
        setStatus(status, "Sorry, your request could not be sent. Please check your connection and try again, or email us at hello@thedermatology.vet.", "err");
      })
      .then(function () { button.disabled = false; });
  }

  var forms = document.querySelectorAll("form[data-enquiry]");
  for (var i = 0; i < forms.length; i++) forms[i].addEventListener("submit", onSubmit);
})();
