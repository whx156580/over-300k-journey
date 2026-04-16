---
title: RAG 黄金测试集构建方法
module: testing
area: ai-eval
stack: ragas
level: advanced
status: active
tags: [ragas, ai-eval, rag, dataset, benchmark, testset]
updated: 2026-04-16
---

## 1. 背景
- **问题场景**: 没有高质量测试集时，RAG 评测分数很难指导真正的系统优化。
- **学习目标**: 建立黄金测试集的构建思路，让评测从临时抽样变成长期基准。
- **前置知识**: 了解 RAG 结构、问答样本、标注流程和基础数据治理。

## 2. 核心结论
- 黄金测试集比评测框架本身更重要，它决定了评测是否可信。
- 好的测试集要覆盖高频问题、长尾问题、歧义问题和风险问题。
- 数据集建设是持续过程，不是一次性产物。
- 测试集必须能反映真实用户问题，而不是只体现标注者想象中的问题。

## 3. 原理拆解
- **关键概念**: 黄金测试集通常包含问题、标准答案、标准证据、标签和难度信息。
- **运行机制**: 通过收集真实问题、清洗聚类、定义标注规则、双人复核等步骤沉淀基准集。
- **图示说明**: 测试集建设是一条“收集 -> 筛选 -> 标注 -> 复核 -> 持续迭代”的流水线。

```mermaid
flowchart LR
    A["收集真实问题"] --> B["清洗与去重"]
    B --> C["标注答案与证据"]
    C --> D["复核与质检"]
    D --> E["形成基准集"]
    E --> F["持续补样本"]
```

## 4. 实战步骤

### 4.1 环境准备
- 依赖版本: 无强制工具，可结合 Python、表格或标注平台
- 安装命令: 无

```bash
echo "Build benchmark from real user questions"
```

### 4.2 核心代码

```python
sample = {
    "question": "退款申请多久处理完成？",
    "ground_truth": "标准退款申请会在 3 个工作日内处理完成。",
    "gold_contexts": ["退款流程规定：标准退款申请在 3 个工作日内完成处理。"],
    "tags": ["refund", "sla", "faq"],
    "difficulty": "medium",
}
```

### 4.3 如何验证
- 本地运行命令: 无统一命令，建议周期性抽样复核。
- 预期结果: 不同标注者对同一问题能得到相近结论，评测结果能稳定反映系统变化。
- 失败时重点检查: 问题是否真实、答案是否唯一、证据是否明确、标签口径是否一致。

```bash
python review_testset.py
```

## 5. 项目实践建议
- **适用场景**: 需要长期优化和回归评测的 RAG / Agent 系统。
- **不适用场景**: 一次性 Demo、没有真实用户问题来源的临时原型。
- **落地建议**: 给测试集加标签体系，例如业务域、难度、风险等级、问题类型。
- **与其他方案对比**: 与随机抽样相比，黄金测试集更适合版本对比和长期质量治理。

## 6. 踩坑记录
- **常见问题**: 测试集只覆盖高频 FAQ，没有覆盖复杂推理或歧义问题。
- **错误现象**: 系统在评测集上表现很好，但真实用户依然抱怨多。
- **定位方式**: 对照线上问题分布，检查测试集是否过度理想化。
- **解决方案**: 测试集要同时覆盖简单题、复杂题、长尾题和风险题。

## 7. 面试高频 Q&A
### Q1: 为什么说测试集质量比指标本身更重要？
### A1:
因为指标只能基于样本计算。如果样本不真实、不完整或标注口径不一致，再漂亮的分数也没有指导意义。

### Q2: 黄金测试集需要不断更新吗？
### A2:
需要。业务文档、用户问题和系统能力都在变化，测试集如果不演进，很快就会失去代表性。

## 8. 延伸阅读
- [Ragas Testset Concepts](https://docs.ragas.io/en/stable/concepts/test_data/)
- [Ragas Documentation](https://docs.ragas.io/)
- [Google ML Test Score](https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/)

## 9. 关联内容
- 相关笔记: [RAG 检索阶段指标设计](./rag_retrieval_metric_design.md)
- 相关代码: [Ragas README](../README.md)
- 相关测试: 后续可在 `projects/` 中补测试集版本管理方案

---
[返回首页](../../../../README.md)
