---
title: Python 常见坑位清单
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, pitfalls, defaults, late-binding, imports, truthiness]
updated: 2026-04-17
---

## 目录
- [为什么学](#为什么学)
- [学什么](#学什么)
- [怎么用](#怎么用)
- [业界案例](#业界案例)
- [延伸阅读](#延伸阅读)
- [Self-Check](#Self-Check)
- [参考答案](#参考答案)
- [参考链接](#参考链接)
- [版本记录](#版本记录)

## 为什么学
- 很多 Python 问题不是不会写，而是会在“看起来很像对的代码”里埋坑。
- 这类坑位最伤人的地方在于它们往往不会立刻报错，而是等到多人协作、重复调用或边界数据进来时才暴露。
- 把常见坑位收成一份清单，可以显著减少重复踩坑和排障时间。

## 学什么
- 高发坑位通常集中在可变默认参数、闭包晚绑定、导入副作用、真假值判断和宽泛异常处理。
- 很多问题的根因不是语法不懂，而是对象模型、作用域和执行时机理解不够。
- 真正有用的清单不是只列坑，还要给出“什么时候应该警觉、该怎么规避”。

## 怎么用
### 示例 1：可变默认参数

```python hl_lines="1 7"
def add_case(name: str, bucket=None):
    bucket = [] if bucket is None else bucket
    bucket.append(name)
    return bucket


left = add_case("login")
right = add_case("order")
print(left, right)
```


### 示例 2：闭包晚绑定

```python hl_lines="2 6"
handlers = []
for name in ("a", "b", "c"):
    handlers.append(lambda value=name: value)

print([handler() for handler in handlers])
```


### 示例 3：真假值判断与宽泛异常

```python hl_lines="2 7"
payload = {"retry": 0}
retry = payload.get("retry")

if retry is None:
    print("missing")
else:
    print(retry)

try:
    int("3")
except ValueError:
    print("value error handled")
```


排查清单:
- 函数参数里是否出现了 `[]`、`{}` 这类可变默认值？
- 循环里创建的闭包是否绑定了最终变量，而不是当前变量快照？
- `if not value` 到底是在判断缺失、空字符串、0，还是三者全混在一起？
- `except Exception` 是真的需要兜底，还是把可定位的问题吞掉了？

## 业界案例
- 测试数据工厂最容易因为共享默认列表而互相污染，最后表现成“为什么后一个用例带上了前一个标签”。
- 循环注册回调或任务时，闭包晚绑定常让所有处理函数最后都拿到同一个变量值。
- 接口响应里 `0`、空字符串和 `None` 混用时，如果只写 `if not x`，很容易把“值为 0”误判成“字段缺失”。

## 延伸阅读
- 很多坑位其实都能追溯到两个问题：对象是否共享、变量何时绑定。
- 最稳的规避方式通常不是记更多技巧，而是把边界表达得更显式，例如判空用 `is None`、默认值用 `None` + 内部初始化。
- 这类清单最适合和 code review 一起使用，因为很多坑自己写时不容易察觉。

## Self-Check
### 概念题
1. 为什么 Python 的很多坑会“先运行一阵再出问题”？
2. 可变默认参数和闭包晚绑定各自对应什么执行时机问题？
3. 为什么 `if not value` 有时不够精确？

### 编程题
1. 如何重写一个带空列表默认参数的函数？
2. 如何在循环里安全创建多个返回当前变量值的 lambda？

### 实战场景
1. 你在 code review 里看到一个测试辅助函数写成 `def f(data=[]): ...`，你会怎么解释风险并给出替代写法？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
因为这些坑很多都不是语法错误，而是对象共享、变量绑定或判断条件表达不清的问题，要到特定调用顺序或边界输入下才会暴露。
讲解回看: [为什么学](#为什么学)

### 概念题 2
可变默认参数对应“函数定义时只求值一次”，闭包晚绑定对应“闭包读取变量时拿到的是最终绑定值”。
讲解回看: [学什么](#学什么)

### 概念题 3
因为它会把 `None`、`0`、空字符串、空列表都当成假值；有些场景你其实只想判断其中一种。
讲解回看: [排查清单](#怎么用)

### 编程题 1
把默认值改成 `None`，函数内部再显式初始化，例如 `bucket = [] if bucket is None else bucket`。
讲解回看: [代码示例](#代码示例)

### 编程题 2
可以用默认参数冻结当前值，例如 `lambda value=name: value`。
讲解回看: [代码示例](#代码示例)

### 实战场景 1
我会说明默认列表只会创建一次，多个调用会共享状态；更稳的写法是 `data=None`，函数内部再创建新列表。
讲解回看: [排查清单](#怎么用)

## 参考链接
- [Python 常见问题 FAQ](https://docs.python.org/3/faq/programming.html)
- [Python 官方教程](https://docs.python.org/3/tutorial/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-17: 新增“Python 常见坑位清单”，补齐初学者和进阶同学都高频遇到的执行时机与边界陷阱。

---
[返回 Python 学习总览](../README.md)
