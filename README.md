# 宗教与神话比较库

一个数据驱动的静态知识库，按传统、母题、时期三个维度对比世界宗教与神话。站点由 JSON 数据确定性生成，经过机器校验，待核实内容会诚实标注。页面不用 JavaScript，只有纯 HTML 和内联 SVG。

仓库：<https://github.com/TianDiHuAng/shenhua>

## 当前规模

| 指标 | 数值 |
|---|---|
| 条目 | **679**（L3 114 / L2 565） |
| 层级 | 核心 40 / 重要 74 / 补充 565 |
| 来源 | **609**（已核对 563；链接可达 553，受限 56） |
| 站点页面 | **690** |
| 质量校验 | `check.py` 0 errors；`check_links.py` 14857 处站内引用 0 断链 |

| 单元 | 主题 | 条目 | 核心 / 重要 / 补充 |
|---|---|---|---|
| U1 | 神话体系 | 90 | 10 / 14 / 66 |
| U2 | 宗教传统 | 93 | 8 / 14 / 71 |
| U3 | 母题 | 78 | 10 / 12 / 56 |
| U4 | 人物 | 418 | 12 / 34 / 372 |

## 快速开始

直接用浏览器打开根目录的 `index.html`，它会跳转到 `site/index.html`。也可以起一个本地服务：

```bash
python -m http.server 8000
# 浏览器访问 http://localhost:8000/site/
```

## 可视化页面

| 页面 | 内容 |
|---|---|
| `site/index.html` | 首页，按单元导航 |
| `site/stats.html` | 统计概览：各单元、各层级、各时期条目数（SVG 图表） |
| `site/matrix.html` | 覆盖矩阵：传统 × 母题 × 时期 |
| `site/timeline.html` | 时期总览 |
| `site/all.html` | 全站条目索引 |
| `site/sources.html` | 来源库与核验状态 |
| `site/about.html` | 方法论 |
| `site/units/U*.html` | 四个单元的列表页 |
| `site/entries/*.html` | 条目详情页（含内联 SVG 图示） |

## 目录结构

```
scope.md              编辑基准线与入选方法
coverage.json         每条条目的状态、层级、来源数，以及覆盖矩阵数据
coverage_matrix.md    人类可读的覆盖矩阵
sources.json          权威来源库（原典 / 学术 / 百科 / 机构），是来源的唯一权威数据
data/units/U1-U4.json 条目数据
tools/
  build_coverage.py   派生 coverage.json 与矩阵
  build_sources.py    只追加 sources.json 中尚不存在的来源，不覆盖已有条目
  check.py            质量守门：必填字段、双源、待核实、去重、SVG、一致性、来源 URL 等
  check_links.py      站内链接全量核验
  linkcheck.py        外部链接三态核验（需要联网）
  gen_site.py         从 JSON 渲染站点到 site/
site/                 生成的静态站点
PROGRESS.md / REPORT.md / DECISIONS.md / BLOCKERS.md / METRICS.json  进度、报告、决策与指标记录
```

## 修改数据后重新生成

```bash
python tools/build_coverage.py
python tools/check.py          # 必须 0 errors
python tools/gen_site.py
python tools/check_links.py    # 必须 0 broken links
```

## 条目规范

- **L1 骨架**：必填 `id/title/level/tier/period/summary/related/sources`，同时设置 `needs_verification` 和 `pending_notes`。
- **L2 / L3**：补齐来源文本、故事梗概、版本差异、研究者解读（`holder` + `school`）、相似母题（`basis_source` 必须有文献依据）、内联 SVG 和待核实。
- **来源**：只能引用 `sources.json` 里已定义的 id。新增来源要字段齐全（`id/title/author/year/year_display/type/url/url2/link_ok/verified/note`），并通过 `check.py`。
- **写作纪律**：不编造数字、人名和引文；需要双源互证；引用未在线核验的来源必须标注待核实；神话类比必须有文献依据。

## 已知事项

- `check.py` 目前有 331 条 warning，都是 comparisons 字段写得过于笼统。它们不阻塞构建，可以用 `python tools/check.py --strict` 查看明细并逐步细化。
- 56 个来源的链接在当前环境里访问受限（`link_ok: blocked`），联网条件恢复后可以运行 `tools/linkcheck.py` 复核。
