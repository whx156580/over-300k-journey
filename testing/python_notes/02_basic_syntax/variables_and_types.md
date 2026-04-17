---
title: 变量与数据类型 (Variables & Data Types)
module: testing
area: python_notes
stack: python
level: basics
status: active
tags: [python, variables, types, objects, type-hints]
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
- **问题场景**: 刚从 Java/C++ 转过来的开发者容易对 Python 的“变量名只是引用”感到困惑，或者在处理 JSON 数据时因为类型自动推断而产生 Bug（如 `1` 与 `"1"` 不相等）。
- **学习目标**: 理解 Python 的动态强类型特性，掌握核心内置类型及其内存表现，学会使用类型注解 (Type Hints) 提升代码健壮性。
- **前置知识**: 无。

## 核心结论
- **变量即标签**: Python 变量名是绑定到对象的引用，变量本身无类型，对象才有类型。
- **动态强类型**: 无需预声明类型（动态），但类型不匹配时绝不自动转换（强类型）。
- **Identity vs Equality**: `is` 检查“身份”（内存地址），`==` 检查“值”。

## 原理拆解
- **PyObject**: 每一个 Python 对象在 C 层面都是一个 `PyObject` 结构体，包含引用计数和类型指针。
- **小整数池**: Python 预分配了 `-5` 到 `256` 之间的整数，这些对象在全局是单例的。

## 官方文档与兼容性
| 规则名称 | 官方出处 | PEP 链接 | 兼容性 |
| :--- | :--- | :--- | :--- |
| 内置类型 | [Built-in Types](https://docs.python.org/3/library/stdtypes.html) | N/A | Python 1.0+ |
| 类型注解 | [Typing — Support for type hints](https://docs.python.org/3/library/typing.html) | [PEP 484](https://peps.python.org/pep-0484/) | Python 3.5+ |
| 变量注解 | [Variable Annotations](https://peps.python.org/pep-0526/) | [PEP 526](https://peps.python.org/pep-0526/) | Python 3.6+ |

## 代码示例

### 示例 1：内存引用与身份追踪
观察变量重定向后的内存地址变化。

```python
x = [1, 2]
print(f"Initial ID: {id(x)}")

y = x # 共享引用
print(f"Shared ID: {id(y)}")

x = [3, 4] # x 重新绑定到新对象
print(f"New ID: {id(x)}")
assert x is not y # 现在指向不同对象
```

### 示例 2：强类型特性实验
演示 Python 不会自动转换不兼容类型，避免静默失败。

```python
num = 100
text = "Count: "

try:
    # 尝试直接拼接（Java/JS 中常见）
    result = text + num
except TypeError as e:
    print(f"Caught expected error: {e}")

# 正确做法：显式转换
correct_result = text + str(num)
print(correct_result)
```

### 示例 3：类型注解 (Type Hints) 实战
使用现代语法描述函数契约。

```python
from typing import List, Optional

def process_items(items: List[int], prefix: Optional[str] = None) -> List[str]:
    """
    处理整数列表，返回带前缀的字符串列表。
    """
    p = prefix if prefix else "ITEM"
    return [f"{p}_{i}" for i in items]

res = process_items([1, 2, 3], prefix="VAL")
print(res)
assert res[0] == "VAL_1"
```

## 性能基准测试
对比常用内置类型的内存占用。

```python
import sys

# 整数 vs 浮点数 vs 字符串
data = {
    "int_0": 0,
    "int_big": 2**64,
    "float": 3.14,
    "str_empty": "",
    "str_short": "abc"
}

for name, val in data.items():
    print(f"{name:>10}: {sys.getsizeof(val):>3} bytes")
```

## 易错点与最佳实践
| 特性 | 常见陷阱 | 最佳实践 |
| :--- | :--- | :--- |
| **None 判断** | 使用 `if val == None`。 | 始终使用 `if val is None`（单例判断性能更高）。 |
| **类型遮蔽** | 变量取名为 `list` 或 `str`。 | 避免与内置类型同名，改用 `item_list` 或 `name_str`。 |
| **浮点数比较** | `0.1 + 0.2 == 0.3` 返回 False。 | 使用 `math.isclose()` 进行精度范围内的比较。 |

## Self-Check
1. 为什么 `a = 256; b = 256; a is b` 为 True，但 `a = 257; b = 257; a is b` 在某些环境下可能为 False？
2. `type(obj)` 与 `isinstance(obj, type)` 在处理继承关系时有什么区别？
3. 如何在不运行代码的情况下检查类型注解错误？（提示：`mypy`）。

## 参考链接
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html)
- [Real Python: Type Checking Guide](https://realpython.com/python-type-checking/)

---
[版本记录](./variables_and_types.md) | [返回首页](../README.md)
