#!/usr/bin/env python3
"""check.py — 《宗教与神话比较库》质量守门员。

规则对应 TASK_myth.md 硬性规则 + WORKFLOW.md R1–R16，并按 DECISIONS.md D2
把"来源 verified"降级为"未在线核验来源必须标注待核实"。
用法：python tools/check.py [--file data/units/U1.json] [--quiet]
"""
import sys, os, json, re, glob
import xml.etree.ElementTree as ET

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ERRORS, WARNINGS = [], []

def err(msg):
    ERRORS.append(msg)

def warn(msg):
    WARNINGS.append(msg)

def load_json(rel):
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        err("缺少文件：%s" % rel)
        return None
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        err("JSON 解析失败：%s — %s" % (rel, e))
        return None

def valid_id(sid):
    return isinstance(sid, str) and re.fullmatch(r"[a-z0-9-]+", sid) is not None

# ---------- 1. sources.json ----------
def check_sources():
    d = load_json("sources.json")
    if not d:
        return set()
    srcs = d.get("sources", [])
    if len(srcs) < 80:
        err("来源不足 80 条：当前 %d 条" % len(srcs))
    ids = set()
    allowed_types = {"原典", "学术著作", "权威百科", "官方机构"}
    for s in srcs:
        sid = s.get("id", "")
        if not valid_id(sid):
            err("来源 id 非法：%r（仅允许 a-z0-9-）" % sid)
        if sid in ids:
            err("来源 id 重复：%s" % sid)
        ids.add(sid)
        for k in ("title", "author", "type", "url", "note"):
            if not isinstance(s.get(k), str) or not s[k].strip():
                err("来源 %s 缺少必填字段 %s" % (sid, k))
        if s.get("type") not in allowed_types:
            err("来源 %s 类型不在四分类内：%r" % (sid, s.get("type")))
        if s.get("url") and not re.match(r"^https?://", s["url"]):
            err("来源 %s URL 非法：%r" % (sid, s["url"]))
        y = s.get("year")
        if y is not None and (not isinstance(y, int) or isinstance(y, bool)):
            err("来源 %s 年份必须为整数（负数=公元前）：%r" % (sid, y))
        if not isinstance(s.get("verified"), bool):
            err("来源 %s verified 必须为布尔值" % sid)
        if not s.get("verified") and "未在线" not in s.get("note", "") and "动态更新" not in s.get("note", ""):
            err("来源 %s verified=false 必须在 note 说明未核验原因" % sid)
    return ids

# ---------- 2. scope.md 与 coverage.json ----------
def parse_scope_ids():
    path = os.path.join(ROOT, "scope.md")
    if not os.path.exists(path):
        err("缺少 scope.md")
        return {}
    out = {}
    for line in open(path, encoding="utf-8").read().splitlines():
        if not line.startswith("|"):
            continue
        cols = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cols) >= 6 and valid_id(cols[0]) and re.match(r"^(myth|rel|motif|fig)-", cols[0]):
            out[cols[0]] = {"title": cols[1], "tier": cols[2], "period": cols[4]}
    return out

def check_coverage(scope):
    cov = load_json("coverage.json")
    if not cov:
        return None
    entries = cov.get("entries", [])
    ids = [e.get("id") for e in entries]
    if len(ids) != len(set(ids)):
        err("coverage.json 存在重复条目 id")
    if set(ids) != set(scope):
        miss = set(scope) - set(ids)
        extra = set(ids) - set(scope)
        if miss:
            err("coverage.json 缺少 scope 条目：%s" % sorted(miss)[:8])
        if extra:
            err("coverage.json 多出 scope 未定义条目：%s" % sorted(extra)[:8])
    for e in entries:
        for k in ("id", "name", "unit", "tier", "level", "status", "last_updated"):
            if k not in e:
                err("coverage 条目 %s 缺少字段 %s" % (e.get("id"), k))
        if e.get("level") not in ("L1", "L2", "L3"):
            err("coverage 条目 %s level 非法：%r" % (e.get("id"), e.get("level")))
        if e.get("id") in scope and e.get("name") != scope[e["id"]]["title"]:
            err("coverage 条目 %s 名称与 scope.md 不一致：%r vs %r" % (
                e["id"], e.get("name"), scope[e["id"]]["title"]))
        if e.get("id") in scope and e.get("tier") != scope[e["id"]]["tier"]:
            err("coverage 条目 %s 层级与 scope.md 不一致" % e["id"])
    m = cov.get("matrix", {})
    dims = m.get("dimensions", {})
    for key in ("traditions", "motifs", "periods"):
        if not dims.get(key):
            err("coverage.json 矩阵缺少维度 %s" % key)
    if len(m.get("cells", [])) == 0:
        err("coverage.json 覆盖矩阵为空")
    return cov

