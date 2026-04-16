---
title: k6 阶梯加压与场景建模
module: testing
area: performance
stack: k6
level: advanced
status: active
tags: [k6, performance-testing, scenario, stages, workload]
updated: 2026-04-16
---

## 1. 背景
- **问题场景**: 真实业务流量很少是恒定不变的，单一 `vus + duration` 只能覆盖最基础的压测模型。
- **学习目标**: 学会把业务流量拆成预热、爬坡、稳态、峰值等阶段，并映射到 k6 场景里。
- **前置知识**: 理解吞吐、并发、响应时间以及 k6 基础脚本结构。

## 2. 核心结论
- 阶梯加压比固定并发更接近真实流量变化。
- 场景建模要围绕业务目标，而不是工具参数本身。
- 稳态压测和峰值压测关注的问题不同，不能混成一个结果看。
- 一个好的性能脚本，首先是一份清晰的流量模型说明。

## 3. 原理拆解
- **关键概念**: `stages` 用于描述并发随时间变化，`scenarios` 用于表达不同类型用户或不同请求模式。
- **运行机制**: k6 按配置逐阶段调整虚拟用户数量，并分别统计阶段过程中的性能指标。
- **图示说明**: 常见压测模型会经历预热、爬坡、稳态和回落几个阶段。

```mermaid
flowchart LR
    A["预热"] --> B["爬坡"]
    B --> C["稳态压测"]
    C --> D["峰值冲击"]
    D --> E["回落观察"]
```

## 4. 实战步骤

### 4.1 环境准备
- 依赖版本: k6 CLI
- 安装命令: 参考官方安装方式

```bash
k6 version
```

### 4.2 核心代码

```javascript
import http from "k6/http";

export const options = {
  stages: [
    { duration: "1m", target: 20 },
    { duration: "3m", target: 80 },
    { duration: "5m", target: 80 },
    { duration: "1m", target: 150 },
    { duration: "1m", target: 0 },
  ],
};

export default function () {
  http.get("https://quickpizza.grafana.com");
}
```

### 4.3 如何验证
- 本地运行命令: `k6 run script.js`
- 预期结果: 图表中能看到并发变化对应的响应时间和错误率变化。
- 失败时重点检查: 阶段设计是否与业务实际接近、压测机是否足够支撑、目标环境是否稳定。

```bash
k6 run script.js
```

## 5. 项目实践建议
- **适用场景**: 大促预演、活动秒杀、工作日高峰模拟、日常基线回归。
- **不适用场景**: 目标不明确，只想“压一下看看”的模糊测试。
- **落地建议**: 每个脚本都明确写出阶段含义，不要只留下数字。
- **与其他方案对比**: 与单一恒定并发相比，阶梯模型更适合观察系统拐点和瓶颈暴露时机。

## 6. 踩坑记录
- **常见问题**: 一次脚本混入过多目标，既想测稳态又想测极限。
- **错误现象**: 压测结果很热闹，但无法回答具体问题。
- **定位方式**: 回到测试目标，看脚本是否能回答“系统在什么负载下开始退化”。
- **解决方案**: 把稳态、峰值、容量、破坏性测试拆成不同脚本与不同报告。

## 7. 面试高频 Q&A
### Q1: 为什么固定并发模型不够？
### A1:
因为真实业务流量通常是变化的。固定并发更适合基础基线，阶梯模型更适合观察系统在负载变化过程中的行为。

### Q2: 性能测试里的“场景建模”本质是什么？
### A2:
本质是把真实业务流量、用户行为和系统目标翻译成可执行、可解释的负载模型。

## 8. 延伸阅读
- [k6 Scenarios](https://grafana.com/docs/k6/latest/using-k6/scenarios/)
- [k6 Stages](https://grafana.com/docs/k6/latest/using-k6/k6-options/reference/#stages)
- [k6 Executors](https://grafana.com/docs/k6/latest/using-k6/scenarios/executors/)

## 9. 关联内容
- 相关笔记: [使用 k6 建立性能测试基础模型](../basics/k6_load_testing_basics.md)
- 相关代码: [k6 README](../README.md)
- 相关测试: 后续可在 `projects/` 中补多场景组合压测

---
[返回首页](../../../../README.md)
