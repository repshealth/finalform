/* ==================================================================
   FINAL FORM PHYSIQUE  |  site settings
   Every page reads from here, so each link only needs setting once.
   Anything left empty is hidden on the page.
   ================================================================== */
window.FF_CONFIG = {

  /* REPS dashboard: where quiz leads are saved. FF client slug must
     match Dallas's account in the dashboard. */
  leadsEndpoint: "https://dashboard.jolly-heart-2b8d.workers.dev/api/forms",
  client: "finalform",

  /* Calendly event link for the coaching call, e.g.
     "https://calendly.com/finalform/coaching-call".
     It is embedded on book-call.html. */
  calendly: "",

  /* Dallas's WhatsApp number, digits only with country code,
     e.g. "15551234567". Used on the call-booked page and the
     one-off program pages. */
  whatsapp: "",

  /* Checkout links for the one-off 12-week programs (people whose
     budget is under $100 land on these). */
  checkout: {
    "fat-loss":      "",
    "build-muscle":  "",
    "mens-physique": ""
  },

  /* Prices shown on the one-off program pages, e.g. "$79".
     Leave empty to show no price. */
  price: {
    "fat-loss":      "",
    "build-muscle":  "",
    "mens-physique": ""
  },

  /* Video on the call-booked page. A YouTube or Vimeo link, or a path
     to an .mp4 in this repo (e.g. "videos/welcome.mp4"). */
  callVideo: ""
};
