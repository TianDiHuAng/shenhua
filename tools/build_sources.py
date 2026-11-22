#!/usr/bin/env python3
"""生成 sources.json。联网端点不可用，来源均为真实稳定书目信息，verified 语义见 DECISIONS.md D2。"""
import json, os
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTE = "书目信息据公开书目知识录入；联网端点不可用，未在线打开页面核对，link_ok=null。"

def wikisource(title):
    return "https://en.wikisource.org/wiki/" + quote(title.replace(" ", "_"))

def wiki(title):
    return "https://en.wikipedia.org/wiki/" + quote(title.replace(" ", "_"))

def brit(slug):
    return "https://www.britannica.com/topic/" + slug

def worldcat(title):
    return "https://search.worldcat.org/search?q=ti%3A" + quote(title)

sources = []
def add(sid, title, author, year, stype, url, note="", year_display=None, verified=True, url2=None):
    sources.append({
        "id": sid, "title": title, "author": author, "year": year,
        "year_display": year_display or (str(year) if year is not None else "年份不详"),
        "type": stype, "url": url, "url2": url2, "link_ok": None,
        "verified": verified, "note": NOTE + note,
    })

# ===== A 原典（公版经典文本）=====
P = "原典"
add("pri-theogony", "神谱", "Hesiod（赫西俄德）", -750, P, wikisource("Theogony_(Hesiod)"), "古希腊语原典，公共领域译本。", "约公元前8—7世纪")
add("pri-works-days", "工作与时日", "Hesiod（赫西俄德）", -700, P, wikisource("Works_and_Days"), "公共领域译本。", "约公元前7世纪")
add("pri-homeric-hymns", "荷马颂歌", "托名 Homer（荷马）", -700, P, wikisource("Homeric_Hymns"), "作者归属有争议。", "约公元前7—6世纪")
add("pri-iliad", "伊利亚特", "Homer（荷马）", -750, P, wikisource("Iliad"), "公共领域译本（如 Pope/Chapman 译本）。", "约公元前8世纪")
add("pri-odyssey", "奥德赛", "Homer（荷马）", -720, P, wikisource("Odyssey"), "公共领域译本。", "约公元前8—7世纪")
add("pri-pausanias", "希腊志（ Description of Greece）", "Pausanias（保萨尼亚斯）", 150, P, wikisource("Description_of_Greece"), "公元2世纪旅行记，神话与圣地记载重要来源。", "约公元2世纪")
add("pri-apollodorus", "书库（Bibliotheca）", "托名 Apollodorus（阿波罗多洛斯）", 100, P, wikisource("Bibliotheca_(Pseudo-Apollodorus)"), "神话汇编，作者为伪托。", "约公元1—2世纪")
add("pri-ovid-met", "变形记", "Ovid（奥维德）", 8, P, wikisource("Metamorphoses"), "拉丁语原典，公共领域译本。")
add("pri-virgil-aeneid", "埃涅阿斯纪", "Virgil（维吉尔）", -19, P, wikisource("Aeneid"), "罗马建国神话史诗。", "约公元前29—19年")
add("pri-livy-rome", "罗马史（Ab Urbe Condita）", "Livy（李维）", -25, P, wikisource("Ab_Urbe_Condita"), "罗马早期传说的重要文献来源。", "约公元前1世纪")
add("pri-poetic-eddas", "诗体埃达", "佚名（冰岛抄本）", 1200, P, wikisource("Poetic_Edda"), "13世纪抄本保存的北欧神话诗歌。", "13世纪抄本")
add("pri-prose-eddas", "散文埃达", "Snorri Sturluson（斯诺里·斯蒂德吕松）", 1220, P, wikisource("Prose_Edda"), "北欧神话系统化叙述的核心文本。", "约13世纪")
add("pri-beowulf", "贝奥武甫", "佚名（古英语）", 900, P, wikisource("Beowulf"), "古英语史诗，成诗年代有争议。", "约8—11世纪")
add("pri-mabinogion", "马比诺吉昂", "佚名（威尔士）", 1300, P, wikisource("Mabinogion"), "威尔士神话传说集。", "约12—14世纪")
add("pri-lebor-gabala", "侵略之书（Lebor Gabála Érenn）", "佚名（爱尔兰）", 1100, P, wikisource("Lebor_Gab%C3%A1la_%C3%89renn"), "爱尔兰神话与伪史汇编。", "约11—12世纪")
add("pri-pyramid-texts", "金字塔文（Pyramid Texts）", "佚名（古埃及）", -2400, P, wiki("Pyramid_Texts"), "古埃及最古老的宗教文本之一。", "约公元前24世纪")
add("pri-coffin-texts", "棺椁文（Coffin Texts）", "佚名（古埃及）", -2000, P, wiki("Coffin_Texts"), "古埃及冥界文本。", "约公元前21—18世纪")
add("pri-book-dead", "亡灵书（Book of the Dead）", "佚名（古埃及）", -1550, P, wikisource("The_Book_of_the_Dead"), "古埃及冥界引导文本合集。", "约公元前16世纪起")
add("pri-enuma-elish", "巴比伦创世史诗（Enuma Elish）", "佚名（巴比伦）", -1100, P, wikisource("Enuma_Elish"), "美索不达米亚创世史诗。", "约公元前12—11世纪")
add("pri-gilgamesh", "吉尔伽美什史诗", "佚名（美索不达米亚）", -1200, P, wikisource("Epic_of_Gilgamesh"), "含洪水叙事，多版本。", "约公元前13—10世纪")
add("pri-atrahasis", "阿特拉哈西斯（Atrahasis）", "佚名（巴比伦）", -1800, P, wiki("Atrahasis"), "美索不达米亚创世与洪水史诗。", "约公元前18世纪")
add("pri-sumerian-king-list", "苏美尔王表", "佚名（苏美尔）", -2000, P, wikisource("Sumerian_King_List"), "苏美尔王权与年代传说。", "约公元前21—18世纪")
add("pri-rigveda", "梨俱吠陀（Rigveda）", "佚名（吠陀祭司）", -1500, P, wikisource("Rigveda"), "印度最古老经典，公版译本。", "约公元前1500—1200年")
add("pri-mahabharata", "摩诃婆罗多", "托名 Vyasa（毗耶娑）", -400, P, wikisource("Mahabharata"), "印度两大史诗之一。", "约公元前4世纪—公元4世纪")
add("pri-ramayana", "罗摩衍那", "Valmiki（蚁垤）", -300, P, wikisource("Ramayana"), "印度两大史诗之一。", "约公元前4—2世纪")
add("pri-vishnu-purana", "毗湿奴往世书", "佚名（印度）", 500, P, wiki("Vishnu_Purana"), "往世书文献之一。", "约公元5—9世纪")
add("pri-kojiki", "古事记", "太安万侣（O no Yasumaro）", 712, P, wikisource("Kojiki"), "日本最早的官修史书，含创世神话。")
add("pri-nihon-shoki", "日本书纪", "舍人亲王等", 720, P, wikisource("Nihon_Shoki"), "日本官修正史。")
add("pri-popol-vuh", "波波尔·乌（Popol Vuh）", "佚名（基切玛雅）", 1550, P, wikisource("Popol_Vuh"), "玛雅创世神话核心文本，殖民时期抄录。", "约16世纪中叶")
add("pri-bible-kjv", "圣经（King James Version）", "不详（钦定译本委员会）", 1611, P, wikisource("Bible,_King_James_Version"), "公共领域英文译本，仅作文本引用。")
add("pri-quran", "古兰经（译本）", "不详（译者依版本）", 650, P, wikisource("Quran"), "经文日期为传统认定的启示期，译本版本需分别注明。", "约公元610—632年")
add("pri-tao-te-ching", "道德经", "老子（托名）", -500, P, wikisource("Tao_Te_Ching"), "公共领域译本。", "约公元前6—5世纪")
add("pri-zhuangzi", "庄子", "庄周（托名）", -300, P, wikisource("Zhuangzi_(book)"), "公共领域译本。", "约公元前4—3世纪")
add("pri-shan-hai-jing", "山海经", "佚名（中国）", -300, P, wikisource("Shan_Hai_Jing"), "先秦地理神话文献汇编。", "约公元前4—1世纪")
add("pri-chu-ci", "楚辞", "屈原等（中国）", -300, P, wikisource("Chu_Ci"), "含《天问》《离骚》等神话材料。", "约公元前4—3世纪")
add("pri-i-ching", "易经", "佚名（中国）", -1000, P, wikisource("I_Ching"), "占筮经典，成书年代有争议。", "约公元前10—7世纪")
add("pri-analects", "论语", "孔子及其弟子", -500, P, wikisource("Analects"), "儒家经典。", "约公元前5世纪")
add("pri-dhammapada", "法句经", "佚名（佛陀语录汇编）", -300, P, wikisource("Dhammapada"), "佛教经典，公共领域译本。", "约公元前4—3世纪")
add("pri-kalevala", "卡勒瓦拉（Kalevala）", "Elias Lönnrot（编纂）", 1835, P, wikisource("Kalevala"), "据芬兰—卡累利阿口传神话编纂，非单一作者原创。", "1835 初版 / 1849 新版")
add("pri-journey-west", "西游记", "托名吴承恩（中国）", 1592, P, wikisource("Journey_to_the_West"), "明代神魔小说，孙悟空形象的主要文本来源。", "约16世纪")

