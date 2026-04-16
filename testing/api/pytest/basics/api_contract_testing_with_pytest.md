---
title: 使用 Pytest 做接口契约测试基础
module: testing
area: api
stack: pytest
level: basics
status: active
tags: [pytest, api-testing, contract-testing, requests]
updated: 2026-04-16
---

## 1. 背景
- **问题场景**: 后端接口即使状态码是 200，也可能返回字段缺失、字段类型变化或语义不兼容。
- **学习目标**: 建立“状态码 + 字段结构 + 关键业务约束”三层接口校验意识。
- **前置知识**: 了解 HTTP、JSON、Pytest 基础夹具与断言。

## 2. 核心结论
- 接口测试不能只断言 `status_code == 200`，还要校验字段、类型和关键业务语义。
- 契约测试关注的是“调用双方约定是否被破坏”，不是只验证单次请求是否成功。
- 把接口返回抽象成稳定契约，比写大量脆弱的字符串比较更可维护。
- 使用 `fixture`、`monkeypatch` 和数据工厂能明显提升测试可读性与扩展性。

## 3. 原理拆解
- **关键概念**: 契约测试关注输入输出约定，包括字段是否存在、字段类型、默认值和关键业务边界。
- **运行机制**: 由测试用例构造请求或模拟响应，再用断言验证接口契约是否满足预期。
- **图示说明**: 一个稳定的接口契约测试通常围绕“请求 -> 响应 -> 契约校验”展开。

```mermaid
flowchart LR
    A["构造请求 / Mock 响应"] --> B["调用接口"]
    B --> C["校验状态码"]
    C --> D["校验字段结构"]
    D --> E["校验业务语义"]
```

## 4. 实战步骤

### 4.1 环境准备
- 依赖版本: Python 3.9+、`pytest`、`requests`
- 安装命令:

```bash
pip install pytest requests
```

### 4.2 核心代码

```python
import pytest


def validate_salary_contract(payload: dict) -> None:
    assert "status" in payload
    assert payload["status"] == "success"
    assert "data" in payload
    assert "job_title" in payload["data"]
    assert "salary_min" in payload["data"]
    assert isinstance(payload["data"]["salary_min"], int)
    assert payload["data"]["salary_min"] >= 0


@pytest.mark.integration
def test_salary_contract(mock_api_response):
    payload = mock_api_response.json()
    validate_salary_contract(payload)
```

### 4.3 如何验证
- 本地运行命令: `pytest testing/api/pytest/test_api_contracts.py -q`
- 预期结果: 契约字段和业务边界全部满足断言。
- 失败时重点检查: 字段命名是否变更、字段类型是否漂移、Mock 数据是否过于理想化。

```bash
pytest testing/api/pytest/test_api_contracts.py -q
```

## 5. 项目实践建议
- **适用场景**: 微服务接口、内部中台接口、第三方 API 接入校验。
- **不适用场景**: 只想验证 SDK 封装逻辑、而不是接口契约本身的场景。
- **落地建议**: 把契约校验函数独立出来，避免断言散落在各个测试中。
- **与其他方案对比**: 与只做状态码校验相比，契约测试更能提前发现“静默兼容性破坏”。

## 6. 踩坑记录
- **常见问题**: Mock 数据太理想，无法覆盖真实异常场景。
- **错误现象**: 测试总是通过，但线上接口字段一改就大量报错。
- **定位方式**: 对照真实返回样本、线上日志或 OpenAPI 定义比对字段差异。
- **解决方案**: 增加边界样本、异常样本、兼容性样本，不只测 Happy Path。

## 7. 面试高频 Q&A
### Q1: 契约测试和接口功能测试有什么差异？
### A1:
功能测试更关注业务流程是否正确，契约测试更关注服务边界是否稳定。前者偏业务结果，后者偏服务协作协议。

### Q2: 为什么只断言状态码不够？
### A2:
因为很多兼容性问题不会体现在状态码上。字段缺失、类型变更、默认值改变，都可能让调用方崩掉，但接口仍然返回 200。

## 8. 延伸阅读
- [pytest Getting Started](https://docs.pytest.org/en/stable/getting-started.html)
- [Requests Documentation](https://requests.readthedocs.io/)
- [OpenAPI Specification](https://swagger.io/specification/)

## 9. 关联内容
- 相关笔记: [全链路测试策略与计划](../../../strategy/test_strategy.md)
- 相关代码: [test_api_contracts.py](../test_api_contracts.py)
- 相关测试: [test_unit_salary.py](../../../strategy/tests/test_unit_salary.py)

---
[返回首页](../../../../README.md)
