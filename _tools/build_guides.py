"""Builds the /guides pages, reusing the homepage header and footer. Run after editing them."""
import re, json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent  # run: python3 _tools/build_guides.py
idx = (root/"index.html").read_text()
header = re.search(r'    <header class="site-header">.*?</header>', idx, re.S).group(0)
footer = re.search(r'    <footer class="site-footer">.*?</footer>', idx, re.S).group(0)
csp = re.search(r'<meta\s+http-equiv="Content-Security-Policy".*?/>', idx, re.S).group(0)

def page(path, title, desc, body, ld):
    return f'''<!doctype html>
<html lang="en-GB">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
    {csp}
    <meta name="referrer" content="strict-origin-when-cross-origin" />
    <title>{title}</title>
    <meta name="description" content="{desc}" />
    <link rel="canonical" href="https://liveryclub.com{path}" />
    <meta name="theme-color" content="#f2ede5" media="(prefers-color-scheme: light)" />
    <meta name="theme-color" content="#1c1814" media="(prefers-color-scheme: dark)" />
    <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml" />
    <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png" />
    <meta property="og:type" content="article" />
    <meta property="og:site_name" content="Livery" />
    <meta property="og:locale" content="en_GB" />
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="{desc}" />
    <meta property="og:url" content="https://liveryclub.com{path}" />
    <meta property="og:image" content="https://liveryclub.com/assets/og.jpg" />
    <meta name="twitter:card" content="summary_large_image" />
    <link rel="preload" href="/fonts/fraunces.woff2" as="font" type="font/woff2" crossorigin />
    <link rel="preload" href="/fonts/instrument-sans.woff2" as="font" type="font/woff2" crossorigin />
    <link rel="stylesheet" href="/style.css" />
    <script type="application/ld+json">
{json.dumps(ld, indent=2, ensure_ascii=False)}
    </script>
  </head>
  <body>
    <a class="skip" href="#main">Skip to content</a>

{header}

    <main id="main">
{body}
    </main>

{footer}
    <script src="/nav.js" defer></script>
  </body>
</html>
'''

ORG = {"@type": "Organization", "@id": "https://liveryclub.com/#org", "name": "Livery", "url": "https://liveryclub.com/"}
crumbs = lambda items: {"@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": i+1, "name": n, "item": "https://liveryclub.com"+u} for i,(n,u) in enumerate(items)]}