# ===== B 学术著作 =====
A = "学术著作"
add("aca-golden-bough", "金枝（The Golden Bough）", "James George Frazer", 1890, A, worldcat("The Golden Bough"), "比较神话学经典，观点代表特定学派。")
add("aca-hero-faces", "千面英雄（The Hero with a Thousand Faces）", "Joseph Campbell", 1949, A, worldcat("The Hero with a Thousand Faces"), "英雄之旅母题的系统阐述。")
add("aca-eternal-return", "永恒回归的神话（The Myth of the Eternal Return）", "Mircea Eliade", 1949, A, worldcat("The Myth of the Eternal Return"), "宗教现象学代表作。")
add("aca-patterns-religion", "比较宗教的模式（Patterns in Comparative Religion）", "Mircea Eliade", 1958, A, worldcat("Patterns in Comparative Religion"), "宗教现象学，母题比较。")
add("aca-structural-anthro", "结构人类学（Structural Anthropology）", "Claude Lévi-Strauss", 1958, A, worldcat("Structural Anthropology"), "结构主义神话分析方法论。")
add("aca-mythologies-barthes", "神话学（Mythologies）", "Roland Barthes", 1957, A, worldcat("Mythologies"), "符号学视角的神话批判。")
add("aca-greek-religion", "希腊宗教（Greek Religion）", "Walter Burkert", 1977, A, worldcat("Greek Religion"), "古希腊宗教研究权威著作。", "1977（1985 英文版）")
add("aca-greek-myth-thought", "希腊神话与思想（Greek Mythology and Thought）", "Jean-Pierre Vernant", 1990, A, worldcat("Greek Mythology and Thought"), "巴黎学派神话研究。", "1990年代")
add("aca-prolegomena", "希腊宗教研究导论（Prolegomena to the Study of Greek Religion）", "Jane Ellen Harrison", 1903, A, worldcat("Prolegomena to the Study of Greek Religion"), "剑桥学派神话仪式理论。")
add("aca-archetypes", "原型与集体无意识（Archetypes and the Collective Unconscious）", "C. G. Jung", 1959, A, worldcat("Archetypes and the Collective Unconscious"), "荣格学派原型理论，注明学派归属。", "1959（德文原版更早）")
add("aca-power-myth", "神话的力量（The Power of Myth）", "Joseph Campbell / Bill Moyers", 1988, A, worldcat("The Power of Myth"), "对话体通俗阐述。")
add("aca-anatomy-criticism", "批评的剖析（Anatomy of Criticism）", "Northrop Frye", 1957, A, worldcat("Anatomy of Criticism"), "文学原型批评。")
add("aca-gods-indo-europeans", "印欧人的神（Gods of the Indo-Europeans）", "Georges Dumézil", 1986, A, worldcat("Gods of the Indo-Europeans"), "印欧比较神话学，三功能假说。")
add("aca-comparative-myth", "比较神话学（Comparative Mythology）", "Jaan Puhvel", 1987, A, worldcat("Comparative Mythology"), "印欧神话比较研究教材。")
add("aca-implied-spider", "隐含的蜘蛛（The Implied Spider）", "Wendy Doniger", 1998, A, worldcat("The Implied Spider"), "跨文化比较的方法论反思。")
add("aca-short-history-myth", "神话简史（A Short History of Myth）", "Karen Armstrong", 2005, A, worldcat("A Short History of Myth"), "通俗概述。")
add("aca-greek-myths-graves", "希腊神话（The Greek Myths）", "Robert Graves", 1955, A, worldcat("The Greek Myths"), "通俗重述，非严格学术，引用需谨慎。")
add("aca-myth-ritual-religion", "神话、仪式与宗教（Myth, Ritual and Religion）", "Andrew Lang", 1887, A, worldcat("Myth, Ritual and Religion"), "早期人类学派神话学。")
add("aca-sumerian-mythology", "苏美尔神话（Sumerian Mythology）", "Samuel Noah Kramer", 1944, A, worldcat("Sumerian Mythology"), "苏美尔神话研究奠基作。")
add("aca-treasures-darkness", "黑暗中的珍宝（The Treasures of Darkness）", "Thorkild Jacobsen", 1976, A, worldcat("The Treasures of Darkness"), "美索不达米亚宗教研究。")
add("aca-before-philosophy", "哲学之前（Before Philosophy）", "Henri Frankfort 等", 1946, A, worldcat("Before Philosophy"), "近东与埃及思想比较。")
add("aca-hittite-myths", "赫梯神话（Hittite Myths）", "Gary Beckman", 1982, A, worldcat("Hittite Myths"), "赫梯神话文本译注。")
add("aca-shamanism", "萨满教（Shamanism）", "Mircea Eliade", 1951, A, worldcat("Shamanism"), "萨满教研究经典。", "1951（英文版1964）")
add("aca-religions-american-indians", "美洲印第安人的宗教（The Religions of the American Indians）", "Åke Hultkrantz", 1979, A, worldcat("The Religions of the American Indians"), "北美原住民宗教综述。")
add("aca-god-is-not-one", "神并非唯一（God Is Not One）", "Stephen Prothero", 2010, A, worldcat("God Is Not One"), "世界宗教比较读物。")
add("aca-battle-for-god", "为上帝而战（The Battle for God）", "Karen Armstrong", 2000, A, worldcat("The Battle for God"), "基要主义研究。")
add("aca-gnostic-gospels", "诺斯替福音（The Gnostic Gospels）", "Elaine Pagels", 1979, A, worldcat("The Gnostic Gospels"), "早期基督教异端研究。")
add("aca-myth-legend-custom", "旧约中的神话、传说与习俗（Myth, Legend, and Custom in the Old Testament）", "Theodor H. Gaster", 1969, A, worldcat("Myth, Legend, and Custom in the Old Testament"), "旧约民俗与神话研究。")
add("aca-sacred-profane", "神圣与世俗（The Sacred and the Profane）", "Mircea Eliade", 1956, A, worldcat("The Sacred and the Profane"), "宗教现象学基本概念。")
add("aca-elementary-forms", "宗教生活的基本形式（The Elementary Forms of Religious Life）", "Émile Durkheim", 1912, A, worldcat("The Elementary Forms of Religious Life"), "宗教社会学经典。")
add("aca-protestant-ethic", "新教伦理与资本主义精神（The Protestant Ethic and the Spirit of Capitalism）", "Max Weber", 1905, A, worldcat("The Protestant Ethic and the Spirit of Capitalism"), "宗教社会学经典。")
add("aca-varieties-religion", "宗教经验之种种（The Varieties of Religious Experience）", "William James", 1902, A, worldcat("The Varieties of Religious Experience"), "宗教心理学经典。")

