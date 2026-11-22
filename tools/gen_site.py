#!/usr/bin/env python3
"""gen_site.py — 从 JSON 数据层确定性渲染零 JS 静态站点到 site/。"""
import sys, os, json, re, html, glob
from collections import defaultdict

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "site")
UNIT_NAMES = {"U1": "神话体系", "U2": "宗教传统", "U3": "母题", "U4": "人物"}
UNIT_DESC = {
    "U1": "按文化传统划分的神话体系，收录各传统的宇宙观、神祇谱系与代表性叙事。",
    "U2": "以介绍与比较为主的世界宗教传统及其主要分支，采用学术描述性立场。",
    "U3": "跨传统比较的叙事母题，只记录学界有文献依据的比较研究。",
    "U4": "常被用于跨传统比较的神祇、教主与英雄人物。",
}
PERIOD_NAMES = {"ancient": "古代", "classical": "古典", "medieval": "中世纪", "modern": "近现代", "oral": "口传传统"}
TIER_CLASS = {"核心": "core", "重要": "imp", "补充": "sup"}

def esc(s):
    return html.escape(str(s if s is not None else ""), quote=True)

def sanitize_svg(svg):
    s = (svg or "").replace("/<", "/><")
    s = re.sub(r"y='([^']*?)' width=", r"y='\1' width=", s)
    return s

def load(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return json.load(f)

def parse_scope():
    out = {}
    for line in open(os.path.join(ROOT, "scope.md"), encoding="utf-8").read().splitlines():
        if not line.startswith("|"):
            continue
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) >= 6 and re.fullmatch(r"[a-z0-9-]+", c[0]) and re.match(r"^(myth|rel|motif|fig)-", c[0]):
            out[c[0]] = {"title": c[1], "tier": c[2], "period": c[4], "desc": c[5]}
    return out

scope = parse_scope()
sources = {s["id"]: s for s in load("sources.json")["sources"]}
coverage = load("coverage.json")
written = {}
for p in sorted(glob.glob(os.path.join(ROOT, "data", "units", "*.json"))):
    for e in load(os.path.relpath(p, ROOT).replace("\\", "/")).get("entries", []):
        written[e["id"]] = e

def write_page(rel, body, title, prefix=""):
    nav_items = [
        (prefix + "index.html", "首页"),
        (prefix + "all.html", "全站索引"),
        (prefix + "units/U1.html", "神话体系"),
        (prefix + "units/U2.html", "宗教传统"),
        (prefix + "units/U3.html", "母题"),
        (prefix + "units/U4.html", "人物"),
        (prefix + "matrix.html", "覆盖矩阵"),
        (prefix + "sources.html", "来源库"),
        (prefix + "about.html", "方法论"),
    ]
    nav = "\n".join('    <a href="%s">%s</a>' % (esc(h), esc(t)) for h, t in nav_items)
    doc = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s — 宗教与神话比较库</title>
<link rel="stylesheet" href="%sstyle.css">
</head>
<body>
<span id="theme-dark"></span><span id="theme-light"></span>
<header class="site-head">
  <div class="theme-switch"><a href="#theme-dark">深色</a> <a href="#theme-light">浅色</a></div>
  <h1>宗教与神话比较库</h1>
  <div class="sub">学术描述性立场 · 双源校验 · 待核实诚实标注 · 零 JS 静态站点</div>
</header>
<nav class="topnav">
%s
</nav>
<main>
%s
</main>
<footer class="site-foot">
  数据与呈现分离：修改 <code>data/</code> 后运行 <code>tools/gen_site.py</code> 重新生成。本站不使用任何图片，图示均为内联 SVG。
