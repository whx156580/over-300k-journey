---
title: 性能剖析
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, profiling, timeit, cprofile, memory]
updated: 2026-04-16
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
- 性能优化最容易犯的错就是“没测就改”。剖析工具的作用是先找热点，再谈优化。
- 测试工程虽然不一定天天写高性能服务，但经常会写数据处理脚本、日志分析工具和批量任务，性能问题并不少见。
- 掌握时间、CPU、内存三个维度的观测方式，才能避免只看一种指标就做结论。

## 学什么
- `timeit` 适合测小片段耗时，`cProfile` 适合看函数级调用统计。
- `line_profiler` 适合定位慢行，`memory_profiler` 和 `objgraph` 适合观察内存增长与对象关系。
- 火焰图适合做更直观的热点可视化，但前提仍然是先拿到可靠 profile 数据。

## 怎么用
### 示例 1：`timeit`

```python hl_lines="3"
import timeit

result = timeit.timeit("sum(range(100))", number=1000)
print(round(result, 4))
```


### 示例 2：`cProfile`

```python hl_lines="9 10 15 17"
import cProfile
import io
import pstats


def compute() -> int:
    return sum(i * i for i in range(1000))


profiler = cProfile.Profile()
profiler.enable()
compute()
profiler.disable()

stream = io.StringIO()
stats = pstats.Stats(profiler, stream=stream).sort_stats("cumulative")
stats.print_stats(3)
print("compute" in stream.getvalue())
```


### 示例 3：第三方工具的安全导入

```python hl_lines="3 5 7"
optional_tools = {}

for name in ("line_profiler", "memory_profiler", "objgraph"):
    try:
        optional_tools[name] = __import__(name)
    except ImportError:
        optional_tools[name] = None

print(sorted(optional_tools))
```


实战建议:
- 先用 `timeit` 或真实压测场景确认“真的慢”。
- 再用 `cProfile` 看热点函数，必要时下钻到逐行或内存分析。
- 优化后重新测量，确保收益真实存在。

## 业界案例
- 批量日志解析脚本跑得慢时，先看是不是字符串处理、正则或 I/O 成为热点。
- 测试报告生成耗时过长时，可用 `cProfile` 找出最重的聚合和序列化步骤。
- 长时间运行的守护脚本内存上涨时，可用 `memory_profiler` 或 `objgraph` 排查对象泄漏。

## 延伸阅读
- [timeit 文档](https://docs.python.org/3/library/timeit.html)
- [cProfile 文档](https://docs.python.org/3/library/profile.html)
- 火焰图常与 `py-spy`、`snakeviz` 等工具配合使用。

## Self-Check
### 概念题
1. 为什么性能优化前必须先做测量？
2. `timeit` 和 `cProfile` 的使用场景有什么区别？
3. 逐行分析工具为什么通常不应该作为第一步？

### 编程题
1. 如何用 `cProfile` 快速查看最耗时的几个函数？
2. 如果某些性能分析库在当前环境未安装，示例代码怎样才能仍然安全运行？

### 实战场景
1. 测试报告生成变慢了，你应该直接优化模板渲染，还是先做 profile？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
因为性能问题常常不是直觉里最慢的那一段。先测量才能知道真正热点在哪，避免在错误位置浪费时间。
讲解回看: [为什么学](#为什么学)

### 概念题 2
`timeit` 更适合微基准和小片段耗时，`cProfile` 更适合从整体调用栈看函数级热点。
讲解回看: [学什么](#学什么)

### 概念题 3
因为逐行分析成本更高、信息更细。通常先用粗粒度工具定位热点区域，再决定是否下钻到逐行或内存层面。
讲解回看: [怎么用](#怎么用)

### 编程题 1
创建 `Profile()`，在 `enable()` 和 `disable()` 之间执行目标函数，再通过 `pstats.Stats(...).sort_stats("cumulative").print_stats(n)` 输出热点列表。
讲解回看: [怎么用](#怎么用)

### 编程题 2
可以像本节示例那样用 `try/except ImportError` 做可选导入，把工具缺失当成能力降级而不是直接崩溃。
讲解回看: [怎么用](#怎么用)

### 实战场景 1
先做 profile。慢点可能不在模板渲染，而在数据聚合、文件 I/O、序列化或排序阶段。没有证据就下手优化，常常会偏离真正瓶颈。
讲解回看: [业界案例](#业界案例)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-16: 初版整理，补齐示例、自测题与落地建议。

---
[返回 Python 学习总览](../README.md)
