---
title: 使用 Pytest 做 OpenAPI Schema 校验
module: testing
area: api
stack: pytest
level: advanced
status: active
tags: [pytest, api-testing, openapi, schema, contract]
updated: 2026-04-16
---

## 1. 背景
- **问题场景**: 接口变更频繁时，团队容易漏掉字段类型变化、字段删改和响应结构不兼容问题。
- **学习目标**: 学会把 OpenAPI / Schema 定义变成可执行校验，减少人工比对成本。
- **前置知识**: 了解 OpenAPI、JSON Schema 和基础接口测试。

## 2. 核心结论
- Schema 校验是契约测试的工程化升级版，能把结构校验标准化。
- 它擅长发现结构不兼容，但不能代替业务断言。
- 最好的实践是“Schema 校验 + 关键业务字段断言”组合使用。
- 契约文档如果不和实际实现同步，测试也会失真。

## 3. 原理拆解
- **关键概念**: Schema 定义描述接口允许返回的字段结构、类型和约束。
- **运行机制**: 测试调用接口后，把真实响应与约定 Schema 比对，不匹配就失败。
- **图示说明**: 结构校验相当于在响应数据和接口契约之间做一次自动比对。

```mermaid
flowchart LR
    A["发送接口请求"] --> B["获取真实响应"]
    B --> C["加载 OpenAPI / Schema"]
    C --> D["执行结构校验"]
    D --> E["补充业务断言"]
```

## 4. 实战步骤

### 4.1 环境准备
- 依赖版本: Python 3.9+、`pytest`、`jsonschema`
- 安装命令:

```bash
pip install pytest jsonschema requests
```

### 4.2 核心代码

```python
from jsonschema import validate


salary_schema = {
    "type": "object",
    "properties": {
        "status": {"type": "string"},
        "data": {
            "type": "object",
            "properties": {
                "job_title": {"type": "string"},
                "salary_min": {"type": "integer"},
            },
            "required": ["job_title", "salary_min"],
        },
    },
    "required": ["status", "data"],
}


def test_salary_schema(mock_api_response):
    payload = mock_api_response.json()
    validate(instance=payload, schema=salary_schema)
    assert payload["data"]["salary_min"] >= 0
```

### 4.3 如何验证
- 本地运行命令: `pytest testing/api/pytest/test_api_contracts.py -q`
- 预期结果: 结构变化会被 Schema 校验捕获，业务边界异常会被显式断言捕获。
- 失败时重点检查: Schema 是否和文档一致、Mock 是否贴近真实返回、兼容字段是否需要允许可选。

```bash
pytest testing/api/pytest/test_api_contracts.py -q
```

## 5. 项目实践建议
- **适用场景**: 中台接口、开放平台接口、多人协作的服务边界治理。
- **不适用场景**: 没有稳定契约文档、接口处于高频试验期的阶段。
- **落地建议**: 将 OpenAPI 文档版本化，并在流水线中触发兼容性校验。
- **与其他方案对比**: 与手写大量字段断言相比，Schema 更标准化；但它不如手工业务断言理解业务语义。

## 6. 踩坑记录
- **常见问题**: 只依赖 Schema，不补业务语义断言。
- **错误现象**: 结构完全合法，但业务结果明显错误，测试仍然通过。
- **定位方式**: 区分“结构不兼容”和“业务不正确”两类失败。
- **解决方案**: 对核心业务字段补业务约束，例如金额范围、状态枚举、分页逻辑。

## 7. 面试高频 Q&A
### Q1: Schema 校验和普通接口断言相比，优势是什么？
### A1:
优势在于结构规则可复用、可规模化、适合团队统一约束，不用在每个测试里重复写一堆字段存在性判断。

### Q2: 为什么 Schema 校验不能替代业务断言？
### A2:
因为它主要验证“格式是否对”，而业务断言验证的是“含义是否对”。两者关注点不同。

## 8. 延伸阅读
- [Pytest Documentation](https://docs.pytest.org/)
- [JSON Schema Documentation](https://python-jsonschema.readthedocs.io/)
- [OpenAPI Specification](https://swagger.io/specification/)

## 9. 关联内容
- 相关笔记: [使用 Pytest 做接口契约测试基础](../basics/api_contract_testing_with_pytest.md)
- 相关代码: [test_api_contracts.py](../test_api_contracts.py)
- 相关测试: 后续可在 `projects/` 中补 OpenAPI 驱动回归

---
[返回首页](../../../../README.md)
