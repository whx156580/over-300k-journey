---
title: 面向对象
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, oop, property, slots, mro]
updated: 2026-04-16
---

## 目录
- [概念](#概念)
- [核心机制](#核心机制)
- [代码示例](#代码示例)
- [易错点](#易错点)
- [小练习](#小练习)
- [Self-Check](#Self-Check)
- [参考答案](#参考答案)
- [参考链接](#参考链接)
- [版本记录](#版本记录)

## 概念
- 面向对象的关键不只是“有类和对象”，而是通过封装、继承、多态组织复杂状态与行为。
- 在 Python 里，类变量、实例变量、属性、描述符、MRO 等机制共同决定对象行为。
- 测试工程常用 OOP 封装页面对象、接口客户端、测试数据模型和资源句柄。

## 核心机制
- 类变量属于类本身，实例变量属于对象实例，两者查找路径不同。
- `property` 让你用属性访问语法包装校验或计算逻辑。
- `__slots__` 可限制实例可绑定属性，减少拼写错误和内存开销。
- 继承、多态和 MRO 决定方法覆盖与查找顺序；抽象基类 `abc` 可约束子类接口。

## 代码示例
### 示例 1：类变量、实例变量与 `property`

```python hl_lines="2 5 8 13"
class TestUser:
    role = "viewer"

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self._age = age

    @property
    def age(self) -> int:
        return self._age


user = TestUser("alice", 18)
print(TestUser.role, user.age)
```


### 示例 2：`__slots__` 与继承

```python hl_lines="2 8 11"
class Device:
    __slots__ = ("name",)

    def __init__(self, name: str) -> None:
        self.name = name


class Phone(Device):
    __slots__ = ("platform",)

    def __init__(self, name: str, platform: str) -> None:
        super().__init__(name)
        self.platform = platform


phone = Phone("pixel", "android")
print(phone.name, phone.platform)
```


### 示例 3：多态、MRO 与抽象基类

```python hl_lines="4 5 9 14 15"
from abc import ABC, abstractmethod


class Reporter(ABC):
    @abstractmethod
    def render(self) -> str:
        raise NotImplementedError


class JsonReporter(Reporter):
    def render(self) -> str:
        return '{"status": "ok"}'


reporter = JsonReporter()
print(reporter.render())
print(JsonReporter.mro()[0].__name__)
```

## 易错点
- 把可变类变量当作实例状态使用，常会导致多个对象意外共享同一份数据。
- `property` 里隐藏太多副作用会让调用者误以为只是读属性，结果触发网络请求或昂贵计算。
- 继承层级过深会让 MRO 和覆盖关系变得难懂，很多时候组合比继承更稳妥。

## 小练习
1. 设计一个 `PageObject` 基类，并让两个页面子类分别实现 `open()` 方法。
2. 用 `property` 给年龄字段加上非负校验。
3. 写一个抽象基类约束不同报告生成器都实现 `render()` 方法。


建议先手写一遍，再对照“参考答案”检查抽象边界是否清晰。

## Self-Check
### 概念题
1. 类变量和实例变量的查找顺序有什么差异？
2. `property` 为什么能提升封装性？
3. MRO 在多继承下解决了什么问题？

### 编程题
1. 如何让子类必须实现某个方法？
2. `__slots__` 能帮你防止哪类错误？

### 实战场景
1. 在自动化测试框架里，什么时候适合用继承，什么时候更适合组合？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
访问实例属性时会先找实例字典，再回溯到类；类变量定义在类上，会被所有实例共享，除非实例上显式覆盖同名属性。
讲解回看: [核心机制](#核心机制)

### 概念题 2
它允许你保留属性访问语法，同时在读取或写入时插入校验、计算和保护逻辑，不需要暴露显式 getter/setter。
讲解回看: [核心机制](#核心机制)

### 概念题 3
它定义了方法查找顺序，避免解释器在多继承图里不知道该先调用哪个父类实现。
讲解回看: [核心机制](#核心机制)

### 编程题 1
使用 `abc.ABC` 和 `@abstractmethod`。未实现抽象方法的子类将不能被实例化。
讲解回看: [代码示例](#代码示例)

### 编程题 2
它能限制实例可绑定的属性名，减少拼写错误导致的“悄悄加出一个新属性”的问题，同时也可能降低内存占用。
讲解回看: [代码示例](#代码示例)

### 实战场景 1
当多个对象共享稳定接口和少量共同实现时可用继承；当能力模块彼此独立、组合关系频繁变化时，用组合通常更清晰、更容易测试。
讲解回看: [易错点](#易错点)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-16: 初版整理，补齐示例、自测题与落地建议。

---
[返回 Python 学习总览](../README.md)
