#!/usr/bin/env python3
"""阶段4 批量写作：按精确来源映射生成 L1 骨架（每轮 ≤40 条）。
L1 定义见 TASK_myth.md：定义、时间或位置、一两句概述、相关条目。
来源映射均为 sources.json 中真实存在的 id，不现场编造。
"""
import sys, os, json, glob

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))

# 核心 38 条的精确来源映射（每条 ≥2 个真实来源 id）
SOURCE_MAP = {
    # U1 神话体系核心（myth-greek 已为 L2 样板）
    "myth-norse": ["pri-poetic-eddas", "pri-prose-eddas"],
    "myth-egyptian": ["pri-pyramid-texts", "pri-book-dead"],
    "myth-mesopotamian": ["pri-enuma-elish", "pri-gilgamesh"],
    "myth-chinese": ["pri-shan-hai-jing", "pri-chu-ci"],
    "myth-hindu": ["pri-rigveda", "pri-mahabharata"],
    "myth-japanese": ["pri-kojiki", "pri-nihon-shoki"],
    "myth-maya": ["pri-popol-vuh", "ins-world-history"],
    "myth-aztec": ["ins-world-history", "ins-british-museum"],
    "myth-celtic": ["pri-mabinogion", "pri-lebor-gabala"],
    # U2 宗教传统核心
    "rel-christianity": ["pri-bible-kjv", "aca-gnostic-gospels"],
    "rel-islam": ["pri-quran", "enc-brit-islam"],
    "rel-judaism": ["pri-bible-kjv", "aca-myth-legend-custom"],
    "rel-buddhism": ["pri-dhammapada", "enc-brit-buddhism"],
    "rel-hinduism": ["pri-rigveda", "aca-patterns-religion"],
    "rel-taoism": ["pri-tao-te-ching", "pri-zhuangzi"],
    "rel-confucianism": ["pri-analects", "pri-i-ching"],
    "rel-shinto": ["pri-kojiki", "enc-brit-shinto"],
    # U3 母题核心（motif-creation 已为 L2 样板）
    "motif-flood": ["pri-gilgamesh", "pri-atrahasis"],
    "motif-underworld": ["pri-book-dead", "enc-wiki-underworld"],
    "motif-herojourney": ["aca-hero-faces", "pri-odyssey"],
    "motif-sun": ["aca-eternal-return", "pri-rigveda"],
    "motif-mother-goddess": ["aca-golden-bough", "aca-patterns-religion"],
    "motif-dragon": ["enc-wiki-dragon", "aca-comparative-myth"],
    "motif-worldtree": ["enc-wiki-world-tree", "pri-poetic-eddas"],
    "motif-eschatology": ["aca-eternal-return", "enc-wiki-mythology"],
    "motif-trickster": ["aca-comparative-myth", "enc-wiki-list-myth"],
    # U4 人物核心
    "fig-zeus": ["pri-theogony", "pri-iliad"],
    "fig-odin": ["pri-poetic-eddas", "pri-prose-eddas"],
    "fig-ra": ["pri-pyramid-texts", "pri-book-dead"],
    "fig-pangu": ["aca-short-history-myth", "enc-wiki-mythology"],
    "fig-nuwa": ["pri-chu-ci", "aca-short-history-myth"],
    "fig-buddha": ["pri-dhammapada", "enc-brit-buddhism"],
    "fig-jesus": ["pri-bible-kjv", "aca-gnostic-gospels"],
    "fig-muhammad": ["pri-quran", "enc-brit-islam"],
    "fig-moses": ["pri-bible-kjv", "aca-myth-legend-custom"],
    "fig-vishnu": ["pri-vishnu-purana", "pri-mahabharata"],
    "fig-shiva": ["aca-patterns-religion", "enc-brit-hinduism"],
    "fig-indra": ["pri-rigveda", "aca-gods-indo-europeans"],
}

