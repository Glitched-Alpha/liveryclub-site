// "Leave the waitlist" link from waitlist emails: removes the person straight away.
(async () => {
  const title = document.querySelector("[data-leave-title]");
  const text = document.querySelector("[data-leave-text]");
  const home = document.querySelector("[data-leave-home]");
  const q = new URLSearchParams(location.search);
  const show = (t, p) => {
    title.textContent = t;
    text.textContent = p;
    home.hidden = false;
  };
  // Keep the link's details out of the address bar and history.
  history.replaceState(null, "", "/leave");
  try {
    const res = await fetch("https://imdoayrrwunixcybqaai.supabase.co/functions/v1/waitlist", {
      method: "POST",
      headers: {
        "content-type": "application/json",
        apikey: "sb_publishable_wy47W7AE1oeuAYOnt-bqFg_mIbZ5Cwl", // public by design
      },
      body: JSON.stringify({ action: "leave", id: q.get("id"), t: q.get("t") }),
    });
    if (res.ok) {
      show(
        "You've left the waitlist.",
        "We've removed your details and won't email you about Livery again. If you change your mind, you're always welcome back.",
      );
    } else {
      show(
        "That link didn't work.",
        "It may have already been used. If you're still getting emails, reply to one and we'll remove you.",
      );
    }
  } catch {
    show("Something went wrong.", "Please try the link again, or reply to any of our emails and we'll remove you.");
  }
})();
