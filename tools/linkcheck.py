#!/usr/bin/env python3
"""linkcheck.py — 联网恢复后补核 sources.json 链接三态。

三态（WORKFLOW.md 第五步）：
  true    = HTTP < 400（可达）
  "blocked" = 401/403/429/503（服务器反爬拒绝脚本，URL 有效）
  false   = 404/DNS 失败/超时（真死链）
  null    = 离线文献（url=null，不核验；本机现状）
用法：python tools/linkcheck.py [--timeout 12] [--dry-run]
仅更新 link_ok 字段，不改 verified（书目核对状态另计）。
"""
import sys, os, json, ssl, urllib.request, urllib.error

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "sources.json")
UA = "Mozilla/5.0 (compatible; MythReligionLibrary/1.0; link-check)"

def check(url, timeout):
    req = urllib.request.Request(url, headers={"User-Agent": UA}, method="HEAD")
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
            return True if r.status < 400 else "blocked"
    except urllib.error.HTTPError as e:
        if e.code in (401, 403, 429, 503):
            return "blocked"
        return False
    except Exception:
        return False

def main():
    args = sys.argv[1:]
    timeout = 12
    if "--timeout" in args:
        timeout = int(args[args.index("--timeout") + 1])
    dry = "--dry-run" in args
    with open(PATH, encoding="utf-8") as f:
        data = json.load(f)
    stats = {"true": 0, "blocked": 0, "false": 0, "null": 0}
    for s in data["sources"]:
        url = s.get("url")
        if not url:
            s["link_ok"] = None
            stats["null"] += 1
            continue
        result = check(url, timeout)
        s["link_ok"] = result
        stats[str(result).lower() if isinstance(result, bool) else result] += 1
        print("[%s] %s — %s" % (result, s["id"], url))
    print("linkcheck: %s" % stats)
    if not dry:
        with open(PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print("sources.json link_ok 已更新。")
    else:
        print("dry-run：未写入 sources.json。")
    return 0

if __name__ == "__main__":
    sys.exit(main())
