---
title: 数据方向 Capstone Projects
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, capstone, data, pipeline, validation, projects]
updated: 2026-04-17
---

## 目录
- [为什么学](#为什么学)
- [学什么](#学什么)
- [怎么用](#怎么用)
- [业界案例](#业界案例)
- [延伸阅读](#延伸阅读)
- [Self-Check](#Self-Check)
- [参考答案](#参考答案)
- [参考链接](#参考链接)
- [版本记录](#版本记录)

## 为什么学
- 数据方向很容易学成“会用几个库”，但真正的工作成果通常是一个稳定的数据流程、一个可信的报表链路，或者一个能被别人接手的数据工具。
- capstone 项目能帮你把清洗、校验、数据库、分析、监控和交付说明串起来，避免只停留在 notebook 式练习。
- 做完这类项目之后，你对数据工作的理解会更接近“交付数据产品”，而不只是“跑出一个结果”。

## 学什么
- 项目 1：`daily-kpi-pipeline`。读取接口和数据库数据，做清洗、校验、聚合，产出日报。
- 项目 2：`data-quality-monitor`。对关键数据表做规则检查、异常告警和趋势对比。
- 项目 3：`experiment-analysis-kit`。对实验或业务事件做指标计算、分层对比和结果导出。

## 怎么用
### 示例 1：先把数据管道分层，而不是直接一把梭到底

```python hl_lines="2 8"
pipeline = {
    "extract": "api + sql + files",
    "transform": "clean + normalize",
    "validate": "schema + business rules",
    "publish": "report + dashboard",
}

print(list(pipeline), pipeline["publish"])
```


### 示例 2：把质量规则写成显式配置

```python hl_lines="2 7 10"
rules = {
    "row_count_positive": True,
    "null_rate_under_5_percent": True,
    "event_time_ordered": False,
}

failed = [name for name, passed in rules.items() if not passed]
print(failed, len(failed))
```


### 示例 3：把输出物和验证结果绑在一起交付

```python hl_lines="2 8"
delivery = {
    "report_generated": True,
    "quality_gate_passed": True,
    "lineage_documented": False,
}

ready = all(delivery.values())
print(ready, delivery["report_generated"])
```


推荐交付物:
- 一份最小数据流程说明，写清输入源、字段假设、质量规则和输出去向。
- 一组可重复执行的样例数据或测试数据，能验证清洗和聚合逻辑。
- 一份发布前检查清单，至少包含字段校验、空值率、时间范围和结果去向确认。

里程碑建议:
- 第 1 阶段：先把输入源和目标产物定义清楚，别一开始就卷花哨指标。
- 第 2 阶段：补质量校验、异常样例、日志和失败说明。
- 第 3 阶段：补自动运行入口、报表导出、质量 gate 和文档。

验收标准:
- 你能解释每个字段从哪里来、经过什么处理、最终去哪里。
- 你能在结果之外，说清这份数据是否可信、为什么可信。
- 你交付的不只是一个结果文件，还包括运行方法、验证方法和问题排查入口。

## 业界案例
- 很多数据项目的问题不在分析本身，而在上游字段变化后没人发现，或者结果出了偏差却没有质量 gate 和追溯说明。
- 一个好的数据 capstone 往往不只是算对了，还要能解释流程、保留证据、暴露异常。
- 如果你能把“清洗 + 校验 + 输出 + 文档”四件事同时做顺，数据方向的工程感会明显上一个台阶。

## 延伸阅读
- 这篇建议和 `python_database_programming.md`、`data_analysis_and_visualization.md`、`python_security_basics.md`、`memory_profiling_tracemalloc_gc.md` 一起练。
- 如果项目要从单机脚本扩成定时任务或服务，可以再加 `fastapi_and_asgi_delivery.md` 或 `redis_celery_and_background_jobs.md` 的内容。
- 如果你正在做真实业务分析，最适合的 capstone 就是把一个经常手工跑的报表流程改造成可重复交付的脚本。

## Self-Check
1. 为什么数据方向的 capstone 不能只交一个 CSV 或图表结果？
2. 一条数据流程为什么必须把质量规则显式写出来？
3. 什么时候你应该优先补 lineage、校验和异常说明，而不是继续加新指标？

## 参考答案
1. 因为真实交付需要的不只是结果，还要知道结果怎么来的、是否可信、出了问题怎么查。
2. 因为没有显式规则，数据是否可信就只能靠感觉，协作和回归验证也很难做。
3. 当结果已经开始被业务依赖，或者数据源和字段变化频繁时，质量与可追溯性通常比继续加指标更重要。

## 参考链接
- [Python `csv` 文档](https://docs.python.org/3/library/csv.html)
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
- [Python `sqlite3` 文档](https://docs.python.org/3/library/sqlite3.html)

## 版本记录
- 2026-04-17：首版，新增数据方向的 capstone 项目建议与质量交付视角。
