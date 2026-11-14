#!/usr/bin/env python3
"""
The Dermatology Vet — static site generator.

Visual treatment follows the template shared by the sister sites in the VHI
group (theeye.vet, thecancer.vet, theexotics.vet): full-width white header with
a home icon and square social icons, a full-width media hero, centred Nunito
headings, grey #f5f5f5 cards with black "Read More" buttons, a "For Appointment
Contact" box, clinic columns in the footer, and the same floating tele-consult
pill and round WhatsApp / call / YouTube buttons.

Run:  python3 build.py
Output: plain static .html files in this folder. Edit the content in pages.py
and re-run, or edit the generated HTML directly if you prefer.
"""
import os
import pages as P

OUT = os.path.dirname(os.path.abspath(__file__))
CSS_VERSION = "5"  # bump when assets/styles.css changes, so browsers fetch the new file

# --------------------------------------------------------------------------
NAV = [
    ("Home", "index.html"),
    ("Services", "services.html"),
    ("Team", "team.html"),
    ("Clinic", "clinic.html"),
    ("TDV Connect", "tdv-connect.html"),
    ("Careers", "careers.html"),
    ("Contact", "contact.html"),
]

ICON = {
"wa": '<svg viewBox="0 0 24 24"><path d="M.06 24l1.7-6.2A11.9 11.9 0 1 1 12 24a11.9 11.9 0 0 1-5.8-1.5L.06 24zM6.6 20.2l.36.2a9.9 9.9 0 1 0-3.4-3.4l.23.37-1 3.63 3.8-.8zm11.4-5.1c-.15-.25-.55-.4-1.15-.7s-1.4-.7-1.6-.78-.36-.12-.5.13-.6.77-.73.93-.27.18-.5.06a8.1 8.1 0 0 1-2.4-1.48 9 9 0 0 1-1.65-2.06c-.17-.3 0-.45.13-.58s.25-.3.37-.45a1.7 1.7 0 0 0 .25-.42.46.46 0 0 0 0-.44c-.07-.12-.55-1.33-.76-1.82s-.4-.42-.55-.43h-.47a.9.9 0 0 0-.65.3 2.75 2.75 0 0 0-.86 2.05A4.77 4.77 0 0 0 8 11.1a10.9 10.9 0 0 0 4.2 3.7c2.46 1.1 2.46.74 2.9.7a2.5 2.5 0 0 0 1.66-1.17 2 2 0 0 0 .15-1.17z"/></svg>',
"tel": '<svg viewBox="0 0 24 24"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.24 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.4 11.4 0 0 0 .57 3.6 1 1 0 0 1-.25 1z"/></svg>',
"mail": '<svg viewBox="0 0 24 24"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4-8 5-8-5V6l8 5 8-5z"/></svg>',
"video": '<svg viewBox="0 0 24 24"><path d="M17 10.5V7a1 1 0 0 0-1-1H4a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-3.5l4 4v-11z"/></svg>',
"ig": '<svg viewBox="0 0 24 24"><path d="M12 2.2c3.2 0 3.6 0 4.9.07 3.3.15 4.8 1.7 5 5 .06 1.3.07 1.7.07 4.9s0 3.6-.07 4.9c-.15 3.3-1.7 4.8-5 5-1.3.06-1.7.07-4.9.07s-3.6 0-4.9-.07c-3.3-.15-4.8-1.7-5-5C2.03 15.6 2 15.2 2 12s0-3.6.07-4.9c.15-3.3 1.7-4.8 5-5C8.4 2.2 8.8 2.2 12 2.2zm0 3.1a6.7 6.7 0 1 0 0 13.4 6.7 6.7 0 0 0 0-13.4zm0 11a4.3 4.3 0 1 1 0-8.6 4.3 4.3 0 0 1 0 8.6zm6.9-11.2a1.56 1.56 0 1 1-3.1 0 1.56 1.56 0 0 1 3.1 0z"/></svg>',
"fb": '<svg viewBox="0 0 24 24"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.75-1.6 1.5V12h2.8l-.45 2.9h-2.35v7A10 10 0 0 0 22 12z"/></svg>',
"li": '<svg viewBox="0 0 24 24"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9h4v12H3zM9 9h3.8v1.7h.05a4.2 4.2 0 0 1 3.75-2c4 0 4.75 2.6 4.75 6.1V21h-4v-5.5c0-1.3 0-3-1.85-3s-2.1 1.44-2.1 2.9V21H9z"/></svg>',
"yt": '<svg viewBox="0 0 24 24"><path d="M23 12s0-3.4-.44-5a2.8 2.8 0 0 0-2-2C18.8 4.5 12 4.5 12 4.5s-6.8 0-8.6.5a2.8 2.8 0 0 0-2 2C1 8.6 1 12 1 12s0 3.4.44 5a2.8 2.8 0 0 0 2 2c1.8.5 8.6.5 8.6.5s6.8 0 8.6-.5a2.8 2.8 0 0 0 2-2c.4-1.6.4-5 .4-5zM9.75 15.25v-6.5L15.5 12z"/></svg>',
"derm": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5M8.5 10.5h.01M11.5 8.5h.01M13.5 12h.01M9.5 13.5h.01"/></svg>',
"ear": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M6 10a6 6 0 1 1 12 0c0 3-2 4-3.2 5.2S13 17.5 13 19a3 3 0 0 1-6 0"/><path d="M10 10a2 2 0 1 1 4 0c0 1.2-1 1.6-1.6 2.3"/></svg>',
"flask": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M9 3v6.2L4.2 18A2 2 0 0 0 6 21h12a2 2 0 0 0 1.8-3L15 9.2V3M8 3h8M7.5 14h9"/></svg>',
"paw": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="7" cy="8" r="2"/><circle cx="12" cy="6" r="2"/><circle cx="17" cy="8" r="2"/><circle cx="19" cy="13" r="1.8"/><path d="M12 11c-2.5 0-5 2-5 4.6 0 2 1.5 3.4 3.4 3.4h3.2c1.9 0 3.4-1.4 3.4-3.4C17 13 14.5 11 12 11z" stroke-linejoin="round"/></svg>',
"horse": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20c0-4 2-6 5-7l2.5-1 1-3.5L15 5l2-2 2 3-1.5 2.5.5 4c0 3-1.5 5-4 6"/><path d="M8.5 8.5h.01"/></svg>',
"bird": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M16 7a3 3 0 1 0-3-3v2.5A9 9 0 0 1 4 15.5 9 9 0 0 0 19 9V7z"/><path d="M14.5 4.5h.01M19 9h2"/></svg>',
"home": '<svg viewBox="0 0 24 24"><path d="M12 3.2 1.8 12h3v9h5.7v-6h3v6h5.7v-9h3z"/></svg>',
"arrow": '<svg viewBox="0 0 24 24"><path d="M13.3 4.3a1 1 0 0 1 1.4 0l7 7a1 1 0 0 1 0 1.4l-7 7a1 1 0 1 1-1.4-1.4l5.3-5.3H3a1 1 0 1 1 0-2h15.6l-5.3-5.3a1 1 0 0 1 0-1.4z"/></svg>',
"headset": '<svg viewBox="0 0 24 24"><path d="M12 2a9 9 0 0 0-9 9v6a3 3 0 0 0 3 3h2.5v-8H5v-1a7 7 0 0 1 14 0v1h-3.5v8H19v.5a1.5 1.5 0 0 1-1.5 1.5H13v2h4.5a3.5 3.5 0 0 0 3.5-3.5V11a9 9 0 0 0-9-9z"/></svg>',
"pin": '<svg viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 5.3 7 13 7 13s7-7.7 7-13a7 7 0 0 0-7-7zm0 9.6A2.6 2.6 0 1 1 12 6.4a2.6 2.6 0 0 1 0 5.2z"/></svg>',
"clock": '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm1 10.4 3.6 2.2-1 1.7L11 13.4V6.5h2z"/></svg>',
"up": '<svg viewBox="0 0 24 24"><path d="M12 7.6 3.7 15.9l1.8 1.8L12 11.2l6.5 6.5 1.8-1.8z"/></svg>',
"user": '<svg viewBox="0 0 24 24" fill="none" stroke="#67768e" stroke-width="1.5"><circle cx="12" cy="8.5" r="4"/><path d="M4.5 20.5a7.5 7.5 0 0 1 15 0" stroke-linecap="round"/></svg>',
"img": '<svg viewBox="0 0 24 24" fill="none" stroke="#67768e" stroke-width="1.5"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="8.5" cy="9.5" r="1.6"/><path d="m3.5 17.5 5-4.5 4 3.4 3-2.4 5 4" stroke-linecap="round" stroke-linejoin="round"/></svg>',
}

