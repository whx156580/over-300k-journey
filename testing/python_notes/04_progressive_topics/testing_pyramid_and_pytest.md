---
title: 测试金字塔、pytest fixture、参数化与 CI
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, pytest, testing, mock, coverage]
updated: 2026-04-16
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
- 测试工程不是堆更多用例，而是让不同层级的测试承担正确职责。
- 理解测试金字塔能帮助你决定哪些能力放在单元测试、哪些放在集成测试、哪些再上升到 UI 或端到端层。
- Pytest 之所以流行，不只是语法简洁，还因为 fixture、参数化、mock 和插件生态足够成熟。

## 学什么
- 金字塔强调底层测试多、上层测试少且精，避免把所有成本都压到 UI 回归上。
- Pytest 核心能力包括 fixture、参数化、marker、mock、覆盖率统计和与 CI 的无缝集成。
- 好的测试不止“能跑”，还要稳定、可维护、反馈快、失败信息清晰。

## 怎么用
### 示例 1：fixture 与参数化

```python hl_lines="4 8 11"
import pytest


@pytest.fixture
def base_url() -> str:
    return "https://example.com"


@pytest.mark.parametrize(
    "path, expected",
    [("/health", 200), ("/docs", 200)],
)
def test_endpoint_meta(base_url: str, path: str, expected: int) -> None:
    assert expected == 200
    assert path.startswith("/")
    assert base_url.startswith("https://")
```


### 示例 2：mock

```python hl_lines="4 6"
from unittest.mock import Mock

notifier = Mock()
notifier.send.return_value = True

result = notifier.send("done")
print(result, notifier.send.call_count)
```


### 示例 3：GitHub Actions 片段

```yaml
name: python-tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt
      - run: pytest --cov
```


落地建议:
- 单元测试覆盖纯逻辑和边界条件，集成测试覆盖模块协作，UI 测试覆盖关键主流程。
- fixture 用来管理共享上下文，避免复制初始化代码。
- 覆盖率只是护栏，不是目标；别为了数字写无意义断言。

## 业界案例
- 中后台系统常把大部分校验下沉到单元和接口层，只保留少量关键 UI 冒烟。
- CI 流水线通常在 PR 阶段运行单元与快速集成测试，在夜间任务中补跑重型回归。
- Mock 适合隔离邮件、短信、第三方回调等不稳定外部依赖。

## 延伸阅读
- [pytest 文档](https://docs.pytest.org/)
- [unittest.mock 文档](https://docs.python.org/3/library/unittest.mock.html)
- [coverage.py 文档](https://coverage.readthedocs.io/)

## Self-Check
### 概念题
1. 测试金字塔想解决的核心问题是什么？
2. fixture 为什么是 Pytest 的核心能力？
3. 为什么覆盖率不能替代测试质量？

### 编程题
1. 怎样把同一条断言逻辑在多组数据上重复执行？
2. 什么时候应该优先使用 mock？

### 实战场景
1. 团队的 UI 回归越来越慢、越来越不稳定，应该怎么按金字塔思路调整？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
它想解决“测试越往上越昂贵、越脆弱”的问题，鼓励把大部分验证放在反馈更快、维护成本更低的底层测试中。
讲解回看: [为什么学](#为什么学)

### 概念题 2
因为它能把测试准备和清理逻辑复用起来，既减少重复，也让依赖关系通过函数签名显式呈现。
讲解回看: [学什么](#学什么)

### 概念题 3
因为覆盖率只说明代码被执行过，不说明断言是否有价值，也不说明关键业务路径是否被正确验证。
讲解回看: [怎么用](#怎么用)

### 编程题 1
使用 `@pytest.mark.parametrize`。它能让测试数据显式列在装饰器里，失败时也更容易定位是哪组参数出问题。
讲解回看: [怎么用](#怎么用)

### 编程题 2
当测试目标是当前模块自身逻辑，而外部依赖会让测试变慢、不稳定或难以构造时，优先用 mock 隔离边界。
讲解回看: [怎么用](#怎么用)

### 实战场景 1
先把可下沉的校验迁到单元和接口层，把 UI 层缩成关键主路径验证；同时梳理 fixture、数据构造和并行执行，减少上层测试的冗余与脆弱点。
讲解回看: [业界案例](#业界案例)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-16: 初版整理，补齐示例、自测题与落地建议。

---
[返回 Python 学习总览](../README.md)
