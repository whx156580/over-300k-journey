---
title: 可观测性：日志、指标与链路追踪
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, observability, logging, metrics, tracing, opentelemetry]
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
- 代码出问题时，“能不能看见发生了什么”往往比“代码本身写得多优雅”更决定排障效率。
- 可观测性通常由三块组成：日志负责还原事件，指标负责发现趋势，链路追踪负责串起跨服务调用路径。
- 对服务端、平台任务和异步系统来说，没有可观测性，很多问题只能靠猜。

## 学什么
- 日志更适合回答“发生了什么”，指标更适合回答“最近是不是变差了”，追踪更适合回答“慢在哪一段链路上”。
- 好的日志要结构化，好的指标要有标签和维度，好的追踪要能把一次请求的上下游串起来。
- 可观测性不是上线后才补的附件，而是接口设计、后台任务和异步调用从一开始就该考虑的横切能力。

## 怎么用
### 示例 1：结构化日志

```python hl_lines="2 7"
event = {
    "event": "sync_finished",
    "trace_id": "trace-1001",
    "job_name": "daily-report",
    "duration_ms": 183,
    "status": "ok"
}

print(event["event"], event["trace_id"], event["duration_ms"])
```


### 示例 2：最小指标聚合

```python hl_lines="2 8"
metrics = {
    "request_total": 12,
    "request_error_total": 1,
    "request_p95_ms": 280
}

error_rate = metrics["request_error_total"] / metrics["request_total"]
print(round(error_rate, 3), metrics["request_p95_ms"])
```


### 示例 3：链路上下文最小表达

```python hl_lines="2 7"
trace_context = {
    "trace_id": "trace-42",
    "span_id": "span-api",
    "parent_span_id": "span-gateway"
}

print(trace_context["trace_id"], trace_context["parent_span_id"])
```


落地建议:
- 日志字段尽量统一，不要同一类事件今天叫 `trace_id`、明天叫 `requestId`。
- 关键指标至少要覆盖吞吐、错误率和延迟，再根据业务补充队列长度、任务堆积等专项指标。
- 如果系统有跨服务调用，尽早把 trace id 贯穿起来，否则排慢接口时会非常被动。

## 业界案例
- 很多接口服务的问题不是没报错，而是日志只能看到“失败了”，却看不到 trace id、请求参数和上游来源。
- 异步任务经常表面上“都执行了”，但一旦缺少队列积压指标和失败计数，实际上已经悄悄降级。
- 跨服务排障时，没有统一 trace id，常见结果是每个服务都各自有日志，但没人能把一次请求拼完整。

## 延伸阅读
- 结构化日志常和 JSON logger、集中采集平台一起使用。
- 指标体系常和 Prometheus / Grafana 一类工具配合；链路追踪常见生态包括 OpenTelemetry。
- 最有效的可观测性不是“把所有东西都打出来”，而是提前想清楚问题来时你最想回答哪些问题。

## Self-Check
### 概念题
1. 日志、指标、追踪三者最核心的分工是什么？
2. 为什么 trace id 对跨服务排障很重要？
3. 为什么说结构化日志比随手拼字符串更适合工程环境？

### 编程题
1. 如何表达一条带 trace id、耗时和状态的最小事件日志？
2. 如何从总请求数和错误数计算一个最小错误率指标？

### 实战场景
1. 你们的异步任务“偶尔慢、偶尔失败”，但日志里只有一句 `task failed`，你会优先补哪些日志字段和指标？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
日志偏事件还原，指标偏趋势量化，追踪偏跨服务路径定位。
讲解回看: [学什么](#学什么)

### 概念题 2
因为它能把同一次请求或任务在不同服务、不同步骤里的记录串起来，减少“各看各的日志”。
讲解回看: [怎么用](#怎么用)

### 概念题 3
因为结构化字段更容易过滤、聚合和关联，也更适合接入日志平台和告警规则。
讲解回看: [为什么学](#为什么学)

### 编程题 1
可以用字典收敛 `event`、`trace_id`、`duration_ms`、`status` 这类字段，再统一输出。
讲解回看: [代码示例](#代码示例)

### 编程题 2
通过 `error_total / request_total` 计算，并明确总数不能为 0 的边界处理。
讲解回看: [代码示例](#代码示例)

### 实战场景 1
至少要补任务名、trace id、输入主键、重试次数、耗时、失败原因、队列积压、成功率和超时计数。
讲解回看: [业界案例](#业界案例)

## 参考链接
- [logging 文档](https://docs.python.org/3/library/logging.html)
- [OpenTelemetry 文档](https://opentelemetry.io/docs/)
- [Prometheus 文档](https://prometheus.io/docs/introduction/overview/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-17: 新增“可观测性：日志、指标与链路追踪”，补齐 Python 从业者常见生产排障能力。

---
[返回 Python 学习总览](../README.md)