# ---------- 3. 条目 JSON ----------
SVG_WHITELIST = {
    "svg", "g", "text", "tspan", "rect", "circle", "ellipse", "line",
    "polyline", "polygon", "path", "title", "desc", "defs", "marker",
    "symbol", "use", "linearGradient", "radialGradient", "stop", "clipPath",
}
SVG_FORBID_ATTR_PREFIX = ("on",)

def check_svg(svg, eid):
    if not isinstance(svg, str) or "<svg" not in svg:
        err("条目 %s SVG 缺失或格式错误" % eid)
        return
    fixed = svg.replace("/<", "/><")
    if fixed != svg:
        warn("条目 %s SVG 存在 '/<' 笔误（已按 WORKFLOW 记录，生成器将自动修复）" % eid)
    try:
        root = ET.fromstring(fixed)
    except Exception as e:
        err("条目 %s SVG XML 解析失败：%s" % (eid, e))
        return
    if root.tag.split("}")[-1] != "svg":
        err("条目 %s SVG 根元素不是 svg" % eid)
    vb = root.get("viewBox")
    if not vb:
        err("条目 %s SVG 缺少 viewBox" % eid)
        return
    nums = [float(x) for x in re.split(r"[\s,]+", vb.strip()) if x]
    if len(nums) != 4:
        err("条目 %s viewBox 必须为 4 个数字" % eid)
        return
    minx, miny, w, h = nums
    for el in root.iter():
        tag = el.tag.split("}")[-1]
        if tag not in SVG_WHITELIST:
            err("条目 %s SVG 含非白名单元素 <%s>" % (eid, tag))
        for k, v in el.attrib.items():
            if k.lower().startswith(SVG_FORBID_ATTR_PREFIX):
                err("条目 %s SVG 含事件属性 %s" % (eid, k))
            if "javascript:" in v.lower():
                err("条目 %s SVG 含 javascript: 链接" % eid)
        if tag == "text":
            fill = el.get("fill", "")
            if fill and "var(" not in fill and fill != "currentColor":
                warn("条目 %s SVG 文字 fill 未使用 CSS 变量/currentColor：%r" % (eid, fill))
        # 元素出界检查（数值属性）
        try:
            boxes = []
            if tag == "rect":
                x, y = float(el.get("x", 0)), float(el.get("y", 0))
                boxes = [(x, y, x + float(el.get("width", 0)), y + float(el.get("height", 0)))]
            elif tag == "circle":
                cx, cy, r = float(el.get("cx", 0)), float(el.get("cy", 0)), float(el.get("r", 0))
                boxes = [(cx - r, cy - r, cx + r, cy + r)]
            elif tag == "ellipse":
                cx, cy = float(el.get("cx", 0)), float(el.get("cy", 0))
                rx, ry = float(el.get("rx", 0)), float(el.get("ry", 0))
                boxes = [(cx - rx, cy - ry, cx + rx, cy + ry)]
            elif tag == "line":
                boxes = [(min(float(el.get("x1", 0)), float(el.get("x2", 0))),
                          min(float(el.get("y1", 0)), float(el.get("y2", 0))),
                          max(float(el.get("x1", 0)), float(el.get("x2", 0))),
                          max(float(el.get("y1", 0)), float(el.get("y2", 0))))]
            elif tag in ("polyline", "polygon"):
                pts = [float(v) for v in re.split(r"[\s,]+", el.get("points", "").strip()) if v]
                xs, ys = pts[0::2], pts[1::2]
                if xs and ys:
                    boxes = [(min(xs), min(ys), max(xs), max(ys))]
            elif tag == "text":
                x, y = float(el.get("x", 0)), float(el.get("y", 0))
                boxes = [(x, y, x, y)]
            for x0, y0, x1, y1 in boxes:
                if x0 < minx - 1 or y0 < miny - 1 or x1 > minx + w + 1 or y1 > miny + h + 1:
                    err("条目 %s SVG 元素 <%s> 超出 viewBox：(%s,%s)-(%s,%s)" % (eid, tag, x0, y0, x1, y1))
        except (TypeError, ValueError):
            pass  # 含 var()/百分比的坐标无法静态判定，跳过
    # 文字重叠近似检测（WARN，不阻断）：同一行附近且 x 范围相交的 text
    _tx = []
    for el in root.iter():
        if el.tag.split("}")[-1] == "text":
            try:
                _x = float(el.get("x", 0)); _y = float(el.get("y", 0))
                _fs = float(el.get("font-size", 12))
            except (TypeError, ValueError):
                continue
            _a = el.get("text-anchor", "start"); _t = "".join(el.itertext())
            _tx.append((_x, _y, _fs, _a, _t))
    def _bx(x, f, a, t):
        w = len(t) * f * 0.9
        if a == "middle":
            return (x - w / 2, x + w / 2)
        if a == "end":
            return (x - w, x)
        return (x, x + w)
    for i in range(len(_tx)):
        for j in range(i + 1, len(_tx)):
            x1, y1, f1, a1, t1 = _tx[i]; x2, y2, f2, a2, t2 = _tx[j]
            b1 = _bx(x1, f1, a1, t1); b2 = _bx(x2, f2, a2, t2)
            if abs(y1 - y2) < min(f1, f2) * 0.6 and max(b1[0], b2[0]) < min(b1[1], b2[1]):
                warn("条目 %s SVG 文字可能重叠：'%s' 与 '%s'" % (eid, t1[:8], t2[:8]))

