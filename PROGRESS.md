# PROGRESS.md — 进度与续跑点（AUTONOMOUS.md 协议）

> 每次启动先读本文件。协议规定：不写 ALL_DONE，以"饱和"为终点；每轮执行一次完整循环后结束，由外部脚本再次拉起。

## 当前状态
- 协议轮次：AUTONOMOUS-27~45（核心+重要L3全覆盖，L3=114/197）；SATURATED=false
- 状态：维护+深化；119条全L2及以上（其中 L3=4/40 核心）；绝不写ALL_DONE
- ALL_DONE：**协议规定不写**

## 阶段进度（协议接入前的阶段0-5 已完成）
- [x] 阶段0 范围：scope.md 118 条 / coverage.json / 覆盖矩阵
- [x] 阶段1 来源库：sources.json 122 条
- [x] 阶段2 校验器：tools/check.py
- [x] 阶段3 样板 + 生成器 + check_links.py
- [x] 阶段4 L1 全覆盖：118/118
- [x] 阶段4 核心层 L2：**40/40（本轮达成）**
- [x] 阶段4 核心层 L2：**40/40（达成）**
- [x] 阶段4 重要层 L2：**42/42（达成）**
- [x] 补充层 L2：**36/36（AUTONOMOUS-11 全清）**
- [x] **全库 119 条全部 L2**（含 N1 概念条目，2026-11-22 达成）
- [x] 阶段5 站点：130 页（含索引/时间线/统计/矩阵/来源/方法论）+ REPORT.md
- [ ] 饱和判定：远未饱和（见 SATURATION.json）

## 当前模式：维护 + L3 深化（SATURATED=true）
- 用户指令继续完善 → 核心条目分批深化至 L3（争议并列/关键数据/复杂图示），每轮 ≤10 条核心，25% 抽检，check+commit。
- 其余仍做：体检 F、复核待核实项、更新过期数据、跟进动态（联网不可用则记录）。
- 若又发现新的有权威依据缺口 → 退出饱和回正常循环。**绝不写 ALL_DONE**。

## 下一轮起点（AUTONOMOUS-28）
- 核心条目 L3 深化批次2：从剩余核心条目中取 5-6 条（如 myth-mesopotamian/chinese/hindu/japanese/maya/aztec/celtic 及宗教核心），补 controversies（真实争论、列各方）+ data_points（有据事实），同步 gen_site 渲染。
- 抽检 L3 内容真实性（重点：不编造数字/人名；争议须列真实学派）。

## 覆盖率快照
- 条目：197（扩充六批 +78；批次6 超限已记 D13-勘误）；L1 0 / L2 83 / L3 114；**核心40/40 + 重要74/74 全 L3**；补充83保持L2
- 来源 122（书目已核对 75）；待核实 119
- 校验：check.py 0 errors / 0 warnings；check_links.py 0 断链（130 页、2689 引用）
- 协议状态文件：BACKLOG.md / METRICS.json / SATURATION.json 已建立

## 锁定与阻断
- 联网阻塞已于 2026-11-23 解除（D14）：Python urllib 直连核验 122 条来源（66 true / 56 blocked / 0 false）。
