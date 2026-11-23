# -*- coding: utf-8 -*-
"""linkcheck.py — 批量核验 sources.json 链接三态（联网恢复后补核）。
true=HTTP<400；"blocked"=401/403/429/503（服务器反爬，URL 有效）；false=404/DNS失败/超时。
用法：python tools/linkcheck.py [--limit N] [--timeout 15] [--dry-run]
"""
import sys, os, json, ssl, time, urllib.request, urllib.error, socket

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "sources.json")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
CTX = ssl._create_unverified_context()
socket.setdefaulttimeout(15)

def check(url, timeout=15, tries=2):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*"}, method="GET")
            with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
                return True if r.status < 400 else "blocked"
        except urllib.error.HTTPError as e:
            if e.code in (401, 403, 429, 503):
                return "blocked"
            if e.code == 404:
                return False
            if i == tries - 1:
                return False
        except Exception:
            if i == tries - 1:
                return False
            time.sleep(1)
    return False

def main():
    args = sys.argv[1:]
    limit = int(args[args.index("--limit") + 1]) if "--limit" in args else None
    dry = "--dry-run" in args
    data = json.load(open(PATH, encoding="utf-8"))
    srcs = data["sources"]
    stats = {"true": 0, "blocked": 0, "false": 0, "null": 0}
    changes = []
    n = 0
    for s in srcs:
        if limit and n >= limit:
            break
        url = s.get("url")
        if not url:
            stats["null"] += 1
            continue
        n += 1
        res = check(url)
        key = str(res).lower() if isinstance(res, bool) else res
        stats[key] += 1
        old = s.get("link_ok")
        s["link_ok"] = res
        mark = "" if old == res else " *changed(%s→%s)" % (old, res)
        print("[%-7s] %s%s" % (key, s["id"], mark))
        if old != res:
            changes.append((s["id"], old, res))
        if not dry:
            json.dump(data, open(PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
            open(PATH, "a", encoding="utf-8").write("\n")
    print("\n统计:", stats, "| 检查:", n, "| 变更:", len(changes))
    return 0

if __name__ == "__main__":
    sys.exit(main())
