"""Builds the three one-off program pages. The quiz sends people here when
their budget is under $100, to the page for the goal they picked.
Checkout links, prices and WhatsApp live in js/config.js.

Edit the copy in GOALS below, then run from the repo root:
    python3 scripts/build_goals.py
"""
import html, json, os


GOALS = {
  "fat-loss": {
    "name": "Fat Loss",
    "photo": "kb-overhead.webp",
    "photo_alt": "Dallas pressing a kettlebell overhead",
    "photo_pos": "50% 30%",
    "lead": "Built to strip body fat while holding on to the muscle you've worked for, so the effort you're putting in finally shows.",
    "includes": [
      ("12 weeks of training", "Written by Dallas to keep your muscle while you lean out, session by session."),
      ("Nutrition and macro targets", "A deficit you can actually live with. No starving, no cutting out everything you enjoy."),
      ("Steps and cardio set for you", "Exactly how much to do and when, so you're not guessing on the treadmill."),
      ("Exercise demos", "See how every movement should be done, so every rep counts."),
      ("Progression built in", "Each block builds on the last, so the fat keeps coming off."),
      ("Yours to keep", "Pay once, no subscription. Run it at your own pace."),
    ],
    "phases": [
      ("Weeks 1 to 4", "Set the foundation", "Nutrition dialled in, training baseline set and the daily habits that make fat loss stick."),
      ("Weeks 5 to 8", "Push the drop", "The deficit tightened where it's needed while training keeps progressing, so the scale and the mirror both move."),
      ("Weeks 9 to 12", "Reveal it", "The final push for definition, then a plan to keep the results once the 12 weeks are done."),
    ],
  },
  "build-muscle": {
    "name": "Build Muscle",
    "photo": "pushdown.webp",
    "photo_alt": "Dallas doing a cable pushdown",
    "photo_pos": "50% 25%",
    "lead": "Built to add real size, with training that progresses every week and food that fuels the growth instead of just adding fat.",
    "includes": [
      ("12 weeks of hypertrophy training", "Written by Dallas to add real size, session by session."),
      ("Nutrition built for growth", "A surplus that adds muscle, not just weight, with macro targets to hit."),
      ("Progressive overload built in", "Every session builds on the last, so you're always heading somewhere."),
      ("Exercise demos", "See how every movement should be done, so every rep counts."),
      ("Weak-point focus", "Lagging body parts brought up, so the whole physique grows in proportion."),
      ("Yours to keep", "Pay once, no subscription. Run it at your own pace."),
    ],
    "phases": [
      ("Weeks 1 to 4", "Build the base", "Technique tightened, baseline lifts set and eating to grow without overdoing it."),
      ("Weeks 5 to 8", "Progress", "Volume and load climb week to week, and your food adjusts as your bodyweight moves."),
      ("Weeks 9 to 12", "Push", "A peak block to drive the biggest gains of the program, then a plan for what comes next."),
    ],
  },
  "mens-physique": {
    "name": "Men's Physique",
    "photo": "hero-studio.webp",
    "photo_alt": "Dallas Botchway, studio shot on black",
    "photo_pos": "50% 15%",
    "lead": "Built around the look the division rewards: wide shoulders, a tight waist and conditioning that holds up. Written by a pro who's won on that stage.",
    "includes": [
      ("12 weeks of physique training", "Shoulders, lats and the V-taper prioritised, written by an IFBB Pro."),
      ("Nutrition for lean mass", "Macros set to build the right muscle while keeping you sharp and conditioned."),
      ("Weak-point programming", "The areas that hold most physiques back get brought up first."),
      ("Exercise demos", "See how every movement should be done, so every rep counts."),
      ("Conditioning built in", "Cardio and steps that sharpen you up without eating into your gains."),
      ("Yours to keep", "Pay once, no subscription. Run it at your own pace."),
    ],
    "phases": [
      ("Weeks 1 to 4", "Assess and build", "Your weak points identified, your baseline set and your nutrition dialled in."),
      ("Weeks 5 to 8", "Shape", "V-taper focus, with conditioning ramping up as the physique comes together."),
      ("Weeks 9 to 12", "Sharpen", "Conditioning and presentation sharpened, with clear next steps on or off the stage."),
    ],
  },
}

