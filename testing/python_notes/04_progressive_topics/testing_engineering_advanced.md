---
title: 测试工程进阶：conftest、分层、flaky 与契约测试
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, pytest, conftest, flaky, contract-testing]
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
- 会写 pytest 用例只是起点，真正的测试工程问题通常出在目录分层、fixture 边界、数据构造、flaky 测试和团队协作约定。
- 当项目规模上来以后，测试痛点很少是“不会断言”，更多是“慢、不稳、难排障、难维护”。
- 这一主题的目标，是把测试从“能跑”推进到“可维护、可协作、可定位问题”。

## 学什么
- `conftest.py` 用于共享 fixture 和测试基础设施，但边界不清会带来隐式依赖和调试困难。
- 测试分层的重点不是建更多目录，而是让单元、接口、集成、UI 各自承担稳定职责。
- flaky 测试要从根因治理，包括时间依赖、共享状态、并发竞争、外部依赖和数据污染。
- 契约测试适合用来验证调用方和提供方在字段、类型、状态码和错误码上的稳定边界。

## 怎么用
### 示例 1：把共享上下文收敛到 fixture

```python hl_lines="4 8 11"
import pytest


@pytest.fixture(scope="session")
def settings() -> dict:
    return {"base_url": "https://example.com", "env": "test"}


def build_headers(config: dict) -> dict:
    return {"X-Env": config["env"]}


print(build_headers({"env": "test"})["X-Env"])
```


### 示例 2：用简单检查表达最小契约

```python hl_lines="2 6 7"
response = {"id": 1, "name": "smoke", "status": "passed"}
required_fields = {"id", "name", "status"}

print(required_fields.issubset(response))
assert isinstance(response["id"], int)
assert response["status"] in {"passed", "failed"}
```


### 示例 3：先识别 flaky 测试常见信号

```toml
[tool.pytest.ini_options]
markers = [
  "contract: contract level checks",
  "slow: long running tests",
]
addopts = "-q -ra"
```


落地建议:
- `conftest.py` 里只放真正共享且稳定的 fixture，避免把整个项目的测试魔法都塞进去。
- 优先治理 flaky 根因，而不是简单靠重跑掩盖问题。
- 契约测试最适合放在接口层，帮助你在 UI 测试之前更早发现字段和协议漂移。

## 业界案例
- 很多团队的 pytest 仓库前期跑得还行，后期越来越慢，往往不是因为测试“变多了”，而是 fixture 范围太大、数据构造太重、外部依赖没隔离。
- flaky 测试最常见的来源是共享测试账号、时间窗口判断、异步任务未完成就断言，以及测试之间状态污染。
- 契约测试在多服务协作里很有价值，因为它能在联调和上线前更早暴露字段变化和错误码不一致。

## 延伸阅读
- 如果一个测试项目必须靠“重跑三次”才能稳定通过，问题通常不是偶然，而是工程设计没处理好不确定性。
- fixture 不是越多越高级，真正有价值的是边界清晰、依赖可见、初始化成本可控。
- 契约测试不是替代集成测试，而是把一部分接口稳定性验证前移。

## Self-Check
### 概念题
1. 为什么 `conftest.py` 既方便又容易失控？
2. flaky 测试最常见的根因有哪些？
3. 契约测试和普通接口断言的价值差异是什么？

### 编程题
1. 什么样的共享上下文适合提成 fixture，什么样的不适合？
2. 如何为响应对象设计一个最小契约检查？

### 实战场景
1. 团队的 pytest 仓库越来越慢、偶发失败越来越多，你会先从目录分层、fixture、测试数据和外部依赖中的哪几处下手？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
因为它能减少重复，但也容易把依赖藏起来；一旦共享逻辑过重，排障和理解成本都会变高。
讲解回看: [学什么](#学什么)

### 概念题 2
时间依赖、共享状态、外部依赖不稳定、异步完成时机不确定、测试数据污染和并发竞争都很常见。
讲解回看: [业界案例](#业界案例)

### 概念题 3
普通接口断言更像单次验证，契约测试更强调“字段、类型、状态码、错误码这些边界是否持续稳定”。
讲解回看: [为什么学](#为什么学)

### 编程题 1
共享且稳定、初始化成本可控、跨多用例复用的上下文适合提成 fixture；强业务耦合或副作用过重的逻辑不适合。
讲解回看: [怎么用](#怎么用)

### 编程题 2
先定义必填字段集合，再检查类型、枚举值和关键状态码，这样比只断言某一个字段更接近契约思路。
讲解回看: [怎么用](#怎么用)

### 实战场景 1
先定位最重的 fixture 和最不稳定的用例，再拆共享状态、压缩外部依赖、补分层与契约检查，最后再谈并行和重跑策略。
讲解回看: [落地建议](#怎么用)

## 参考链接
- [pytest fixtures 文档](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [pytest good practices](https://docs.pytest.org/en/stable/explanation/goodpractices.html)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-17: 初版整理，补充测试工程进阶主题骨架与最小示例。

---
[返回 Python 学习总览](../README.md)
