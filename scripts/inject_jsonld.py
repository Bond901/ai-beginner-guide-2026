#!/usr/bin/env python3
# Inject JSON-LD structured data into <head> of each page, derived from existing meta.
#   index.html        -> WebSite
#   about.html        -> BreadcrumbList (Home > About)
#   guides/*.html     -> Article + BreadcrumbList (Home > Category > Title)
# Idempotent: re-running replaces the previously injected block.
# Run after adding/renaming a guide or changing a title/date:
#   python3 scripts/inject_jsonld.py
import glob, os, re, json

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://bond901.github.io/ai-beginner-guide-2026/"
OG_IMAGE = BASE + "assets/og.png"
AUTHOR = {"@type": "Person", "name": "Bond901", "url": "https://github.com/Bond901"}
PUBLISHER = {"@type": "Organization", "name": "AI Beginner Guide 2026",
             "logo": {"@type": "ImageObject", "url": OG_IMAGE}}

# guide filename -> (category display name, index anchor id)
CATS = {
    "llm-core-concepts-guide-2026.html":      ("基礎觀念", "cat-base"),
    "prompt-engineering-evolution-guide.html":("基礎觀念", "cat-base"),
    "ai-instruction-guide-2026.html":         ("基礎觀念", "cat-base"),
    "claude-desktop-guide.html":              ("平台工具", "cat-tools"),
    "openai-tools-guide.html":                ("平台工具", "cat-tools"),
    "gemini-tools-guide.html":                ("平台工具", "cat-tools"),
    "ai-extensions-guide-2026.html":          ("進階 · Agent 擴充", "cat-adv"),
    "claude-code-skills-guide.html":          ("進階 · Agent 擴充", "cat-adv"),
    "claude-opus-4-8-guide.html":             ("進階 · Agent 擴充", "cat-adv"),
    "rag-guide-2026.html":                    ("流程 · 應用", "cat-flow"),
    "ai-sdlc-guide-2026.html":                ("流程 · 應用", "cat-flow"),
}

GUARD = re.compile(r"[ \t]*<!-- jsonld -->.*?</script>\n?", re.S)


def isodate(d):
    # schema.org datetime prefers full ISO 8601 with timezone; pages store date-only.
    return d + "T00:00:00+08:00" if d and len(d) == 10 else d


def meta(html, pat):
    m = re.search(pat, html)
    return m.group(1) if m else None


def build(name, html):
    og_title = meta(html, r'property="og:title" content="([^"]*)"') or meta(html, r"<title>([^<]*)</title>")
    desc = meta(html, r'property="og:description" content="([^"]*)"') or ""
    canon = meta(html, r'rel="canonical" href="([^"]*)"') or BASE
    img = meta(html, r'property="og:image" content="([^"]*)"') or OG_IMAGE
    lu = meta(html, r'name="last-updated" content="([^"]+)"')
    lv = meta(html, r'name="last-verified" content="([^"]+)"')
    leaf = (og_title or "").split(" — ")[0].strip()

    if name == "index.html":
        return [{
            "@context": "https://schema.org", "@type": "WebSite",
            "name": "AI Beginner Guide 2026", "url": BASE,
            "description": desc, "inLanguage": "zh-Hant", "publisher": PUBLISHER,
        }]

    if name == "about.html":
        return [{
            "@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "首頁", "item": BASE},
                {"@type": "ListItem", "position": 2, "name": "關於本站", "item": canon},
            ],
        }]

    if name not in CATS:
        return None  # 未登錄分類的新 guide：先略過（請在 CATS 補上後重跑）
    cat_name, cat_anchor = CATS[name]
    article = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": leaf, "description": desc, "image": img, "inLanguage": "zh-Hant",
        "author": AUTHOR, "publisher": PUBLISHER,
        "mainEntityOfPage": {"@type": "WebPage", "@id": canon},
    }
    if lu:
        article["datePublished"] = isodate(lu)
    article["dateModified"] = isodate(lv or lu)
    crumb = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "首頁", "item": BASE},
            {"@type": "ListItem", "position": 2, "name": cat_name, "item": BASE + "#" + cat_anchor},
            {"@type": "ListItem", "position": 3, "name": leaf, "item": canon},
        ],
    }
    return [article, crumb]


def inject(path, name):
    html = open(path, encoding="utf-8").read()
    html = GUARD.sub("", html)                       # strip previous block (idempotent)
    objs = build(name, html)
    if not objs:                                     # unknown guide (not in CATS): skip
        open(path, "w", encoding="utf-8").write(html)
        return "SKIP (add to CATS)"
    payload = objs[0] if len(objs) == 1 else objs    # single object or array
    block = '<!-- jsonld -->\n<script type="application/ld+json">\n' + \
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n</script>\n"
    html = html.replace("</head>", block + "</head>", 1)
    open(path, "w", encoding="utf-8").write(html)
    return objs[0]["@type"] + ("+BreadcrumbList" if len(objs) == 2 else "")


pages = [("index.html", os.path.join(REPO, "index.html"))]
if os.path.exists(os.path.join(REPO, "about.html")):
    pages.append(("about.html", os.path.join(REPO, "about.html")))
for f in sorted(glob.glob(os.path.join(REPO, "guides", "*.html"))):
    pages.append((os.path.basename(f), f))

for name, path in pages:
    kind = inject(path, name)
    print("%-44s %s" % (name, kind))
print("done: %d pages" % len(pages))
