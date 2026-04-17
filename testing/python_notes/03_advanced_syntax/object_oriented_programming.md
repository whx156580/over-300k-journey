---
title: 面向对象 (Object-Oriented Programming)
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, oop, mro, abc, slots, property]
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
- **问题场景**: 自动化测试框架中，Page Object Model (POM) 需要抽象通用操作；或者需要构建复杂的测试数据模型，保证行为与数据的高度封装。
- **学习目标**: 掌握 Python 特有的 OOP 机制（如 MRO、描述符、抽象类），能够编写可维护、高复用性的类体系。
- **前置知识**: [基础语法](../02_basic_syntax/variables_and_types.md)、[函数基础](../02_basic_syntax/function_basics.md)。

## 核心结论
- **查找顺序**: Python 采用 C3 算法计算 MRO (Method Resolution Order)，决定了多继承下的方法调用链。
- **内存优化**: `__slots__` 显式声明实例属性，取消 `__dict__` 动态绑定，能显著降低海量小对象的内存开销。
- **接口约束**: 通过 `abc.ABC` 与 `@abstractmethod` 强制子类实现特定协议，确保架构一致性。

## 原理拆解
- **C3 线性化**: 多继承时，Python 会生成一个扁平的查找序列，保证父类方法不被重复访问且遵循局部优先级。
- **属性拦截**: `property` 本质是资料描述符，拦截了实例属性的读写请求。

## 官方文档与兼容性
| 规则名称 | 官方出处 | PEP 链接 | 兼容性 |
| :--- | :--- | :--- | :--- |
| MRO (C3 算法) | [Python MRO](https://www.python.org/download/releases/2.3/mro/) | N/A | Python 2.3+ |
| 抽象基类 (ABC) | [abc 模块](https://docs.python.org/3/library/abc.html) | [PEP 3119](https://peps.python.org/pep-3119/) | Python 2.6+ |
| `__slots__` | [__slots__ 定义](https://docs.python.org/3/reference/datamodel.html#slots) | N/A | Python 2.2+ |

## 代码示例

### 示例 1：多继承与 MRO (钻石继承)
理解方法查找链，避免重复调用。

```python
class Base:
    def action(self):
        print("Base action")

class Left(Base):
    def action(self):
        print("Left action")
        super().action()

class Right(Base):
    def action(self):
        print("Right action")
        super().action()

class Child(Left, Right):
    def action(self):
        print("Child action")
        super().action()

# 运行 Child().action()
# 顺序: Child -> Left -> Right -> Base
Child().action()
print(f"MRO: {[c.__name__ for r in Child.mro()]}") # 修正占位符
```

### 示例 2：Page Object 接口约束 (ABC + POM)
在 UI 自动化中，强制要求每个页面必须实现 `is_loaded` 检查。

```python
from abc import ABC, abstractmethod

class BasePage(ABC):
    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def is_loaded(self) -> bool:
        """子类必须实现此方法以验证页面加载状态"""
        pass

    def open(self, url: str):
        print(f"Opening {url}")
        # 模板方法模式：子类无需重写 open，但必须提供 is_loaded 逻辑
        if not self.is_loaded():
            raise RuntimeError("Page failed to load")

class LoginPage(BasePage):
    def is_loaded(self) -> bool:
        return True # 模拟成功

lp = LoginPage(None)
lp.open("https://example.com/login")
```

### 示例 3：海量数据对象的内存优化 (__slots__)
在处理百万级测试数据时，使用 `__slots__` 节省内存。

```python
class Measurement:
    __slots__ = ("timestamp", "value", "unit")
    def __init__(self, ts, val, unit):
        self.timestamp = ts
        self.value = val
        self.unit = unit

# 尝试动态添加属性会报错
m = Measurement(1620000000, 25.5, "C")
try:
    m.extra = "fail"
except AttributeError as e:
    print(f"Caught expected error: {e}")
```

## 性能基准测试
对比使用 `__slots__` 后的对象创建耗时与内存占用。

```python
import timeit
import sys

setup = """
class Normal:
    def __init__(self, a, b): self.a, self.b = a, b
class Slotted:
    __slots__ = ("a", "b")
    def __init__(self, a, b): self.a, self.b = a, b
"""

t_normal = timeit.timeit("Normal(1, 2)", setup=setup, number=1000000)
t_slots = timeit.timeit("Slotted(1, 2)", setup=setup, number=1000000)

print(f"Normal create: {t_normal:.4f}s")
print(f"Slotted create: {t_slots:.4f}s")

# 内存占用示意 (sys.getsizeof 无法直接展示 dict 节省，需工具辅助)
print("Tip: __slots__ typically saves ~50% memory for small objects.")
```

## 易错点与最佳实践
| 特性 | 常见陷阱 | 最佳实践 |
| :--- | :--- | :--- |
| **多继承** | `super()` 调用链断裂。 | 始终在所有层级使用 `super().method()` 转发调用。 |
| **可变类变量** | `class A: list_var = []`，所有实例共享同一个列表。 | 在 `__init__` 中初始化实例变量 `self.list_var = []`。 |
| **ABC 实例化** | 尝试实例化包含未实现抽象方法的子类。 | 确保子类重写了所有标记为 `@abstractmethod` 的成员。 |

## Self-Check
1. `super()` 调用的是父类方法吗？还是 MRO 中的下一个方法？
2. 为什么带有 `__slots__` 的类不能直接多继承？
3. `property` 的 `setter` 装饰器依赖于什么前提条件？

## 参考链接
- [Python Data Model - Objects, values and types](https://docs.python.org/3/reference/datamodel.html)
- [C3 Linearization Paper](https://www.python.org/download/releases/2.3/mro/)

---
[版本记录](./object_oriented_programming.md) | [返回首页](../README.md)
