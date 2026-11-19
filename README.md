# Final Form Physique

One-to-one coaching site for Dallas Botchway, with a quiz funnel. Static site, no build step for the main pages.

## The funnel

The quiz on `index.html` asks: goal, training experience, when they want to start, budget, then name, email, phone and Instagram (optional). Every answer is saved to the REPS dashboard as a lead, tagged with where the person was sent.

Where they go depends on budget and goal:

| Budget | Goal | Lands on |
| --- | --- | --- |
| Under $100 a month | Fat loss | `fat-loss.html`, the one-off 12-week fat loss program |
| Under $100 a month | Build muscle | `build-muscle.html`, the one-off 12-week build muscle program |
| Under $100 a month | Men's physique | `mens-physique.html`, the one-off 12-week men's physique program |
| $150+ or $200+ a month | Any | `book-call.html`, "we can help", with the Calendly booking embedded |

Once someone books on `book-call.html`, they're sent to `call-booked.html`: the call confirmation, a video from Dallas and a button to confirm the call on WhatsApp.

Name and email from the quiz are pre-filled into Calendly so nobody types them twice.

## Settings: `js/config.js`

Every link and number lives in this one file, and every page reads from it. Anything left empty is hidden.

- `leadsEndpoint`, `client`: the REPS dashboard. `client` must match Dallas's slug there (currently `finalform`).
- `calendly`: the Calendly event link. Until set, the call page says booking opens shortly.
- `whatsapp`: Dallas's number, digits only with country code.
- `checkout`: checkout links for the three one-off programs.
- `price`: the price shown on each program page, e.g. `"$79"`.
- `callVideo`: a YouTube or Vimeo link, or an `.mp4` path, for the call-booked page. Until set, a photo of Dallas shows.

**Calendly redirect:** the call page watches for Calendly's "booked" message and moves people to `call-booked.html` itself. As a backup, also set the event's confirmation page in Calendly (Event settings > Confirmation page > Redirect to an external site) to `https://YOUR-DOMAIN/call-booked.html`.

## Files

| Path | What it is |
| --- | --- |
| `index.html` | Homepage and quiz |
| `fat-loss.html`, `build-muscle.html`, `mens-physique.html` | One-off program pages. **Generated:** edit the copy in `scripts/build_goals.py`, then run `python3 scripts/build_goals.py` |
| `book-call.html` | Thank-you page for higher budgets, with the Calendly embed |
| `call-booked.html` | Call confirmation, video and WhatsApp |
| `js/config.js` | All links and numbers |
| `css/site.css` | Styles shared by every page |
| `images/` | Dallas's photos, the FF mark and icons |

## Hosting

`wrangler.jsonc` deploys the folder as static assets on Cloudflare. `.nojekyll` lets GitHub Pages serve it as is.
