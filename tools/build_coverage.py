#!/usr/bin/env python3
"""从 scope.md 派生 coverage.json 与 coverage_matrix.md（单一数据源，避免手写 118 条 JSON 出错）。"""
import json, re, os
from datetime import datetime, timezone, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCOPE = os.path.join(ROOT, "scope.md")
TZ = timezone(timedelta(hours=8))

PREFIX_UNIT = {"myth-": "U1", "rel-": "U2", "motif-": "U3", "fig-": "U4"}
TIER_LEVEL = {"核心": "L2", "重要": "L1", "补充": "L1"}

# 从 scope 一句话说明派生"预期覆盖"的关键词表（诚实标注为 expected，非已写）
MOTIF_KEYWORDS = {
    "motif-creation": ["创世", "开辟", "起源", "宇宙", "化生", "造人", "世界起源", "天地"],
    "motif-flood": ["洪水", "大洪水", "洪水传说"],
    "motif-underworld": ["冥界", "死者", "亡灵", "冥界观"],
    "motif-herojourney": ["英雄", "历险", "探寻", "远行", "史诗"],
    "motif-sun": ["太阳", "日神", "日轮", "太阳神"],
    "motif-mother-goddess": ["母神", "生育", "丰产", "大地女神", "女神"],
    "motif-dragon": ["龙", "巨蛇", "羽蛇", "蛇"],
    "motif-worldtree": ["世界树", "宇宙树", "宇宙轴"],
    "motif-eschatology": ["末世", "诸神黄昏", "终结", "再生", "末日"],
    "motif-trickster": ["诡计", "欺骗", "变形", "越界"],
}

def parse_scope():
    text = open(SCOPE, encoding="utf-8").read()
    rows = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cols = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cols) < 6:
            continue
        eid = cols[0]
        if not re.fullmatch(r"[a-z0-9-]+", eid):
            continue
        if not any(eid.startswith(p) for p in PREFIX_UNIT):
            continue
        rows.append({
            "id": eid, "name": cols[1], "tier": cols[2],
            "frameworks": [f for f in cols[3].split(",") if f],
            "period": cols[4], "desc": cols[5],
        })
    return rows

def main():
    rows = parse_scope()
    now = datetime.now(TZ).strftime("%Y-%m-%dT%H:%M:%S+08:00")
    today = now[:10]
    entries = []
    for r in rows:
        entries.append({
            "id": r["id"], "name": r["name"],
            "unit": PREFIX_UNIT["%s-" % r["id"].split("-")[0]],
            "tier": r["tier"], "level": "L1", "status": "pending",
            "sources_count": 0, "needs_verification_count": 0,
            "last_updated": today,
        })
    # 从已写条目 JSON 同步真实状态（level / 来源数 / 待核实数）
    import glob
    written = {}
    for p in glob.glob(os.path.join(ROOT, "data", "units", "*.json")):
        with open(p, encoding="utf-8") as f:
            for e in json.load(f).get("entries", []):
                written[e["id"]] = e
    for e in entries:
        w = written.get(e["id"])
        if w:
            e["level"] = w.get("level", "L1")
            e["status"] = "done" if e["level"] in ("L2", "L3") else "in_progress"
            e["sources_count"] = len(set(w.get("sources", [])))
            e["needs_verification_count"] = 1 if w.get("needs_verification") else 0
    core_motifs = [r["id"] for r in rows if r["id"].startswith("motif-") and r["tier"] == "核心"]
    traditions = [r for r in rows if r["id"].startswith(("myth-", "rel-"))]
    cells = []
    for t in traditions:
        for mid in core_motifs:
            expected = any(k in t["desc"] for k in MOTIF_KEYWORDS.get(mid, []))
            cells.append({
                "tradition": t["id"], "motif": mid, "period": t["period"],
                "expected": expected, "status": "empty",
            })
    for c in cells:
        w = written.get(c["tradition"])
        if w and c["expected"]:
            c["status"] = w["level"]
    by_unit = {}
    by_tier = {}
    for r in rows:
        u = PREFIX_UNIT["%s-" % r["id"].split("-")[0]]
        by_unit[u] = by_unit.get(u, 0) + 1
        by_tier[r["tier"]] = by_tier.get(r["tier"], 0) + 1
    src_path = os.path.join(ROOT, "sources.json")
    verified_n = 0
    if os.path.exists(src_path):
        with open(src_path, encoding="utf-8") as f:
            verified_n = sum(1 for s in json.load(f)["sources"] if s.get("verified"))
    cov = {
        "generated": now,
        "summary": {
            "total": len(rows), "by_unit": by_unit, "by_tier": by_tier,
            "by_level": {
                "L1": sum(1 for e in entries if e["level"] == "L1"),
                "L2": sum(1 for e in entries if e["level"] == "L2"),
                "L3": sum(1 for e in entries if e["level"] == "L3"),
            },
            "l2_done": sum(1 for e in entries if e["level"] in ("L2", "L3")),
            "l3_done": sum(1 for e in entries if e["level"] == "L3"),
            "verified_sources": verified_n,
        },
        "entries": entries,
        "matrix": {
            "dimensions": {
                "traditions": [t["id"] for t in traditions],
                "motifs": core_motifs,
                "periods": ["ancient", "classical", "medieval", "early_modern", "modern", "oral"],
            },
            "cells": cells,
        },
    }
    with open(os.path.join(ROOT, "coverage.json"), "w", encoding="utf-8") as f:
        json.dump(cov, f, ensure_ascii=False, indent=2)
        f.write("\n")

    # 人类可读覆盖矩阵：按时期分组，行=传统，列=10 核心母题
    names = {r["id"]: r["name"] for r in rows}
    motif_names = {r["id"]: r["name"] for r in rows}
    col_ids = core_motifs
    lines = [
        "# 覆盖矩阵 — 传统 × 母题类型 × 时期",
        "",
        "> 派生自 scope.md。`✓`=该传统说明中预期涉及此母题（expected），`·`=未预期；",
        "> 单元格状态随阶段4写作由 `tools/build_coverage.py` 更新为 L1/L2/L3。",
        "",
    ]
    for period in ["ancient", "classical", "medieval", "early_modern", "modern", "oral"]:
        ps = [t for t in traditions if t["period"] == period]
        if not ps:
            continue
        lines += ["## 时期：%s（%d 个传统）" % (period, len(ps)), "",
                  "| 传统 | " + " | ".join(motif_names[m] for m in col_ids) + " |",
                  "|---|" + "---|" * len(col_ids)]
        cmap = {(c["tradition"], c["motif"]): c for c in cells}
        for t in ps:
            marks = ["✓" if cmap[(t["id"], m)]["expected"] else "·" for m in col_ids]
            lines.append("| %s | %s |" % (names[t["id"]], " | ".join(marks)))
        lines.append("")
    with open(os.path.join(ROOT, "coverage_matrix.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("coverage.json: %d entries, %d matrix cells" % (len(entries), len(cells)))
    print("by_unit=%s by_tier=%s" % (by_unit, by_tier))

if __name__ == "__main__":
    main()
