---
title: pytest-asyncio 与性质测试入门
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, pytest, asyncio, hypothesis, property-based-testing]
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
- 同步测试会覆盖很多逻辑，但一旦项目里出现协程函数、异步客户端和并发流程，普通 pytest 用法就不够了。
- 性质测试则解决另一类问题：不是拿几组固定样例去验证，而是验证某个不变量在一批输入下始终成立。
- 对从业者来说，这两类测试能补足“异步逻辑难测”和“边界样例想不全”的短板。

## 学什么
- `pytest-asyncio` 主要解决协程测试函数如何在事件循环里运行。
- 性质测试的核心是先定义不变量，再用工具或批量输入去打它，而不是手工穷举有限样例。
- 这两类测试都强调“把行为边界说清楚”，而不是单纯堆更多 case。

## 怎么用
### 示例 1：先用 `asyncio.run()` 理解异步测试目标

```python hl_lines="4 8"
import asyncio


async def normalize_name(value: str) -> str:
    await asyncio.sleep(0)
    return value.strip().lower()


result = asyncio.run(normalize_name("  Alice  "))
print(result)
```


### 示例 2：用批量输入表达一个最小不变量

```python hl_lines="4 5"
def reverse_twice(text: str) -> str:
    return text[::-1][::-1]


samples = ["a", "abc", "测试", ""]
print(all(reverse_twice(item) == item for item in samples))
```


### 示例 3：可选导入 Hypothesis

```python hl_lines="1 6"
try:
    import hypothesis  # noqa: F401
except ImportError:
    hypothesis = None


print(hypothesis is None or hypothesis is not None)
```


落地建议:
- 异步测试先把协程边界和事件循环边界搞清楚，再谈 fixture 和并发组合。
- 性质测试最关键的是选对不变量，例如“排序后长度不变”“反转两次等于原值”“解析后再序列化仍可对齐”。
- 不要把性质测试理解成“随机测更多”；它更像是系统化表达边界规律。

## 业界案例
- 异步 HTTP 客户端、消息消费和后台协程任务都很适合接入异步测试能力。
- 解析器、转换器、序列化 / 反序列化函数很适合做性质测试，因为它们通常存在明显不变量。
- 很多边界 bug 不是固定样例测不出来，而是你根本没想到那类输入；性质测试正好能补这一层。

## 延伸阅读
- 如果项目已有大量异步逻辑，建议继续补 `pytest-asyncio` 的 fixture、事件循环隔离和超时控制。
- 如果想把性质测试真正落地，下一步要学的是如何设计高价值不变量，而不是只会安装 Hypothesis。
- 性质测试适合和传统样例测试一起使用，而不是完全替代样例测试。

## Self-Check
### 概念题
1. `pytest-asyncio` 主要补的是哪类测试能力？
2. 性质测试和普通样例测试最大的区别是什么？
3. 为什么说不变量设计比“随机生成更多数据”更重要？

### 编程题
1. 如何用最小方式运行并验证一个协程函数？
2. 如何给“反转两次等于原值”写一个批量输入校验？

### 实战场景
1. 你们有一个异步接口客户端，还经常因为特殊输入导致解析函数出错，你会怎样组合异步测试和性质测试？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
主要补协程测试函数如何运行、等待和验证这一层能力。
讲解回看: [学什么](#学什么)

### 概念题 2
样例测试验证少量固定输入输出，性质测试更关注某个规律或不变量在一批输入下是否成立。
讲解回看: [为什么学](#为什么学)

### 概念题 3
因为如果不变量本身没定义清楚，哪怕生成再多输入，也可能只是重复验证无关行为。
讲解回看: [落地建议](#怎么用)

### 编程题 1
可以先用 `asyncio.run(coro())` 运行协程并断言结果，理解测试目标后再迁移到 `pytest-asyncio`。
讲解回看: [代码示例](#代码示例)

### 编程题 2
可以先准备一组样本，再用 `all(reverse_twice(x) == x for x in samples)` 做最小不变量验证。
讲解回看: [代码示例](#代码示例)

### 实战场景 1
异步客户端行为用异步测试覆盖；纯转换 / 解析函数的边界不变量用性质测试补齐，两者搭配最稳。
讲解回看: [业界案例](#业界案例)

## 参考链接
- [pytest-asyncio 文档](https://pytest-asyncio.readthedocs.io/)
- [Hypothesis 文档](https://hypothesis.readthedocs.io/)
- [pytest 文档](https://docs.pytest.org/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-17: 新增“pytest-asyncio 与性质测试入门”，补齐异步测试与边界性质验证能力。

---
[返回 Python 学习总览](../README.md)
