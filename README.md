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
scope.md                 编辑基准线：119 条入选清单 + 三框架并集方法
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
site/                    生成的静态站点（129 页，零 JS；含时间线/索引/矩阵/来源/方法论）
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
- **来源**：只能引用 `sources.json` 中已定义的 id。`sources.json` 是权威数据：联网核验后的 URL 修正、`link_ok`、以及后续批次追加的来源都直接记录在其中，`tools/build_sources.py` 内的硬编码值已落后于它。该脚本现在只【追加】`sources.json` 中尚不存在的 id，不会覆盖或删除已有条目（重跑结果与已提交文件逐字节一致）。新增来源可直接编辑 `sources.json`，但每个来源必须字段齐全（`id/title/author/year/year_display/type/url/url2/link_ok/verified/note`）并通过 `tools/check.py`。
- **写作纪律**：不编造数字/人名/引文；双源互证；引用未在线核验来源必须标待核实；神话类比必须有文献依据。

## 当前状态

119/119 条全部达 L2（核心 40 + 重要 43 + 补充 36，含 N1 概念条目「神话与宗教的区别」）；122 条来源（75 书目已核对）；129 页站点（含时间线/时期总览），0 校验错误、0 断链。

项目已按 AUTONOMOUS.md 自主扩充协议达到 **SATURATED=true**（连续多轮缺口发现无新增缺口 + 全库全 L2），现处于**维护模式**：每轮只做体检、复核待核实项、更新过期数据、跟进动态（联网不可用则记录），**不写 ALL_DONE**。若又发现新的有权威依据缺口，则退出饱和回到正常扩充循环。

联网检索与抓取端点在本环境不可用，详见 `DECISIONS.md` D2；恢复后可运行 `tools/linkcheck.py` 补核链接三态。
