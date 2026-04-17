---
title: 上下文管理器进阶 (Context Managers)
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, context-manager, with, contextlib, resource-management]
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
- **问题场景**: 忘记关闭数据库连接导致连接池爆满、文件句柄未释放导致磁盘写入异常、或者测试脚本崩溃导致临时测试数据残留在环境中。
- **学习目标**: 掌握 `with` 语句的底层协议，能够编写鲁棒的类式与生成器式上下文管理器，实现资源的自动化生命周期管理。
- **前置知识**: [面向对象](./object_oriented_programming.md)、[异常体系](./exceptions.md)。

## 核心结论
- **确定性清理**: `with` 块保证了无论是否发生异常，清理逻辑（`__exit__` 或 `finally`）必然执行。
- **职责分明**: `__enter__` 负责“拿资源”，`__exit__` 负责“还资源”。
- **异常控制**: `__exit__` 返回 `True` 会静默（吞掉）异常，返回 `False`（默认）则会向上传播异常。

## 原理拆解
- **上下文协议**: 一个对象只需实现 `__enter__()` 和 `__exit__(exc_type, exc_val, exc_tb)` 即可成为上下文管理器。
- **执行流**: 
  1. 调用 `__enter__` 并将返回值赋给 `as` 后的变量。
  2. 执行 `with` 块内的业务逻辑。
  3. 无论成功与否，调用 `__exit__`。

## 官方文档与兼容性
| 规则名称 | 官方出处 | PEP 链接 | 兼容性 |
| :--- | :--- | :--- | :--- |
| `with` 语句 | [The with statement](https://docs.python.org/3/reference/compound_stmts.html#with) | [PEP 343](https://peps.python.org/pep-0343/) | Python 2.5+ |
| `contextlib` | [Utilities for with-statement](https://docs.python.org/3/library/contextlib.html) | N/A | Python 2.5+ |
| 异步上下文 | [Asynchronous Context Managers](https://docs.python.org/3/reference/datamodel.html#asynchronous-context-managers) | [PEP 492](https://peps.python.org/pep-0492/) | Python 3.5+ |

## 代码示例

### 示例 1：类驱动的测试资源管理器
模拟在 UI 测试中自动启停浏览器驱动。

```python
from typing import Any

class MockBrowser:
    """模拟浏览器驱动资源"""
    def __init__(self, name: str):
        self.name = name
        self.active = False

    def __enter__(self) -> 'MockBrowser':
        print(f"--- [ENTER] Starting {self.name} ---")
        self.active = True
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> bool:
        print(f"--- [EXIT] Closing {self.name} ---")
        self.active = False
        # 如果发生异常，打印异常类型
        if exc_type:
            print(f"Exception detected during exit: {exc_type.__name__}")
        return False # 不吞异常，继续抛出

# 验证
with MockBrowser("Playwright") as driver:
    print(f"Driver status: {driver.active}")
    assert driver.active is True
```

### 示例 2：生成器驱动的轻量级装饰器
利用 `contextlib` 快速封装临时状态切换。

```python
from contextlib import contextmanager

@contextmanager
def temporary_config(settings: dict, key: str, value: Any):
    """
    临时修改配置，并在退出时还原。
    """
    old_value = settings.get(key)
    settings[key] = value
    print(f"Config set: {key}={value}")
    try:
        yield settings
    finally:
        settings[key] = old_value
        print(f"Config restored: {key}={old_value}")

# 验证
global_settings = {"debug": False, "timeout": 30}
with temporary_config(global_settings, "debug", True):
    assert global_settings["debug"] is True
assert global_settings["debug"] is False
```

### 示例 3：异常压制实验 (Suppression)
演示如何有条件地“吞掉”特定异常。

```python
class IgnoreSpecificError:
    def __init__(self, exc_to_ignore):
        self.exc_to_ignore = exc_to_ignore

    def __enter__(self): return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 如果抛出的异常是目标类型，返回 True 阻止传播
        if exc_type and issubclass(exc_type, self.exc_to_ignore):
            print(f"Ignoring expected error: {exc_val}")
            return True
        return False

# 验证
with IgnoreSpecificError(ValueError):
    print("Trying to parse bad int...")
    int("abc") # 会抛出 ValueError，但被吞掉

print("Program continues normally.")
```

## 性能基准测试
对比 `with` 语句与传统 `try-finally` 的开销。

```python
import timeit

def with_style():
    with open(__file__, "r") as f:
        pass

def try_finally_style():
    f = open(__file__, "r")
    try:
        pass
    finally:
        f.close()

t1 = timeit.timeit(with_style, number=10000)
t2 = timeit.timeit(try_finally_style, number=10000)

print(f"With statement: {t1:.4f}s")
print(f"Try-finally: {t2:.4f}s") # 性能差异微乎其微，建议优先使用 with
```

## 易错点与最佳实践
| 特性 | 常见陷阱 | 最佳实践 |
| :--- | :--- | :--- |
| **吞掉异常** | 无脑在 `__exit__` 中返回 `True`。 | 仅在确实处理了异常且不再需要上报时才返回 `True`。 |
| **资源释放** | 在 `__enter__` 之前发生错误。 | 确保 `__enter__` 之前的初始化逻辑（如 `__init__`）足够健壮。 |
| **代码冗余** | 对已支持 `with` 的库（如 `requests`）手动调用 `close`。 | 优先检查库文档，使用其内置的上下文管理支持。 |

## Self-Check
1. `with A() as a, B() as b:` 这种写法的嵌套执行顺序是怎样的？
2. 在生成器式管理器中，如果不写 `try...finally` 而直接 `yield`，发生异常会怎样？
3. `contextlib.closing` 是为了解决什么样的问题？

## 参考链接
- [Python Context Managers: The with Statement](https://realpython.com/python-with-statement/)
- [Standard Library contextlib docs](https://docs.python.org/3/library/contextlib.html)

---
[版本记录](./context_managers.md) | [返回首页](../README.md)
