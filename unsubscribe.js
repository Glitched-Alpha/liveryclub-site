// "Unsubscribe from tips and news" link in Livery emails: turns them off straight away.
(async () => {
  const title = document.querySelector("[data-unsub-title]");
  const text = document.querySelector("[data-unsub-text]");
  const home = document.querySelector("[data-unsub-home]");
  const q = new URLSearchParams(location.search);
  const show = (t, p) => {
    title.textContent = t;
    text.textContent = p;
    home.hidden = false;
  };
  // Keep the link's details out of the address bar and history.
  history.replaceState(null, "", "/unsubscribe");
  try {
    const res = await fetch("https://imdoayrrwunixcybqaai.supabase.co/functions/v1/welcome-email", {
      method: "POST",
      headers: {
        "content-type": "application/json",
        apikey: "sb_publishable_wy47W7AE1oeuAYOnt-bqFg_mIbZ5Cwl", // public by design
      },
      body: JSON.stringify({ action: "unsubscribe", id: q.get("id"), t: q.get("t") }),
    });
    if (res.ok) {
      show(
        "You're unsubscribed.",
        "You won't get tips and news from Livery any more. You'll still get emails you need for your account, like password resets. You can turn tips back on in Account whenever you like.",
      );
    } else {
      show(
        "That link didn't work.",
        "It may have already been used. If you're still getting emails, reply to one and we'll sort it.",
      );
    }
  } catch {
    show("Something went wrong.", "Please try the link again, or reply to any of our emails and we'll sort it.");
  }
})();
