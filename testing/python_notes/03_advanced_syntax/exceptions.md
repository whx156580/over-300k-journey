---
title: 异常体系 (Exception Handling)
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, exception, raise-from, context-manager, error-handling]
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
- **问题场景**: 接口请求失败时需要区分“可重试错误”与“致命配置错误”，或者在多层调用中保留原始报错的上下文以便排障。
- **学习目标**: 掌握异常链机制，能够设计符合业务语义的自定义异常类，并能高效利用 `traceback` 进行调试。
- **前置知识**: [流程控制](../02_basic_syntax/control_flow.md)。

## 核心结论
- **异常链**: 使用 `raise from` 显式链接异常，保留 `__cause__` 追踪原始根因。
- **捕获策略**: 始终捕获具体的异常类（如 `ValueError`），严禁无脑 `except Exception: pass`。
- **清理保障**: `finally` 块确保资源（文件、Socket）在报错时也能正常释放。

## 原理拆解
- **MRO 层级**: 所有异常继承自 `BaseException`。`Exception` 是应用级异常的基类，`SystemExit`/`KeyboardInterrupt` 直接继承自 `BaseException`。
- **上下文传播**: 异常在未被捕获时会沿着调用栈向上传播，直到被处理或导致进程退出。

## 官方文档与兼容性
| 规则名称 | 官方出处 | PEP 链接 | 兼容性 |
| :--- | :--- | :--- | :--- |
| 异常层级 | [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html) | N/A | Python 1.5+ |
| 异常链 (raise from) | [The raise statement](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement) | [PEP 3134](https://peps.python.org/pep-3134/) | Python 3.0+ |
| `ExceptionGroup` | [Exception groups](https://docs.python.org/3/library/exceptions.html#exception-groups) | [PEP 654](https://peps.python.org/pep-0654/) | Python 3.11+ |

## 代码示例

### 示例 1：自定义异常体系与 `raise from`
在复杂的测试框架中构建语义化的报错。

```python
class AppError(Exception):
    """应用级异常基类"""
    pass

class DatabaseError(AppError):
    """数据库操作异常"""
    pass

def query_user(user_id: int):
    try:
        # 模拟底层连接失败
        raise ConnectionError("Timeout on port 5432")
    except ConnectionError as e:
        # 显式建立异常链
        raise DatabaseError(f"Failed to fetch user {user_id}") from e

try:
    query_user(1)
except DatabaseError as err:
    print(f"Captured: {err}")
    print(f"Original cause: {err.__cause__}")
```

### 示例 2：异常上下文管理器 (pytest-style)
演示如何编写一个用于测试的断言上下文管理器。

```python
import contextlib

@contextlib.contextmanager
def assert_raises(expected_exc):
    try:
        yield
    except expected_exc:
        print(f"Caught expected: {expected_exc.__name__}")
    else:
        raise AssertionError(f"Did not raise {expected_exc.__name__}")

with assert_raises(ValueError):
    int("abc")
```

### 示例 3：异常组处理 (Python 3.11+)
处理并发任务中可能同时抛出的多个异常。

```python
def run_concurrent_tasks():
    # 模拟两个并发任务同时失败
    excs = [ValueError("Invalid ID"), TypeError("Invalid type")]
    raise ExceptionGroup("Multiple errors occurred", excs)

try:
    run_concurrent_tasks()
except* ValueError as eg:
    print(f"Handled ValueErrors: {len(eg.exceptions)}")
except* TypeError as eg:
    print(f"Handled TypeErrors: {len(eg.exceptions)}")
```

## 性能基准测试
对比异常处理对正常流程的影响（仅在触发异常时有显著开销）。

```python
import timeit

# 正常路径
t_normal = timeit.timeit("int('123')", number=1000000)
# 异常路径 (极其缓慢)
t_except = timeit.timeit("""
try:
    int('abc')
except ValueError:
    pass
""", number=100000) # 次数减小 10 倍

print(f"Normal path: {t_normal:.4f}s")
print(f"Exception path (10x scaled): {t_except * 10:.4f}s")
```

## 易错点与最佳实践
| 特性 | 常见陷阱 | 最佳实践 |
| :--- | :--- | :--- |
| **过度捕获** | `except Exception` 捕获了不该处理的系统错误。 | 尽量精确捕获目标异常。 |
| **信息丢失** | 直接 `raise NewError()` 丢弃了原始 traceback。 | 始终使用 `raise NewError() from e`。 |
| **else 块缺失** | 在 try 块中放入太多代码，导致误捕获。 | 仅在 try 块放可能报错的代码，其余移入 `else`。 |

## Self-Check
1. `raise from None` 有什么特殊用途？
2. 在 `finally` 块中使用 `return` 会产生什么副作用？
3. `traceback.format_exc()` 与直接 `print(e)` 的区别是什么？

## 参考链接
- [Effective Python: Chapter 4 - Metaprogramming and Attributes](https://example.com)
- [Python Traceback Module](https://docs.python.org/3/library/traceback.html)

---
[版本记录](./exceptions.md) | [返回首页](../README.md)