# ── Guide: MOT history ──────────────────────────────────────────────
mot_path = "/guides/check-mot-history/"
mot_title = "How to check your car's MOT history (and what advisories mean)"
mot_desc = "Check any car's MOT history free in under a minute. What dangerous, major, minor and advisory items mean, and what to look for before you buy."
mot_body = '''      <article class="article wrap">
        <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Livery</a> <span aria-hidden="true">/</span> <a href="/guides/">Guides</a></nav>
        <p class="eyebrow">Guide · 4 min read</p>
        <h1>How to check your car's MOT history, and what it's actually telling you</h1>
        <p class="article-meta">By Aniket Chakraborty, founder of Livery · Updated <time datetime="2026-11-04">4 November 2026</time></p>

        <p class="article-lede">Your car's MOT history is one of the most useful free records there is. It shows every test the car has had, what it failed on, what the tester flagged and the mileage each time. Here's how to find it and how to read it.</p>

        <h2 id="how">How to check it</h2>
        <div class="steps-pair">
          <div class="step-card">
            <h3>Quick one-off check</h3>
            <p>Go to <a href="https://www.gov.uk/check-mot-history" rel="noopener">Check the MOT history of a vehicle</a> on GOV.UK and enter the registration. It's free, and you don't need to own the car.</p>
          </div>
          <div class="step-card step-card-livery">
            <h3>Keep it with everything else</h3>
            <p>In Livery, add your car by its plate and its MOT history sits alongside your MOT and tax reminders, service records and receipts, so you never have to look it up again.</p>
            <a class="btn btn-primary" href="/?ref=guide-mot#waitlist">Join the waitlist</a>
            <p class="small">Livery is opening soon.</p>
          </div>
        </div>
        <p>For cars in England, Scotland and Wales you'll see results back to 2005. In Northern Ireland, results go back to 2017. To download the actual certificates or see which garage did each test (England, Scotland and Wales only), you'll also need the 11-digit reference number from the V5C logbook.</p>

        <h2 id="results">What the results mean</h2>
        <p>Since May 2018, problems found at an MOT are sorted into categories:</p>
        <dl class="defects">
          <div class="defect defect-dangerous"><dt>Dangerous</dt><dd>An immediate risk to road safety or a serious environmental issue. It's a fail, and the car shouldn't be driven until it's fixed.</dd></div>
          <div class="defect defect-major"><dt>Major</dt><dd>Could affect safety, other road users or the environment. It's a fail, and it needs repairing straight away.</dd></div>
          <div class="defect defect-minor"><dt>Minor</dt><dd>Little or no effect on safety. The car passes, but get it repaired as soon as you can.</dd></div>
          <div class="defect defect-advisory"><dt>Advisory</dt><dd>Something that could get worse. The car passes, but keep an eye on it.</dd></div>
        </dl>
        <p>Advisories are where most people get caught out. A tyre "close to the legal limit" or brake pads "wearing thin" this year is often next year's fail.</p>

        <h2 id="buying">What to look for when buying a used car</h2>
        <ul>
          <li><strong>Mileage that goes backwards, or jumps oddly.</strong> Each test records the mileage, so a drop between tests is a big warning sign.</li>
          <li><strong>The same advisory year after year.</strong> Repeated "corrosion" or "oil leak" notes suggest a problem that's never been fixed.</li>
          <li><strong>Gaps.</strong> A missing year can mean the car was off the road, or driven without an MOT. Ask the seller why.</li>
          <li><strong>Lots of fails on the same item.</strong> Suspension or brake parts failing again and again can point to a bigger issue.</li>
        </ul>

        <h2 id="record">Keep your own record</h2>
        <p>The MOT history only covers the test itself. It won't show the services, repairs and receipts in between, and those are what prove a car has been looked after.</p>
        <p>Livery keeps it all together: your MOT and tax dates with a reminder before they're due, your car's MOT history, and every service, repair and receipt in one history file.</p>

        <aside class="article-cta">
          <h2>Be one of the first in.</h2>
          <p>Livery is opening soon, by invite. Join the waitlist and add your plate, and your car will be waiting in your garage.</p>
          <a class="btn btn-primary" href="/?ref=guide-mot#waitlist">Join the waitlist</a>
        </aside>

        <p class="article-sources">Sources: <a href="https://www.gov.uk/check-mot-history" rel="noopener">GOV.UK, Check the MOT history of a vehicle</a>; <a href="https://www.gov.uk/government/publications/mot-changes-from-may-2018-guidance-for-mot-testers/overview-of-mot-changes-from-may-2018" rel="noopener">GOV.UK, MOT changes from May 2018</a>.</p>
      </article>'''
mot_ld = {"@context": "https://schema.org", "@graph": [
  {"@type": "Article", "@id": "https://liveryclub.com"+mot_path+"#article", "headline": mot_title, "description": mot_desc,
   "inLanguage": "en-GB", "datePublished": "2026-11-04", "dateModified": "2026-11-04",
   "author": {"@type": "Person", "name": "Aniket Chakraborty", "jobTitle": "Founder, Livery"},
   "publisher": ORG, "mainEntityOfPage": "https://liveryclub.com"+mot_path, "image": "https://liveryclub.com/assets/og.jpg"},
  crumbs([("Livery","/"),("Guides","/guides/"),("Check MOT history", mot_path)])]}
(root/"guides/check-mot-history/index.html").write_text(page(mot_path, mot_title+" | Livery", mot_desc, mot_body, mot_ld))

# ── Guides index ───────────────────────────────────────────────────
g_path = "/guides/"
g_title = "Car ownership guides | Livery"
g_desc = "Plain-English guides to owning a car in the UK: MOT history, service records, modifications and running costs."
g_body = '''      <section class="article wrap">
        <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Livery</a></nav>
        <p class="eyebrow">Guides</p>
        <h1>Car ownership, explained.</h1>
        <p class="article-lede">Plain-English guides to the parts of owning a car that are easy to forget, from MOTs to service history.</p>
        <div class="guide-list">
          <a class="guide-card" href="/guides/check-mot-history/">
            <p class="eyebrow">MOT · 4 min read</p>
            <h2>How to check your car's MOT history, and what it's actually telling you</h2>
            <p>Find any car's MOT history for free, what dangerous, major, minor and advisory items mean, and what to look for before you buy.</p>
            <span class="guide-more">Read the guide →</span>
          </a>
        </div>
      </section>'''
g_ld = {"@context": "https://schema.org", "@graph": [
  {"@type": "CollectionPage", "name": g_title, "url": "https://liveryclub.com"+g_path, "inLanguage": "en-GB", "publisher": ORG},
  crumbs([("Livery","/"),("Guides", g_path)])]}
(root/"guides/index.html").write_text(page(g_path, g_title, g_desc, g_body, g_ld))
print("ok")
