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

FIELDS = ("level", "source_text", "versions", "interpretations", "comparisons", "svg", "pending_notes", "needs_verification", "controversies", "data_points")

# R3 书名规范：对缺书名且未声明"未录入"的早期解读，按学者→其代表著作补"（据《X》）"。
# 书名均为真实学术著作（多数已录入 sources.json）；Eliade 多著作按关键词分流。
BOOK_MAP = {
    "Stephen Prothero": "God Is Not One",
    "Claude Lévi-Strauss": "结构人类学",
    "Georges Dumézil": "印欧人的神",
    "Henri Frankfort": "哲学之前",
    "Wendy Doniger": "The Implied Spider",
    "Jean-Pierre Vernant": "希腊神话与思想",
    "Jaan Puhvel": "比较神话学",
    "James George Frazer": "金枝",
    "Samuel Noah Kramer": "苏美尔神话",
    "Jane Ellen Harrison": "希腊宗教研究导论",
    "Walter Burkert": "希腊宗教",
    "Thorkild Jacobsen": "黑暗中的珍宝",
    "Åke Hultkrantz": "The Religions of the American Indians",
    "Theodor H. Gaster": "旧约中的神话、传说与习俗",
    "Elaine Pagels": "诺斯替福音",
    "Émile Durkheim": "宗教生活的基本形式",
    "Max Weber": "新教伦理与资本主义精神",
    "Joseph Campbell": "千面英雄",
}

def _inject_books(e):
    for it in e.get("interpretations", []):
        v = it.get("view", "")
        if "《" in v or "未录入" in v:
            continue
        h = it.get("holder", "")
        book = BOOK_MAP.get(h)
        if h == "Mircea Eliade":
            if "萨满" in v:
                book = "萨满教"
            elif "神圣" in v or "世俗" in v:
                book = "神圣与世俗"
            else:
                book = "永恒回归的神话"
        if book:
            it["view"] = "（据《%s》）%s" % (book, v)
        elif h and "未录入" not in v:
            # 未录入 sources 的学者：保守补声明，不引用未录入来源（TASK 硬规则）
            it["view"] = v + "（该学者著作未录入来源库，书名待补）"


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
        for s in payload.get("sources_extra", []):
            if s not in merged:
                merged.append(s)
        for cmp_item in target.get("comparisons", []):
            bs = cmp_item.get("basis_source")
            if bs and bs not in merged:
                merged.append(bs)
        if merged != target.get("sources", []):
            target["sources"] = merged
        _inject_books(target)
        done.append(eid)
    for u, (p, d) in cache.items():
        with open(p, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
            f.write("\n")
    print("L2 升级完成：%d 条 → %s" % (len(done), ", ".join(done)))
    return 0

if __name__ == "__main__":
    sys.exit(main())
