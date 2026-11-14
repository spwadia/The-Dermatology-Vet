# -*- coding: utf-8 -*-
"""
Content for The Dermatology Vet.

One clinic to begin with: Pune, on the 5th floor of NECO Alpha, Pimple Nilakh,
in the same premises as The Eye Vet. Co-founder: Dr Madhavi Awale.

PLACEHOLDERS to replace before going live are marked with  [[TODO]]  below:
  - phone numbers and WhatsApp number (build.py → CONTACT)
  - clinic opening date and hours (CLINIC)
  - Dr Awale's photograph and her sign-off on her profile (FOUNDER)
  - social media URLs (build.py → header/footer, href="#")
  - real client reviews (see the commented block in the home page)
"""

ICONS = {}  # filled from build.ICON at build time

# --------------------------------------------------------------------------
# SERVICES  (title, slug, icon, teaser, long-form body)
# --------------------------------------------------------------------------
SERVICES = [
    ("Consultation &amp; Diagnosis", "service-consultation", "derm",
     "A full dermatological work-up: history, lesion mapping, skin scrapes, tape cytology, "
     "trichogram, Wood&rsquo;s lamp, fungal culture and biopsy where indicated."),
    ("Allergy Testing &amp; Diet Trials", "service-allergy", "flask",
     "Serum IgE allergy testing, intradermal testing where indicated, and properly supervised "
     "eight-week elimination diet trials &mdash; run to protocol, not guesswork."),
    ("The Chronic Ear", "service-ear", "ear",
     "Video-otoscopy, deep ear flushing under general anaesthesia, myringotomy and middle-ear "
     "sampling for the ear that keeps coming back."),
    ("Equine Dermatology", "service-equine", "horse",
     "Visits to stud farms, riding schools and private yards for sweet itch, sarcoids, "
     "pastern dermatitis and non-healing wounds."),
    ("Exotics &amp; Avian", "service-exotics", "bird",
     "Feather-destructive disorders, scaly face in budgerigars, dysecdysis in reptiles and "
     "pododermatitis in rabbits and guinea pigs."),
    ("Tele-dermatology", "service-teleconsult", "video",
     "TDV Connect &mdash; a written specialist opinion within two working days for referring "
     "veterinarians anywhere in India, from history and photographs."),
]