# 重要 42 条的精确来源映射
IMPORTANT_SOURCE_MAP = {
    # U1 重要 14
    "myth-roman": ["pri-ovid-met", "pri-virgil-aeneid", "pri-livy-rome"],
    "myth-sumerian": ["pri-sumerian-king-list", "aca-sumerian-mythology"],
    "myth-akkadian": ["pri-gilgamesh", "pri-atrahasis"],
    "myth-persian": ["aca-gods-indo-europeans", "enc-brit-mythology"],
    "myth-finnish": ["pri-kalevala", "aca-comparative-myth"],
    "myth-slavic": ["enc-brit-mythology", "aca-comparative-myth"],
    "myth-hittite": ["aca-hittite-myths", "ins-oriental-institute"],
    "myth-yoruba": ["ins-british-museum", "enc-wiki-list-myth"],
    "myth-dogon": ["aca-structural-anthro", "ins-british-museum"],
    "myth-polynesian": ["enc-wiki-list-myth", "ins-world-history"],
    "myth-australian": ["enc-wiki-list-myth", "ins-world-history"],
    "myth-inca": ["ins-world-history", "ins-british-museum"],
    "myth-olmec": ["ins-world-history", "ins-british-museum"],
    "myth-canaanite": ["aca-myth-legend-custom", "ins-oriental-institute"],
    # U2 重要 10
    "rel-jainism": ["enc-brit-hinduism", "enc-wiki-world-religion"],
    "rel-sikhism": ["enc-wiki-world-religion", "enc-brit-hinduism"],
    "rel-zoroastrianism": ["aca-gods-indo-europeans", "enc-wiki-world-religion"],
    "rel-shamanism": ["aca-shamanism", "aca-religions-american-indians"],
    "rel-manichaeism": ["aca-gnostic-gospels", "enc-wiki-world-religion"],
    "rel-bahai": ["enc-wiki-world-religion", "ins-pluralism"],
    "rel-mormonism": ["enc-wiki-world-religion", "ins-pluralism"],
    "rel-tibetan-buddhism": ["enc-brit-buddhism", "enc-wiki-world-religion"],
    "rel-zen": ["enc-brit-buddhism", "enc-wiki-world-religion"],
    "rel-pureland": ["enc-brit-buddhism", "enc-wiki-world-religion"],
    # U3 重要 6
    "motif-twin": ["aca-comparative-myth", "aca-golden-bough"],
    "motif-sacrifice": ["aca-golden-bough", "aca-myth-ritual-religion"],
    "motif-scapegoat": ["aca-myth-legend-custom", "aca-golden-bough"],
    "motif-culturehero": ["aca-hero-faces", "aca-myth-ritual-religion"],
    "motif-moon": ["aca-eternal-return", "enc-wiki-mythology"],
    "motif-quest": ["aca-hero-faces", "pri-odyssey"],
    # U4 重要 12
    "fig-hera": ["pri-theogony", "pri-iliad"],
    "fig-athena": ["pri-iliad", "pri-odyssey"],
    "fig-apollo": ["pri-homeric-hymns", "pri-iliad"],
    "fig-hades": ["pri-theogony", "enc-wiki-underworld"],
    "fig-thor": ["pri-prose-eddas", "pri-poetic-eddas"],
    "fig-loki": ["pri-prose-eddas", "pri-poetic-eddas"],
    "fig-osiris": ["pri-book-dead", "aca-golden-bough"],
    "fig-anubis": ["pri-book-dead", "ins-british-museum"],
    "fig-gilgamesh": ["pri-gilgamesh", "aca-treasures-darkness"],
    "fig-inanna": ["aca-sumerian-mythology", "pri-sumerian-king-list"],
    "fig-fuxi": ["pri-i-ching", "pri-shan-hai-jing"],
    "fig-sun-wukong": ["pri-journey-west", "aca-short-history-myth"],
}