</footer>
</body>
</html>
""" % (esc(title), esc(prefix), nav, body)
    path = os.path.join(SITE, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(doc)

def crumb(items):
    return '<div class="breadcrumb">' + " › ".join(
        ('<a href="%s">%s</a>' % (esc(h), esc(t)) if h else esc(t)) for h, t in items) + "</div>"

def badge(e):
    s = '<span class="badge %s">%s</span>' % (TIER_CLASS.get(e["tier"], "sup"), esc(e["tier"]))
    s += '<span class="badge l2">%s</span>' % esc(e["level"])
    if e.get("needs_verification"):
        s += '<span class="badge flag">待核实</span>'
    return s

def entry_line(eid, prefix=""):
    meta = scope[eid]
    e = written.get(eid)
    if e:
        href = "%sentries/%s.html" % (prefix, esc(eid))
        title = '<a href="%s">%s</a>' % (href, esc(meta["title"]))
        b = badge(e)
        summary = '<div class="meta">%s</div>' % esc(e.get("summary", "")[:110])
    else:
        title = esc(meta["title"])
        b = '<span class="badge sup">待撰写</span>'
        summary = '<div class="meta">%s</div>' % esc(meta["desc"])
    return '<li>%s %s <span class="meta">[%s]</span>%s</li>' % (
        title, b, esc(PERIOD_NAMES.get(meta["period"], meta["period"])), summary)

def src_items(e, prefix=""):
    ids = e.get("sources", [])
    if not ids:
        return ""
    lis = []
    for sid in ids:
        s = sources.get(sid)
        if not s:
            continue
        url = s.get("url")
        label = esc(s["title"]) + "（" + esc(s["author"]) + (("，" + esc(s["year_display"])) if s.get("year_display") else "") + "）"
        link = '<a href="%s" target="_blank" rel="noopener">%s</a>' % (esc(url), label) if url else label
        flag = "" if s.get("verified") else ' <span class="badge flag">未在线核验</span>'
        lis.append("<li>%s%s</li>" % (link, flag))
    return '<div class="src-list"><strong>来源（%d）</strong><ul>%s</ul></div>' % (len(lis), "".join(lis))

# ---------- 首页 ----------
def build_home():
    total = len(scope)
    l2 = sum(1 for e in written.values() if e.get("level") in ("L2", "L3"))
    stats = [
        (total, "计划条目"), (len(written), "已撰写条目"), (l2, "L2 深度条目"),
        (len(sources), "权威来源"), (coverage["summary"]["verified_sources"], "书目已核对来源"),
    ]
    stat_html = "\n".join('<div class="stat"><span class="num">%s</span><span class="label">%s</span></div>' % (n, l) for n, l in stats)
    cards = []
    for u in ("U1", "U2", "U3", "U4"):
        cnt = sum(1 for eid in scope if scope[eid]["title"] and eid.startswith(
            {"U1": "myth-", "U2": "rel-", "U3": "motif-", "U4": "fig-"}[u]))
        done = sum(1 for eid in written if eid.startswith({"U1": "myth-", "U2": "rel-", "U3": "motif-", "U4": "fig-"}[u]))
        cards.append('<div class="card"><h3><a href="units/%s.html">%s %s</a></h3><p>%s</p><p class="meta">计划 %d 条 · 已撰写 %d 条</p></div>' % (
            u, u, UNIT_NAMES[u], esc(UNIT_DESC[u]), cnt, done))
    body = """
<div class="section">
  <p>本站以学术与描述性立场，系统整理世界主要神话体系、宗教传统，以及跨文化的叙事母题与代表人物。
     所有条目均标注来源与待核实项；引用未在线核验来源的内容一律显式标记，不替读者下结论。</p>
  <div class="stats">%s</div>
</div>
<h2>四大板块</h2>
<div class="grid">%s</div>
<h2>快速入口</h2>
<div class="grid">
  <div class="card"><h3><a href="all.html">全站条目索引</a></h3><p>按单元浏览全部 118 个计划条目。</p></div>
  <div class="card"><h3><a href="matrix.html">覆盖矩阵</a></h3><p>传统 × 母题类型 × 时期三维覆盖视图。</p></div>
  <div class="card"><h3><a href="sources.html">来源库</a></h3><p>%d 条权威来源，含原典、学术著作、百科与机构资源。</p></div>
  <div class="card"><h3><a href="about.html">方法论与诚实标注</a></h3><p>范围方法、三框架并集、双源规则与待核实机制。</p></div>
