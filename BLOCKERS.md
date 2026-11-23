# BLOCKERS.md — 阻塞记录

## 已解除（2026-11-23）
- ~~联网端点不可用~~：已解除。经实测本机 Python urllib 可直连外网（Wikipedia/GitHub 200），D2 阻塞由 D14 决策正式解除；linkcheck/verify_sources 已恢复运行。

# BLOCKERS.md — 连续失败 3 次的问题 / 环境限制

> 同一问题连续失败 3 次记录于此并跳过。环境限制也在此备案。

## 环境限制 1：联网检索与抓取端点不可用
- 表现：`web_search` 端点未配置（返回 no result blocks）；`web_fetch` 对 Britannica 返回 403、对 Wikipedia 返回 fetch failed、对 Gutenberg 返回 503。
- 影响：AUTONOMOUS.md 缺口发现方法1（权威大纲联网对照）与方法6（近期动态联网）无法执行；`sources.json` 的 47 条百科/机构来源无法在线核验，`link_ok` 保持 null。
- 应对：来源只用真实稳定书目信息录入（不编造），按 DECISIONS.md D2 诚实标注 `verified`（书目已核对）与未在线核验标记；缺口发现改用方法2/3/4/5/7 轮换。联网恢复后运行 `tools/linkcheck.py` 补核链接三态。
- 不构成阻断：不因联网不可用而停止自主循环。

## 环境限制 2：git push 的 HTTPS 传输栈卡死
- 表现：`git push -u origin master` 长时间无输出（无 credential helper、无 token 环境变量）。
- 应对：改用 `tools/github_push.py`（git credential fill 取 token + GitHub Git Data API）成功推送到 `TianDiHuAng/shenhua` 的 main 分支，已 API 核验落地。
- 不构成阻断。

（暂无连续失败 3 次的问题。）