SERVICE_BODY = {
"service-consultation": """
<p class="lead">Most skin cases that reach us have already been treated two or three times. The work of a
dermatology consultation is not to try the next product &mdash; it is to find out what is actually there.</p>
<h2>What a first consultation involves</h2>
<p>A specialist dermatology consultation runs between 45 and 60 minutes. It is longer than a general
practice appointment because the history is the diagnosis in at least half of all cases: when the itch
started, where on the body it started, what season, what diet, what has been given and what each
treatment did or did not change.</p>
<h3>The cytology-first work-up</h3>
<p>We take samples before we prescribe. In Indian practice this matters more than it does in the West,
because the case mix here is parasitic and infectious before it is allergic:</p>
<ul>
  <li><strong>Deep skin scrapes</strong> &mdash; for <em>Demodex</em> and <em>Sarcoptes</em>. Mange is the
      single largest group in published Indian caseloads.</li>
  <li><strong>Tape-strip and impression cytology</strong> &mdash; for bacterial overgrowth and
      <em>Malassezia</em>, read in-house on the day.</li>
  <li><strong>Trichogram</strong> &mdash; hair plucks to separate self-trauma from a true alopecia.</li>
  <li><strong>Wood&rsquo;s lamp and fungal culture</strong> &mdash; for dermatophytosis, which runs
      around a fifth to a third of Indian derm caseloads depending on the city and the season.</li>
  <li><strong>Bacterial culture and sensitivity</strong> &mdash; where a pyoderma has failed first-line
      treatment. Methicillin resistance is now reported in Indian series and changes the plan entirely.</li>
  <li><strong>Skin biopsy</strong> &mdash; for suspected immune-mediated, neoplastic or
      unexplained disease, read by a veterinary pathologist.</li>
</ul>
<div class="callout"><p><strong>Antimicrobial stewardship.</strong> We culture before we reach for a
second-line antibiotic, and we treat infections to cytological cure rather than to the end of a packet.
It is slower on the day and better over a year.</p></div>
<h2>What you leave with</h2>
<p>A written diagnosis or a ranked differential list, a treatment plan with doses and dates, a recheck
schedule, and a letter to your own veterinarian the same week. Skin disease is managed over months,
so the plan matters more than the first prescription.</p>
""",
"service-allergy": """
<p class="lead">There is no blood test that diagnoses a food allergy, and no allergy test that diagnoses
atopic dermatitis. Both are clinical diagnoses &mdash; reached by excluding everything else first.</p>
<h2>The elimination diet trial</h2>
<p>An adverse food reaction is diagnosed one way only: a strict elimination diet for eight weeks,
followed by a provocation challenge. A trial that runs six weeks, or that allows a single treat,
a flavoured tablet or a chew, tells you nothing at all &mdash; which is why most diet trials fail
before they begin.</p>
<p>We set the trial up properly: a novel or hydrolysed protein chosen around what the animal has
already eaten, written instructions for everyone in the household, a strategy for medication that
does not break the trial, and a scheduled check at weeks four and eight.</p>
<h3>Allergy testing, and what it is actually for</h3>
<p>Serum IgE testing and intradermal testing do not tell you whether an animal is allergic. They tell
you <em>what to put in an immunotherapy vaccine</em> once the clinical diagnosis of atopic dermatitis
has already been made. Used in that order they are valuable; used as a screening test they generate
false positives and wasted money.</p>
<div class="callout"><p><strong>On immunotherapy in India.</strong> Allergen-specific immunotherapy
(ASIT) is not currently manufactured or licensed in India and we do not promise it. Where it is
clinically indicated we will say so and discuss the import position honestly. Everything else in the
allergy plan &mdash; parasite control, infection control, barrier care, diet and modern anti-pruritic
medication &mdash; is available here today.</p></div>
<h2>Long-term control</h2>
<p>For most atopic animals the realistic goal is comfortable skin on the lowest effective treatment,
reviewed twice a year. Oclacitinib is available in India both as the originator and as generics, which
makes long-term control affordable for a far wider range of households than in most markets.</p>
""",
"service-ear": """
<p class="lead">A chronic ear is not an ear problem. It is a skin problem that happens to be in an ear,
plus whatever the last six courses of ear drops have left behind.</p>
<h2>Why ears relapse</h2>
<p>Otitis externa runs at roughly 8&ndash;14% of dermatology caseload in Indian series. Almost every
chronic case has three layers: a <em>primary</em> cause (allergy, a foreign body, a parasite, an
endocrine disease), <em>predisposing</em> anatomy, and <em>perpetuating</em> factors &mdash; biofilm,
resistant rods, a stenotic canal, a ruptured ear drum. Treating only the infection treats only the
layer you can see.</p>
<h3>Video-otoscopy</h3>
<p>We examine the canal and the ear drum under general anaesthesia with a video-otoscope, on a screen
you can see afterwards. That makes three things possible that a hand-held otoscope cannot:</p>
<ul>
  <li><strong>A deep flush under direct vision</strong> &mdash; removing the debris and biofilm that
      topical treatment cannot penetrate.</li>
  <li><strong>Assessment of the ear drum</strong> &mdash; which decides whether a given medication is
      safe to use at all.</li>
  <li><strong>Myringotomy and middle-ear sampling</strong> &mdash; where otitis media is suspected,
      which is the most commonly missed reason an ear will not clear.</li>
</ul>
<p>Foreign bodies, polyps and small masses can be retrieved or sampled in the same procedure.</p>
<div class="callout"><p><strong>When surgery is the kind answer.</strong> For an end-stage canal that
has closed and calcified, total ear canal ablation is a cure rather than a failure. We will say so
plainly, and arrange it with a surgeon in the group.</p></div>
""",
"service-equine": """
<p class="lead">Horses are seen where they live. We visit stud farms, riding schools, racing yards and
private stables across Pune and the surrounding district.</p>
<h2>What we see most</h2>
<ul>
  <li><strong>Insect bite hypersensitivity (sweet itch)</strong> &mdash; the mane-and-tail itch that
      returns every monsoon, managed with barrier strategy, rug and stabling changes and medication.</li>
  <li><strong>Sarcoids</strong> &mdash; assessment, biopsy where it is safe to take one, and a treatment
      plan that accounts for site, type and the horse&rsquo;s job.</li>
  <li><strong>Pastern dermatitis</strong> &mdash; the chronically scabbed heel, which is a pattern and
      not a diagnosis; the work is in finding the cause underneath.</li>
  <li><strong>Non-healing wounds and exuberant granulation tissue.</strong></li>
  <li><strong>Dermatophytosis and rain scald</strong> in yards with a herd problem rather than an
      individual one.</li>
</ul>
<p>Yard visits can be arranged for several horses in one attendance, which is usually the sensible way
to handle a herd outbreak. Your own veterinarian stays in charge of the case throughout.</p>
""",
"service-exotics": """
<p class="lead">Skin and feather disease in exotic companion animals is rarely only skin deep &mdash; it
is usually husbandry, nutrition or an underlying systemic disease showing on the outside.</p>
<h2>Birds</h2>
<ul>
  <li><strong>Feather-destructive behaviour</strong> &mdash; worked up medically before it is called
      behavioural, in partnership with <a href="https://thebehaviour.vet" target="_blank" rel="noopener">The Behaviour Vet</a>.</li>
  <li><strong>Scaly face</strong> (<em>Knemidocoptes</em>) in budgerigars and passerines.</li>
  <li><strong>Pododermatitis</strong> &mdash; bumblefoot, where perch design is usually the real
      prescription.</li>
</ul>
<h2>Reptiles</h2>
<ul>
  <li><strong>Dysecdysis</strong> &mdash; retained shed, and the humidity and hydration failures behind it.</li>
  <li><strong>Scale rot and thermal burns</strong> from substrate and heat-source problems.</li>
  <li><strong>Abscesses and mite infestations.</strong></li>
</ul>
<h2>Small mammals</h2>
<ul>
  <li><strong>Rabbits and guinea pigs</strong> &mdash; pododermatitis, <em>Cheyletiella</em>, Trixacarus,
      and the barbering that follows a dental or an arthritic problem.</li>
  <li><strong>Ferrets</strong> &mdash; symmetrical alopecia, which is adrenal disease until proven otherwise.</li>
</ul>
<p>Exotic cases are seen jointly with <a href="https://theexotics.vet" target="_blank" rel="noopener">The Exotics Vet</a>
where the species or the anaesthetic calls for it.</p>
""",
"service-teleconsult": """
<p class="lead">TDV Connect is a specialist dermatology opinion for veterinarians, delivered without the
client having to travel.</p>
<h2>How it works</h2>
<ol>
  <li>You send the history, your photographs and any cytology images through the referral form.</li>
  <li>A dermatologist reviews the case and replies within two working days &mdash; usually sooner.</li>
  <li>You receive a written opinion: a differential list, the next diagnostic step, a treatment plan
      with doses, and a clear statement of when the case should be seen in person instead.</li>
</ol>
<p>The case stays yours. We do not contact your client, and we do not take the case on unless you ask
us to. Where a physical referral is the right answer we will say so rather than manage a case badly
at a distance.</p>
<div class="callout"><p><strong>For pet owners.</strong> A tele-consult is also available to you
directly if you live outside Pune &mdash; but a first dermatology opinion is almost always
better in person, because cytology cannot be done down a camera. We will tell you honestly which one
your animal needs.</p></div>
<h2>What it costs</h2>
<p>Tele-dermatology is charged per case, not per message, and a follow-up question on the same case
within thirty days is included. Current fees are confirmed when you submit the form.</p>
"""
}