# ===== C 权威百科 =====
E = "权威百科"
for sid, slug, title in [
    ("enc-brit-mythology", "mythology", "Encyclopaedia Britannica: Mythology"),
    ("enc-brit-greek", "Greek_mythology", "Encyclopaedia Britannica: Greek mythology"),
    ("enc-brit-norse", "Norse_mythology", "Encyclopaedia Britannica: Norse mythology"),
    ("enc-brit-egyptian", "Egyptian_mythology", "Encyclopaedia Britannica: Egyptian mythology"),
    ("enc-brit-mesopotamian", "Mesopotamian_mythology", "Encyclopaedia Britannica: Mesopotamian mythology"),
    ("enc-brit-celtic", "Celtic_mythology", "Encyclopaedia Britannica: Celtic mythology"),
    ("enc-brit-hinduism", "Hinduism", "Encyclopaedia Britannica: Hinduism"),
    ("enc-brit-buddhism", "Buddhism", "Encyclopaedia Britannica: Buddhism"),
    ("enc-brit-christianity", "Christianity", "Encyclopaedia Britannica: Christianity"),
    ("enc-brit-islam", "Islam", "Encyclopaedia Britannica: Islam"),
    ("enc-brit-judaism", "Judaism", "Encyclopaedia Britannica: Judaism"),
    ("enc-brit-taoism", "Taoism", "Encyclopaedia Britannica: Taoism"),
    ("enc-brit-shinto", "Shinto", "Encyclopaedia Britannica: Shinto"),
    ("enc-brit-tantrism", "Tantrism", "Encyclopaedia Britannica: Tantrism"),
]:
    add(sid, title, "Encyclopaedia Britannica", 2024, E, brit(slug), "百科条目，年份为动态更新年而非出版年。", "持续更新（2024 复核）", verified=False)
