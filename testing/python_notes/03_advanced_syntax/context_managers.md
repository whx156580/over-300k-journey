---
title: 上下文管理器
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, context-manager, with, contextlib, resource]
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
- `with` 语句用于把“获取资源”和“释放资源”绑定到一个清晰边界里。
- 文件、锁、数据库连接、临时目录、网络会话都非常适合用上下文管理器表达。
- 上下文管理器让资源释放变成结构化能力，而不是靠人记得手动 `close()`。

## 核心机制
- 实现了 `__enter__` 和 `__exit__` 的对象可以配合 `with` 使用。
- `__enter__` 返回要绑定给 `as` 后变量的对象。
- `__exit__` 会在退出时被调用，无论代码块正常结束还是发生异常。
- `contextlib.contextmanager` 能把生成器快速封装为上下文管理器，适合轻量场景。

## 代码示例
### 示例 1：自定义类实现 `with`

```python hl_lines="2 6 10"
class Recorder:
    def __enter__(self):
        self.messages = ["open"]
        return self

    def __exit__(self, exc_type, exc, tb):
        self.messages.append("close")
        return False


with Recorder() as recorder:
    recorder.messages.append("working")

print(recorder.messages)
```


### 示例 2：`contextlib.contextmanager`

```python hl_lines="4 7 8 11"
from contextlib import contextmanager


@contextmanager
def managed_flag():
    state = {"opened": True}
    try:
        yield state
    finally:
        state["opened"] = False


with managed_flag() as flag:
    print(flag["opened"])
```


### 示例 3：异常情况下仍然释放资源

```python hl_lines="6 12 16"
class SafeCleanup:
    def __enter__(self):
        self.cleaned = False
        return self

    def __exit__(self, exc_type, exc, tb):
        self.cleaned = True
        return False


cleanup = None
try:
    with SafeCleanup() as cleanup:
        raise RuntimeError("boom")
except RuntimeError:
    pass

print(cleanup.cleaned)
```

## 易错点
- `__exit__` 返回 `True` 会吞掉异常，如果你只是想做清理但不想隐藏错误，应该返回 `False` 或 `None`。
- 手写上下文管理器时忘记释放资源，等于只用了 `with` 的语法，没得到它的价值。
- 用生成器实现上下文管理器时，`yield` 前后代码的职责要清晰：前半段负责准备，后半段负责清理。

## 小练习
1. 写一个上下文管理器，进入时打印 `start`，退出时打印 `end`。
2. 用 `contextmanager` 封装一个临时配置开关。
3. 模拟一个带异常的代码块，验证 `__exit__` 仍会执行。


建议先手写一遍，再对照“参考答案”检查抽象边界是否清晰。

## Self-Check
### 概念题
1. `with` 语句想解决的核心问题是什么？
2. `__enter__` 和 `__exit__` 分别负责什么？
3. 什么情况下 `contextlib.contextmanager` 比类更合适？

### 编程题
1. 如何确保异常发生时也能执行清理逻辑？
2. 为什么很多文件读写示例都推荐 `with open(...) as f`？

### 实战场景
1. 你在接口测试里需要临时创建一批测试数据，测试结束必须回收，应该怎样组织代码？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
它解决的是资源生命周期管理问题：什么时候拿到资源，什么时候一定释放，异常发生时是否还能保证清理动作执行。
讲解回看: [概念](#概念)

### 概念题 2
`__enter__` 负责准备并返回上下文对象，`__exit__` 负责退出清理，并决定是否吞掉异常。
讲解回看: [核心机制](#核心机制)

### 概念题 3
当上下文逻辑简单、状态不多时，用生成器包装会更轻便；如果需要更多方法和复杂状态，类实现通常更清晰。
讲解回看: [核心机制](#核心机制)

### 编程题 1
在类实现里把清理写进 `__exit__`，在生成器实现里把清理写进 `finally`。这两种方式都能覆盖异常退出路径。
讲解回看: [代码示例](#代码示例)

### 编程题 2
因为它能保证文件句柄在作用域结束后及时关闭，避免忘记 `close()` 或异常导致资源泄漏。
讲解回看: [概念](#概念)

### 实战场景 1
可以把“创建数据”和“回收数据”封装进上下文管理器，在 `with` 块里执行业务断言。这样无论断言是否失败，回收逻辑都能执行。
讲解回看: [概念](#概念)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-16: 初版整理，补齐示例、自测题与落地建议。

---
[返回 Python 学习总览](../README.md)
