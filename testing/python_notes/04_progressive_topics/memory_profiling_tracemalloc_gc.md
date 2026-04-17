---
title: 内存排障：tracemalloc、gc 与对象增长
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, memory, tracemalloc, gc, profiling, leak]
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
- 很多 Python 程序不是“慢”而已，而是跑久了越来越吃内存，最后把容器打爆或让任务被系统杀掉。
- 时间性能问题和内存问题经常交织在一起，但工具和分析思路并不完全一样。
- 从业者遇到长时间运行任务、数据处理程序和守护进程时，迟早要面对对象增长、引用残留和垃圾回收行为。

## 学什么
- `tracemalloc` 适合看内存分配快照和增量，`gc` 适合观察垃圾回收统计和对象追踪行为。
- 内存排障的重点不是“某一刻占了多少 MB”，而是“哪些对象一直涨、为什么没释放、涨幅从哪里开始”。
- 真正的修复常常要回到缓存策略、对象生命周期和数据结构选择，而不是只盯工具输出。

## 怎么用
### 示例 1：用 `tracemalloc` 做最小快照比较

```python hl_lines="1 6 8"
import tracemalloc


tracemalloc.start()
before = tracemalloc.take_snapshot()
data = [str(i) for i in range(1000)]
after = tracemalloc.take_snapshot()
stats = after.compare_to(before, "lineno")

print(len(data), len(stats) > 0)
tracemalloc.stop()
```


### 示例 2：观察 `gc` 计数

```python hl_lines="1 4"
import gc


before = gc.get_count()
sample = [{"i": i} for i in range(100)]
after = gc.get_count()

print(len(sample), before, after)
```


### 示例 3：用结构化视角记录内存排障结果

```python hl_lines="2 8"
memory_report = {
    "suspect_area": "cache growth",
    "snapshot_diff_kb": 128,
    "gc_count": (1, 0, 0),
    "next_action": "check object retention"
}

print(memory_report["suspect_area"], memory_report["snapshot_diff_kb"])
```


落地建议:
- 先确认“真的在持续上涨”，再决定是看 `tracemalloc`、对象图，还是回到业务缓存策略。
- 把快照前后的负载条件尽量保持一致，不然对比结果容易失真。
- 遇到长期增长问题时，要同时看对象生命周期、全局缓存、闭包引用和任务结果积压。

## 业界案例
- 长驻 worker 经常因为结果缓存、任务上下文残留或列表越攒越大而慢慢吃满内存。
- 数据处理脚本一次性把大批数据全读进内存，也是典型问题，往往需要回到分批处理或生成器设计。
- 接口服务内存上涨时，不少时候不是“泄漏”那么神秘，而是对象本来就被全局结构持有，根本没机会释放。

## 延伸阅读
- `tracemalloc` 很适合做第一轮定位；如果已经确认是对象增长问题，再考虑更细的对象关系分析工具。
- `gc` 数据本身不是结论，它更像提示你“回收行为和对象生命周期有没有异常信号”。
- 内存问题经常和业务设计相关，例如缓存没上限、结果集不分批、任务上下文不及时清理。

## Self-Check
### 概念题
1. 为什么内存排障不能只看“当前用了多少内存”？
2. `tracemalloc` 和 `gc` 更适合分别观察什么？
3. 为什么很多“内存泄漏”最后其实是对象生命周期设计问题？

### 编程题
1. 如何用 `tracemalloc` 做一次最小快照对比？
2. 如何查看 Python 当前的垃圾回收计数？

### 实战场景
1. 你的后台任务跑 3 小时后 RSS 一直涨，你会怎样安排“确认增长 -> 做快照 -> 缩小对象范围 -> 回到业务设计”的排查顺序？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
因为真正要找的是增长趋势和增长来源；单看瞬时占用，既看不出是否持续上涨，也看不出谁在涨。
讲解回看: [为什么学](#为什么学)

### 概念题 2
`tracemalloc` 更适合观察分配快照和增长位置，`gc` 更适合看回收计数和对象追踪层面的信号。
讲解回看: [学什么](#学什么)

### 概念题 3
因为对象往往不是“神秘地没释放”，而是仍然被缓存、全局变量、闭包或结果集合持有。
讲解回看: [业界案例](#业界案例)

### 编程题 1
先 `tracemalloc.start()`，拍两次快照，再用 `compare_to()` 做差异比较。
讲解回看: [代码示例](#代码示例)

### 编程题 2
可以使用 `gc.get_count()` 查看当前各代垃圾回收计数。
讲解回看: [代码示例](#代码示例)

### 实战场景 1
先确认在稳定负载下是否持续增长，再用快照找增长区域，再回看缓存、对象持有关系和数据结构设计。
讲解回看: [落地建议](#怎么用)

## 参考链接
- [tracemalloc 文档](https://docs.python.org/3/library/tracemalloc.html)
- [gc 文档](https://docs.python.org/3/library/gc.html)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-17: 新增“内存排障：tracemalloc、gc 与对象增长”，补齐 Python 从业者的内存问题定位基础。

---
[返回 Python 学习总览](../README.md)
