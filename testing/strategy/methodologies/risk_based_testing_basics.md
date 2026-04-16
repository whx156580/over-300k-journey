---
title: 基于风险的测试方法基础
module: testing
area: strategy
stack: methodologies
level: basics
status: active
tags: [testing-strategy, risk-based-testing, prioritization, quality]
updated: 2026-04-16
---

## 1. 背景
- **问题场景**: 时间、人力和环境都有限时，团队不可能对所有功能投入同样的测试强度。
- **学习目标**: 掌握基于风险安排测试优先级的基本思路，避免把有限资源平均摊薄。
- **前置知识**: 了解测试分层、需求分析、缺陷分级和基本项目流程。

## 2. 核心结论
- 风险越高的功能，越应该优先投入更深的测试。
- 风险一般由“影响度”和“发生概率”共同决定。
- 测试策略的本质不是追求全测，而是在约束下做更高价值的覆盖。
- 风险评估需要和产品、开发、测试共同完成，不能只靠测试单方判断。

## 3. 原理拆解
- **关键概念**: 影响度衡量问题发生后的业务损失，发生概率衡量缺陷出现的可能性。
- **运行机制**: 给业务功能打风险分，再依据风险等级分配测试类型、测试深度和回归频率。
- **图示说明**: 一个常见方法是用“影响度 x 概率”的矩阵做优先级分层。

```mermaid
flowchart LR
    A["识别功能模块"] --> B["评估影响度"]
    B --> C["评估发生概率"]
    C --> D["计算风险等级"]
    D --> E["制定测试优先级"]
```

## 4. 实战步骤

### 4.1 环境准备
- 依赖版本: 无强制技术依赖
- 安装命令: 无

```bash
echo "Risk based testing starts from requirement analysis"
```

### 4.2 核心代码

```python
def risk_score(impact: int, probability: int) -> int:
    return impact * probability


features = [
    {"name": "支付", "impact": 5, "probability": 4},
    {"name": "个人资料编辑", "impact": 2, "probability": 3},
]

for feature in features:
    feature["score"] = risk_score(feature["impact"], feature["probability"])

print(sorted(features, key=lambda item: item["score"], reverse=True))
```

### 4.3 如何验证
- 本地运行命令: 用任何 Python 环境执行上面的示意代码即可。
- 预期结果: 高风险模块排在前面，并对应更高优先级的测试投入。
- 失败时重点检查: 风险输入值是否和真实业务一致，评估标准是否统一。

```bash
python risk_model.py
```

## 5. 项目实践建议
- **适用场景**: 迭代节奏快、核心链路清晰、测试资源有限的研发团队。
- **不适用场景**: 对安全、合规、金融级高风险场景做“只测高分项”的极端简化。
- **落地建议**: 把风险评估结果直接映射到测试计划，例如 P0 做单测 + 集成 + E2E，P2 只做冒烟。
- **与其他方案对比**: 与平均分配测试精力相比，风险驱动策略更贴近真实业务价值。

## 6. 踩坑记录
- **常见问题**: 风险评分只看技术难度，不看真实业务影响。
- **错误现象**: 团队把大量精力花在低价值功能，关键链路反而覆盖不够。
- **定位方式**: 回看线上事故、投诉、交易损失、核心转化链路和历史缺陷分布。
- **解决方案**: 用业务损失、用户规模、变更频率、依赖复杂度共同评估风险。

## 7. 面试高频 Q&A
### Q1: 为什么说测试策略不是“测得越多越好”？
### A1:
因为测试资源永远有限。真正成熟的测试策略，是把有限资源投到最可能出问题、且出问题代价最大的地方。

### Q2: 风险高的模块一定只做自动化吗？
### A2:
不一定。高风险模块通常需要多层测试协同，包括评审、单测、接口测试、E2E、监控和灰度验证，而不只是某一种自动化手段。

## 8. 延伸阅读
- [ISTQB Foundation Level Overview](https://www.istqb.org/)
- [Google Testing Blog](https://testing.googleblog.com/)
- [Testing Strategy 文档](../test_strategy.md)

## 9. 关联内容
- 相关笔记: [全链路测试策略与计划](../test_strategy.md)
- 相关代码: [test_unit_salary.py](../tests/test_unit_salary.py)
- 相关测试: 可继续扩展到 `quality-gates/` 与 `metrics/`

---
[返回首页](../../../README.md)
