# -*- coding: utf-8 -*-
"""verify_sources.py — 联网核对 sources.json 的书目信息（标题/作者/年份）。
用 Wikipedia REST/API 查证；结果写入 verification-report.json 并打印差异。
"""
import sys, os, json, ssl, time, urllib.parse, urllib.request

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CTX = ssl._create_unverified_context()
UA = {"User-Agent": "MythReligionLib/1.0 (bibliographic verification; local research)"}

# 需核对的条目：id -> (Wikipedia 条目名, 期望关键词)
TARGETS = {
    "pri-theogony": ("Theogony", ["Hesiod", "8th", "7th"]),
    "pri-works-days": ("Works and Days", ["Hesiod"]),
    "pri-iliad": ("Iliad", ["Homer"]),
    "pri-odyssey": ("Odyssey", ["Homer"]),
    "pri-poetic-eddas": ("Poetic Edda", ["Edda"]),
    "pri-prose-eddas": ("Prose Edda", ["Snorri"]),
    "pri-enuma-elish": ("Enûma Eliš", ["Babylon", "creation"]),
    "pri-gilgamesh": ("Epic of Gilgamesh", ["Gilgamesh"]),
    "pri-rigveda": ("Rigveda", ["Rigveda", "Sanskrit"]),
    "pri-kojiki": ("Kojiki", ["712"]),
    "pri-nihon-shoki": ("Nihon Shoki", ["720"]),
    "pri-popol-vuh": ("Popol Vuh", ["K'iche", "Quiché"]),
    "pri-tao-te-ching": ("Tao Te Ching", ["Laozi", "Laozi"]),
    "pri-analects": ("Analects", ["Confucius"]),
    "pri-mahabharata": ("Mahabharata", ["Vyasa"]),
    "pri-ramayana": ("Ramayana", ["Valmiki"]),
    "pri-bible-kjv": ("King James Version", ["1611"]),
    "pri-shan-hai-jing": ("Classic of Mountains and Seas", ["Shan Hai Jing"]),
}

def wiki_summary(title):
    q = urllib.parse.urlencode({"action": "query", "prop": "extracts", "exintro": 1,
                                "explaintext": 1, "format": "json", "redirects": 1, "titles": title})
    url = "https://en.wikipedia.org/w/api.php?" + q
    for attempt in range(2):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20, context=CTX)
            d = json.loads(r.read())
            for _, v in d["query"]["pages"].items():
                if "missing" in v:
                    return None, None
                return v.get("title"), (v.get("extract") or "")
        except Exception:
            if attempt == 0:
                time.sleep(1)
    return None, None

def main():
    srcs = {s["id"]: s for s in json.load(open(os.path.join(ROOT, "sources.json"), encoding="utf-8"))["sources"]}
    out = []
    ok = miss = 0
    for sid, (title, keys) in TARGETS.items():
        t, ex = wiki_summary(title)
        s = srcs.get(sid, {})
        if not t:
            print("[MISS] %-22s 维基无此条目: %s" % (sid, title))
            out.append({"id": sid, "wiki": None, "status": "missing"})
            miss += 1
            continue
        hits = [k for k in keys if k.lower() in ex.lower()]
        status = "ok" if hits else "check"
        print("[%-5s] %-22s -> %-34s %s" % (status, sid, t[:34], ("命中:" + ",".join(hits)) if hits else "关键词未命中，需人工核对"))
        out.append({"id": sid, "wiki": t, "mine": s.get("title"), "year": s.get("year"),
                    "hits": hits, "status": status, "extract_head": ex[:160]})
        ok += 1
        time.sleep(0.3)
    json.dump(out, open(os.path.join(ROOT, "verification-report.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print("\n核对完成: 成功 %d, 缺失 %d -> verification-report.json" % (ok, miss))

if __name__ == "__main__":
    main()
