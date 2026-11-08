// Livery — liveryclub.com

// Waitlist (Livery is invite-only until launch). Posts to the "waitlist" edge
// function in Livery's Supabase project; it answers { ok: true } either way.
const WAITLIST_URL = "https://imdoayrrwunixcybqaai.supabase.co/functions/v1/waitlist";
const PUBLISHABLE_KEY = "sb_publishable_wy47W7AE1oeuAYOnt-bqFg_mIbZ5Cwl"; // public by design
const SHARE_TEXT = "Livery: a private digital garage for UK drivers. Join the waitlist:";
const SITE = "https://liveryclub.com";

const plate = document.querySelector("[data-plate-input]");
if (plate) {
  plate.addEventListener("input", () => {
    const raw = plate.value
      .toUpperCase()
      .replace(/[^A-Z0-9]/g, "")
      .slice(0, 7);
    // Current-style plates read "AB12 CDE"; anything else is left as typed.
    plate.value = /^[A-Z]{2}\d{2}[A-Z]{1,3}$/.test(raw) ? `${raw.slice(0, 4)} ${raw.slice(4)}` : raw;
  });
}

// Launch: "Create my free garage" opens sign-up in the app, then Add vehicle
// with the reg filled in. Without JavaScript the form still opens sign-up.
for (const form of document.querySelectorAll("[data-start-form]")) {
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const reg = String(new FormData(form).get("reg") || "")
      .toUpperCase()
      .replace(/[^A-Z0-9]/g, "")
      .slice(0, 8);
    const url = new URL("https://app.liveryclub.com/auth");
    url.searchParams.set("mode", "signup");
    if (reg) url.searchParams.set("redirect", `/garage/new?reg=${reg}`);
    location.assign(url.toString());
  });
}

for (const box of document.querySelectorAll("[data-wl]")) {
  const wl = box.querySelector("[data-wl-form]");
  const done = box.querySelector("[data-wl-done]");
  const msg = wl.querySelector(".wl-msg");
  const btn = wl.querySelector('button[type="submit"]');
  const say = (text, bad) => {
    msg.textContent = text;
    msg.classList.toggle("bad", !!bad);
  };
  wl.addEventListener("submit", async (e) => {
    e.preventDefault();
    const f = new FormData(wl);
    const email = String(f.get("email") || "").trim();
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return say("Please enter a valid email address.", true);
    if (!f.get("consent")) return say("Please tick the box to join the waitlist.", true);
    btn.disabled = true;
    say("Adding you to the list…");
    try {
      const res = await fetch(WAITLIST_URL, {
        method: "POST",
        headers: { "content-type": "application/json", apikey: PUBLISHABLE_KEY },
        body: JSON.stringify({
          email,
          car: String(f.get("car") || "").replace(/\s/g, "") || undefined,
          first_name: String(f.get("first_name") || "").trim() || undefined,
          consent: true,
          company: String(f.get("company") || ""),
          source: new URLSearchParams(location.search).get("ref") || "liveryclub.com",
        }),
      });
      const data = await res.json().catch(() => ({}));
      if (!res.ok || !data.ok) throw new Error(data.error || "Something went wrong. Please try again.");
      done.querySelector("[data-wl-email]").textContent = email;
      wl.hidden = true;
      done.hidden = false;
      done.focus();
    } catch (err) {
      say(err.message || "Something went wrong. Please try again.", true);
    } finally {
      btn.disabled = false;
    }
  });

  const shareUrl = `${SITE}/?ref=share`;
  done.querySelector("[data-share-whatsapp]").href =
    `https://wa.me/?text=${encodeURIComponent(`${SHARE_TEXT} ${shareUrl}`)}`;
  done.querySelector("[data-share-x]").href =
    `https://x.com/intent/post?text=${encodeURIComponent(SHARE_TEXT)}&url=${encodeURIComponent(shareUrl)}`;
  done.querySelector("[data-share]").addEventListener("click", async (ev) => {
    const b = ev.currentTarget;
    try {
      if (navigator.share) {
        await navigator.share({ title: "Livery", text: SHARE_TEXT, url: shareUrl });
      } else {
        await navigator.clipboard.writeText(`${SHARE_TEXT} ${shareUrl}`);
        b.textContent = "Link copied";
      }
    } catch {
      /* closed the share sheet */
    }
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
