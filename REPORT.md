# REPORT.md — AUTONOMOUS-58（2026-11-23）

## 本轮主题：系统性体检F（264 条目）

### 方法
用 Python difflib 对全部条目的 id 与 title 做相似度检测（id cutoff=0.85，title 完全匹配），系统性发现隐藏重复——此前每批都有重复需合并，说明逐批查重不够彻底。

### 发现与修复
- 真重复 2 组：myth-aboriginal（=早批次 myth-australian）、rel-sikh（=早批次 rel-sikhism）→ 合并内容到早批次条目（保留更全 sources/L3 层级），删除重复。
- 误报 6 组（myth-japanese/javanese、fig-hera/ra、fig-hathor/thor、fig-enki/enkidu、rel-mandaeism/manichaeism、myth-turkic/ugric）——实为不同条目，保留。
- 修复 4 处指向 myth-aboriginal 的 related 引用。
- check 0 errors；站点 278 页。

### 现状
- 条目 264（核心 40 / 重要 74 / 补充 150），L3 累计 114。
- 来源 190 条。
- 结论：全库标题零重复、id 零真重复，数据结构健康。
