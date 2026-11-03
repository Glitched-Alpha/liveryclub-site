// Livery — liveryclub.com
const APP = "https://app.liveryclub.com";

// Header hairline once the page scrolls.
const header = document.querySelector(".site-header");
const onScroll = () => header.classList.toggle("scrolled", window.scrollY > 8);
onScroll();
window.addEventListener("scroll", onScroll, { passive: true });

// Number plate: format as typed, then start sign-up with that car ready to add.
const form = document.querySelector("[data-plate]");
if (form) {
  const input = form.querySelector("input");
  input.addEventListener("input", () => {
    const raw = input.value
      .toUpperCase()
      .replace(/[^A-Z0-9]/g, "")
      .slice(0, 7);
    // Current-style plates read "AB12 CDE"; anything else is left as typed.
    input.value = /^[A-Z]{2}\d{2}[A-Z]{1,3}$/.test(raw)
      ? `${raw.slice(0, 4)} ${raw.slice(4)}`
      : raw;
  });
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const reg = input.value.replace(/\s/g, "");
    const next = reg.length >= 2 ? `/garage/new?reg=${encodeURIComponent(reg)}` : "/garage/new";
    window.location.href = `${APP}/auth?mode=signup&redirect=${encodeURIComponent(next)}`;
  });
}

// Key-date dials fill once, when they come into view.
const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const C = 2 * Math.PI * 42;
const rings = [...document.querySelectorAll(".dial .value")];
const fill = (ring, frac) => {
  ring.style.strokeDasharray = `${C * frac} ${C}`;
};
rings.forEach((r) => {
  fill(r, reduce ? Number(r.dataset.frac) : 0);
  if (!reduce) r.style.transition = "stroke-dasharray 1.4s cubic-bezier(0.32, 0.72, 0, 1)";
});
if (!reduce && "IntersectionObserver" in window) {
  const io = new IntersectionObserver(
    (entries) => {
      if (!entries.some((e) => e.isIntersecting)) return;
      rings.forEach((r, i) => setTimeout(() => fill(r, Number(r.dataset.frac)), i * 120));
      io.disconnect();
    },
    { threshold: 0.4 },
  );
  const dials = document.querySelector(".dials");
  if (dials) io.observe(dials);
} else {
  rings.forEach((r) => fill(r, Number(r.dataset.frac)));
}

const year = document.querySelector("[data-year]");
if (year) year.textContent = String(new Date().getFullYear());