def check_entries(source_ids, scope, cov):
    files = sorted(glob.glob(os.path.join(ROOT, "data", "units", "*.json")))
    if not files:
        warn("data/units/ 尚无条目文件（阶段0/1 属正常）")
        return []
    cov_map = {e["id"]: e for e in (cov or {}).get("entries", [])}
    seen = set()
    all_entries = []
    for path in files:
        rel = os.path.relpath(path, ROOT).replace("\\", "/")
        d = load_json(rel)
        if not d:
            continue
        for e in d.get("entries", []):
            eid = e.get("id", "")
            if not valid_id(eid):
                err("条目 id 非法：%r" % eid)
                continue
            if eid in seen:
                err("条目 id 全局重复：%s" % eid)
            seen.add(eid)
            all_entries.append(e)
            if eid not in scope:
                err("条目 %s 不在 scope.md 中" % eid)
            level = e.get("level")
            if level not in ("L1", "L2", "L3"):
                err("条目 %s level 非法：%r" % (eid, level))
            base = ["id", "title", "level", "tier", "period", "summary", "related", "sources"]
            l2 = ["source_text", "versions", "interpretations", "comparisons", "svg"]
            l3 = ["controversies", "data_points"]
            required = base + (l2 if level in ("L2", "L3") else []) + (l3 if level == "L3" else [])
            for k in required:
                if k not in e or (isinstance(e[k], str) and not e[k].strip()):
                    err("条目 %s（%s）缺少必填字段/内容：%s" % (eid, level, k))
            if e.get("title") != scope.get(eid, {}).get("title"):
                err("条目 %s 标题与 scope.md 不一致" % eid)
            if e.get("tier") != scope.get(eid, {}).get("tier"):
                err("条目 %s 层级与 scope.md 不一致" % eid)
            if e.get("period") not in ("ancient", "classical", "medieval", "modern", "oral"):
                err("条目 %s period 非法：%r" % (eid, e.get("period")))
            # 来源引用
            srcs = e.get("sources", [])
            if not isinstance(srcs, list):
                err("条目 %s sources 必须为数组" % eid)
                srcs = []
            for sid in srcs:
                if sid not in source_ids:
                    err("条目 %s 引用了未在 sources.json 定义的来源：%s" % (eid, sid))
            if len(set(srcs)) != len(srcs):
                err("条目 %s sources 存在重复 id" % eid)
            # 双源规则 + D2 未核验来源联动
            needs = bool(e.get("needs_verification"))
            pending = e.get("pending_notes", "")
            if len(set(srcs)) < 2 and not (needs and pending.strip()):
                err("条目 %s 来源少于 2 个且未标待核实（双源规则）" % eid)
            if needs and not pending.strip():
                err("条目 %s needs_verification=true 但 pending_notes 为空" % eid)
            if pending.strip() and not needs:
                err("条目 %s 有 pending_notes 但 needs_verification=false" % eid)
            src_objs = [s for s in json.load(open(os.path.join(ROOT, "sources.json"), encoding="utf-8"))["sources"] if s["id"] in srcs]
            if any(not s.get("verified") for s in src_objs) and not (needs and pending.strip()):
                err("条目 %s 引用未在线核验来源，必须 needs_verification=true 且写明 pending_notes（D2）" % eid)
            # 相关条目内部链接
            for rid in e.get("related", []):
                if rid not in scope:
                    err("条目 %s 相关条目链接到不存在的 id：%s" % (eid, rid))
            # 年份合法性（若条目带 year 字段）
            y = e.get("year")
            if y is not None:
                if not isinstance(y, int) or isinstance(y, bool):
                    err("条目 %s year 必须为整数" % eid)
                yd = e.get("year_display", "")
                m = re.search(r"\d+", str(yd))
                if m and int(m.group()) != abs(y):
                    err("条目 %s year_display 首个数字 %s 与 |year|=%d 不一致" % (eid, m.group(), abs(y)))
            # L2 结构细节
            if level in ("L2", "L3"):
                if not isinstance(e.get("versions"), list) or len(e["versions"]) < 1:
                    err("条目 %s versions 至少需要 1 条版本差异" % eid)
                for it in e.get("interpretations", []):
                    if not all(k in it for k in ("holder", "school", "view")):
                        err("条目 %s 解读缺少 holder/school/view（须标明是谁、哪一学派）" % eid)
                for it in e.get("comparisons", []):
                    if not all(k in it for k in ("tradition", "basis_source", "note")):
                        err("条目 %s 比较缺少 tradition/basis_source/note（须有文献依据）" % eid)
                    if it.get("basis_source") not in source_ids:
                        err("条目 %s 比较的 basis_source 未定义：%s" % (eid, it.get("basis_source")))
                check_svg(e.get("svg"), eid)
            # 与 coverage.json 一致性
            ce = cov_map.get(eid)
            if ce and ce.get("level") != level:
                err("条目 %s 的 level(%s) 与 coverage.json(%s) 不一致" % (eid, level, ce.get("level")))
            if ce and ce.get("sources_count") != len(set(srcs)):
                warn("条目 %s sources_count 与 coverage.json 不一致（运行 build_coverage 可刷新）" % eid)
    return all_entries

