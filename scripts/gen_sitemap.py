#!/usr/bin/env python3
# Regenerate sitemap.xml by scanning index.html + guides/*.html.
# Run after adding/renaming a guide:  python3 scripts/gen_sitemap.py
import glob, os, re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://bond901.github.io/ai-beginner-guide-2026/"

pages = [("", "index.html")] + [("guides/", os.path.basename(f)) for f in sorted(glob.glob(os.path.join(REPO, "guides", "*.html")))]
rows = []
for prefix, name in pages:
    h = open(os.path.join(REPO, prefix, name), encoding="utf-8").read()
    m = re.search(r'name="last-verified" content="([^"]+)"', h)
    lastmod = m.group(1) if m else "2026-05-30"
    loc = BASE if (prefix == "" and name == "index.html") else BASE + prefix + name
    rows.append((loc, lastmod))

out = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
out += "".join('  <url><loc>%s</loc><lastmod>%s</lastmod></url>\n' % (loc, lm) for loc, lm in rows)
out += '</urlset>\n'
open(os.path.join(REPO, "sitemap.xml"), "w", encoding="utf-8").write(out)
print("sitemap.xml written: %d URLs" % len(rows))
