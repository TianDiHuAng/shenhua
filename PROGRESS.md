# PROGRESS.md — 进度与续跑点

> 每次启动先读本文件，从"下一轮起点"继续。全部阶段完成后写入 `ALL_DONE`。

## 当前状态
- 阶段：阶段4 L2 深度升级进行中
- 轮次：第 1–7 轮完成（基线 + 38 核心 + 42 重要 + 36 补充 L1；第5、6、7轮各升级 10 条核心到 L2）
- ALL_DONE：否

## 阶段进度
- [x] 项目骨架（目录、DECISIONS、PROGRESS、BLOCKERS、git init）
- [x] 阶段0 范围：scope.md / coverage.json / 覆盖矩阵（118 条）
- [x] 阶段1 来源库：sources.json 122 条
- [x] 阶段2 校验器：tools/check.py（0 errors）
- [x] 阶段3 样板：myth-greek、motif-creation 两个 L2（0 errors）
- [x] 生成器：tools/gen_site.py + style.css + check_links.py（0 broken links）
- [x] 阶段4 批次复检：第2轮 4/4 合格
- [x] 阶段4 L1 全覆盖：118/118 条（40 核心 + 42 重要 + 36 补充，均按 TASK 顺序）
- [ ] 阶段4 L2 深度升级：32/118（2 样板 + 第5/6/7轮各 10 条核心）→ 按 核心→重要→补充 逐批升级
- [x] 阶段5 站点：127 页生成、索引/矩阵/来源/方法论/REPORT.md 齐备
- [ ] 最终 ALL_DONE（L2 升级完成后写）

## 下一轮起点
- 阶段4 L2 升级第 8 轮：剩余 **8 条核心人物条目**从 L1 升到 L2（一次性完成核心层 L2）。
  - 剩余核心 id（8）：fig-nuwa, fig-buddha, fig-jesus, fig-muhammad, fig-moses, fig-vishnu, fig-shiva, fig-indra。

## 覆盖率快照
- 条目录入：118/118；L1：86；L2：32；L3：0（核心已 L2：32/40）
- 来源：122（书目已核对 75）；待核实条目：118
- 覆盖矩阵：expected 30 格全填（L1 多格 / L2 部分已升）
- 校验：check.py 0 errors / check_links.py 0 broken links（127 页、1950 条引用）

## 锁定与阻断
- 见 BLOCKERS.md（联网端点不可用已记入 DECISIONS.md D2，不作为阻断）。