# ---------- 4. 站内链接（若已生成站点）----------
def check_site_links(entries):
    site = os.path.join(ROOT, "site")
    if not os.path.isdir(site):
        return
    known = {e["id"] for e in entries}
    for path in glob.glob(os.path.join(site, "**", "*.html"), recursive=True):
        html = open(path, encoding="utf-8").read()
        for m in re.finditer(r'href="([^"#]+)', html):
            href = m.group(1)
            if href.startswith(("http://", "https://", "mailto:")):
                continue
            target = os.path.normpath(os.path.join(os.path.dirname(path), href.split("?")[0]))
            if not os.path.exists(target):
                err("站内断链：%s → %s" % (os.path.relpath(path, ROOT), href))

def main():
    args = sys.argv[1:]
    quiet = "--quiet" in args
    scope = parse_scope_ids()
    source_ids = check_sources()
    cov = check_coverage(scope)
    entries = check_entries(source_ids, scope, cov)
    check_site_links(entries)
    if not quiet:
        print("=== check.py 报告 ===")
        print("条目文件：%d；已加载条目：%d；来源：%d" % (
            len(glob.glob(os.path.join(ROOT, "data", "units", "*.json"))), len(entries), len(source_ids)))
        for w in WARNINGS:
            print("[WARN] " + w)
        for e in ERRORS:
            print("[ERROR] " + e)
        print("结果：%d errors, %d warnings" % (len(ERRORS), len(WARNINGS)))
    return 1 if ERRORS else 0

if __name__ == "__main__":
    sys.exit(main())
