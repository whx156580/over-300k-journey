---
title: 函数基础
module: testing
area: python_notes
stack: python
level: basics
status: active
tags: [python, function, scope, legb, kwargs]
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
- 函数用于封装可复用逻辑，是测试代码从脚本化迈向工程化的第一步。
- 理解参数传递和作用域，比记忆 `*args`、`**kwargs` 的符号本身更重要。
- 一个好函数应该有清晰输入、稳定输出和单一职责。

## 语法规则
- `def` 用于定义函数，`return` 决定返回值；未显式返回时默认返回 `None`。
- 作用域查找遵循 LEGB：Local、Enclosing、Global、Built-in。
- 默认参数在函数定义时求值，可变默认参数要格外小心。
- `*args` 接收额外位置参数，`**kwargs` 接收额外关键字参数。

## 代码示例
### 示例 1：默认参数与关键字参数

```python hl_lines="1 2"
def build_url(host: str, path: str = "/health", *, https: bool = True) -> str:
    scheme = "https" if https else "http"
    return f"{scheme}://{host}{path}"


print(build_url("example.com"))
print(build_url("localhost:8000", path="/docs", https=False))
```


### 示例 2：`*args` 与 `**kwargs`

```python hl_lines="1 4"
def collect(*args: int, **kwargs: str) -> tuple[int, dict[str, str]]:
    return sum(args), kwargs


total, meta = collect(1, 2, 3, env="test", owner="qa")
print(total)
print(meta["env"])
```


### 示例 3：LEGB 作用域

```python hl_lines="5 6 11 12"
label = "global"


def outer() -> str:
    label = "enclosing"

    def inner() -> str:
        return label

    return inner()


print(outer())
print(label)
```

## 易错点
- 把空列表、空字典当作默认参数，会让多次调用共享状态。
- 函数职责过多时，参数会越堆越多，最后很难测试、也很难复用。
- 滥用 `**kwargs` 会让函数边界不清晰，调用者也不容易知道真正需要哪些参数。

## 小练习
1. 写一个函数，接收主机名和路径，返回完整 URL，并支持关键字参数控制协议。
2. 写一个函数，接收任意数量的数字并返回总和。
3. 通过嵌套函数演示 LEGB 查找顺序。

完成后再对照“参考答案”和“Self-Check”复盘。

## Self-Check
### 概念题
1. LEGB 规则的四层作用域分别是什么？
2. 为什么可变默认参数容易出问题？
3. `*args` 和 `**kwargs` 各自适合什么场景？

### 编程题
1. 如何定义一个必须用关键字传入的参数？
2. 怎么重写一个带空列表默认参数的函数？

### 实战场景
1. 你在封装 HTTP 请求辅助函数时，想兼容额外 headers、timeout、params，签名该如何设计？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
Local、Enclosing、Global、Built-in。解释器会按这个顺序查找名称绑定。
讲解回看: [语法规则](#语法规则)

### 概念题 2
因为默认参数在函数定义时只求值一次，后续调用会共享同一个对象，导致状态泄漏。
讲解回看: [易错点](#易错点)

### 概念题 3
`*args` 适合位置参数数量不固定的场景，`**kwargs` 适合附加命名参数或配置透传场景，但要避免滥用。
讲解回看: [语法规则](#语法规则)

### 编程题 1
在函数签名中放一个 `*`，其后的参数都必须用关键字形式调用，例如 `def f(a, *, debug=False)`。
讲解回看: [代码示例](#代码示例)

### 编程题 2
把默认值改成 `None`，函数内部再写 `items = [] if items is None else items`，避免多次调用共享同一列表。
讲解回看: [易错点](#易错点)

### 实战场景 1
优先显式声明核心参数，再用少量关键字参数补充扩展项。只有在透传第三方 SDK 参数时，才谨慎使用 `**kwargs`。
讲解回看: [概念](#概念)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-16: 初版整理，补齐示例、自测题与落地建议。

---
[返回 Python 学习总览](../README.md)
