---
title: 装饰器 (Decorators)
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, decorator, wraps, closures, aop]
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
- **问题场景**: 接口测试中需要统一处理重试、权限校验、耗时统计或结果缓存，而不希望侵入业务逻辑。
- **学习目标**: 理解闭包机制，掌握函数装饰器与类装饰器，能够处理多层嵌套与参数传递。
- **前置知识**: [函数基础](../02_basic_syntax/function_basics.md)、[闭包概念]。

## 核心结论
- **本质**: 装饰器是返回可调用对象的高阶函数，遵循 `func = decorator(func)` 的等价替换。
- **元信息**: 必须使用 `functools.wraps` 保留被装饰函数的签名与文档。
- **应用顺序**: 多个装饰器应用时“由近及远”（从下往上），调用时“由外向内”（从上往下）。

## 原理拆解
- **闭包机制**: 装饰器利用闭包特性，将被装饰函数作为自由变量绑定在包装器函数中。
- **语法糖**: `@` 符号仅是语法糖，底层逻辑是函数对象的引用替换。

## 官方文档与兼容性
| 规则名称 | 官方出处 | PEP 链接 | 兼容性 |
| :--- | :--- | :--- | :--- |
| 装饰器语法 | [Function definitions](https://docs.python.org/3/reference/compound_stmts.html#function-definitions) | [PEP 318](https://peps.python.org/pep-0318/) | Python 2.4+ |
| 类装饰器 | [Class definitions](https://docs.python.org/3/reference/compound_stmts.html#class-definitions) | [PEP 3129](https://peps.python.org/pep-3129/) | Python 2.6+ |
| `functools.wraps` | [functools 模块](https://docs.python.org/3/library/functools.html#functools.wraps) | N/A | Python 2.5+ |

## 代码示例

### 示例 1：带参数的智能重试装饰器 (函数式)
在接口测试中，针对特定异常进行指数退避重试。

```python
import time
import random
from functools import wraps
from typing import Callable, Any

def retry(max_attempts: int = 3, delay: float = 1.0):
    """
    带参数的重试装饰器。
    """
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise e
                    # 指数退避 + 抖动
                    sleep_time = delay * (2 ** (attempts - 1)) + random.uniform(0, 0.1)
                    print(f"Retrying {func.__name__} ({attempts}/{max_attempts}) after {sleep_time:.2f}s...")
                    time.sleep(sleep_time)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.1)
def unstable_api():
    if random.random() < 0.7:
        raise ConnectionError("Network flaked")
    return "Success"

print(unstable_api())
```

### 示例 2：带状态的类装饰器 (统计调用频率)
利用类实例存储装饰器的执行状态。

```python
from functools import wraps
from typing import Any, Callable

class CallCounter:
    """
    类装饰器：记录函数被调用的总次数。
    """
    def __init__(self, func: Callable):
        wraps(func)(self)
        self.func = func
        self.count = 0

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.count += 1
        return self.func(*args, **kwargs)

@CallCounter
def process_data(data: str):
    return f"processed {data}"

process_data("A")
process_data("B")
print(f"Call count: {process_data.count}")
```

### 示例 3：装饰器链与执行顺序
演示多层装饰器下 `wraps` 和执行顺序的重要性。

```python
from functools import wraps

def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold
@italic
def greet(name: str):
    return f"Hello, {name}"

# 调用逻辑：bold(italic(greet)) -> <b><i>Hello, Alice</i></b>
print(greet("Alice"))
assert greet.__name__ == "greet"
```

## 性能基准测试
使用 `timeit` 对比装饰器引入的调用开销。

```python
import timeit

setup = """
from functools import wraps
def noop(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def raw_func(x): return x
@noop
def decorated_func(x): return x
"""

raw_time = timeit.timeit("raw_func(1)", setup=setup, number=1000000)
dec_time = timeit.timeit("decorated_func(1)", setup=setup, number=1000000)
print(f"Raw function: {raw_time:.4f}s")
print(f"Decorated function: {dec_time:.4f}s")
print(f"Overhead per call: {(dec_time - raw_time) / 1000000 * 1e6:.2f}μs")
```

## 易错点与最佳实践
| 特性 | 常见陷阱 | 最佳实践 |
| :--- | :--- | :--- |
| **元信息丢失** | 忘记使用 `@wraps`，导致 `help(func)` 或 `func.__name__` 指向包装器。 | 始终导入 `from functools import wraps` 并应用。 |
| **参数泄露** | 在包装器中固定参数，导致无法支持可变长参数 `*args, **kwargs`。 | 包装器签名始终使用 `(*args, **kwargs)` 转发请求。 |
| **类装饰器状态** | 类装饰器在类定义阶段就已实例化，状态是全局共享的。 | 如需每个实例独立状态，应在 `__get__` 中处理描述符逻辑。 |

## Self-Check
1. 如何编写一个既能作为 `@dec` 使用，也能作为 `@dec(params)` 使用的装饰器？
2. 装饰器链中，靠近函数定义的装饰器先执行还是后执行？
3. 在类方法上使用装饰器时，`self` 参数是如何通过装饰器传递的？

## 参考链接
- [Python Expert: Decorators Deep Dive](https://example.com)
- [Fluent Python: Function as Objects](https://example.com)

---
[版本记录](./decorators.md) | [返回首页](../README.md)
