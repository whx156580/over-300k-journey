---
title: 变量与数据类型
module: testing
area: python_notes
stack: python
level: basics
status: active
tags: [python, variables, types, identity, annotations]
updated: 2026-04-16
---

## 目录
- [概念](#概念)
- [语法规则](#语法规则)
- [代码示例](#代码示例)
- [易错点](#易错点)
- [小练习](#小练习)
- [Self-Check](#Self-Check)
- [参考答案](#参考答案)
- [参考链接](#参考链接)
- [版本记录](#版本记录)

## 概念
- Python 是动态类型语言，变量名绑定的是对象引用，不是提前声明好的内存槽位。
- “强类型”表示不会在运行时偷偷把 `"1"` 当作数字 `1` 用；类型不匹配时会明确抛错。
- 类型标注主要服务于阅读、补全和静态检查，不会在运行时自动替你做类型转换。

## 语法规则
- 给变量赋值时，左边是名字，右边是对象；重新赋值本质上是让名字指向另一个对象。
- `==` 比较值是否相等，`is` 比较是否是同一个对象，判断 `None` 时优先使用 `is None`。
- 常见内置类型包括 `int`、`float`、`bool`、`str`、`list`、`tuple`、`dict`、`set`。
- 类型标注写法常见为 `name: str = "alice"`，函数签名可写成 `def add(a: int, b: int) -> int:`。

## 代码示例
### 示例 1：动态类型与类型标注

```python hl_lines="1 4"
age: int = 28
nickname = "qa_runner"
is_active = True

print(type(age).__name__, type(nickname).__name__, type(is_active).__name__)
```

示例要点:
- 第 1 行展示变量注解。
- 第 4 行验证运行时真实类型。

### 示例 2：`is` 与 `==`

```python hl_lines="5 6 7"
left = [1, 2, 3]
right = [1, 2, 3]
alias = left

print(left == right)
print(left is right)
print(left is alias)
```

示例要点:
- 第 5 行比较值。
- 第 6 至 7 行比较对象身份。

### 示例 3：`None` 判断

```python hl_lines="2 3"
def format_user(name: str | None) -> str:
    if name is None:
        return "anonymous"
    return name.strip().lower()


print(format_user(None))
print(format_user("  Alice  "))
```

## 易错点
- 把 `is` 当作通用相等比较符，结果在列表、字典、长字符串上得到错误结论。
- 误以为类型标注会自动帮你转换类型；实际上传入字符串仍然会在业务逻辑里爆错。
- 在调试时只看变量名、不看 `type()` 和 `id()`，很容易把“值相同”和“对象相同”混为一谈。

## 小练习
1. 定义一个函数，接收 `str | None`，输入 `None` 时返回默认用户名，其他情况返回去除空白后的结果。
2. 创建两个值相同但不是同一对象的列表，分别打印 `==` 和 `is` 的结果。
3. 用类型标注定义一个 `dict[str, int]`，统计测试结果中 `passed` 与 `failed` 的数量。

完成后再对照“参考答案”和“Self-Check”复盘。

## Self-Check
### 概念题
1. 为什么说 Python 既是动态类型语言，又是强类型语言？
2. `is` 与 `==` 应该分别在什么场景下使用？
3. 类型标注在团队协作中最大的价值是什么？

### 编程题
1. 写一个函数，传入 `None` 返回 `"guest"`，否则返回小写用户名。
2. 怎样打印两个变量是否指向同一个对象？

### 实战场景
1. 接口测试里从 JSON 里取到的 `id` 有时是字符串、有时是整数，应该如何处理？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
动态类型指变量不需要预先声明类型，运行时再绑定对象；强类型指类型不兼容时不会悄悄转换，而是显式报错。
讲解回看: [概念](#概念)

### 概念题 2
`==` 用于比较值是否相等，`is` 用于判断是否是同一个对象。判断 `None`、单例对象时优先使用 `is`。
讲解回看: [语法规则](#语法规则)

### 概念题 3
它提升可读性、补全质量和静态检查能力，让函数边界更清楚，尤其适合多人维护的测试代码和工具脚本。
讲解回看: [概念](#概念)

### 编程题 1
可以参考示例 3：在函数入口用 `if name is None` 处理空值，其他情况对字符串做 `strip().lower()` 再返回。
讲解回看: [代码示例](#代码示例)

### 编程题 2
直接打印 `a is b`。如果还要进一步排查，可配合 `id(a)` 和 `id(b)` 观察内存身份标识。
讲解回看: [代码示例](#代码示例)

### 实战场景 1
不要依赖隐式转换。应在解析边界统一做类型归一化，例如通过显式转换、类型校验或 Pydantic 模型约束，再把内部使用类型固定下来。
讲解回看: [易错点](#易错点)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-16: 初版整理，补齐示例、自测题与落地建议。

---
[返回 Python 学习总览](../README.md)