# 补充 36 条的精确来源映射（区域性传统多依赖百科/机构资源，已统一标待核实）
SUPP_SOURCE_MAP = {
    # U1 补充 18
    "myth-etruscan": ["enc-wiki-list-myth", "ins-met"],
    "myth-phoenician": ["aca-myth-legend-custom", "enc-brit-mythology"],
    "myth-thracian": ["enc-brit-mythology", "enc-wiki-list-myth"],
    "myth-turkic": ["enc-wiki-list-myth", "aca-gods-indo-europeans"],
    "myth-ugric": ["enc-wiki-list-myth", "aca-comparative-myth"],
    "myth-korean": ["enc-wiki-list-myth", "ins-world-history"],
    "myth-vietnamese": ["enc-wiki-list-myth", "ins-world-history"],
    "myth-basque": ["enc-wiki-list-myth", "enc-brit-mythology"],
    "myth-lithuanian": ["enc-wiki-list-myth", "aca-comparative-myth"],
    "myth-georgian": ["enc-wiki-list-myth", "aca-comparative-myth"],
    "myth-armenian": ["enc-wiki-list-myth", "aca-comparative-myth"],
    "myth-maori": ["enc-wiki-list-myth", "ins-world-history"],
    "myth-micronesian": ["enc-wiki-list-myth", "ins-world-history"],
    "myth-plains-native": ["aca-religions-american-indians", "enc-wiki-list-myth"],
    "myth-northwest-native": ["aca-religions-american-indians", "ins-british-museum"],
    "myth-siberian": ["aca-shamanism", "enc-wiki-list-myth"],
    "myth-dravidian": ["pri-rigveda", "enc-brit-hinduism"],
    "myth-berber": ["enc-wiki-list-myth", "ins-world-history"],
    # U2 补充 8
    "rel-caodai": ["enc-wiki-world-religion", "ins-pluralism"],
    "rel-tenrikyo": ["enc-wiki-world-religion", "ins-pluralism"],
    "rel-yiguandao": ["enc-wiki-world-religion", "ins-pluralism"],
    "rel-vaishnavism": ["pri-vishnu-purana", "enc-brit-hinduism"],
    "rel-shaivism": ["enc-brit-hinduism", "aca-patterns-religion"],
    "rel-tantrism": ["enc-brit-tantrism", "aca-patterns-religion"],
    "rel-ancient-egyptian": ["pri-book-dead", "aca-before-philosophy"],
    "rel-ancient-greek": ["pri-pausanias", "aca-greek-religion"],
    # U3 补充 4
    "motif-labyrinth": ["enc-wiki-mythology", "aca-hero-faces"],
    "motif-phoenix": ["enc-wiki-mythology", "aca-golden-bough"],
    "motif-skyfather": ["aca-gods-indo-europeans", "aca-comparative-myth"],
    "motif-cosmicegg": ["enc-wiki-creation", "aca-eternal-return"],
    # U4 补充 6
    "fig-quetzalcoatl": ["ins-world-history", "enc-wiki-list-myth"],
    "fig-mictlantecuhtli": ["enc-wiki-list-myth", "ins-world-history"],
    "fig-amaterasu": ["pri-kojiki", "enc-brit-shinto"],
    "fig-susanoo": ["pri-kojiki", "enc-wiki-list-myth"],
    "fig-dagda": ["enc-wiki-list-myth", "pri-lebor-gabala"],
    "fig-cu-chulainn": ["enc-wiki-list-myth", "pri-mabinogion"],
}

# 跨单元关联建议（补足 L1 的"相关条目"，id 均来自 scope）
CROSS_LINKS = {
    "myth-norse": ["fig-odin", "motif-eschatology", "motif-worldtree"],
    "myth-egyptian": ["fig-ra", "motif-underworld"],
    "myth-mesopotamian": ["fig-gilgamesh", "motif-flood", "motif-creation"],
    "myth-chinese": ["fig-pangu", "fig-nuwa", "motif-dragon"],
    "myth-hindu": ["fig-vishnu", "fig-shiva", "fig-indra", "motif-creation"],
    "myth-japanese": ["fig-amaterasu", "motif-sun"],
    "myth-maya": ["motif-creation", "motif-eschatology"],
    "myth-aztec": ["fig-quetzalcoatl", "motif-sun"],
    "myth-celtic": ["fig-dagda", "fig-cu-chulainn"],
    "rel-christianity": ["fig-jesus", "fig-moses", "rel-judaism", "rel-islam"],
    "rel-islam": ["fig-muhammad", "rel-judaism", "rel-christianity"],
    "rel-judaism": ["fig-moses", "rel-christianity", "rel-islam"],
    "rel-buddhism": ["fig-buddha", "rel-hinduism", "rel-tibetan-buddhism"],
    "rel-hinduism": ["fig-vishnu", "fig-shiva", "rel-buddhism"],
    "rel-taoism": ["pri-tao-te-ching", "rel-confucianism"],
    "rel-confucianism": ["rel-taoism", "pri-analects"],
    "rel-shinto": ["myth-japanese", "fig-amaterasu"],
    "motif-flood": ["myth-mesopotamian", "fig-gilgamesh", "motif-creation"],
    "motif-underworld": ["myth-egyptian", "fig-osiris", "fig-hades"],
    "motif-herojourney": ["fig-gilgamesh", "fig-hera"],
    "motif-sun": ["fig-ra", "fig-amaterasu", "myth-japanese"],
    "motif-mother-goddess": ["fig-nuwa", "fig-inanna"],
    "motif-dragon": ["myth-chinese", "fig-quetzalcoatl"],
    "motif-worldtree": ["myth-norse", "fig-odin"],
    "motif-eschatology": ["myth-norse", "myth-maya"],
    "motif-trickster": ["fig-loki", "fig-sun-wukong"],
    "fig-zeus": ["myth-greek", "fig-hera", "fig-hades"],
    "fig-odin": ["myth-norse", "fig-thor", "fig-loki"],
    "fig-ra": ["myth-egyptian", "fig-osiris"],
    "fig-pangu": ["myth-chinese", "fig-nuwa", "motif-creation"],
    "fig-nuwa": ["myth-chinese", "fig-pangu", "motif-mother-goddess"],
    "fig-buddha": ["rel-buddhism"],
    "fig-jesus": ["rel-christianity"],
    "fig-muhammad": ["rel-islam"],
    "fig-moses": ["rel-judaism", "rel-christianity"],
    "fig-vishnu": ["rel-hinduism", "myth-hindu"],
    "fig-shiva": ["rel-hinduism", "myth-hindu"],
    "fig-indra": ["myth-hindu", "rel-hinduism"],
}

