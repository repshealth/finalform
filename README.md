# Final Form Physique

Landing page for Dallas Botchway's Final Form Physique app. Same layout and sections as the Physique X page, rebranded in the FF logo colours (black, white and red #BD3C2C).

Static site, no build step. Open `index.html` and it runs.

## Files

| Path | What it is |
| --- | --- |
| `index.html` | The whole page: styles, content and script |
| `images/photos/` | Dallas's photos |
| `images/app/` | App screenshots. **Placeholders** borrowed from other clients' builds until Dallas's own screens are ready. Swap them in with the same file names (440 x 956) |
| `images/logo-mark.png` | The FF mark on a transparent background (nav and footer) |
| `images/favicon.png`, `apple-touch-icon.png`, `app-icon.png` | Icons from the app icon |
| `wrangler.jsonc` | Cloudflare settings, for deploying as static assets |
| `.nojekyll` | Lets GitHub Pages serve the files as they are |

## Still to fill in

All the settings live at the top of the `<script>` block at the bottom of `index.html`:

- `FF_CHECKOUT`: checkout links for the monthly, 3 month and annual plans. Until set, the plan buttons scroll to the quiz.
- `FF_WHATSAPP`: Dallas's number, digits only with country code. Until set, the WhatsApp button is hidden.
- `FF_INSTAGRAM`: his profile URL. Until set, the footer link is hidden.
- `FF_CLIENT`: the client slug in the REPS dashboard (currently `finalform`). Quiz leads post to the dashboard's `/api/forms` under this slug, so it needs to match his account there.

Also placeholders:

- **Prices** ($19.99 / $49.99 / $149.99) in the pricing section and the quiz result. Search for `PLACEHOLDER PRICES`.
- **App screenshots** in `images/app/`.