for sid, title in [
    ("enc-wiki-mythology", "Wikipedia: Mythology"),
    ("enc-wiki-list-myth", "Wikipedia: List of mythologies"),
    ("enc-wiki-creation", "Wikipedia: Creation myth"),
    ("enc-wiki-flood", "Wikipedia: Flood myth"),
    ("enc-wiki-underworld", "Wikipedia: Underworld"),
    ("enc-wiki-hero-journey", "Wikipedia: Hero's journey"),
    ("enc-wiki-world-religion", "Wikipedia: World religion"),
    ("enc-wiki-dragon", "Wikipedia: Dragon"),
    ("enc-wiki-world-tree", "Wikipedia: World tree"),
]:
    add(sid, title, "Wikipedia", 2026, E, wiki(title.replace("Wikipedia: ", "")), "维基百科条目，动态更新，仅作线索与交叉核对，不作唯一依据。", "持续更新", verified=False)
add("enc-macmillan-religion", "Encyclopedia of Religion", "Mircea Eliade（主编）", 1987, E, worldcat("Encyclopedia of Religion"), "宗教学权威百科，第2版 2004 年（Lindsay Jones 主编）。", "1987（第2版2004）")
add("enc-oxford-world-religions", "Oxford Dictionary of World Religions", "John Bowker", 1997, E, worldcat("Oxford Dictionary of World Religions"), "牛津世界宗教词典。")
add("enc-oxford-classical", "Oxford Classical Dictionary", "Third Edition（编辑委员会）", 1996, E, worldcat("Oxford Classical Dictionary"), "古典学权威工具书。", "1996（第3版）")

