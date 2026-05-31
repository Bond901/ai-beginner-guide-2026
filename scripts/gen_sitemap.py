#!/usr/bin/env python3
# Regenerate sitemap.xml by scanning index.html + about.html + guides/*.html.
# Run after adding/renaming a guide:  python3 scripts/gen_sitemap.py
import glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://bond901.github.io/ai-beginner-guide-2026/"

root_pages = [("", "index.html")]
if os.path.exists(os.path.join(REPO, "about.html")):
    root_pages.append(("", "about.html"))
pages = root_pages + [("guides/", os.path.basename(f)) for f in sorted(glob.glob(os.path.join(REPO, "guides", "*.html")))]
rows = []
missing = []
for prefix, name in pages:
    h = open(os.path.join(REPO, prefix, name), encoding="utf-8").read()
    m = re.search(r'name="last-verified" content="([^"]+)"', h)
    if not m:
        missing.append(prefix + name)   # collect; don't guess a date, don't bail on first
        continue
    loc = BASE if (prefix == "" and name == "index.html") else BASE + prefix + name
    rows.append((loc, m.group(1)))

if missing:   # fail-loud: a page without last-verified is an author error, not ours to paper over
    print("ERROR: missing last-verified meta; cannot generate sitemap:", file=sys.stderr)
    for f in missing:
        print("  - " + f, file=sys.stderr)
    sys.exit(1)

out = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
out += "".join('  <url><loc>%s</loc><lastmod>%s</lastmod></url>\n' % (loc, lm) for loc, lm in rows)
out += '</urlset>\n'
open(os.path.join(REPO, "sitemap.xml"), "w", encoding="utf-8").write(out)
print("sitemap.xml written: %d URLs" % len(rows))