TICK = '<span class="ff-tick"><svg viewBox="0 0 12 12" aria-hidden="true"><path d="M1.6 6.2 4.4 9 10.4 3"/></svg></span>'
WA = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>'

e = html.escape

def page(slug, g):
    title = f"Your 12-Week {g['name']} Program"
    inc = "\n".join(f'          <li>{TICK}<div><b>{e(a)}</b><span class="t">{e(b)}</span></div></li>' for a, b in g["includes"])
    ph = "\n".join(f'''        <div class="ff-step">
          <div class="ff-step-n">{i+1:02d}</div>
          <p class="ff-micro" style="margin-bottom:.5rem">{e(w)}</p>
          <h3 class="ff-h3">{e(t)}</h3>
          <p>{e(d)}</p>
        </div>''' for i, (w, t, d) in enumerate(g["phases"]))
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} | Final Form Physique</title>
<meta name="robots" content="noindex">
<meta name="theme-color" content="#0A0A0A">
<link rel="icon" type="image/png" href="images/favicon.png">
<link rel="apple-touch-icon" href="images/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@300;400;500;600;700&family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/site.css">
<script src="js/config.js"></script>
</head>
<body>
<!-- Generated by scripts/build_goals.py. Edit the copy there, not here. -->
<div id="ff-page">

  <div class="ff-nav-wrap">
    <nav class="ff-nav">
      <a href="index.html" class="ff-brand"><img src="images/logo-mark.png" alt="Final Form Physique"><span>Final Form</span></a>
      <a href="#next" class="ff-btn ff-btn-solid ff-btn-sm">Get The Program</a>
    </nav>
  </div>

  <header class="ff-hero ff-ty-hero">
    <div class="ff-shell ff-hero-grid">
      <div>
        <p class="ff-lead" id="ffHello" style="margin-bottom:1.2rem;color:#fff;font-weight:600">Thanks for applying.</p>
        <h1 class="ff-h1"><span class="thin">This is</span><br><span class="red">for you.</span></h1>
        <p class="ff-lead" style="margin:1.4rem 0 1.2rem">One-to-one coaching isn't the right fit for your budget right now. So here's the next best thing: Dallas's plan for your goal, at a fraction of the cost of coaching.</p>
        <p class="ff-h3" style="margin:0 0 1rem">{e(title.replace("Your ", "The "))}</p>
        <p class="ff-lead" style="margin-bottom:2.2rem">{e(g["lead"])}</p>
        <div class="ff-hero-btns">
          <a href="#next" class="ff-btn ff-btn-solid">Get The Program</a>
          <a href="#included" class="ff-btn ff-btn-line">What's Included &#8595;</a>
        </div>
      </div>
      <div class="ff-hero-photo">
        <img src="images/photos/{g["photo"]}" alt="{e(g["photo_alt"])}" style="object-position:{g["photo_pos"]}">
        <div class="ff-hero-badge"><b>12 Weeks</b>Custom {e(g["name"])}</div>
      </div>
    </div>
  </header>

  <section class="ff-sec ff-sec-alt" id="included">
    <div class="ff-shell">
      <div class="ff-head-split">
        <h2 class="ff-h2"><span class="thin">What's in your</span><br>12 weeks</h2>
        <p class="ff-note">Everything you need to run the full 12 weeks, written by Dallas.</p>
      </div>
      <ul class="ff-includes">
{inc}
      </ul>
    </div>
  </section>

  <section class="ff-sec">
    <div class="ff-shell">
      <div class="ff-head-split">
        <h2 class="ff-h2"><span class="thin">How the</span><br>12 weeks run</h2>
        <p class="ff-note">Three blocks, each one building on the last.</p>
      </div>
      <div class="ff-steps">
{ph}
      </div>
    </div>
  </section>

  <section class="ff-sec" id="next" style="padding-top:0">
    <div class="ff-shell">
      <div class="ff-next">
        <div>
          <h2 class="ff-h2"><span class="thin">Start your</span><br>12 weeks today</h2>
          <p>Everything above, ready the moment you check out. One payment, no subscription. When you're ready for one-to-one coaching, you can apply again any time.</p>
          <p class="ff-h2" id="ffPrice" style="margin-top:1.4rem"></p>
        </div>
        <div class="ff-next-actions">
          <a class="ff-btn ff-btn-white" id="ffBuy" href="#" target="_blank" rel="noopener">Get The Program</a>
          <a class="ff-btn ff-wa" id="ffWhatsApp" href="#" target="_blank" rel="noopener">{WA}Questions? WhatsApp Dallas</a>
          <p class="ff-next-note" id="ffBuyNote">Secure checkout. Instant access.</p>
        </div>
      </div>
    </div>
  </section>

  <footer>
    <div class="ff-shell">
      <div class="ff-foot-top">
        <div>
          <a href="index.html" class="ff-brand"><img src="images/logo-mark.png" alt="Final Form Physique"><span>Final Form Physique</span></a>
          <p>Transforming your physique to its final form. One-to-one coaching with IFBB Pro Dallas Botchway.</p>
        </div>
      </div>
      <div class="ff-wordmark">Final Form</div>
      <div class="ff-foot-bottom">
        <span>&copy; <span class="ff-year">2026</span> Final Form Physique. All rights reserved.</span>
        <span>Built for the ones who put the work in.</span>
      </div>
    </div>
  </footer>

