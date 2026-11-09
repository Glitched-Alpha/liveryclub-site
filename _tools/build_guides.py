"""Builds every page under /guides, reusing the homepage header, footer and CSP.

Run after editing a guide or the homepage header/footer:
    python3 _tools/build_guides.py

Guide content lives in _tools/guides_content.py. Each guide gets: canonical URL,
Open Graph tags, Article + BreadcrumbList (+ FAQPage) structured data, a contents
list, related guides, and a sitemap entry. Links into the app are plain (no
tracking parameters), so Google sees one URL per page.
"""
import html
import json
import pathlib
import re
import sys

root = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from guides_content import GUIDES  # noqa: E402

SITE = "https://liveryclub.com"
APP = "https://app.liveryclub.com"
SIGNUP = f"{APP}/auth?mode=signup"
AUTHOR = {"@type": "Person", "name": "Aniket Chakraborty", "jobTitle": "Founder, Livery"}
ORG = {"@type": "Organization", "@id": f"{SITE}/#org", "name": "Livery", "url": f"{SITE}/"}

idx = (root / "index.html").read_text()
header = re.search(r'    <header class="site-header">.*?</header>', idx, re.S).group(0)
footer = re.search(r'    <footer class="site-footer">.*?</footer>', idx, re.S).group(0)
csp = re.search(r'<meta\s+http-equiv="Content-Security-Policy".*?/>', idx, re.S).group(0)

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"]


def long_date(iso):
    y, m, d = (int(x) for x in iso.split("-"))
    return f"{d} {MONTHS[m - 1]} {y}"


def crumbs(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u}
        for i, (n, u) in enumerate(items)]}


def page(path, title, desc, body, ld, og_type="article"):
    t, d = html.escape(title, quote=True), html.escape(desc, quote=True)
    return f'''<!doctype html>
<html lang="en-GB">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
    {csp}
    <meta name="referrer" content="strict-origin-when-cross-origin" />
    <title>{t}</title>
    <meta name="description" content="{d}" />
    <link rel="canonical" href="{SITE}{path}" />
    <meta name="theme-color" content="#f2ede5" media="(prefers-color-scheme: light)" />
    <meta name="theme-color" content="#1c1814" media="(prefers-color-scheme: dark)" />
    <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml" />
    <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png" />
    <meta property="og:type" content="{og_type}" />
    <meta property="og:site_name" content="Livery" />
    <meta property="og:locale" content="en_GB" />
    <meta property="og:title" content="{t}" />
    <meta property="og:description" content="{d}" />
    <meta property="og:url" content="{SITE}{path}" />
    <meta property="og:image" content="{SITE}/assets/og.jpg" />
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


def words(s):
    return len(re.sub(r"<[^>]+>", " ", s).split())


def guide_url(g):
    return f"/guides/{g['slug']}/"


def related_block(g):
    by_slug = {x["slug"]: x for x in GUIDES}
    cards = []
    for slug in g["related"]:
        r = by_slug[slug]
        cards.append(f'''          <a class="guide-card" href="{guide_url(r)}">
            <p class="eyebrow">{r["topic"]}</p>
            <h3>{r["h1"]}</h3>
            <span class="guide-more">Read the guide →</span>
          </a>''')
    return ('''        <section class="related" aria-labelledby="related-title">
          <h2 id="related-title">Keep reading</h2>
          <div class="guide-list">
''' + "\n".join(cards) + '''
          </div>
        </section>''')


def faq_block(g):
    if not g.get("faq"):
        return ""
    items = "\n".join(
        f'''          <details>
            <summary>{q}</summary>
            <p>{a}</p>
          </details>''' for q, a in g["faq"])
    return f'''        <section class="article-faq" aria-labelledby="faq-title">
          <h2 id="faq-title">Questions people ask</h2>
{items}
        </section>'''


def toc_block(body):
    heads = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body)
    if len(heads) < 4:
        return ""
    lis = "\n".join(f'            <li><a href="#{i}">{re.sub(r"<[^>]+>", "", t)}</a></li>' for i, t in heads)
    return f'''        <nav class="toc" aria-label="On this page">
          <p>On this page</p>
          <ol>
{lis}
          </ol>
        </nav>'''


def build_guide(g):
    path = guide_url(g)
    body = g["body"].strip("\n")
    faq = faq_block(g)
    minutes = max(3, round((words(body) + words(faq)) / 230))
    sources = "; ".join(f'<a href="{u}" rel="noopener">{n}</a>' for n, u in g["sources"])
    cta = g.get("cta") or {
        "title": "Your car, organised.",
        "text": "Livery is free for up to two cars. Add a number plate and your MOT, tax, MOT history and key dates are set up in seconds, with a reminder before anything's due.",
        "button": "Create my free garage",
        "href": SIGNUP,
    }
    article = f'''      <article class="article wrap">
        <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Livery</a> <span aria-hidden="true">/</span> <a href="/guides/">Guides</a></nav>
        <p class="eyebrow">{g["topic"]} · {minutes} min read</p>
        <h1>{g["h1"]}</h1>
        <p class="article-meta">By Aniket Chakraborty, founder of Livery · Updated <time datetime="{g["updated"]}">{long_date(g["updated"])}</time></p>

        <p class="article-lede">{g["lede"]}</p>

