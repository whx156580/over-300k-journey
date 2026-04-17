---
title: 元编程与描述符协议
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, metaprogramming, metaclass, descriptors, magic-methods]
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
- **问题场景**: 框架开发中需要自动化类注册（如插件系统）、声明式属性校验（如 ORM）或控制对象生命周期。
- **学习目标**: 掌握 `__new__`、`type` 元类、描述符协议，能够构建高度抽象的类结构。
- **前置知识**: [面向对象](./object_oriented_programming.md)、[装饰器](./decorators.md)。

## 核心结论
- **元类** (`metaclass`) 是类的模板，它在 Python 加载模块、创建类对象时介入。
- **描述符** (`descriptor`) 是将属性访问代理到特定类方法的机制，是 `property` 的底层支柱。
- **__new__** 负责“分配内存并返回实例”，是实现单例模式的最稳健入口。

## 原理拆解
- **类创建流程**: 
  1. 解释器扫描 `class` 定义。
  2. 调用元类的 `__new__`（创建类对象）。
  3. 调用元类的 `__init__`（初始化类对象）。
- **属性查找顺序**:
  1. 数据描述符 (`__set__`) -> 2. 实例字典 -> 3. 非数据描述符 (`__get__`) -> 4. 类字典。

## 官方文档与兼容性
| 规则名称 | 官方出处 | PEP 链接 | 兼容性 |
| :--- | :--- | :--- | :--- |
| 元类 (Metaclasses) | [Data Model](https://docs.python.org/3/reference/datamodel.html#metaclasses) | [PEP 3115](https://peps.python.org/pep-3115/) | Python 3.0+ |
| 描述符协议 | [Descriptor HowTo](https://docs.python.org/3/howto/descriptor.html) | [PEP 252](https://peps.python.org/pep-0252/) | Python 2.2+ |
| `__set_name__` | [Customizing class creation](https://docs.python.org/3/reference/datamodel.html#object.__set_name__) | [PEP 487](https://peps.python.org/pep-0487/) | Python 3.6+ |

## 代码示例

### 示例 1：线程安全单例模式 (元类实现)
实现一个真正的全局唯一实例，即便在高并发环境下也能保证安全。

```python
import threading
from typing import Any, Dict

class SingletonMeta(type):
    """
    线程安全的单例元类。
    """
    _instances: Dict[Any, Any] = {}
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        # 双重检查锁定 (Double-Checked Locking)
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    # 调用父类的 __call__ 来真正创建实例
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.connected = True

# 验证
db1 = DatabaseConnection()
db2 = DatabaseConnection()
assert db1 is db2
```

### 示例 2：描述符协议完整实现 (属性校验)
通过描述符实现对属性的类型和范围约束，且逻辑可复用。

```python
from typing import Any

class IntegerField:
    """
    数据描述符：强制要求属性为整数且在指定范围内。
    """
    def __init__(self, min_val: int = 0) -> None:
        self.min_val = min_val

    def __set_name__(self, owner: Any, name: str) -> None:
        # PEP 487 引入，自动获取属性名
        self.storage_name = f"_{name}"

    def __get__(self, instance: Any, owner: Any) -> Any:
        if instance is None:
            return self
        return getattr(instance, self.storage_name, None)

    def __set__(self, instance: Any, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"Expected int, got {type(value)}")
        if value < self.min_val:
            raise ValueError(f"Value must be >= {self.min_val}")
        setattr(instance, self.storage_name, value)

class Product:
    price = IntegerField(min_val=1)
    stock = IntegerField(min_val=0)

    def __init__(self, price: int, stock: int) -> None:
        self.price = price
        self.stock = stock

# 验证
p = Product(100, 50)
assert p.price == 100
```

### 示例 3：动态属性注册器 (元类进阶)
自动收集所有子类，常用于插件系统。

```python
from typing import Dict, Type

class PluginRegistry(type):
    registry: Dict[str, Type['BasePlugin']] = {}

    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)
        if name != "BasePlugin":
            mcs.registry[name.lower()] = cls
        return cls

class BasePlugin(metaclass=PluginRegistry):
    pass

class HttpPlugin(BasePlugin): pass
class SshPlugin(BasePlugin): pass

assert "httpplugin" in PluginRegistry.registry
```

## 性能基准测试
使用 `timeit` 对比普通属性访问与描述符访问的开销。

```python
import timeit

setup = """
class Normal:
    def __init__(self): self.val = 1
class Descriptor:
    def __init__(self, v): self.v = v
    def __get__(self, i, o): return self.v
class DescObj:
    val = Descriptor(1)
n = Normal()
d = DescObj()
"""

normal_time = timeit.timeit("n.val", setup=setup, number=1000000)
desc_time = timeit.timeit("d.val", setup=setup, number=1000000)
print(f"Normal access: {normal_time:.4f}s")
print(f"Descriptor access: {desc_time:.4f}s")
```

## 易错点与最佳实践
| 特性 | 常见陷阱 | 最佳实践 |
| :--- | :--- | :--- |
| **元类** | 在普通业务逻辑中滥用元类，导致代码极难维护。 | 优先使用类装饰器或 `__init_subclass__`，元类仅用于“改变类创建过程”。 |
| **描述符** | 在 `__get__` 中忘记处理 `instance is None` 的情况。 | 始终检查 `instance`，如果是类访问，返回描述符对象本身。 |
| **__new__** | 忘记调用 `super().__new__` 或返回错误的类型。 | 必须返回正确的实例对象，否则 `__init__` 不会被调用。 |

## Self-Check
1. 如何利用 `__set_name__` 避免在描述符中手动传入属性名？
2. 数据描述符和非数据描述符在属性查找顺序上有什么区别？
3. 为什么单例模式推荐在 `__new__` 中实现而不是 `__init__`？

## 参考链接
- [Expert Python Programming - Metaprogramming Section](https://example.com)
- [Fluent Python - Descriptors Chapter](https://example.com)

---
[版本记录](./metaprogramming_and_descriptors.md) | [返回首页](../README.md)
