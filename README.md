# 宗教与神话比较库

按 `TASK_myth.md` 与 `WORKFLOW.md` 搭建的静态知识库：数据驱动、机器校验、诚实标注、零 JS、纯 HTML + 内联 SVG。

## 快速开始

直接打开项目根目录的 `index.html`（或 `site/index.html`）。本地预览也可运行：

```bash
python -m http.server 8000
# 浏览器访问 http://localhost:8000/site/
```

## 目录结构

```
scope.md                 编辑基准线：118 条入选清单 + 三框架并集方法
coverage.json            每条状态/层级/来源数 + 三维覆盖矩阵数据
coverage_matrix.md       人类可读的 传统×母题×时期 矩阵
sources.json             122 条权威来源（原典/学术/百科/机构）
data/units/U*.json       四个单元的条目数据（L1/L2/L3）
tools/
  build_coverage.py      从 scope.md + 条目 JSON 派生 coverage.json 与矩阵
  build_sources.py       生成 sources.json（书目信息与核对标注）
  build_l1.py            按精确来源映射批量生成 L1 骨架（每轮 ≤40）
  check.py               质量守门员：必填/双源/待核实/去重/SVG/一致性/断链
  check_links.py         站内链接全量核验
  gen_site.py            从 JSON 确定性渲染站点到 site/
site/                    生成的静态站点（127 页，零 JS）
index.html               根入口（跳转到 site/index.html）
DECISIONS.md             无人值守决策记录（含联网限制 D2）
PROGRESS.md              进度与下一轮起点（每次启动先读）
REPORT.md                统计报告、复检记录、空白格子清单
BLOCKERS.md              连续失败 3 次的问题
```

## 改数据后重新生成

```bash
python tools/build_coverage.py
python tools/check.py          # 必须 0 errors
python tools/gen_site.py
python tools/check_links.py    # 必须 0 broken links
```

## 新增 / 升级条目

- **L1 骨架**：在 `data/units/U*.json` 的 `entries` 数组加条目，必填 `id/title/level/tier/period/summary/related/sources`，并设 `needs_verification` 与 `pending_notes`。
- **L2 升级**：补齐七节——来源文本、故事梗概、版本差异、研究者解读（`holder`+`school`）、相似母题（`basis_source` 必须有文献依据）、内联 SVG、待核实。
- **来源**：只能引用 `sources.json` 中已定义的 id；新增来源先改 `tools/build_sources.py` 再重跑。
- **写作纪律**：不编造数字/人名/引文；双源互证；引用未在线核验来源必须标待核实；神话类比必须有文献依据。

## 当前状态

118/118 条 L1 全覆盖，2 条 L2 样板；122 条来源（75 书目已核对）；127 页站点，0 校验错误、0 断链。
L2 深度升级按 `PROGRESS.md` 的"下一轮起点"继续（核心→重要→补充，L3 仅核心条目）。

联网检索与抓取端点在本环境不可用，详见 `DECISIONS.md` D2；恢复后可运行 `tools/linkcheck.py` 补核链接三态。
