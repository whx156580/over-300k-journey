---
title: 核心容器：列表、元组、集合、字典 (Collections)
module: testing
area: python_notes
stack: python
level: basics
status: active
tags: [python, list, dict, set, tuple, performance]
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
- **问题场景**: 在自动化测试中，我们需要存储数千个接口响应结果（列表）、根据用例 ID 快速查找状态（字典）、对比两个测试环境的差异项（集合）或者传递不可篡改的配置记录（元组）。
- **学习目标**: 掌握四种基础容器的高阶用法，理解其时间复杂度差异，能够根据业务场景选择最优容器。
- **前置知识**: [变量与数据类型](./variables_and_types.md)。

## 核心结论
- **有序 vs 无序**: 列表、元组有序；集合无序；字典（3.7+）保持插入顺序。
- **性能关键**: 集合和字典的成员检查 (`in`) 复杂度为 $O(1)$，而列表为 $O(n)$。
- **可变性**: 列表、集合、字典可变；元组不可变。

## 原理拆解
- **哈希冲突**: 字典和集合基于哈希表。若对象不可哈希（如列表），则不能作为字典的键或集合元素。
- **动态扩容**: 列表在 `append` 时会自动预分配超额空间，以实现均摊 $O(1)$ 的追加性能。

## 官方文档与兼容性
| 规则名称 | 官方出处 | PEP 链接 | 兼容性 |
| :--- | :--- | :--- | :--- |
| 内置容器 | [Built-in Types - Sequence/Mapping/Set](https://docs.python.org/3/library/stdtypes.html) | N/A | Python 1.0+ |
| 字典有序性 | [Ordered dicts](https://docs.python.org/3.7/library/stdtypes.html#dict) | N/A | Python 3.7+ |
| `collections` 模块 | [High-performance container datatypes](https://docs.python.org/3/library/collections.html) | N/A | Python 2.4+ |

## 代码示例

### 示例 1：集合运算与环境对比
快速找出两个测试环境配置的差异。

```python
env_prod = {"debug=False", "timeout=30", "db=prod_db"}
env_staging = {"debug=True", "timeout=30", "db=prod_db"}

# 找出 staging 特有的配置 (差集)
staging_only = env_staging - env_prod
# 找出共同的配置 (交集)
common_config = env_prod & env_staging

print(f"Staging unique: {staging_only}")
assert "debug=True" in staging_only
```

### 示例 2：字典的高级操作 (Merging & Default)
合并配置字典并处理缺失键。

```python
from collections import defaultdict

# 1. 自动计数器
counter = defaultdict(int)
for status in ["PASS", "FAIL", "PASS"]:
    counter[status] += 1

# 2. 字典合并 (Python 3.9+)
base_conf = {"retry": 1, "headless": True}
user_conf = {"retry": 3, "env": "dev"}
final_conf = base_conf | user_conf # 合并并覆盖

print(f"Final Config: {final_conf}")
assert final_conf["retry"] == 3
```

### 示例 3：元组解包与具名元组 (NamedTuple)
让返回的结构化数据更具可读性。

```python
from typing import NamedTuple

class TestResult(NamedTuple):
    id: int
    status: str
    duration: float

res = TestResult(101, "PASSED", 0.45)
# 既可以按索引访问，也可以按名称访问
print(f"ID: {res.id}, Duration: {res[2]}s")
assert res.status == "PASSED"
```

## 性能基准测试
对比列表与集合在成员查找上的巨大性能差异。

```python
import timeit

n = 10000
test_list = list(range(n))
test_set = set(range(n))

# 查找中间元素
target = n // 2

t_list = timeit.timeit(lambda: target in test_list, number=1000)
t_set = timeit.timeit(lambda: target in test_set, number=1000)

print(f"List search: {t_list:.6f}s")
print(f"Set search: {t_set:.6f}s")
print(f"Speedup: {t_list/t_set:.1f}x")
```

## 易错点与最佳实践
| 特性 | 常见陷阱 | 最佳实践 |
| :--- | :--- | :--- |
| **可变默认参数** | `def add(val, l=[])`。 | 始终使用 `l=None`。 |
| **字典查找** | `if key in d: val = d[key]`。 | 直接使用 `d.get(key, default)` 减少哈希计算。 |
| **列表删除** | 在循环 `for x in my_list` 中删除元素。 | 遍历副本 `for x in my_list[:]` 或使用推导式重建列表。 |

## Self-Check
1. 为什么列表不能作为字典的键，而元组可以？
2. `my_dict.get("missing", [])` 与 `defaultdict` 在处理缺失键时有什么本质区别？
3. 如何在保持顺序的前提下对列表进行去重？

## 参考链接
- [Python TimeComplexity Guide](https://wiki.python.org/moin/TimeComplexity)
- [Real Python: Dictionary Deep Dive](https://realpython.com/python-dicts/)

---
[版本记录](./collections.md) | [返回首页](../README.md)
