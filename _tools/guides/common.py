"""Shared bits for guide text: the Livery box and app links (no tracking parameters)."""
import html

APP = "https://app.liveryclub.com"
SIGNUP = f"{APP}/auth?mode=signup"
SIGNUP_CHECK = f"{APP}/auth?mode=signup&redirect=%2Fcheck"
SIGNUP_PLUS = f"{APP}/auth?mode=signup&redirect=%2Fplus"

MARK = ('<svg viewBox="0 0 100 100" aria-hidden="true"><rect width="100" height="100" rx="23" fill="#F2EDE5" />'
        '<g fill="none" stroke-linecap="round"><path d="M27 15 V44 A33 33 0 0 0 60 77 H88" stroke="#2A231E" stroke-width="10" />'
        '<path d="M40 15 V44 A20 20 0 0 0 60 64 H88" stroke="#8E5E3B" stroke-width="6" />'
        '<path d="M50 15 V44 A10 10 0 0 0 60 54 H88" stroke="#4F5A43" stroke-width="3" /></g></svg>')


def livery(title, text, button="Create my free garage", href=SIGNUP):
    """A 'How Livery helps' box inside a guide."""
    paras = "".join(f"\n          <p>{p}</p>" for p in ([text] if isinstance(text, str) else text))
    return f'''        <div class="livery-box">
          <h3>{MARK} {title}</h3>{paras}
          <a class="btn btn-primary" href="{html.escape(href, quote=True)}">{button}</a>
        </div>'''
