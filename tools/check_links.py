#!/usr/bin/env python3
"""check_links.py — 全量核验 site/ 内 HTML 的相对链接与资源引用，直到 0 断链。"""
import sys, os, re, glob

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "site")

def main():
    pages = sorted(glob.glob(os.path.join(SITE, "**", "*.html"), recursive=True))
    broken = []
    checked = 0
    for path in pages:
        html = open(path, encoding="utf-8").read()
        for m in re.finditer(r'(?:href|src)="([^"]+)"', html):
            href = m.group(1).split("?")[0].split("#")[0]
            if not href or href.startswith(("http://", "https://", "mailto:", "javascript:", "data:")):
                continue
            if href.startswith("#"):
                continue
            checked += 1
            target = os.path.normpath(os.path.join(os.path.dirname(path), href))
            if not os.path.exists(target):
                broken.append((os.path.relpath(path, ROOT).replace("\\", "/"), href))
    print("check_links: %d pages, %d internal refs checked" % (len(pages), checked))
    for p, h in broken:
        print("[BROKEN] %s → %s" % (p, h))
    print("结果：%d broken links" % len(broken))
    return 1 if broken else 0

if __name__ == "__main__":
    sys.exit(main())