def parse_scope():
    out = {}
    order = []
    for line in open(os.path.join(ROOT, "scope.md"), encoding="utf-8").read().splitlines():
        if not line.startswith("|"):
            continue
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) >= 6 and c[0].replace("-", "").isalpha() and "-" in c[0] and c[0].split("-")[0] in ("myth", "rel", "motif", "fig"):
            out[c[0]] = {"title": c[1], "tier": c[2], "period": c[4], "desc": c[5]}
            order.append(c[0])
    return out, order

def main():
    scope, order = parse_scope()
    srcs = {s["id"]: s for s in json.load(open(os.path.join(ROOT, "sources.json"), encoding="utf-8"))["sources"]}
    # 已有条目
    existing = {}
    unit_files = {}
    for p in glob.glob(os.path.join(ROOT, "data", "units", "U*.json")):
        d = json.load(open(p, encoding="utf-8"))
        unit_files[d["unit_id"]] = p
        for e in d["entries"]:
            existing[e["id"]] = e
    tier_arg = next((sys.argv[i + 1] for i, a in enumerate(sys.argv) if a == "--tier" and i + 1 < len(sys.argv)), "核心")
    active_map = {"重要": IMPORTANT_SOURCE_MAP, "补充": SUPP_SOURCE_MAP}.get(tier_arg, SOURCE_MAP)
    limit = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else None
    pending = [(k, v) for k, v in active_map.items() if k not in existing and k in scope]
    if limit:
        pending = pending[:limit]
    made = []
    for eid, sid in pending:
        for s in sid:
            assert s in srcs, "来源 id 未定义：%s (%s)" % (s, eid)
        m = scope[eid]
        unverified = [s for s in sid if not srcs[s]["verified"]]
        note = "L1 骨架阶段：来源文本、版本差异、学者解读、跨传统比较与图示待 L2 补充。"
        if unverified:
            note += " 引用未在线核验来源：" + "、".join(unverified) + "（DECISIONS.md D2）。"
        # 相关条目：跨单元建议 + 同单元相邻
        related = list(CROSS_LINKS.get(eid, []))
        prefix = eid.split("-")[0]
        same = [x for x in order if x.split("-")[0] == prefix]
        i = same.index(eid)
        for j in (i - 1, i + 1):
            if 0 <= j < len(same) and same[j] not in related:
                related.append(same[j])
        related = [r for r in related if r in scope][:6]
        entry = {
            "id": eid, "title": m["title"], "level": "L1", "tier": m["tier"],
            "period": m["period"], "summary": m["desc"], "related": related,
            "sources": sid, "needs_verification": True, "pending_notes": note,
            "year": None,
        }
        made.append(entry)
        prefix_u = {"myth": "U1", "rel": "U2", "motif": "U3", "fig": "U4"}[prefix]
        existing.setdefault("__new__", [])
        bucket = existing.setdefault("__bucket__" + prefix_u, [])
        bucket.append(entry)
    if len(made) > 40:
        print("[ERROR] 本轮 %d 条超过 40 条配额" % len(made))
        return 1
    # 写入单元文件
    unit_titles = {"U1": "神话体系", "U2": "宗教传统", "U3": "母题", "U4": "人物"}
    for u in ("U1", "U2", "U3", "U4"):
        bucket = existing.get("__bucket__" + u, [])
        if not bucket:
            continue
        path = unit_files.get(u) or os.path.join(ROOT, "data", "units", "%s.json" % u)
        d = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {"unit_id": u, "title": unit_titles[u], "entries": []}
        have = {e["id"] for e in d["entries"]}
        for e in bucket:
            if e["id"] not in have:
                d["entries"].append(e)
        d["entries"].sort(key=lambda e: order.index(e["id"]) if e["id"] in order else 999)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print("%s: +%d → %d entries" % (u, len(bucket), len(d["entries"])))
    print("本轮新增 %d 条 L1 骨架" % len(made))
    return 0

if __name__ == "__main__":
    sys.exit(main())