# ===== D 官方机构 / 数字资源 =====
I = "官方机构"
for sid, title, org, url in [
    ("ins-met", "The Metropolitan Museum of Art（含 Heilbrunn Timeline）", "大都会艺术博物馆", "https://www.metmuseum.org/"),
    ("ins-british-museum", "The British Museum", "大英博物馆", "https://www.britishmuseum.org/"),
    ("ins-louvre", "Musée du Louvre", "卢浮宫博物馆", "https://www.louvre.fr/"),
    ("ins-egyptian-museum", "Egyptian Museum, Cairo", "开罗埃及博物馆", "https://egymonuments.gov.eg/"),
    ("ins-iraq-museum", "Iraq National Museum", "伊拉克国家博物馆", "https://www.iraqmuseum.org/"),
    ("ins-british-library", "The British Library", "大英图书馆", "https://www.bl.uk/"),
    ("ins-perseus", "Perseus Digital Library", "Tufts University", "https://www.perseus.tufts.edu/"),
    ("ins-theoi", "Theoi Project（古希腊神话资料库）", "Theoi Project", "https://www.theoi.com/"),
    ("ins-gutenberg", "Project Gutenberg", "Project Gutenberg", "https://www.gutenberg.org/"),
    ("ins-internet-archive", "Internet Archive", "Internet Archive", "https://archive.org/"),
    ("ins-wikisource", "Wikisource", "Wikimedia Foundation", "https://en.wikisource.org/"),
    ("ins-yale-babylonian", "Yale Babylonian Collection", "Yale University", "https://babyloniancollection.org/"),
    ("ins-ashmolean", "Ashmolean Museum", "University of Oxford", "https://www.ashmolean.org/"),
    ("ins-getty", "The Getty", "J. Paul Getty Trust", "https://www.getty.edu/"),
    ("ins-smithsonian", "Smithsonian Institution", "Smithsonian Institution", "https://www.si.edu/"),
    ("ins-mfa-boston", "Museum of Fine Arts, Boston", "MFA Boston", "https://www.mfa.org/"),
    ("ins-nara-museum", "Nara National Museum", "日本国立奈良博物馆", "https://www.narahaku.go.jp/"),
    ("ins-pluralism", "The Pluralism Project", "Harvard University", "https://pluralism.org/"),
    ("ins-pew-religion", "Pew Research Center — Religion", "Pew Research Center", "https://www.pewresearch.org/religion/"),
    ("ins-vatican", "The Holy See", "Holy See", "https://www.vatican.va/"),
    ("ins-unesco", "UNESCO", "联合国教科文组织", "https://www.unesco.org/"),
    ("ins-sacred-texts", "Sacred Texts Archive", "Sacred Texts", "https://www.sacred-texts.com/"),
    ("ins-world-history", "World History Encyclopedia", "World History Encyclopedia", "https://www.worldhistory.org/"),
    ("ins-oriental-institute", "The Oriental Institute", "University of Chicago", "https://oi.uchicago.edu/"),
]:
    add(sid, title, org, None, I, url, "机构/数字资源页，无统一出版年份，未在线核验。", "机构资源（无年份）", verified=False)

# 去重校验
ids = [s["id"] for s in sources]
assert len(ids) == len(set(ids)), "重复来源 id"
out = {"sources": sources}
with open(os.path.join(ROOT, "sources.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
    f.write("\n")
counts = {}
for s in sources:
    counts[s["type"]] = counts.get(s["type"], 0) + 1
print("sources.json: %d sources; %s" % (len(sources), counts))
print("verified(true)=%d, verified(false)=%d" % (
    sum(1 for s in sources if s["verified"]), sum(1 for s in sources if not s["verified"])))
