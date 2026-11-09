// Livery — monthly / annual switch on the pricing section.
// The launch offer (£39.99 a year) ends at UK midnight at the end of 31 January;
// after that the page shows £49.99 by itself. Keep in step with the app
// (app_settings.billing.early_price_until).
const OFFER_ENDS = new Date("2027-02-01T00:00:00Z");
const offerOn = Date.now() < OFFER_ENDS.getTime();

const PRICES = {
  monthly: {
    was: "",
    amt: "£5.99",
    per: "a month",
    note: "Billed monthly. History checks £3.99 each. Cancel any time to stop it renewing.",
    foot: "£5.99 a month",
  },
  annual: offerOn
    ? {
        was: "£4.17",
        amt: "£3.33",
        per: "a month",
        note: "Billed £39.99 yearly (usually £49.99), with 3 full history checks a year included. Launch offer until 31 January; your price stays while you're subscribed.",
        foot: "£3.33 a month, billed £39.99 yearly",
      }
    : {
        was: "",
        amt: "£4.17",
        per: "a month",
        note: "Billed £49.99 yearly, with 3 full history checks a year included. Save 30% on monthly.",
        foot: "£4.17 a month, billed £49.99 yearly",
      },
};

if (!offerOn) {
  for (const el of document.querySelectorAll("[data-offer]")) el.hidden = true;
  const save = document.querySelector("[data-save]");
  if (save) save.textContent = "Save 30%";
}

const billing = document.querySelector("[data-billing]");
if (billing) {
  const buttons = [...billing.querySelectorAll("[data-period]")];
  const set = (period) => {
    const p = PRICES[period];
    for (const b of buttons) b.setAttribute("aria-checked", String(b.dataset.period === period));
    const was = document.querySelector("[data-was]");
    if (was) {
      was.textContent = p.was;
      was.hidden = !p.was;
    }
    document.querySelector("[data-amt]").textContent = p.amt;
    document.querySelector("[data-per]").textContent = p.per;
    document.querySelector("[data-note]").textContent = p.note;
    document.querySelector("[data-foot-price]").textContent = p.foot;
  };
  for (const b of buttons) b.addEventListener("click", () => set(b.dataset.period));
  // Arrow keys move between the two options, as in a radio group.
  billing.addEventListener("keydown", (e) => {
    if (!["ArrowLeft", "ArrowRight", "ArrowUp", "ArrowDown"].includes(e.key)) return;
    e.preventDefault();
    const next = buttons.find((b) => b.getAttribute("aria-checked") !== "true");
    set(next.dataset.period);
    next.focus();
  });
}

// Show the right annual price straight away (matters once the offer has ended).
if (billing) {
  const annual = billing.querySelector('[data-period="annual"]');
  if (annual?.getAttribute("aria-checked") === "true") annual.click();
}
