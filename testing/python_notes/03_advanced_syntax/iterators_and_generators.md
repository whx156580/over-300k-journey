---
title: 迭代器、生成器与 yield/send/throw/close
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, iterator, generator, yield, coroutine]
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
- 迭代器协议让对象可以被 `for` 循环消费；生成器用更轻量的方式实现惰性计算。
- `yield` 会暂停函数执行并保留上下文，下一次继续时从暂停点恢复。
- `send`、`throw`、`close` 让生成器不只是“产出数据”，还具备协作式控制能力。

## 核心机制
- 可迭代对象实现 `__iter__`，迭代器还需要实现 `__next__`。
- 生成器函数一旦包含 `yield`，调用时不会立即执行函数体，而是返回生成器对象。
- `send(value)` 把值送回上一个 `yield` 表达式，首次启动时只能 `send(None)`。
- `throw(exc)` 会在生成器暂停点抛出异常；`close()` 会触发 `GeneratorExit` 并终止迭代。

## 代码示例
### 示例 1：自定义迭代器

```python hl_lines="6 8 11"
class CountDown:
    def __init__(self, start: int) -> None:
        self.current = start

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


print(list(CountDown(3)))
```


### 示例 2：`yield` 与 `send`

```python hl_lines="4 5 9 10 11"
def accumulator():
    total = 0
    while True:
        number = yield total
        total += 0 if number is None else number


gen = accumulator()
print(next(gen))
print(gen.send(3))
print(gen.send(5))
gen.close()
```


### 示例 3：`throw` 与异常处理

```python hl_lines="2 4 9"
def receiver():
    try:
        yield "ready"
    except ValueError:
        yield "recovered"


gen = receiver()
print(next(gen))
print(gen.throw(ValueError("boom")))
```

## 易错点
- 把生成器当作列表反复消费，第二次通常什么都拿不到，因为它已经被耗尽。
- 首次对生成器调用 `send(非 None)` 会报错，因为生成器还没有运行到第一个 `yield`。
- 自定义迭代器如果忘记在结束时抛 `StopIteration`，就会写出错误的无限迭代。

## 小练习
1. 实现一个每次产出平方数的生成器，支持上限控制。
2. 写一个生成器，接收外部发送的数并累计总和。
3. 把一个列表包装成自定义迭代器，只遍历其中的偶数项。


建议先手写一遍，再对照“参考答案”检查抽象边界是否清晰。

## Self-Check
### 概念题
1. 可迭代对象和迭代器的区别是什么？
2. `yield` 和 `return` 在函数里最大的语义差别是什么？
3. 为什么 `send()` 常被说成是“协作式”的？

### 编程题
1. 怎样安全地启动一个支持 `send()` 的生成器？
2. 如何把生成器里的资源释放动作写得更稳妥？

### 实战场景
1. 日志流很大，不能一次性全部读入内存，应该优先考虑列表还是生成器？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
可迭代对象能返回迭代器，迭代器本身还负责通过 `__next__` 一个个产出元素。不是所有可迭代对象都是迭代器。
讲解回看: [核心机制](#核心机制)

### 概念题 2
`return` 会结束函数并返回结果，`yield` 会暂停函数、保留现场，并在后续继续恢复执行。
讲解回看: [概念](#概念)

### 概念题 3
因为调用方和生成器之间会在 `yield` 位置来回切换控制权，调用方能把数据送回生成器，生成器再决定如何继续处理。
讲解回看: [核心机制](#核心机制)

### 编程题 1
先调用 `next(gen)` 或 `gen.send(None)`，把执行流推进到第一个 `yield` 位置，然后再发送真实值。
讲解回看: [代码示例](#代码示例)

### 编程题 2
在消费结束后调用 `close()`，或者在生成器内部配合 `try/finally` 处理清理逻辑，确保提早退出时也能释放资源。
讲解回看: [易错点](#易错点)

### 实战场景 1
优先考虑生成器。它按需产出数据，内存占用更稳定，尤其适合大文件、流式接口和分批处理场景。
讲解回看: [概念](#概念)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-16: 初版整理，补齐示例、自测题与落地建议。

---
[返回 Python 学习总览](../README.md)
