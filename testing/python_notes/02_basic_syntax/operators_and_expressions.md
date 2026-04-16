---
title: 运算符与表达式
module: testing
area: python_notes
stack: python
level: basics
status: active
tags: [python, operators, expressions, comparison, bitwise]
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
- 表达式是会产生值的代码片段，运算符决定这些值如何组合与计算。
- 理解优先级、结合性和短路逻辑，比记忆所有符号本身更重要。
- 位运算在权限标记、状态位、二进制协议解析中很常见，测试工程里也会遇到。

## 语法规则
- 算术、比较、逻辑和位运算都能出现在同一个表达式中，但复杂表达式建议加括号增强可读性。
- 链式比较 `a < b < c` 会按数学语义求值，中间值只求一次。
- `and`、`or` 具有短路特性，左侧已经足够决定结果时，右侧不会执行。
- `&`、`|`、`^`、`~`、`<<`、`>>` 作用于整数的二进制位，不要与 `and`、`or` 混用。

## 代码示例
### 示例 1：链式比较

```python hl_lines="2"
score = 85
result = 60 <= score < 90
print(result)
```


### 示例 2：短路逻辑

```python hl_lines="6 7"
def expensive_check() -> bool:
    print("expensive_check called")
    return True


print(False and expensive_check())
print(True or expensive_check())
```

观察结果:
- 这段代码不会打印 `expensive_check called`，因为两次都被短路了。

### 示例 3：位运算

```python hl_lines="5 7 8"
READ = 0b001
WRITE = 0b010
EXECUTE = 0b100

permission = READ | WRITE
print(permission)
print(permission & WRITE == WRITE)
print(permission & EXECUTE == EXECUTE)
```

## 易错点
- 把 `&` 当成逻辑与使用，尤其在布尔表达式里会让代码读起来非常危险。
- 链式比较里夹带副作用函数虽然能运行，但会降低可读性，排查起来也困难。
- 依赖 `and/or` 返回布尔值时容易踩坑，因为它们返回的是“最后一个被求值的对象”，不一定是 `True/False`。

## 小练习
1. 写一个表达式，判断温度是否处于 `[18, 26)` 区间。
2. 定义 `ADMIN = 0b1000`、`EDITOR = 0b0100`，计算同时拥有两个权限的结果。
3. 写一个函数，只有当 `debug` 为 `True` 时才调用代价较高的诊断函数。

完成后再对照“参考答案”和“Self-Check”复盘。

## Self-Check
### 概念题
1. 什么是链式比较，它和 `a < b and b < c` 有什么差异？
2. `and`、`or` 的短路机制有什么价值？
3. 位运算最典型的工程用途是什么？

### 编程题
1. 如何判断一个整数权限集中是否包含 `WRITE` 位？
2. 怎样写一个不会触发昂贵函数调用的布尔判断？

### 实战场景
1. 日志分析脚本里有一个 `parse()` 很慢，只在文件存在时才需要调用，表达式该怎么写？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
链式比较写成 `a < b < c`，语义更接近数学表达式，而且中间值只求一次，可读性通常也更好。
讲解回看: [语法规则](#语法规则)

### 概念题 2
它可以避免不必要的计算，也常用于“前置条件通过后再执行昂贵逻辑”的场景，比如对象判空和延迟调用。
讲解回看: [代码示例](#代码示例)

### 概念题 3
它常用于权限标记、状态位组合、协议解析、硬件寄存器控制等需要紧凑表达多个开关状态的场景。
讲解回看: [概念](#概念)

### 编程题 1
使用按位与：`permission & WRITE == WRITE`。先取交集，再判断目标位是否完整保留。
讲解回看: [代码示例](#代码示例)

### 编程题 2
把廉价条件写在左侧，例如 `debug and expensive_check()`。当 `debug` 为 `False` 时，右侧不会执行。
讲解回看: [代码示例](#代码示例)

### 实战场景 1
可写成 `path.exists() and parse(path)`。这样文件不存在时就不会进入解析逻辑，同时表达式仍然保持简洁。
讲解回看: [易错点](#易错点)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-16: 初版整理，补齐示例、自测题与落地建议。

---
[返回 Python 学习总览](../README.md)