# --------------------------------------------------------------------------
# CLINIC  One to begin with, in the same premises as The Eye Vet in Pune.
# Address as published on theeye.vet/contact.  [[TODO]] opening date and hours
# --------------------------------------------------------------------------
CLINIC = {
    "name": "The Dermatology Vet, Pune",
    "lines": ["5th Floor, NECO Alpha", "Matoshri Colony, Nandanwan Society",
              "Ingawale Nagar, Pimple Nilakh", "Pimpri-Chinchwad, Maharashtra 411027"],
    "landmark": "In the same premises as The Eye Vet",
    "maps": "https://www.google.com/maps/search/?api=1&amp;query=The+Eye+Vet+NECO+Alpha+Pimple+Nilakh+Pune",
    "embed": "https://www.google.com/maps?q=The+Eye+Vet,+NECO+Alpha,+Pimple+Nilakh,+Pune&amp;output=embed",
}

# --------------------------------------------------------------------------
# FOUNDER  Public facts only: Practo and DocIndia listings, IAVD webinar posts.
# Society memberships (IAVD, Asian Society, ESVD) confirmed by the user, 9 November 2026.
# Photo: studio portrait supplied by the user, 11 November 2026 (original in _source/),
#        cropped to 4:5 so her crossed arms stay in frame.
# [[TODO]] Dr Awale to read and approve this profile before launch.
# --------------------------------------------------------------------------
FOUNDER = {
    "name": "Dr Madhavi Awale",
    "role": "Co-founder",
    "photo": "assets/team/madhavi-awale-2026.jpg",
    "quals": "BVSc &amp; AH &middot; MVSc &middot; Dermatology training, ESAVS",
    "short": "A veterinarian who has made skin disease the centre of her work. Dr Awale trained in "
             "small animal dermatology with the European School for Advanced Veterinary Studies and "
             "has run Pet Wellness Clinic and Derm Centre in Pune since 2016. She sees referred cases "
             "at our Pune clinic and reviews the cases vets across India send through TDV Connect.",
    "bio": """
<p>Dr Madhavi Awale co-founded The Dermatology Vet to give India the specialist veterinary skin
service it has never had.</p>
<p>She qualified from Bombay Veterinary College in 2010, took a master&rsquo;s degree in veterinary
pharmacology, and trained in small animal dermatology with the European School for Advanced
Veterinary Studies (ESAVS). Since 2016 she has run Pet Wellness Clinic and Derm Centre in Pimple
Saudagar, Pune, a practice built around skin disease in dogs and cats.</p>
<p>She also teaches other vets, including in the IAVD dermatology webinar series. At The Dermatology
Vet she sees referred cases in Pune and reviews the cases that vets across India send through
<a href="tdv-connect.html">TDV Connect</a>.</p>""",
    "credentials": [
        ("BVSc &amp; AH", "Bombay Veterinary College, Mumbai, 2010"),
        ("MVSc, Pharmacology", "Sardarkrushinagar Dantiwada Agricultural University, 2012"),
        ("Small Animal Dermatology", "European School for Advanced Veterinary Studies (ESAVS), 2018"),
        ("Memberships", "Indian Association for Veterinary Dermatology (IAVD)<br>"
                        "Asian Society of Veterinary Dermatology<br>"
                        "European Society of Veterinary Dermatology (ESVD)"),
        ("Registered", "Maharashtra State Veterinary Council"),
    ],
}

FAQ = [
    ("Where are you?",
     "<p>On the 5th floor of NECO Alpha, Ingawale Nagar, Pimple Nilakh, Pune &mdash; in the same "
     "premises as The Eye Vet. Pune is our only clinic for now. If you are further away, start with a "
     "tele-consult.</p>"),
    ("Do I need a referral from my own vet?",
     "<p>It helps a great deal, and we prefer it &mdash; your veterinarian&rsquo;s history, previous "
     "test results and treatment record save time and money at the first consultation. But you can also "
     "book directly. Either way we write to your own vet and the case goes back to them.</p>"),
    ("Will you take my animal away from my regular vet?",
     "<p>No. We are a referral service only. We see the skin problem, send a written plan back to your "
     "veterinarian, and they continue to look after everything else. No referral commission changes "
     "hands in either direction.</p>"),
    ("How long does a first consultation take?",
     "<p>Between 45 and 60 minutes. Please allow longer on the day in case we need to take samples or "
     "run cytology while you wait.</p>"),
    ("What should I bring?",
     "<p>Any previous test results and clinical records, the packaging or photographs of every "
     "medication, shampoo and food your animal is currently on, and &mdash; if you can &mdash; photographs "
     "of the skin at its worst. Please do not bath the animal for 48 hours beforehand, and do not start "
     "any new treatment in the week before.</p>"),
    ("Will my pet be cured?",
     "<p>Sometimes. Parasitic, infectious and food-related disease can usually be resolved completely. "
     "Atopic dermatitis and several other conditions are controlled rather than cured &mdash; the goal "
     "is a comfortable animal on the least medication that achieves it. We will tell you honestly which "
     "category your animal is in at the first visit.</p>"),
    ("How much does it cost?",
     "<p>Fees are confirmed when you book, and we give a written estimate before any procedure or test. "
     "Dermatology is managed over months rather than in a single visit, so at the point of diagnosis we "
     "will also set out what a year of good control is likely to cost.</p>"),
    ("Do you see cats, horses, birds and exotic pets?",
     "<p>Yes &mdash; all of them. Equine cases are seen on the yard. Avian, reptile and small-mammal "
     "cases are seen jointly with exotics colleagues in the group where the species or the anaesthetic "
     "calls for it.</p>"),
]