CONTACT = {
    "phone_display": "+91 XXXXX XXXXX",
    "phone_href": "+91XXXXXXXXXX",
    "wa_href": "https://wa.me/91XXXXXXXXXX",
    "email": "hello@thedermatology.vet",
    "referrals": "refer@thedermatology.vet",
    "careers": "careers@thedermatology.vet",
}


def head(title, desc, canonical):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://thedermatology.vet/{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="The Dermatology Vet">
<link rel="icon" href="assets/logo/favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="assets/logo/favicon-192.png" sizes="192x192" type="image/png">
<link rel="apple-touch-icon" href="assets/logo/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,400;0,600;0,700;0,800;0,900;1,400&family=Poppins:wght@600&family=Montserrat:wght@800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css?v={CSS_VERSION}">
</head>
<body>"""


def header(active):
    home_cls = "nav-home active" if active == "index.html" else "nav-home"
    parts = ['<a class="%s" href="index.html" aria-label="Home">%s</a>' % (home_cls, ICON["home"])]
    for label, href in NAV[1:]:
        cls = ' class="active"' if href == active else ''
        parts.append('<a href="%s"%s>%s</a>' % (href, cls, label))
    parts.append('<a class="nav-tel" href="tel:%s" aria-label="Call us">%s</a>' % (CONTACT["phone_href"], ICON["tel"]))
    links = "".join(parts)
    return f"""
