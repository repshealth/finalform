# Final Form Physique

One-to-one coaching site for Dallas Botchway, with a quiz funnel that sends each lead to a goal page. Static site, no build step for the homepage.

## Pages

| Page | What it is |
| --- | --- |
| `index.html` | Homepage: one-to-one coaching, the three programs, how it works, Meet Dallas, FAQ and the quiz |
| `fat-loss.html` | Where the quiz sends people who pick **Fat loss**: the 12-week custom fat loss program |
| `build-muscle.html` | Same for **Build muscle** |
| `mens-physique.html` | Same for **Men's physique** |
| `css/site.css` | Styles shared by all four pages |
| `images/` | Dallas's photos, the FF mark and the icons |

## The quiz

Five steps: goal, training experience, when they want to start, monthly budget, then name, email, phone and Instagram (optional).
Clicking a program card on the homepage starts the quiz with that goal already picked.

On submit the lead posts to the REPS dashboard (`FF_LEADS_ENDPOINT`, client `FF_CLIENT = "finalform"`) with every answer attached, then the person lands on their goal page with their first name in the URL so the page greets them.
`FF_CLIENT` has to match Dallas's client slug in the dashboard. Both settings are at the top of the script in `index.html`.

## The goal pages

These are generated. Edit the copy in `scripts/build_goals.py`, then run:

    python3 scripts/build_goals.py

Settings at the top of that file:

- `BOOKING`: a call booking link (e.g. Calendly). Empty hides the button.
- `WHATSAPP`: Dallas's number, digits only with country code. Empty hides the button.

With both empty, the "What happens now" panel just tells them the team will be in touch.

## Hosting

`wrangler.jsonc` deploys the folder as static assets on Cloudflare. `.nojekyll` lets GitHub Pages serve it as is.
