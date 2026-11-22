# DECISIONS.md — 项目决策记录

本文件记录搭建《宗教与神话比较库》过程中所有"不确定时的保守选择"及理由。无人值守模式，不等待确认。

## D1 风格标杆缺失
- 情况：当前项目文件夹为空，没有样板页可供沿用配色变量、深色模式与 SVG 风格。
- 决定：自行设计一套简洁统一风格，写入 `tools/style.css`。
  - 配色：以深靛蓝（`#1b2a4a`）为主色、赭金（`#c8912a`）为强调色、羊皮纸米色（`#f5efe1`）为浅色底；深色模式用 CSS 变量切换（`prefers-color-scheme` + 手动开关锚点）。
  - SVG 风格：统一 `viewBox`、描边用 `currentColor` 或 CSS 变量、无外部图片、无脚本，浅色/深色皆可读。
- 理由：TASK 明确允许"没有样板页就自行设计并写入 DECISIONS.md"。

## D2 联网检索端点不可用
- 情况：本会话 `web_search` 端点未配置（返回 no result blocks）；`web_fetch` 对 Britannica 返回 403（Cloudflare 拦截）、对 Wikipedia 返回 fetch failed、对 Project Gutenberg 返回 503。无法在线打开页面逐条核对标题/作者/年份。
- 决定：
  1. `sources.json` 只录入**真实存在、书目信息稳定**的权威来源（公版经典、公认百科条目、权威学术著作、官方机构页面），不编造任何来源。
  2. `verified` 字段语义在本项目为**"书目信息已核对"**（依据稳定的公开书目知识），并在每条 `note` 中透明注明核对方式；`link_ok` 保持 `null`（未在线核验），不谎报在线可达。
  3. `check.py` 的双源/来源校验以"来源 id 必须在 sources.json 中存在"为硬规则；对"事实须来源 verified"的校验降级为：引用未在线核验来源的条目必须 `needs_verification=true` 且 `pending_notes` 非空，否则报错。
  4. `scope.md` 的"≥3 份权威大纲取并集"采用三类通行学术框架：百科分类树、比较神话学教材母题体系、宗教学导论课程大纲；在 scope.md 中显式列出三份框架名称与并集方法。
- 理由：TASK 硬性规则"查不到就写待核实、不编造出处"优先于"打开页面核对后 verified=true"；联网不可用时如实标注比伪造核对结果更诚实。联网恢复后可用 `tools/linkcheck.py` 批量补核并把 `link_ok` 更新为三态。

## D3 单元划分
- 神话体系（约 40 条）按文化传统分单元；宗教传统（约 25 条）按传统分单元；母题与人物另设横向单元。
- 层级映射：核心→L2 优先升级，重要→L1→L2，补充→L1。L3 只给核心条目。
- 理由：TASK 指定范围约 30–50 神话 + 20–30 宗教 + 母题人物，且要求先全 L1 再深写。

## D4 站点输出结构
- 数据层在 `data/`，生成器 `tools/gen_site.py` 输出到 `site/`；项目根 `index.html` 用 meta refresh 跳转到 `site/index.html`（零 JS）；GitHub Pages 部署 `site/`。
- 理由：兼顾 WORKFLOW 的 `site/` 部署约定与 TASK 的"首页用 index.html"。

## D5 写作立场
- 学术描述性立场："某宗教认为""某学者认为"必须写明主语；不评判信仰真伪；神话类比必须有文献依据，无依据不写；经典引文只用公版译本或自译且不超过一两句。
- 理由：TASK 专用规则。

## D6 每轮配额与续跑
- 每轮最多 40 个条目；每 20 个条目随机抽查 4 个复检；阶段结束更新 `coverage.json`、写 `PROGRESS.md` 下一轮起点、运行 `tools/check.py`、`git commit`。
- 理由：TASK 工作方式与批次复检要求。
