// Livery — monthly / annual switch on the pricing section.
const PRICES = {
  monthly: {
    from: false,
    amt: "£5.99",
    per: "a month",
    note: "Billed monthly. Cancel any time.",
    foot: "£5.99 a month",
  },
  annual: {
    from: true,
    amt: "£4.17",
    per: "a month",
    note: "£49.99 billed yearly. Save 30% on monthly.",
    foot: "£4.17 a month, billed yearly",
  },
};

const billing = document.querySelector("[data-billing]");
if (billing) {
  const buttons = [...billing.querySelectorAll("[data-period]")];
  const set = (period) => {
    const p = PRICES[period];
    for (const b of buttons) b.setAttribute("aria-checked", String(b.dataset.period === period));
    document.querySelector("[data-from]").hidden = !p.from;
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