{toc_block(body)}

{body}

{faq}

        <aside class="article-cta">
          <h2>{cta["title"]}</h2>
          <p>{cta["text"]}</p>
          <a class="btn btn-primary" href="{html.escape(cta["href"], quote=True)}">{cta["button"]}</a>
        </aside>

        <p class="article-sources">Sources: {sources}. Rules and prices were checked on {long_date(g["updated"])} and can change, so check the official source before acting on them.</p>

{related_block(g)}
      </article>'''

    graph = [
        {"@type": "Article", "@id": f"{SITE}{path}#article", "headline": g["h1"],
         "description": g["desc"], "inLanguage": "en-GB",
         "datePublished": g["published"], "dateModified": g["updated"],
         "author": AUTHOR, "publisher": ORG, "mainEntityOfPage": f"{SITE}{path}",
         "image": f"{SITE}/assets/og.jpg"},
        crumbs([("Livery", "/"), ("Guides", "/guides/"), (g["crumb"], path)]),
    ]
    if g.get("faq"):
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": re.sub(r"<[^>]+>", "", q),
             "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
            for q, a in g["faq"]]})
    out = root / "guides" / g["slug"] / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(path, g["title"], g["desc"], article, {"@context": "https://schema.org", "@graph": graph}))
    return minutes


def build_index(minutes):
    cards = "\n".join(f'''          <a class="guide-card" href="{guide_url(g)}">
            <p class="eyebrow">{g["topic"]} · {minutes[g["slug"]]} min read</p>
            <h2>{g["h1"]}</h2>
            <p>{g["card"]}</p>
            <span class="guide-more">Read the guide →</span>
          </a>''' for g in GUIDES)
    title = "Car ownership guides for UK drivers | Livery"
    desc = ("Plain-English guides to buying and owning a car in the UK: used car checks, Cat S and N, "
            "clocking, MOT and tax dates, ULEZ and service history.")
    body = f'''      <section class="article wrap">
        <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Livery</a></nav>
        <p class="eyebrow">Guides</p>
        <h1>Car ownership, explained.</h1>
        <p class="article-lede">Plain-English guides to buying, running and looking after a car in the UK, from checking a used car's past to never missing an MOT again.</p>
        <div class="guide-list">
{cards}
        </div>
      </section>'''
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "name": title, "url": f"{SITE}/guides/", "inLanguage": "en-GB",
         "publisher": ORG,
         "hasPart": [{"@type": "Article", "headline": g["h1"], "url": SITE + guide_url(g)} for g in GUIDES]},
        crumbs([("Livery", "/"), ("Guides", "/guides/")])]}
    (root / "guides" / "index.html").write_text(page("/guides/", title, desc, body, ld, og_type="website"))


def build_sitemap():
    sm = root / "sitemap.xml"
    text = sm.read_text()
    keep = [m for m in re.findall(r"  <url>.*?</url>\n", text, re.S) if "/guides/" not in m]
    latest = max(g["updated"] for g in GUIDES)
    entries = keep + [f"  <url><loc>{SITE}/guides/</loc><lastmod>{latest}</lastmod></url>\n"] + [
        f"  <url><loc>{SITE}{guide_url(g)}</loc><lastmod>{g['updated']}</lastmod></url>\n" for g in GUIDES]
    sm.write_text('<?xml version="1.0" encoding="UTF-8"?>\n'
                  '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                  + "".join(entries) + "</urlset>\n")


minutes = {g["slug"]: build_guide(g) for g in GUIDES}
build_index(minutes)
build_sitemap()
print("built", len(GUIDES), "guides:", ", ".join(f"{s} ({m} min)" for s, m in minutes.items()))
