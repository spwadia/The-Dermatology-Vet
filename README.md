# The Dermatology Vet — website

Static site for thedermatology.vet. The design follows the template shared by
the sister sites **theeye.vet**, **thecancer.vet** and **theexotics.vet**
(all WordPress, Astra + Elementor). Sizes and colours were measured from those
sites on 2 November 2026:

- **Header:** full-width white header, 111 px tall, with the logo on the left. On the right: a home icon,
  16 px uppercase Nunito menu, a phone icon and 28 px square black social icons.
  The active page shows in yellow `#f2c941`.
- **Home hero:** full-width 600 px media band with a large uppercase white headline.
  The sister sites use a muted clinic video here.
- **Intro:** a band with an image on the left and the welcome text on the right
  (thecancer.vet).
- **Headings and text:** centred Nunito headings, black 16 px body text.
- **Cards:** `#f5f5f5` cards with 8 px corners, centred titles and black
  "Read More →" buttons.
- **Dark band:** a black band with dark cards for the referral section
  (theexotics.vet).
- **Appointments:** a "For Appointment Contact" grey box with phone, WhatsApp and email.
- **Map:** the clinic map beside a clinic card.
- **Inner pages:** open on a plain centred heading, with no grey title band.
- **Forms:** underlined fields, as on theeye.vet/contact.
- **Footer:** reversed logo and tagline, then "Pune Clinic", "Referring Vets" and
  "Connect With Us" columns, a sister-practice line, and a bottom bar.
- **Floating buttons:** a black "Request a Tele-Consult" pill bottom left, round
  WhatsApp / call / YouTube buttons bottom right, and a back-to-top square.

The footer is `#141414`, not the sisters' `#0c0c1e`, because the reversed TDV
logo may only sit on `#141414`. The two read the same on screen.

When you change `assets/styles.css`, bump `CSS_VERSION` in `build.py` so
browsers fetch the new file.

## Run it locally

```
python3 serve.py 4173
```

Then open http://127.0.0.1:4173

## Editing

Two options — pick one and stick to it:

1. **Edit the HTML directly.** The generated `.html` files are plain, static and
   self-contained. This is fine if you are handing the site to a web developer.
2. **Edit `pages.py` and re-run `python3 build.py`.** Keeps the header, footer
   and navigation identical across all 13 pages. If you take this route, do not
   hand-edit the HTML — it will be overwritten.

| File | What it is |
|---|---|
| `build.py` | Template: `<head>`, header, nav, footer, floating widgets, icons, contact details |
| `pages.py` | All content: services, the clinic, the co-founder, FAQ, SEO overrides |
| `assets/styles.css` | The whole stylesheet |
| `serve.py` | Local preview server |

## Before this goes live — `[[TODO]]`

Search the source for `[[TODO]]`. Nothing below is cosmetic.

- [ ] **Domain.** Confirm `thedermatology.vet` and point it at the site's hosting.
- [x] **Dr Awale's photograph** (`assets/team/madhavi-awale-2026.jpg`). Replaced
      on 11 November 2026 with the studio portrait you supplied (original in
      `_source/`), cropped to 4:5. The earlier Instagram still is no longer on the site.
- [ ] **Dr Awale to read and approve her profile** (`pages.py` → `FOUNDER`).
      It uses only public facts: her Practo and DocIndia listings and the IAVD
      webinar posters. Her three society memberships (IAVD, Asian Society,
      ESVD) were confirmed on 9 November 2026. Check the wording of her title.
- [ ] **Phone and WhatsApp numbers** (`build.py` → `CONTACT`).
- [ ] **Clinic opening date and hours** (`pages.py` → `CLINIC`). The address is
      The Eye Vet's Pune address as published on theeye.vet (5th Floor, NECO
      Alpha, Pimple Nilakh, 411027). Add a unit or suite number if TDV has its own.
- [ ] **Connect the three forms** — appointment, tele-consult, referral. All
      three currently show an alert and submit nothing.
- [ ] **Social media URLs** — every social icon is `href="#"`.
- [ ] **Hero video.** The sister sites open on a 30–60 second muted clinic
      video. Film one at NECO Alpha. The slot is marked in `pages.py` (home
      page hero) and currently shows a dark placeholder behind the headline.
- [ ] **Clinic reception photo** for the intro band beside the welcome text,
      as on thecancer.vet. It currently shows the TDV logo on a white panel.
- [ ] **Service icons.** The cards use outline icons in circles, as on
      thecancer.vet. theeye.vet uses photographs instead. Either works.
- [ ] **YouTube link** for the round red floating button, if TDV will have a
      channel. Otherwise change that button to email.
- [ ] **Privacy policy.** The sister sites link one from the footer bar. TDV
      needs one before the forms collect personal data.
- [ ] **Client reviews.** The home page has a commented-out testimonials block
      in the right position. Populate it only with real, attributable reviews.
- [ ] Add `robots.txt`, `sitemap.xml` and analytics.

## Logo

**New logo, 10 November 2026:** a shield with a paw inside a rounded square
frame, with THE / DERMATOLOGY / VET stacked beside it. It replaces the earlier
Design.pdf mark everywhere on the site. The old files were moved out of
`assets/logo/` so they cannot be used by mistake.

The artwork supplied (`_source/tdv-logo-supplied-2026-11-10.webp`) is a raster
image, and the logo in it is only 342 x 106 px. The site files were made from
it by scaling it up four times and re-sharpening the edges, which keeps them crisp
at header size on high-resolution screens. **Replace them with vector artwork
(SVG or PDF) from the designer when it is available**: the file names can stay
the same.

| File | Version | Use |
|---|---|---|
| `tdv-logo.png` | Lockup, black `#141414` on transparent | Header (63 px tall, the same as The Eye Vet's logo) and the home-page intro panel. On white only |
| `tdv-logo-reversed.png` | Lockup, white on transparent | Footer (56 px tall). On `#141414` only |
| `tdv-icon.png`, `tdv-icon-reversed.png` | The framed shield alone | Small spaces, social avatars |
| `favicon-32.png`, `favicon-192.png` | Framed shield with a white inside | Browser tab, Android home screen |
| `apple-touch-icon.png` | Framed shield on a white tile | iOS home screen |

The paw and the space inside the frame are transparent, so they take the colour
of whatever is behind them. Use the black version on white and the reversed
version on `#141414`, as before. `_source/` is not part of the published site.

**Decision (2 November 2026): the website keeps the sister sites' accent colours.**
The launch set says marketing is black and white only, but the site is
deliberately styled as a sibling of theeye.vet, so its indigo and yellow accents
stay. The black-and-white rule is applied to the logo, which is always black on
white or white on `#141414` and never takes an accent colour. Printed and social
marketing pieces still follow the launch set as written.

## Content notes

One clinic to begin with: Pune, on the 5th floor of NECO Alpha, in the same
premises as The Eye Vet. The site says so in the hero, on the home page, on the
Clinic and Contact pages, in the FAQ and in the footer.

The Information section and its eight condition guides were removed on
2 November 2026 as repetitive of the service pages. The FAQ lives on the Contact
page.

Everything on the site is public information about the practice and its
co-founder.

The footer links up to vhi.vet and across to the four sister practices
(The Eye Vet, The Cancer Vet, The Exotics Vet, The Behaviour Vet), which none
of the existing group sites currently do.