</div>

<script>
(function () {{
  "use strict";

  var CFG = window.FF_CONFIG || {{}};
  var SLUG = {json.dumps(slug)};
  var FF_PROGRAM = {json.dumps(g["name"])};
  var buyUrl = (CFG.checkout || {{}})[SLUG] || '';
  var price = (CFG.price || {{}})[SLUG] || '';

  document.querySelectorAll('.ff-year').forEach(function (el) {{ el.textContent = new Date().getFullYear(); }});

  var name = (new URLSearchParams(window.location.search).get('name') || '').replace(/[^\\p{{L}}' -]/gu, '').trim().slice(0, 40);
  if (name) document.getElementById('ffHello').textContent = 'Thanks for applying, ' + name + '.';

  var priceEl = document.getElementById('ffPrice');
  if (price) priceEl.textContent = price; else priceEl.remove();

  /* Until a checkout link is set, the buy buttons are hidden and the
     panel points people to WhatsApp instead. */
  var buy = document.getElementById('ffBuy');
  if (buyUrl) {{
    buy.href = buyUrl;
    document.querySelectorAll('a[href="#next"]').forEach(function (a) {{ a.href = buyUrl; a.target = '_blank'; a.rel = 'noopener'; }});
  }} else {{
    buy.remove();
    document.getElementById('ffBuyNote').textContent = "Checkout opens soon. We'll be in touch on the number you gave us.";
  }}

  var wa = document.getElementById('ffWhatsApp');
  if (CFG.whatsapp) {{
    var note = 'Hi Dallas, ' + (name ? "it's " + name + '. ' : '') + 'I just did the quiz on your website and I have a question about the 12-week ' + FF_PROGRAM.toLowerCase() + ' program.';
    wa.href = 'https://wa.me/' + CFG.whatsapp.replace(/[^0-9]/g, '') + '?text=' + encodeURIComponent(note);
  }} else {{
    wa.remove();
  }}
}})();
</script>
</body>
</html>
'''

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
for slug, g in GOALS.items():
    with open(os.path.join(root, slug + ".html"), "w") as f:
        f.write(page(slug, g))
    print("wrote", slug + ".html")