<header class="site-header" id="top">
  <div class="header-inner">
    <a class="logo" href="index.html" aria-label="The Dermatology Vet &ndash; home">
      <img src="assets/logo/tdv-logo.png" alt="The Dermatology Vet" width="202" height="63">
    </a>
    <button class="nav-toggle" aria-label="Menu" aria-expanded="false" onclick="var n=document.getElementById('nav');n.classList.toggle('open');this.setAttribute('aria-expanded',n.classList.contains('open'))">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav" id="nav">
      {links}
      <span class="nav-social">
        <a href="#" aria-label="YouTube">{ICON['yt']}</a>
        <a href="#" aria-label="Instagram">{ICON['ig']}</a>
        <a href="#" aria-label="LinkedIn">{ICON['li']}</a>
        <a href="#" aria-label="Facebook">{ICON['fb']}</a>
      </span>
    </nav>
  </div>
</header>"""


def footer():
    addr = "<br>".join(P.CLINIC["lines"])
    return f"""
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <div class="footer-logo">
          <img src="assets/logo/tdv-logo-reversed.png" alt="The Dermatology Vet" width="180" height="56">
        </div>
        <p>The Dermatology Vet, your specialist partner in skin, ear and allergy care for dogs, cats,
        horses, birds and exotic companion animals.</p>
      </div>
      <div>
        <h3>Pune Clinic</h3>
        <p>The Dermatology Vet<br>{addr}<br>{P.CLINIC['landmark']}</p>
        <ul class="f-icons">
          <li>{ICON['tel']}<a href="tel:{CONTACT['phone_href']}">{CONTACT['phone_display']}</a></li>
          <li>{ICON['mail']}<a href="mailto:{CONTACT['email']}">{CONTACT['email']}</a></li>
          <li>{ICON['pin']}<a href="{P.CLINIC['maps']}" target="_blank" rel="noopener">Get directions</a></li>
        </ul>
      </div>
      <div>
        <h3>Referring Vets</h3>
        <p>Send a skin, ear or allergy case. A written opinion within two working days, and the
        patient stays yours.</p>
        <ul class="f-icons">
          <li>{ICON['arrow']}<a href="tdv-connect.html">TDV Connect</a></li>
          <li>{ICON['mail']}<a href="mailto:{CONTACT['referrals']}">{CONTACT['referrals']}</a></li>
          <li>{ICON['arrow']}<a href="careers.html">Careers</a></li>
        </ul>
      </div>
      <div>
        <h3>Connect With Us</h3>
        <div class="f-social">
          <a href="#" aria-label="Facebook">{ICON['fb']}</a>
          <a href="#" aria-label="Instagram">{ICON['ig']}</a>
          <a href="#" aria-label="LinkedIn">{ICON['li']}</a>
          <a href="#" aria-label="YouTube">{ICON['yt']}</a>
        </div>
        <a class="pill" href="contact.html#teleconsult">{ICON['headset']} Request a Tele-Consult</a>
      </div>
    </div>
    <div class="group-note">
      The Dermatology Vet is part of <a href="https://vhi.vet" target="_blank" rel="noopener">Veterinary Holdings International</a>,
      India&rsquo;s specialist veterinary group. Sister practices include
      <a href="https://theeye.vet" target="_blank" rel="noopener">The Eye Vet</a>,
      <a href="https://thecancer.vet" target="_blank" rel="noopener">The Cancer Vet</a>,
      <a href="https://theexotics.vet" target="_blank" rel="noopener">The Exotics Vet</a> and
      <a href="https://thebehaviour.vet" target="_blank" rel="noopener">The Behaviour Vet</a>.
      Every case is referred back to its own veterinarian. We take no referral commission in either direction.
    </div>
  </div>
  <div class="footer-bar">All Rights Reserved 2026 | The Dermatology Vet | A VHI company</div>
</footer>

<a class="tele-tab" href="contact.html#teleconsult">{ICON['headset']} <span><span class="tt-long">Request a </span>Tele-Consult</span></a>
<div class="float-contact">
  <a class="fc-wa" href="{CONTACT['wa_href']}" aria-label="WhatsApp" target="_blank" rel="noopener">{ICON['wa']}</a>
  <a class="fc-tel" href="tel:{CONTACT['phone_href']}" aria-label="Call">{ICON['tel']}</a>
  <a class="fc-yt" href="#" aria-label="YouTube">{ICON['yt']}</a>
</div>
<a class="to-top" href="#top" aria-label="Back to top">{ICON['up']}</a>
</body>
</html>"""


def page(slug, title, desc, body, active=None):
    html = head(title, desc, slug) + header(active or slug) + body + footer()
    with open(os.path.join(OUT, slug), "w", encoding="utf-8") as f:
        f.write(html)
    return slug


if __name__ == "__main__":
    written = P.build(page)
    print(f"Built {len(written)} pages:")
    for w in written:
        print("  ", w)
