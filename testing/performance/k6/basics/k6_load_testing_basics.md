---
title: 使用 k6 建立性能测试基础模型
module: testing
area: performance
stack: k6
level: basics
status: active
tags: [k6, performance-testing, load-testing, threshold]
updated: 2026-04-16
---

## 1. 背景
- **问题场景**: 功能测试通过不代表系统在高并发下稳定，接口可能在流量上升后出现响应抖动、错误率升高或资源耗尽。
- **学习目标**: 了解 k6 压测脚本的核心结构，并能建立最基本的用户模型与阈值门禁。
- **前置知识**: 了解 HTTP、并发、响应时间、P95 和错误率等基本指标。

## 2. 核心结论
- 性能测试不是“把流量打上去”这么简单，而是要先定义场景、指标和判定标准。
- k6 脚本最核心的是 `options`、虚拟用户模型和 `thresholds`。
- 如果没有阈值，性能测试很容易沦为“有图但无结论”。
- 从单接口基线压测开始，比一上来做复杂全链路压测更有效。

## 3. 原理拆解
- **关键概念**: VU 表示虚拟用户，`duration` 表示持续时间，`thresholds` 表示验收门禁。
- **运行机制**: k6 根据脚本中的用户模型发起请求，收集响应时间、吞吐、错误率等指标，再用阈值判断是否达标。
- **图示说明**: 一个基础压测链路可以抽象成“场景定义 -> 流量施压 -> 指标采集 -> 阈值判断”。

```mermaid
flowchart LR
    A["定义场景"] --> B["施加并发流量"]
    B --> C["采集性能指标"]
    C --> D["阈值判断"]
    D --> E["输出结论"]
```

## 4. 实战步骤

### 4.1 环境准备
- 依赖版本: k6 CLI
- 安装命令: 参考官方文档安装对应平台版本

```bash
k6 version
```

### 4.2 核心代码

```javascript
import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  vus: 10,
  duration: "30s",
  thresholds: {
    http_req_failed: ["rate<0.01"],
    http_req_duration: ["p(95)<500"],
  },
};

export default function () {
  const response = http.get("https://quickpizza.grafana.com");

  check(response, {
    "status is 200": (r) => r.status === 200,
  });

  sleep(1);
}
```

### 4.3 如何验证
- 本地运行命令: `k6 run script.js`
- 预期结果: 错误率和响应时间都满足阈值。
- 失败时重点检查: 目标服务可达性、压测环境网络、脚本中阈值是否合理。

```bash
k6 run script.js
```

## 5. 项目实践建议
- **适用场景**: 接口基线压测、版本前回归压测、容量预估前的单场景验证。
- **不适用场景**: 没有明确业务目标、没有目标环境、没有指标基线时的盲目压测。
- **落地建议**: 每个压测脚本都写清楚目标 QPS、用户模型、关键阈值和结论口径。
- **与其他方案对比**: 与只看平均响应时间相比，P95/P99 更能发现尾延迟问题。

## 6. 踩坑记录
- **常见问题**: 把测试机或本地网络瓶颈误判为服务端性能问题。
- **错误现象**: 同一脚本在不同机器差异很大，结果无法复现。
- **定位方式**: 检查压测机 CPU、网络出口、DNS、连接池、环境隔离情况。
- **解决方案**: 先建立稳定基线环境，再逐步扩展到更复杂的压测模型。

## 7. 面试高频 Q&A
### Q1: 为什么性能测试必须定义阈值？
### A1:
没有阈值就只有数据没有结论。阈值把“看起来还行”转成“能不能上线”的明确判断标准。

### Q2: 为什么经常看 P95 而不是平均值？
### A2:
平均值容易掩盖尾部慢请求，而真实用户更容易感知到的是高分位延迟带来的卡顿和超时。

## 8. 延伸阅读
- [Grafana k6 文档](https://grafana.com/docs/k6/latest/)
- [k6 Get Started](https://grafana.com/docs/k6/latest/get-started/)
- [Write your first k6 test](https://grafana.com/docs/k6/latest/get-started/write-your-first-test/)

## 9. 关联内容
- 相关笔记: [全链路测试策略与计划](../../../strategy/test_strategy.md)
- 相关代码: [k6 目录](../)
- 相关测试: [test_api_contracts.py](../../../api/pytest/test_api_contracts.py)

---
[返回首页](../../../../README.md)