# --------------------------------------------------------------------------
# SEO overrides — where the on-page heading makes too long a <title>, or the
# card teaser makes too long a meta description. Keep titles <= 62 characters
# and descriptions <= 160 characters as rendered (entities count as one).
# --------------------------------------------------------------------------
META = {
 "index.html": (
   "The Dermatology Vet &ndash; Veterinary Skin &amp; Allergy Specialists",
   "India&rsquo;s specialist veterinary dermatology referral service &mdash; skin, ear and "
   "allergy medicine for dogs, cats, horses, birds and exotic pets."),
 "services.html": (
   "Services &ndash; The Dermatology Vet",
   "Specialist veterinary dermatology: diagnosis, allergy testing, diet trials, "
   "video-otoscopy, equine, exotics and tele-dermatology."),
}

# ==========================================================================
# Page assembly  (layout follows the sister-site template; see build.py)
# ==========================================================================
def build(page):
    from build import ICON, CONTACT

    _emit = page

    def page(slug, title, desc, body, active=None):
        t, d = META.get(slug, (title, desc))
        return _emit(slug, t, d, body, active)

    written = []
    ARROW = ICON["arrow"]
    EXT = ' target="_blank" rel="noopener"'

    def btn(label, href, cls="btn", extra=""):
        return f'<a class="{cls}" href="{href}"{extra}>{label} {ARROW}</a>'

    def card(title, href, body, icon):
        return f"""
      <article class="card">
        <div class="card-icon">{ICON[icon]}</div>
        <h3>{title}</h3>
        <p>{body}</p>
        {btn("Read More", href)}
      </article>"""

    def card_row(title, href, body, icon):
        return f"""
      <article class="card-row">
        <div class="card-icon">{ICON[icon]}</div>
        <div>
          <h3>{title}</h3>
          <p>{body}</p>
          <div class="card-foot">{btn("Read More", href)}</div>
        </div>
      </article>"""

    def service_cards():
        return "".join(card(t, s + ".html", teaser, icon) for t, s, icon, teaser in SERVICES)

    def service_rows():
        return "".join(card_row(t, s + ".html", teaser, icon) for t, s, icon, teaser in SERVICES)

    def page_head(h1, intro, actions=""):
        acts = f'<div class="actions">{actions}</div>' if actions else ""
        return f"""
<section class="page-head">
  <div class="wrap"><h1>{h1}</h1><p>{intro}</p>{acts}</div>
</section>"""

    def visit_block():
        addr = "<br>".join(CLINIC["lines"])
        return f"""
    <div class="visit">
      <div class="map"><iframe src="{CLINIC['embed']}" title="Map: NECO Alpha, Pimple Nilakh, Pune" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
      <div class="visit-card">
        <h3>Pune Clinic</h3>
        <p class="visit-note">{CLINIC['landmark']}</p>
        <address>The Dermatology Vet<br>{addr}</address>
        <ul class="icon-rows">
          <li>{ICON['tel']}<span><a href="tel:{CONTACT['phone_href']}">{CONTACT['phone_display']}</a> &middot; phone &amp; WhatsApp</span></li>
          <li>{ICON['mail']}<a href="mailto:{CONTACT['email']}">{CONTACT['email']}</a></li>
          <li>{ICON['clock']}<span>By appointment</span></li>
        </ul>
        <div class="actions">
          {btn("Get directions", CLINIC['maps'], extra=EXT)}
          {btn("Book a consultation", "contact.html")}
        </div>
      </div>
    </div>"""

    def appt_box(intro, cta=""):
        side = f"<div>{cta}</div>" if cta else ""
        return f"""
    <div class="appt">
      <div>
        <p class="appt-intro">{intro}</p>
        <h2>For Appointment Contact</h2>
        <ul class="icon-list">
          <li>{ICON['tel']}<span>Pune: <a href="tel:{CONTACT['phone_href']}">{CONTACT['phone_display']}</a></span></li>
          <li>{ICON['wa']}<a href="{CONTACT['wa_href']}"{EXT}>WhatsApp</a></li>
          <li>{ICON['mail']}<a href="mailto:{CONTACT['email']}">{CONTACT['email']}</a></li>
        </ul>
      </div>
      {side}
    </div>"""

    def faq_block(items):
        rows = "".join(
            f"<details><summary>{q}</summary><div class=\"answer\">{a}</div></details>"
            for q, a in items
        )
        return f'<div class="faq">{rows}</div>'

    REFERRAL_BAND = f"""
<section class="section dark">
  <div class="wrap">
    <div class="section-head">
      <h2>Every case goes back to you</h2>
      <p>We are a referral service and nothing else. We see the skin, the ear or the allergy, send you a
      written plan the same week, and return the patient to your care. No referral commission changes
      hands in either direction &mdash; not to us, not from us.</p>
    </div>
    <div class="stats">
      <div class="stat"><div class="n">1 in 7</div><div class="l">Dogs in Indian clinics present with skin disease</div></div>
      <div class="stat"><div class="n">48h</div><div class="l">TDV Connect specialist opinion turnaround</div></div>
      <div class="stat"><div class="n">8 wks</div><div class="l">A diet trial that actually diagnoses anything</div></div>
      <div class="stat"><div class="n">0</div><div class="l">Referral commission, either direction</div></div>
    </div>
    <p class="center" style="margin:38px 0 0">{btn("Refer a case", "tdv-connect.html", "btn btn-light")}</p>
  </div>
</section>

<!-- ====================================================================
     CLIENT REVIEWS — switch this on once you have real, attributable reviews.
     Do not populate it with invented testimonials. Sister sites use a row of
     video testimonials with the owner's name under each.
<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>Testimonials</h2></div>
    <div class="grid grid-4"> ... </div>
  </div>
</section>
     ==================================================================== -->
"""

    # ---------------- Home ----------------
    written.append(page("index.html",
        "The Dermatology Vet &ndash; Veterinary Skin, Ear and Allergy Specialists in India",
        "India's specialist veterinary dermatology referral service. Skin, ear and allergy "
        "medicine for dogs, cats, horses, birds and exotic pets. Part of Veterinary Holdings International.",
        f"""
<section class="hero">
  <div class="hero-media">
    <!-- [[TODO]] The sister sites open on a 30-60 second muted clinic video. Film one at NECO Alpha
         and drop it in here:
         <video autoplay muted loop playsinline poster="assets/hero/poster.jpg"><source src="assets/hero/hero.mp4" type="video/mp4"></video> -->
  </div>
  <h1>Specialist Skin, Ear and Allergy Care for Animals</h1>
</section>

<section class="intro">
  <div class="wrap">
    <div class="intro-grid">
      <div class="intro-media">
        <!-- [[TODO]] Replace with a photograph of the clinic reception once it is fitted out,
             as on thecancer.vet: <img class="photo" src="assets/clinic/reception.jpg" alt="..."> -->
        <img src="assets/logo/tdv-logo.png" alt="The Dermatology Vet" width="340" height="106">
      </div>
      <div class="intro-text">
        <p>Dermatology is the most common reason pets see a vet in India &mdash; and the one specialty
        the country has never had. The Dermatology Vet is a referral service for the skin cases that have
        stopped responding to everything else.</p>
        <p class="intro-place">{ICON['pin']}<span>5th Floor, NECO Alpha, Pimple Nilakh, Pune &middot; in the same premises as The Eye Vet</span></p>
        <div class="actions">
          {btn("Book a consultation", "contact.html")}
          {btn("Refer a case", "tdv-connect.html")}
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Comprehensive Skin Care For Animals</h2>
      <p>Cytology-first diagnosis, allergy work-ups run to protocol, and the chronic ear examined
      properly &mdash; for dogs, cats, horses, birds and exotic companion animals.</p>
    </div>
    <div class="grid grid-3">{service_cards()}</div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="section-head"><h2>Our Team</h2></div>
    <div class="founder founder-box">
      <div class="founder-photo"><img src="{FOUNDER['photo']}" alt="{FOUNDER['name']}" width="880" height="1100" loading="lazy"></div>
      <div class="founder-text">
        <p class="founder-label">Co-founder of The Dermatology Vet</p>
        <h3 class="founder-name">{FOUNDER['name']}</h3>
        <p class="founder-quals">{FOUNDER['quals']}</p>
        <p>{FOUNDER['short']}</p>
        <div class="founder-foot">{btn("Know More", "team.html")}</div>
      </div>
    </div>
  </div>
</section>

{REFERRAL_BAND}

<section class="section">
  <div class="wrap">
    {appt_box("Not sure whether your pet needs a specialist? If the itch has lasted more than a month, "
              "the ears keep coming back, or two courses of treatment have not held &mdash; that is the "
              "point at which a dermatology opinion saves time and money.",
              btn("Get in touch", "contact.html"))}
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="section-head">
      <h2>One clinic, in Pune</h2>
      <p>We see patients on the 5th floor of NECO Alpha in Pimple Nilakh, in the same premises as our
      sister practice The Eye Vet. If you are outside Pune, start with a tele-consult.</p>
    </div>
    {visit_block()}
  </div>
</section>
"""))

    # ---------------- Services ----------------
    written.append(page("services.html", "Services &ndash; The Dermatology Vet",
        "Specialist veterinary dermatology services: consultation and diagnosis, allergy testing and "
        "diet trials, video-otoscopy for the chronic ear, equine, exotics and tele-dermatology.",
        page_head("Our Services",
            "Referral dermatology for every species we are asked to see &mdash; and an honest answer about "
            "which cases genuinely need a specialist.") + f"""
<section class="section">
  <div class="wrap"><div class="grid grid-2">{service_rows()}</div></div>
</section>

<section class="section band" id="teleconsult">
  <div class="wrap">
    <div class="section-head">
      <h2>Request a Tele-Consult</h2>
      <p>For owners outside Pune and for referring veterinarians anywhere in India. Tell us about
      the case and we will come back to you with the next step &mdash; including, where it is the right
      answer, that the animal should be seen in person.</p>
    </div>
    <div class="narrow">
      <form class="form" method="post" action="#" onsubmit="alert('Connect this form to your booking system or inbox before launch.');return false">
        <div class="form-row">
          <div class="field"><label for="t-name">Your name *</label><input id="t-name" name="name" required></div>
          <div class="field"><label for="t-phone">Phone *</label><input id="t-phone" name="phone" type="tel" required></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="t-email">Email *</label><input id="t-email" name="email" type="email" required></div>
          <div class="field"><label for="t-city">City</label><input id="t-city" name="city"></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="t-species">Species</label>
            <select id="t-species" name="species">
              <option>Dog</option><option>Cat</option><option>Horse</option>
              <option>Bird</option><option>Reptile</option><option>Small mammal</option><option>Other</option>
            </select>
          </div>
          <div class="field"><label for="t-who">You are</label>
            <select id="t-who" name="who"><option>A pet owner</option><option>A referring veterinarian</option></select>
          </div>
        </div>
        <div class="field"><label for="t-problem">What is the problem, and how long has it been going on? *</label>
          <textarea id="t-problem" name="problem" required></textarea></div>
        <div class="field"><label for="t-treat">What has already been tried?</label>
          <textarea id="t-treat" name="treatment"></textarea></div>
        <button class="btn" type="submit">Request a Tele-Consult {ARROW}</button>
        <p class="form-note">[[TODO]] This form is not connected. Point it at your booking system,
        CRM or inbox before the site goes live.</p>
      </form>
    </div>
  </div>
</section>
"""))

    # ---------------- Service detail pages ----------------
    for title, slug, icon, teaser in SERVICES:
        others = "".join(
            f'<li><a href="{s}.html">{t}</a></li>' for t, s, _, _ in SERVICES if s != slug
        )
        written.append(page(slug + ".html", f"{title} &ndash; The Dermatology Vet", teaser,
            page_head(title, teaser) + f"""
<section class="section">
  <div class="wrap"><div class="prose">{SERVICE_BODY[slug]}
    <div class="callout"><p><strong>Referring a case?</strong> Send history, photographs and any
    cytology through <a href="tdv-connect.html">TDV Connect</a> and you will have a written opinion
    within two working days.</p></div>
    <h2>Other services</h2><ul>{others}</ul>
    <p style="margin-top:28px">{btn("Book a consultation", "contact.html")}</p>
  </div></div>
</section>
"""))

    # ---------------- Team ----------------
    creds = "".join(f"<li><strong>{k}</strong><span>{v}</span></li>" for k, v in FOUNDER["credentials"])
    written.append(page("team.html", "Our Team &ndash; The Dermatology Vet",
        "Dr Madhavi Awale, co-founder of The Dermatology Vet, and the team being built around her in Pune.",
        page_head("Our Team",
            "A specialist dermatology service, built around a clinician who has made skin disease the "
            "centre of her work.") + f"""
<section class="section band">
  <div class="wrap">
    <div class="founder founder-top">
      <div class="founder-photo"><img src="{FOUNDER['photo']}" alt="{FOUNDER['name']}" width="880" height="1100"></div>
      <div class="founder-text">
        <p class="founder-label">{FOUNDER['role']} of The Dermatology Vet</p>
        <h2 class="founder-name">{FOUNDER['name']}</h2>
        <p class="founder-quals">{FOUNDER['quals']}</p>
        {FOUNDER['bio']}
        <ul class="creds">{creds}</ul>
      </div>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap"><div class="prose">
    <h2>The team around her</h2>
    <p>We are recruiting the veterinarians and dermatology nurses who will work alongside Dr Awale in
    Pune. Dermatology nursing is a skill of its own &mdash; cytology, ear procedures, diet-trial
    coaching and long-term follow-up &mdash; and we train for it. If that could be you, see
    <a href="careers.html">Careers</a>.</p>
    <h2>How the clinical standard is held</h2>
    <p>The Dermatology Vet is one of the specialist businesses of
    <a href="https://vhi.vet" target="_blank" rel="noopener">Veterinary Holdings International</a>.
    Clinical standards are set by the group&rsquo;s Dermatology Specialty Council rather than by any
    individual clinic.</p>
    <h3>Working with the rest of the group</h3>
    <p>Skin disease does not stay in the skin. Cases are seen jointly with sister practices where that
    is what the animal needs &mdash; <a href="https://theeye.vet" target="_blank" rel="noopener">The Eye
    Vet</a>, which shares our premises in Pune, for eyelid and periocular disease;
    <a href="https://thecancer.vet" target="_blank" rel="noopener">The Cancer Vet</a> for skin tumours;
    <a href="https://theexotics.vet" target="_blank" rel="noopener">The Exotics Vet</a> for birds,
    reptiles and small mammals; and <a href="https://thebehaviour.vet" target="_blank" rel="noopener">The
    Behaviour Vet</a> where self-trauma or feather-destructive behaviour has a behavioural component.</p>
  </div></div>
</section>
"""))

    # ---------------- Clinic ----------------
    written.append(page("clinic.html", "Our Clinic &ndash; The Dermatology Vet",
        "The Dermatology Vet, Pune: 5th Floor, NECO Alpha, Pimple Nilakh, in the same premises as "
        "The Eye Vet. Address, map and appointments.",
        page_head("Our Clinic",
            "One clinic to begin with, in Pune &mdash; on the 5th floor of NECO Alpha, in the same premises "
            "as The Eye Vet.") + f"""
<section class="section">
  <div class="wrap">{visit_block()}</div>
</section>
<section class="section band">
  <div class="wrap"><div class="prose">
    <h2>Finding us</h2>
    <p>NECO Alpha is in Ingawale Nagar, Pimple Nilakh, in Pimpri-Chinchwad. Take the lift to the 5th
    floor. We share the premises with <a href="https://theeye.vet" target="_blank" rel="noopener">The Eye
    Vet</a>, our sister ophthalmology practice, so if you have visited The Eye Vet in Pune you already
    know the way.</p>
    <h2>Two specialist teams under one roof</h2>
    <p>Skin disease often reaches the eyelids and the skin around the eyes. Because we work in the same
    premises, the dermatology and ophthalmology teams can see those cases together, without a second
    journey.</p>
    <h2>Appointments</h2>
    <p>Every appointment is booked in advance. Call or WhatsApp us on
    <a href="tel:{CONTACT['phone_href']}">{CONTACT['phone_display']}</a>, or
    <a href="contact.html">request an appointment online</a>. Please bring previous test results and
    the packaging of every medication, shampoo and food your animal is on.</p>
    <h2>Coming from outside Pune</h2>
    <p>Start with a <a href="service-teleconsult.html">tele-consult</a>. If you are a veterinarian, send
    the case through <a href="tdv-connect.html">TDV Connect</a> and you will have a written opinion within
    two working days. If the animal needs to be seen in person, we will tell you, and plan the visit so
    that it takes as few trips as possible.</p>
  </div></div>
</section>
"""))

    # ---------------- TDV Connect ----------------
    written.append(page("tdv-connect.html", "TDV Connect &ndash; Refer a Case &ndash; The Dermatology Vet",
        "Send a skin, ear or allergy case to The Dermatology Vet. A written specialist opinion within "
        "two working days, and the patient stays with you.",
        page_head("TDV Connect",
            "Send us a skin, ear or allergy case. A dermatologist replies in writing within two working days, "
            "and the patient stays yours.",
            btn("Send a case", "#refer") + btn("WhatsApp photos", CONTACT['wa_href'], extra=EXT)) + f"""
<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>Three steps, two working days</h2></div>
    <ol class="steps">
      <li><span class="step-n">1</span><h3>Send the case</h3>
        <p>Use the form below or WhatsApp us. A few lines of history and good photographs are enough to
        start; cytology images and lab results help.</p></li>
      <li><span class="step-n">2</span><h3>Get a written plan</h3>
        <p>Within two working days: what we think it is, the next test worth doing, and a treatment plan
        with doses.</p></li>
      <li><span class="step-n">3</span><h3>Keep the case</h3>
        <p>You carry on treating. If the animal needs to be seen, Dr Awale sees it in Pune and sends it
        back to you with a full report.</p></li>
    </ol>
  </div>
</section>
<section class="section band">
  <div class="wrap">
    <div class="section-head"><h2>An opinion, or a visit</h2></div>
    <div class="grid grid-2">
      <div class="route">
        <span class="route-tag">Anywhere in India</span>
        <h3>Ask for an opinion</h3>
        <p>For cases you can go on managing yourself. Send the history and photographs and we reply with
        a written plan. A follow-up question on the same case within thirty days is included.</p>
      </div>
      <div class="route">
        <span class="route-tag">At our Pune clinic</span>
        <h3>Refer for a visit</h3>
        <p>For cases that need cytology, biopsy, video-otoscopy, allergy testing or anaesthesia. You
        receive a full written report, and the patient comes back to you.</p>
      </div>
    </div>
    <ul class="promises">
      <li><strong>The case stays yours</strong><span>We never contact your client without your say-so.</span></li>
      <li><strong>No referral commission</strong><span>Not to us, and not from us.</span></li>
      <li><strong>Always in writing</strong><span>Every case gets a written reply.</span></li>
    </ul>
  </div>
</section>
<section class="section" id="refer">
  <div class="wrap"><div class="narrow">
    <div class="section-head"><h2>Send a case</h2>
    <p>It takes about five minutes. Photographs taken in daylight help most: the whole animal first, then
    each affected area close up.</p></div>
    <form class="form" method="post" action="#" enctype="multipart/form-data" onsubmit="alert('Connect this form to your referral inbox before launch.');return false">
      <div class="form-row">
        <div class="field"><label for="r-vet">Your name *</label><input id="r-vet" name="vet" required></div>
        <div class="field"><label for="r-practice">Practice and city *</label><input id="r-practice" name="practice" required></div>
      </div>
      <div class="form-row">
        <div class="field"><label for="r-email">Email *</label><input id="r-email" name="email" type="email" required></div>
        <div class="field"><label for="r-phone">Phone or WhatsApp</label><input id="r-phone" name="phone" type="tel"></div>
      </div>
      <div class="form-row">
        <div class="field"><label for="r-type">What do you need?</label>
          <select id="r-type" name="type"><option>A written opinion</option><option>A visit in Pune</option><option>Not sure &mdash; please advise</option></select></div>
        <div class="field"><label for="r-species">Species</label>
          <select id="r-species" name="species"><option>Dog</option><option>Cat</option><option>Horse</option><option>Bird</option><option>Reptile</option><option>Small mammal</option><option>Other</option></select></div>
      </div>
      <div class="field"><label for="r-case">The case in a few lines *</label>
        <textarea id="r-case" name="case" required placeholder="Age and breed, how long it has been going on, what it looks like, what has been tried and what changed"></textarea></div>
      <div class="field"><label for="r-files">Photographs and results</label>
        <input id="r-files" name="files" type="file" multiple accept="image/*,.pdf"></div>
      <button class="btn" type="submit">Send case {ARROW}</button>
      <p class="form-note">[[TODO]] Not connected. Point this at {CONTACT['referrals']} or your
      practice management system.</p>
    </form>
  </div></div>
</section>
"""))

    # ---------------- Careers ----------------
    written.append(page("careers.html", "Careers &ndash; The Dermatology Vet",
        "Clinical and nursing careers in veterinary dermatology with The Dermatology Vet, part of "
        "Veterinary Holdings International.",
        page_head("Careers",
            "Building India&rsquo;s first specialist veterinary dermatology service &mdash; which means "
            "building the team as well as the clinic.") + """
<section class="section">
  <div class="wrap"><div class="prose">
    <h2>Why here</h2>
    <p>There is no established veterinary dermatology specialty in India. That is the difficulty and it
    is also the opportunity: the clinicians who join now will set the standard rather than inherit it.</p>
    <h2>Who we are looking for</h2>
    <ul>
      <li><strong>Veterinary dermatologists</strong> &mdash; board-certified, in training, or with
          substantial dermatology caseload experience.</li>
      <li><strong>Residents</strong> &mdash; through the group&rsquo;s academy, under specialist
          supervision.</li>
      <li><strong>Interns and general practitioners</strong> wanting to build a dermatology caseload.</li>
      <li><strong>Veterinary nurses and technicians</strong> &mdash; dermatology nursing is a specialty
          of its own: cytology, ear procedures, diet-trial coaching and long-term case follow-up.</li>
      <li><strong>Client care and practice management</strong> for the Pune clinic.</li>
    </ul>
    <h2>What we offer</h2>
    <ul>
      <li>Structured education through the group&rsquo;s academy, and support for external
          certification.</li>
      <li>A specialist caseload from day one, fed by the group&rsquo;s referral network.</li>
      <li>Colleagues in ophthalmology, oncology, emergency, radiology, pathology and behaviour.</li>
    </ul>
    <div class="callout"><p>No vacancy that fits? Write to us anyway. Send a CV and a note about the
    kind of dermatology you want to do to
    <a href="mailto:careers@thedermatology.vet">careers@thedermatology.vet</a>.</p></div>
  </div></div>
</section>
"""))

    # ---------------- Contact ----------------
    written.append(page("contact.html", "Contact &ndash; The Dermatology Vet",
        "Book a specialist veterinary dermatology consultation, request a tele-consult, or refer a case "
        "to The Dermatology Vet.",
        page_head("Contact Us", "Book a consultation, request a tele-consult, or send us a referral.") + f"""
<section class="section">
  <div class="wrap">
    <div class="contact-grid">
      <div class="contact-info">
        <div class="info-block"><h3>Visit us</h3>
          <p>The Dermatology Vet<br>{"<br>".join(CLINIC["lines"])}</p>
          <p>{CLINIC['landmark']}</p>
          <ul class="icon-rows"><li>{ICON['pin']}<a href="{CLINIC['maps']}"{EXT}>Get directions</a></li></ul></div>
        <div class="info-block"><h3>Appointments</h3>
          <ul class="icon-rows">
            <li>{ICON['tel']}<a href="tel:{CONTACT['phone_href']}">{CONTACT['phone_display']}</a></li>
            <li>{ICON['wa']}<a href="{CONTACT['wa_href']}"{EXT}>WhatsApp</a></li>
            <li>{ICON['mail']}<a href="mailto:{CONTACT['email']}">{CONTACT['email']}</a></li>
          </ul></div>
        <div class="info-block"><h3>Referring vets</h3>
          <ul class="icon-rows">
            <li>{ICON['mail']}<a href="mailto:{CONTACT['referrals']}">{CONTACT['referrals']}</a></li>
            <li>{ICON['arrow']}<a href="tdv-connect.html">Send a case through TDV Connect</a></li>
          </ul></div>
      </div>
      <div id="teleconsult">
        <h2 class="form-title">Request an appointment</h2>
        <p>Tell us about the problem and we will come back with the first available appointment, or a
        tele-consult if that is the better place to start.</p>
        <form class="form" method="post" action="#" onsubmit="alert('Connect this form to your booking system or inbox before launch.');return false">
          <div class="form-row">
            <div class="field"><label for="c-name">Your name *</label><input id="c-name" name="name" required></div>
            <div class="field"><label for="c-phone">Phone *</label><input id="c-phone" name="phone" type="tel" required></div>
          </div>
          <div class="form-row">
            <div class="field"><label for="c-email">Email *</label><input id="c-email" name="email" type="email" required></div>
            <div class="field"><label for="c-where">How would you like to be seen?</label>
              <select id="c-where" name="where"><option>At the clinic in Pune</option><option>Tele-consult (outside Pune)</option></select></div>
          </div>
          <div class="form-row">
            <div class="field"><label for="c-species">Species</label>
              <select id="c-species" name="species"><option>Dog</option><option>Cat</option><option>Horse</option><option>Bird</option><option>Reptile</option><option>Small mammal</option><option>Other</option></select></div>
            <div class="field"><label for="c-vet">Your own vet&rsquo;s practice</label><input id="c-vet" name="vet"></div>
          </div>
          <div class="field"><label for="c-problem">What is the problem, and how long has it been going on? *</label>
            <textarea id="c-problem" name="problem" required></textarea></div>
          <button class="btn" type="submit">Request appointment {ARROW}</button>
          <p class="form-note">[[TODO]] Not connected. Point this at your booking system or
          {CONTACT['email']} before launch.</p>
        </form>
      </div>
    </div>
  </div>
</section>
<section class="section band">
  <div class="wrap"><div class="narrow">
    <div class="section-head"><h2>Before you book</h2></div>
    {faq_block(FAQ)}
  </div></div>
</section>
"""))

    return written
