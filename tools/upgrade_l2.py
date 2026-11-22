#!/usr/bin/env python3
"""把 l2_data.py 中的 L2_DATA 合并进 data/units/U*.json（只升级已有条目的七节字段）。
用法：python tools/upgrade_l2.py
"""
import sys, os, json, glob

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from l2_data import L2_DATA

FIELDS = ("level", "source_text", "versions", "interpretations", "comparisons", "svg", "pending_notes", "needs_verification")

def main():
    unit_of = {"myth": "U1", "rel": "U2", "motif": "U3", "fig": "U4"}
    cache = {}
    for p in glob.glob(os.path.join(ROOT, "data", "units", "U*.json")):
        with open(p, encoding="utf-8") as f:
            d = json.load(f)
        cache[d["unit_id"]] = (p, d)
    done = []
    for eid, payload in L2_DATA.items():
        u = unit_of[eid.split("-")[0]]
        p, d = cache[u]
        target = next((e for e in d["entries"] if e["id"] == eid), None)
        if not target:
            print("[SKIP] %s 不存在" % eid)
            continue
        for k in FIELDS:
            if k in payload:
                target[k] = payload[k]
        # 数据自洽：把 comparisons 的 basis_source 并入 sources（去重），
        # 保证"比较依据"同时出现在来源列表中；不破坏双源规则（只增不减）。
        merged = list(target.get("sources", []))
        for cmp_item in target.get("comparisons", []):
            bs = cmp_item.get("basis_source")
            if bs and bs not in merged:
                merged.append(bs)
        if merged != target.get("sources", []):
            target["sources"] = merged
        done.append(eid)
    for u, (p, d) in cache.items():
        with open(p, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
            f.write("\n")
    print("L2 升级完成：%d 条 → %s" % (len(done), ", ".join(done)))
    return 0

if __name__ == "__main__":
    sys.exit(main())
