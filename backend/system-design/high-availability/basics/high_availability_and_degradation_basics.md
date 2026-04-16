---
title: 高可用与降级设计基础
module: backend
area: system-design
stack: high-availability
level: basics
status: active
tags: [backend, system-design, high-availability, degradation, resilience]
updated: 2026-04-16
---

## 1. 背景
- **问题场景**: 真正的高并发系统不可能永远不出错，关键在于故障发生时系统是否还能以可接受方式继续服务。
- **学习目标**: 理解高可用的核心目标，以及限流、降级、熔断这些机制为什么重要。
- **前置知识**: 了解基本服务调用链、超时和资源限制概念。

## 2. 核心结论
- 高可用的目标不是“绝不失败”，而是“失败时可控、可恢复、影响可隔离”。
- 降级是为了保住核心能力，而不是追求全部功能同时可用。
- 限流、超时、熔断、隔离通常要配套使用。
- 高可用设计必须结合监控和演练，否则只是纸面方案。

## 3. 原理拆解
- **关键概念**: 降级是在资源不足或依赖异常时主动关闭次要能力，保护核心路径。
- **运行机制**: 当系统检测到延迟升高、错误率上升或下游不可用时，触发保护策略以降低系统负载。
- **图示说明**: 高可用设计核心是“检测风险 -> 触发保护 -> 保住核心路径”。

```mermaid
flowchart LR
    A["系统异常征兆"] --> B["限流 / 超时 / 熔断"]
    B --> C["关闭次要能力"]
    C --> D["保住核心服务"]
```

## 4. 实战步骤

### 4.1 环境准备
- 依赖版本: 无固定工具要求，可配合网关、服务框架和监控系统
- 安装命令: 无

```bash
echo "Design graceful degradation before incidents happen"
```

### 4.2 核心代码

```python
def query_homepage():
    if system_load_high():
        return {
            "banner": [],
            "recommendations": [],
            "core_feed": get_core_feed(),
        }
    return build_full_homepage()
```

### 4.3 如何验证
- 本地运行命令: 无统一命令，通常结合压测、演练或故障注入。
- 预期结果: 异常时核心能力可继续服务，非核心能力被主动降级。
- 失败时重点检查: 降级开关是否可控、核心链路是否被正确识别、保护策略是否真的生效。

```bash
python ha_demo.py
```

## 5. 项目实践建议
- **适用场景**: 首页、下单、支付、登录、消息等核心业务链路。
- **不适用场景**: 极小型单体演示项目，但即便如此也值得建立基本意识。
- **落地建议**: 明确划分核心能力和非核心能力，并提前设计降级路径。
- **与其他方案对比**: 与“系统全量可用”幻想相比，分级服务更符合真实生产环境。

## 6. 踩坑记录
- **常见问题**: 没有定义核心链路，故障时所有功能一起拖垮。
- **错误现象**: 一个次要依赖异常，整条主流程都不可用。
- **定位方式**: 回看调用链和依赖图，找出是否存在关键路径被弱依赖拖死的问题。
- **解决方案**: 做依赖分级、流量隔离和降级演练。

## 7. 面试高频 Q&A
### Q1: 高可用为什么不等于“系统永不出错”？
### A1:
因为真实系统总会遇到故障。高可用更关注的是故障发生时系统能否控制影响范围并快速恢复。

### Q2: 降级的本质是什么？
### A2:
本质是在资源有限或异常情况下，主动放弃次要能力，保护核心价值链路。

## 8. 延伸阅读
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- [Release It!](https://pragprog.com/titles/mnee2/release-it-second-edition/)
- [Martin Fowler - Circuit Breaker](https://martinfowler.com/bliki/CircuitBreaker.html)

## 9. 关联内容
- 相关笔记: 后续可补 `advanced/` 中的熔断与隔离策略
- 相关代码: [high-availability 目录](../README.md)
- 相关测试: 可结合性能与混沌测试补故障演练

---
[返回首页](../../../../README.md)
