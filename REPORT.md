# REPORT.md — 项目报告（L1 全覆盖里程碑）

## 一、统计总览
| 指标 | 数值 |
|---|---|
| 计划条目总数 | 118 |
| 已撰写条目 | **118/118（L1 全覆盖）** |
| U1 神话体系 / U2 宗教传统 / U3 母题 / U4 人物 | 42 / 26 / 20 / 30（全部已写） |
| 层级：核心 / 重要 / 补充 | 40 / 42 / 36（均按 TASK 顺序写作） |
| 写作层级：L1 / L2 / L3 | 86 / 32 / 0（核心已 L2：32/40） |
| 来源总数 | 122（原典 40 / 学术著作 32 / 权威百科 26 / 官方机构 24） |
| 书目已核对来源 | 75 |
| 未在线核验来源 | 47（已在 note 与条目页显式标注） |
| 待核实条目 | 118（116 条为 L1 骨架；2 条 L2 因引用未在线核验来源） |
| 生成页面 | 127 个 HTML（含 118 条目页、4 单元页、首页/索引/矩阵/来源/方法论等） |
| 站内引用 | 1950 条，0 断链 |

## 二、校验结果
- `tools/check.py`：**0 errors, 0 warnings**
- `tools/check_links.py`：**0 broken links**
- SVG：2 个内联图示通过 XML 解析、元素白名单、无脚本/事件属性、viewBox 出界与 CSS 变量检查
- 四方一致性：scope.md ↔ coverage.json ↔ 条目 JSON ↔ 生成页面全部对齐

## 三、覆盖矩阵
- 680 个单元（68 传统 × 10 核心母题）；按时期分：ancient / classical / medieval / modern / oral。
- expected（传统说明中预期涉及该母题）= 30 格，全部已填：**L1 29 格、L2 1 格**。
- 其余 650 格为"未预期组合"，留空属正常，见 `coverage_matrix.md` 与站点覆盖矩阵页。

## 四、批次复检
- **L1 阶段**：第2轮（38 条核心 L1）另起子任务抽查 4 条（fig-ra / motif-sun / myth-japanese / rel-judaism），覆盖 U1–U4 四单元，结果 **4/4 合格**。
- **L2 阶段（第5轮 10 条升级）**：另起子任务抽查 4 条（myth-norse / myth-chinese / myth-maya / rel-islam），结论 **不返工**；列出 6 项定点修订，已在 commit 前全部修补：
  1. `myth-norse` "欧hemerism" → "欧赫墨罗斯主义（Euhemerism）"；
  2. `myth-norse` 待核实补声明萨克索《丹麦人的业绩》未录入来源库；
  3. `myth-chinese` 修正 Lévi-Strauss 来源声明（仅录方法论通论）、"原初巨体化生型创世"改述；
  4. `myth-chinese` 北欧比较依据改为 `aca-eternal-return` 并明示"纯框架性参照"；
  5. `rel-islam` 犹太教比较依据由偏题的旧约民俗著作改为 `enc-brit-judaism`；
  6. "eternal return" 统一译为"永恒回归（eternal return）"。
  修订后重跑 check.py / gen_site.py / check_links.py 全绿，笔误已确认清除。
- **L2 阶段（第6轮 10 条升级）**：抽查 4 条（rel-judaism / rel-taoism / motif-flood / motif-herojourney），结论 **定位小修、不整批返工**；修补项：
  1. `rel-taoism` 佛教比较依据由偏题的 `aca-god-is-not-one` 改为 `enc-brit-buddhism` 并明示"待核实的弱参照"；
  2. `rel-buddhism` 印度教比较依据同型偏题修正为 `enc-brit-hinduism`；
  3. "比较 discipline" → "比较学术规范"；
  4. `rel-shinto` "sacred center" → "神圣中心（sacred center）"，`motif-underworld` "Hero" → "英雄"，术语统一为中文为主+英文括注；
  5. `motif-herojourney` 补声明 Frye 著作未录入来源库。
  修订后全量校验 0 errors / 0 断链。
- **L2 阶段（第7轮 10 条升级）**：抽查 4 条（motif-dragon / motif-trickster / fig-odin / fig-pangu），结论 **不返工**，十条合并零漂移、机器校验 10/10 通过；修补项：
  1. `motif-trickster` SVG 第三节点补副标题"调和两极"，排版对称；
  2. 术语呈现统一：rel-taoism、fig-pangu 的"永恒回归"补英文括注，与前批一致；
  3. 数据自洽：改 `tools/upgrade_l2.py`，升级时自动把 comparisons 的 `basis_source` 并入 `sources` 数组；并修补手工样板 myth-greek，实现全站 basis_source 均在来源列表内。
  依据贴合度的轻微残余（如 fig-pangu 的北欧比较、motif-dragon 的中国龙比较）已在 note 中自限为"框架性弱参照、待补专门文献"，按 D2 诚实标注保留。
  修订后全量校验 0 errors / 0 断链。
- 第 3 轮（42 条重要 L1，分 40+2 两批以遵守每轮 ≤40 配额）与第 4 轮（36 条补充 L1）均通过全量校验。

## 五、写作路径与诚实标注
- 严格遵循"先 L1 全覆盖，再按 核心→重要→补充 升级 L2"：本轮先完成 118 条 L1，未提前深写个别条目。
- 双源规则：每条 ≥2 个来源 id；来源不足或未在线核验者一律 `needs_verification=true` 并写明 `pending_notes`。
- 关键事实需两个独立来源互证；神话类比仅记录学界有文献依据者（条目内 `comparisons` 必填 `basis_source`）。
- 不使用任何图片；图示均为内联 SVG，文字走 CSS 变量，浅色/深色模式皆可读。

## 六、已知限制与后续
1. 联网端点不可用（DECISIONS.md D2）：来源未在线打开核对，`verified` 仅表示书目已核对；恢复后运行 `tools/linkcheck.py` 补核 `link_ok` 三态。
2. L2 深度写作待续：116 条 L1 骨架的来源文本、版本差异、学者解读、比较研究与图示，待按核心→重要→补充逐批升级；L3 仅核心条目。
3. 当前 118 条全部处于待核实状态，反映骨架阶段与联网限制的双重现实，不隐瞒、不硬凑。
