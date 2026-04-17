---
title: 迭代器与生成器 (Iterators & Generators)
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, iterator, generator, yield, coroutines]
updated: 2026-04-17
---

## 目录
- [背景](#背景)
- [核心结论](#核心结论)
- [原理拆解](#原理拆解)
- [官方文档与兼容性](#官方文档与兼容性)
- [代码示例](#代码示例)
- [性能基准测试](#性能基准测试)
- [易错点与最佳实践](#易错点与最佳实践)
- [Self-Check](#Self-Check)
- [参考链接](#参考链接)
- [版本记录](#版本记录)

## 背景
- **问题场景**: 处理 GB 级别的日志文件、无限数据流（如传感器数据）或需要协作式任务调度时，一次性加载到内存会导致 OOM（内存溢出）。
- **学习目标**: 掌握迭代器协议，理解 `yield` 的暂停恢复机制，利用 `send/throw/close` 实现双向通信。
- **前置知识**: [流程控制](../02_basic_syntax/control_flow.md)、[函数基础](../02_basic_syntax/function_basics.md)。

## 核心结论
- **迭代器**: 实现了 `__iter__` 和 `__next__` 协议的对象，是有状态的单向消费流。
- **生成器**: 使用 `yield` 关键字的特殊函数，调用时返回生成器对象，具有更低的内存占用。
- **双向通信**: `send()` 将值传回生成器，`throw()` 注入异常，`close()` 强制终止，这是协程的前身。

## 原理拆解
- **惰性求值 (Lazy Evaluation)**: 只有在调用 `next()` 时才计算下一个值，空间复杂度从 $O(n)$ 降至 $O(1)$。
- **状态机**: 生成器在 `yield` 处挂起，保留局部变量、指令指针和异常状态。

## 官方文档与兼容性
| 规则名称 | 官方出处 | PEP 链接 | 兼容性 |
| :--- | :--- | :--- | :--- |
| 迭代器协议 | [Iterator Types](https://docs.python.org/3/library/stdtypes.html#iterator-types) | [PEP 234](https://peps.python.org/pep-0234/) | Python 2.2+ |
| 生成器表达式 | [Generator Expressions](https://docs.python.org/3/reference/expressions.html#generator-expressions) | [PEP 289](https://peps.python.org/pep-0289/) | Python 2.4+ |
| `yield from` | [yield expression](https://docs.python.org/3/reference/expressions.html#yield-expressions) | [PEP 380](https://peps.python.org/pep-0380/) | Python 3.3+ |

## 代码示例

### 示例 1：无限日志处理流水线 (itertools 协作)
模拟处理一个不断增长的审计日志，实现过滤与格式化。

```python
import itertools
from typing import Generator

def log_stream() -> Generator[str, None, None]:
    """模拟无限产生的原始日志流"""
    for i in itertools.count(1):
        yield f"LOG_LINE_{i}: {'ERROR' if i % 5 == 0 else 'INFO'} - Data packet received"

def error_filter(stream: Generator[str, None, None]) -> Generator[str, None, None]:
    """过滤 ERROR 级别的日志"""
    for line in stream:
        if "ERROR" in line:
            yield line

# 组合流水线：获取前 3 条错误日志
pipeline = error_filter(log_stream())
top_errors = list(itertools.islice(pipeline, 3))
print(f"Top Errors: {top_errors}")
```

### 示例 2：双向通信生成器 (带重置功能的累加器)
演示 `send()` 如何干预生成器的内部状态。

```python
from typing import Generator, Union

def smart_accumulator() -> Generator[int, Union[int, str, None], None]:
    """
    累加器生成器。
    发送数字：继续累加。
    发送 "reset"：清零。
    """
    total = 0
    while True:
        # yield total 返回当前值，并接收外部 send() 进来的值
        val = yield total
        if val == "reset":
            total = 0
        elif isinstance(val, int):
            total += val

gen = smart_accumulator()
print(f"Initial: {next(gen)}")  # 预激生成器，产出 0
print(f"Add 10: {gen.send(10)}") # 产出 10
print(f"Add 20: {gen.send(20)}") # 产出 30
print(f"Reset: {gen.send('reset')}") # 产出 0
```

### 示例 3：资源安全的生成器 (try...finally)
确保生成器在被 `close()` 或意外终止时能正确释放资源（如数据库连接）。

```python
def resource_manager(name: str):
    print(f"Opening resource: {name}")
    try:
        yield f"HANDLE_{name}"
    finally:
        # 无论生成器是正常结束还是被 .close()，都会执行
        print(f"Closing resource: {name}")

gen = resource_manager("DB_CONN")
handle = next(gen)
print(f"Using {handle}")
gen.close() # 手动关闭，触发 finally
```

## 性能基准测试
对比 `list` 推导式与生成器表达式在处理千万级数据时的内存差异。

```python
import sys
import timeit

# 1000 万个元素的对比
n = 10_000_000

# 列表推导式：立即分配内存
list_comp = [i for i in range(n)]
# 生成器表达式：仅保存规则
gen_exp = (i for i in range(n))

print(f"List size: {sys.getsizeof(list_comp) / 1024 / 1024:.2f} MB")
print(f"Generator size: {sys.getsizeof(gen_exp)} Bytes")

# 遍历耗时对比 (生成器略慢，但空间换时间)
t_list = timeit.timeit(lambda: sum([i for i in range(1000)]), number=1000)
t_gen = timeit.timeit(lambda: sum((i for i in range(1000))), number=1000)
print(f"Sum list time: {t_list:.4f}s")
print(f"Sum generator time: {t_gen:.4f}s")
```

## 易错点与最佳实践
| 特性 | 常见陷阱 | 最佳实践 |
| :--- | :--- | :--- |
| **一次性消费** | 生成器耗尽后再次迭代会立即抛出 `StopIteration`。 | 如需重复使用，应重新调用生成器函数或将结果存入 `list`。 |
| **预激失败** | 首次调用就使用 `send(非 None)` 会导致 `TypeError`。 | 必须先调用 `next(gen)` 或 `gen.send(None)` 将其推进到第一个 `yield`。 |
| **异常吞噬** | 在生成器内部捕获了 `GeneratorExit` 但没有重新抛出。 | 除非有特殊清理逻辑，否则不要拦截 `GeneratorExit`，以免 `close()` 失效。 |

## Self-Check
1. `yield from` 解决了什么问题？它是如何简化嵌套迭代的？
2. 为什么自定义迭代器类通常也要实现 `__iter__` 返回 `self`？
3. 在 `for` 循环中，`StopIteration` 异常是如何被处理的？

## 参考链接
- [itertools — Functions creating iterators for efficient looping](https://docs.python.org/3/library/itertools.html)
- [Python Design Patterns: Iterator Pattern](https://example.com)

---
[版本记录](./iterators_and_generators.md) | [返回首页](../README.md)
