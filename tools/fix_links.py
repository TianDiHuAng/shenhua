# -*- coding: utf-8 -*-
"""fix_links.py — 依据联网实核结果修正 sources.json 中失效链接（改为真实存在的页面）。"""
import json, os, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "sources.json")

WS = "https://en.wikisource.org/wiki/"
WP = "https://en.wikipedia.org/wiki/"
def ws(t): return WS + urllib.parse.quote(t.replace(" ", "_"))
def wp(t): return WP + urllib.parse.quote(t.replace(" ", "_"))

# id -> 实测有效的 URL
FIX = {
    # Wikisource：改为实核存在的页面名
    "pri-theogony": ws("Theogony"),
    "pri-works-days": ws("Works and Days"),
    "pri-iliad": ws("The Iliad"),
    "pri-odyssey": ws("The Odyssey"),
    "pri-pausanias": ws("The Description of Greece"),
    "pri-ovid-met": ws("Metamorphoses"),
    "pri-virgil-aeneid": ws("Aeneid"),
    "pri-poetic-eddas": ws("Poetic Edda"),
    "pri-prose-eddas": ws("Prose Edda"),
    "pri-beowulf": ws("Beowulf"),
    "pri-mabinogion": ws("The Mabinogion"),
    "pri-book-dead": ws("The Book of the Dead"),
    "pri-gilgamesh": ws("Epic of Gilgamesh"),
    "pri-rigveda": ws("The Rigveda"),
    "pri-mahabharata": ws("The Mahabharat"),
    "pri-ramayana": ws("The Ramayana"),
    "pri-kojiki": ws("Kojiki"),
    "pri-nihon-shoki": ws("Nihongi"),
    "pri-tao-te-ching": ws("Tao Te Ching"),
    "pri-zhuangzi": ws("Zhuangzi"),
    "pri-i-ching": ws("Book of Changes"),
    "pri-analects": ws("Analects"),
    "pri-dhammapada": ws("Dhammapada"),
    "pri-kalevala": ws("Kalevala"),
    "pri-quran": ws("Qur'an"),
    # Wikisource 无对应页 → 改用 Wikipedia（更稳）
    "pri-homeric-hymns": wp("Homeric Hymns"),
    "pri-apollodorus": wp("Bibliotheca (Pseudo-Apollodorus)"),
    "pri-livy-rome": wp("Ab Urbe Condita (Livy)"),
    "pri-lebor-gabala": wp("Lebor Gabála Érenn"),
    "pri-enuma-elish": wp("Enûma Eliš"),
    "pri-atrahasis": wp("Atrahasis"),
    "pri-sumerian-king-list": wp("Sumerian King List"),
    "pri-popol-vuh": wp("Popol Vuh"),
    "pri-shan-hai-jing": wp("Classic of Mountains and Seas"),
    "pri-chu-ci": wp("Chu Ci"),
    "pri-journey-west": wp("Journey to the West"),
    "pri-bible-kjv": wp("King James Version"),
    "pri-pyramid-texts": wp("Pyramid Texts"),
    "pri-coffin-texts": wp("Coffin Texts"),
}

d = json.load(open(P, encoding="utf-8"))
n = 0
for s in d["sources"]:
    u = FIX.get(s["id"])
    if u and s.get("url") != u:
        print("%-24s %s\n    -> %s" % (s["id"], s.get("url"), u))
        s["url"] = u
        s["link_ok"] = None   # 待重新核验
        n += 1
json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
open(P, "a", encoding="utf-8").write("\n")
print("\n修正链接:", n)
