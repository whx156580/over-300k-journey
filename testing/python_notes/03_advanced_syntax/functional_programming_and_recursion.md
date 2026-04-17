---
title: 函数式编程与递归 (Functional & Recursion)
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, functional, lambda, partial, recursion, lru_cache]
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
- **问题场景**: 传统的 `for` 循环在处理深度嵌套的树状结构（如 HTML DOM 或 递归 JSON）时显得力不从心；或者需要动态生成一系列行为相似但配置不同的测试函数。
- **学习目标**: 掌握“函数是一等公民”的核心理念，熟练运用 `lambda` 简化逻辑，利用 `partial` 实现行为预设，并能编写高性能的递归算法。
- **前置知识**: [函数基础](../02_basic_syntax/function_basics.md)。

## 核心结论
- **行为参数化**: 高阶函数（如 `map`, `filter`, `sorted`）通过接收函数作为参数，实现了算法框架与具体逻辑的分离。
- **闭包工厂**: `partial` 的本质是利用闭包预先填充部分函数参数，生成一个新的特化函数。
- **递归要素**: 任何递归必须包含 **基线条件 (Base Case)**（防止无限循环）和 **递归步骤 (Recursive Step)**。

## 原理拆解
- **一等公民**: 在 Python 中，函数是对象，可以赋值给变量、存入容器、作为参数或返回值。
- **栈溢出 (RecursionLimit)**: 递归过深会导致 `RecursionError`。可以通过 `sys.setrecursionlimit` 调整，但通常应优化算法或改为迭代。

## 官方文档与兼容性
| 规则名称 | 官方出处 | PEP 链接 | 兼容性 |
| :--- | :--- | :--- | :--- |
| `functools` | [Higher-order functions](https://docs.python.org/3/library/functools.html) | N/A | Python 2.5+ |
| `lru_cache` | [functools.lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache) | N/A | Python 3.2+ |
| `lambda` 语法 | [Lambda expressions](https://docs.python.org/3/reference/expressions.html#lambdas) | N/A | Python 1.0+ |

## 代码示例

### 示例 1：复杂对象的多键排序 (Lambda)
演示如何根据多个维度对测试用例结果进行精细化排序。

```python
results = [
    {"name": "Auth", "cost": 0.5, "prio": 1},
    {"name": "Cart", "cost": 1.2, "prio": 2},
    {"name": "Pay", "cost": 0.5, "prio": 0}
]

# 先按耗时升序，耗时相同时按优先级降序
# 技巧：降序数值取反
ordered = sorted(results, key=lambda x: (x["cost"], -x["prio"]))

print(f"Top 1: {ordered[0]['name']}")
assert ordered[0]["name"] == "Pay" # 耗时同为 0.5，但 Pay 优先级更高
```

### 示例 2：利用 `partial` 构建 API 工厂
在测试框架中预设环境与 Headers。

```python
from functools import partial

def request_api(env_base: str, token: str, endpoint: str):
    """
    通用请求函数。
    """
    url = f"{env_base}/{endpoint}"
    return f"Fetching {url} with Token: {token[:4]}..."

# 为特定环境和用户创建快捷入口
qa_client = partial(request_api, "https://qa.api.com", "SECRET_TOKEN")

# 调用时只需传入 endpoint
print(qa_client("users/list"))
assert "qa.api.com/users/list" in qa_client("users/list")
```

### 示例 3：递归解析嵌套字典 (JSON 展平)
处理深度未知的嵌套结构，提取所有叶子节点。

```python
from typing import Dict, Any

def flatten_json(data: Any, prefix: str = "") -> Dict[str, Any]:
    """
    递归将嵌套字典转换为扁平的路径键值对。
    """
    items = {}
    if isinstance(data, dict):
        for k, v in data.items():
            new_key = f"{prefix}.{k}" if prefix else k
            items.update(flatten_json(v, new_key))
    else:
        items[prefix] = data
    return items

# 验证
nested = {"a": {"b": 1, "c": {"d": 2}}, "e": 3}
flat = flatten_json(nested)
print(f"Flat: {flat}")
assert flat["a.c.d"] == 2
```

## 性能基准测试
对比普通递归与开启 `lru_cache` 后的性能量级差异。

```python
import timeit
from functools import lru_cache

def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

@lru_cache(maxsize=None)
def fib_cached(n):
    if n < 2: return n
    return fib_cached(n-1) + fib_cached(n-2)

# 递归 30 次的耗时对比
t_raw = timeit.timeit(lambda: fib(30), number=1)
t_cached = timeit.timeit(lambda: fib_cached(30), number=1)

print(f"Raw Recursion: {t_raw:.4f}s")
print(f"Cached Recursion: {t_cached:.6f}s") # 接近 $O(n)$
```

## 易错点与最佳实践
| 特性 | 常见陷阱 | 最佳实践 |
| :--- | :--- | :--- |
| **Lambda 复杂度** | 在 lambda 里嵌套 if-else 或列表推导式。 | 如果逻辑超过一行，应改用传统的 `def` 定义。 |
| **递归深度** | 处理超大型树结构导致 `StackOverflow`。 | 优先考虑将算法改为基于 `Stack/Queue` 的迭代实现。 |
| **可变闭包变量** | 在闭包中尝试修改外部变量却不声明 `nonlocal`。 | 明确变量作用域，或者利用对象属性进行状态传递。 |

## Self-Check
1. `map(int, ["1", "2"])` 返回的是列表还是迭代器？
2. 递归中的“记忆化” (Memoization) 是为了解决什么重复计算问题？
3. `functools.wraps` 在编写装饰器时起到了什么关键作用？

## 参考链接
- [Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
- [Thinking Recursively in Python](https://realpython.com/python-thinking-recursively/)

---
[版本记录](./functional_programming_and_recursion.md) | [返回首页](../README.md)
