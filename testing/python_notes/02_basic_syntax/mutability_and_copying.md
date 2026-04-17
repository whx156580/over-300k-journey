---
title: 变量可变性与深浅拷贝 (Mutability & Copying)
module: testing
area: python_notes
stack: python
level: basics
status: active
tags: [python, mutability, copy, deepcopy, references]
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
- **问题场景**: 在自动化测试中，修改了一个测试数据对象的字段，结果发现其他测试用例的数据也意外发生了变化；或者在函数内部修改了传入的列表，导致调用方的原始数据被破坏。
- **学习目标**: 掌握可变 (Mutable) 与不可变 (Immutable) 对象的本质区别，理解引用赋值、浅拷贝与深拷贝的底层逻辑。
- **前置知识**: [变量与数据类型](./variables_and_types.md)。

## 核心结论
- **引用本质**: Python 变量名只是对象的“标签”，赋值操作 `b = a` 仅增加一个别名，不产生副本。
- **浅拷贝 (Shallow Copy)**: 仅复制容器本身，容器内的元素仍是原始引用的“影子”。
- **深拷贝 (Deep Copy)**: 递归复制容器及其包含的所有嵌套对象，实现物理上的完全隔离。

## 原理拆解
- **ID 追踪**: `id(obj)` 返回对象在内存中的唯一地址。如果 `id(a) == id(b)`，则修改其中一个必然影响另一个。
- **不可变性**: `str`, `int`, `tuple` 等对象一旦创建，其内存内容不可更改。任何“修改”操作实际上都是创建了一个新对象。

## 官方文档与兼容性
| 规则名称 | 官方出处 | PEP 链接 | 兼容性 |
| :--- | :--- | :--- | :--- |
| `copy` 模块 | [copy — Shallow and deep copy operations](https://docs.python.org/3/library/copy.html) | N/A | Python 1.4+ |
| 对象标识与比较 | [Comparisons](https://docs.python.org/3/reference/expressions.html#comparisons) | N/A | Python 1.0+ |

## 代码示例

### 示例 1：引用别名与可变性陷阱
演示为什么简单的赋值会导致数据污染。

```python
# 原始数据
original_config = {"env": "prod", "retries": 3}
# 仅仅是起了一个别名
shared_config = original_config

shared_config["retries"] = 5

print(f"Original: {original_config['retries']}") # 输出 5
assert original_config is shared_config # 指向同一内存地址
```

### 示例 2：浅拷贝的“影子”效应
展示浅拷贝在处理嵌套结构时的局限性。

```python
import copy

# 嵌套结构：列表内含列表
base_data = [1, [2, 3]]
# 浅拷贝
shallow_copy = copy.copy(base_data)

# 修改最外层：互不影响
shallow_copy[0] = 100
# 修改嵌套层：依然联动！
shallow_copy[1].append(4)

print(f"Base: {base_data}") # [1, [2, 3, 4]]
assert base_data[0] == 1
assert base_data[1] is shallow_copy[1] # 嵌套部分指向同一个对象
```

### 示例 3：深拷贝的完全隔离
演示如何彻底断开数据关联，常用于测试用例的数据初始化。

```python
import copy

complex_template = {
    "user": {"id": 1, "roles": ["admin"]},
    "meta": "v1"
}

# 物理隔离的副本
independent_data = copy.deepcopy(complex_template)

independent_data["user"]["roles"].append("qa")

print(f"Template roles: {complex_template['user']['roles']}") # ['admin']
assert "qa" not in complex_template["user"]["roles"]
```

## 性能基准测试
对比深浅拷贝在处理大规模嵌套对象时的开销。

```python
import timeit
import copy

# 构建一个深度嵌套的大型对象
large_obj = [{"key": [i] * 10} for i in range(1000)]

def test_shallow():
    return copy.copy(large_obj)

def test_deep():
    return copy.deepcopy(large_obj)

t_shallow = timeit.timeit(test_shallow, number=100)
t_deep = timeit.timeit(test_deep, number=100)

print(f"Shallow Copy avg: {t_shallow/100:.6f}s")
print(f"Deep Copy avg: {t_deep/100:.6f}s") # 深拷贝显著更慢
```

## 易错点与最佳实践
| 特性 | 常见陷阱 | 最佳实践 |
| :--- | :--- | :--- |
| **赋值误解** | 认为 `new = old` 会备份数据。 | 永远记住赋值只是增加别名。 |
| **浅拷贝滥用** | 对包含 List/Dict 的配置对象使用浅拷贝，导致全局配置被篡改。 | 涉及嵌套可变对象时，始终使用 `deepcopy`。 |
| **性能损耗** | 在循环中频繁调用 `deepcopy` 处理巨型对象。 | 考虑使用工厂函数生成新对象，或仅拷贝必要的子模块。 |

## Self-Check
1. 如何使用切片操作 `[:]` 实现列表的浅拷贝？
2. 如果元组 `(1, [2])` 包含了一个列表，这个元组还是不可变的吗？
3. `a == b` 与 `a is b` 在拷贝前后的判断结果有何不同？

## 参考链接
- [Python References and Mutability](https://realpython.com/python-variables/)
- [Deep Copy vs Shallow Copy in Python](https://example.com)

---
[版本记录](./mutability_and_copying.md) | [返回首页](../README.md)