</div>
<div class="note">本站处于分层写作阶段：先完成全部条目的 L1 骨架，再按 核心→重要→补充 升级 L2，核心条目可做 L3。当前进度见 <a href="about.html">方法论</a> 与项目根 <code>PROGRESS.md</code>。</div>
""" % (stat_html, "\n".join(cards), len(sources))
    write_page("index.html", body, "首页")

# ---------- 单元页 ----------
def build_units():
    for u in ("U1", "U2", "U3", "U4"):
        prefix = {"U1": "myth-", "U2": "rel-", "U3": "motif-", "U4": "fig-"}[u]
        groups = defaultdict(list)
        for eid, m in scope.items():
            if eid.startswith(prefix):
                groups[m["tier"]].append(eid)
        body = crumb([("", "首页"), ("", "%s %s" % (u, UNIT_NAMES[u]))])
        body += "<h2>%s %s</h2><p>%s</p>" % (u, UNIT_NAMES[u], esc(UNIT_DESC[u]))
        for tier in ("核心", "重要", "补充"):
            ids = sorted(groups.get(tier, []))
            if not ids:
                continue
            body += "<h3>%s（%d 条）</h3><ul>%s</ul>" % (
                tier, len(ids), "\n".join(entry_line(i, "../") for i in ids))
        write_page("units/%s.html" % u, body, "%s %s" % (u, UNIT_NAMES[u]), "../")

# ---------- 条目页 ----------
def build_entries():
    for eid, e in written.items():
        m = scope.get(eid, {"title": e.get("title", eid)})
        u = eid.split("-")[0]
        unit = {"myth": "U1", "rel": "U2", "motif": "U3", "fig": "U4"}.get(u, "U1")
        body = crumb([("", "首页"), ("../units/%s.html" % unit, UNIT_NAMES.get(unit, unit)), ("", m["title"])])
        body += "<h2>%s</h2><p>%s</p>" % (esc(m["title"]), badge(e))
        if e.get("level") == "L1":
            body += '<div class="section"><h3>概述</h3><p>%s</p></div>' % esc(e.get("summary", ""))
        else:
            if e.get("source_text"):
                body += '<div class="section"><h3>1. 来源文本</h3><p>%s</p></div>' % esc(e["source_text"])
            body += '<div class="section"><h3>2. 故事梗概</h3><p>%s</p></div>' % esc(e.get("summary", ""))
            if e.get("versions"):
                body += '<div class="section"><h3>3. 不同版本的差异</h3><ul>%s</ul></div>' % "".join("<li>%s</li>" % esc(v) for v in e["versions"])
            if e.get("interpretations"):
                rows = "".join("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (
                    esc(i.get("holder")), esc(i.get("school")), esc(i.get("view"))) for i in e["interpretations"])
                body += '<div class="section"><h3>4. 象征与研究者的解读</h3><table><tr><th>研究者</th><th>学派</th><th>观点</th></tr>%s</table></div>' % rows
            if e.get("comparisons"):
                rows = "".join("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (
                    esc(c.get("tradition")), esc(sources.get(c.get("basis_source"), {}).get("title", c.get("basis_source"))), esc(c.get("note"))) for c in e["comparisons"])
                body += '<div class="section"><h3>5. 与其他传统的相似母题（仅限有文献依据者）</h3><table><tr><th>传统</th><th>依据来源</th><th>说明</th></tr>%s</table></div>' % rows
            if e.get("svg"):
                body += '<div class="section"><h3>6. 图示</h3><div class="svg-wrap">%s</div></div>' % sanitize_svg(e["svg"])
        if e.get("related"):
            rel_items = []
            for r in e["related"]:
                label = esc(scope.get(r, {}).get("title", r))
                if r in written:
                    rel_items.append('<li><a href="%s.html">%s</a></li>' % (esc(r), label))
                else:
                    rel_items.append('<li>%s <span class="badge sup">待撰写</span></li>' % label)
            body += '<div class="section"><h3>相关条目</h3><ul>%s</ul></div>' % "".join(rel_items)
        body += '<div class="section"><h3>%s</h3>%s</div>' % (
            "7. 待核实" if e.get("level") != "L1" else "待核实",
            '<div class="note">%s</div>' % esc(e.get("pending_notes")) if e.get("pending_notes") else "<p>无。</p>")
        body += src_items(e)
        write_page("entries/%s.html" % eid, body, m["title"], "../")

# ---------- 全站索引 ----------
def build_all():
    body = crumb([("", "首页"), ("", "全站条目索引")]) + "<h2>全站条目索引</h2>"
    for u in ("U1", "U2", "U3", "U4"):
        prefix = {"U1": "myth-", "U2": "rel-", "U3": "motif-", "U4": "fig-"}[u]
        ids = sorted(i for i in scope if i.startswith(prefix))
        body += "<h3>%s %s（%d 条）</h3><ul>%s</ul>" % (
            u, UNIT_NAMES[u], len(ids), "\n".join(entry_line(i) for i in ids))
    write_page("all.html", body, "全站条目索引")

# ---------- 覆盖矩阵 ----------
def build_matrix():
    dims = coverage["matrix"]["dimensions"]
    cells = {(c["tradition"], c["motif"]): c for c in coverage["matrix"]["cells"]}
    motifs = dims["motifs"]
    traditions = coverage["entries"]
    tname = {e["id"]: e["name"] for e in traditions}
    mname = {e["id"]: e["name"] for e in traditions}
    body = crumb([("", "首页"), ("", "覆盖矩阵")])
    body += "<h2>覆盖矩阵：传统 × 母题类型 × 时期</h2>"
    body += '<p class="meta">✓ = 说明中预期涉及该母题（expected）；L2/L3 = 已按该层级撰写；· = 暂无。矩阵由 <code>tools/build_coverage.py</code> 从 scope.md 与已写条目派生。</p>'
    for period in dims["periods"]:
        ts = [e for e in traditions if e["id"] in dims["traditions"] and scope.get(e["id"], {}).get("period") == period]
        if not ts:
            continue
        body += "<h3>时期：%s（%d 个传统）</h3>" % (PERIOD_NAMES.get(period, period), len(ts))
        body += "<table><tr><th>传统</th>%s</tr>" % "".join("<th>%s</th>" % esc(mname.get(m, m)) for m in motifs)
        for t in ts:
            marks = []
            for mid in motifs:
                c = cells.get((t["id"], mid), {})
                marks.append(c.get("status", "empty") if c.get("status") != "empty" else ("✓" if c.get("expected") else "·"))
            body += "<tr><td>%s</td>%s</tr>" % (esc(t["name"]), "".join("<td>%s</td>" % esc(x) for x in marks))
        body += "</table>"
    write_page("matrix.html", body, "覆盖矩阵")

# ---------- 来源库 ----------
def build_sources():
    groups = defaultdict(list)
    for s in sources.values():
        groups[s["type"]].append(s)
    body = crumb([("", "首页"), ("", "来源库")]) + "<h2>来源库（%d 条）</h2>" % len(sources)
    body += '<p class="meta">联网端点不可用，<code>verified</code> 在本项目表示"书目信息已核对"，并不代表已在线打开页面；所有来源的 <code>link_ok</code> 均为 null。详见项目根 <code>DECISIONS.md</code> D2。</p>'
    for typ in ("原典", "学术著作", "权威百科", "官方机构"):
        ss = sorted(groups.get(typ, []), key=lambda x: (x.get("year") is None, x.get("year") or 0))
        body += "<h3>%s（%d 条）</h3>" % (esc(typ), len(ss))
        body += "<table><tr><th>标题</th><th>作者/机构</th><th>年份</th><th>核对</th></tr>"
        for s in ss:
            t = '<a href="%s" target="_blank" rel="noopener">%s</a>' % (esc(s["url"]), esc(s["title"])) if s.get("url") else esc(s["title"])
            v = "书目已核对" if s.get("verified") else '<span class="badge flag">未在线核验</span>'
            body += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (t, esc(s["author"]), esc(s["year_display"]), v)
        body += "</table>"
    write_page("sources.html", body, "来源库")

# ---------- 方法论 ----------
def build_about():
    sm = coverage["summary"]
    body = crumb([("", "首页"), ("", "方法论")])
    body += """
<h2>方法论与诚实标注</h2>
<h3>范围：三份框架取并集</h3>
<p>条目清单见项目根 <code>scope.md</code>。以百科分类树（F1）、比较神话学教材母题体系（F2）、宗教学导论课程大纲（F3）三类通行学术框架取并集，形成 118 条计划条目。</p>
<h3>双源规则与待核实</h3>
<p>每条内容至少引用 2 个独立来源；不足者必须标注 <code>needs_verification=true</code> 并写明待核实项。
   引用未在线核验来源的条目一律显式标记"待核实"。关键事实需两个独立来源互证。</p>
<h3>写作立场</h3>
<p>学术描述性立场："某宗教认为""某学者认为"均写明主语；不评判信仰真伪，不贬低也不推崇。
   神话之间的类比必须有文献依据，无依据的类比不写。经典引文只用公版译本或自译，不超过一两句。</p>
<h3>图示</h3>
<p>不使用任何图片；所有图示为内联 SVG，文字使用 CSS 变量，浅色与深色模式皆可读。</p>
<h3>当前进度</h3>
<p>计划 %d 条；已撰写 %d 条；L2 及以上 %d 条；来源 %d 条（书目已核对 %d 条）。完整进度见项目根 <code>PROGRESS.md</code>。</p>
<div class="note">联网检索端点在本环境不可用（见 <code>DECISIONS.md</code> D2）：来源不编造，未在线核对者如实标注；恢复联网后可用 <code>tools/linkcheck.py</code> 补核链接三态。</div>
""" % (sm["total"], len(written), sm["l2_done"], len(sources), sm["verified_sources"])
    write_page("about.html", body, "方法论")

def main():
    os.makedirs(SITE, exist_ok=True)
    build_home()
    build_units()
    build_entries()
    build_all()
    build_matrix()
    build_sources()
    build_about()
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write('<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=site/index.html"><title>宗教与神话比较库</title></head><body><a href="site/index.html">进入《宗教与神话比较库》</a></body></html>\n')
    print("gen_site: %d pages written to site/" % (
        len(glob.glob(os.path.join(SITE, "**", "*.html"), recursive=True))))

if __name__ == "__main__":
    main()
