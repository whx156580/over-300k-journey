---
title: 使用 Ragas 建立 RAG 评测基础
module: testing
area: ai-eval
stack: ragas
level: basics
status: active
tags: [ragas, ai-eval, rag, faithfulness, context-recall]
updated: 2026-04-16
---

## 1. 背景
- **问题场景**: RAG 系统上线后，团队常常只能凭感觉判断回答“好不好”，缺少稳定、可复现的评测闭环。
- **学习目标**: 理解 Ragas 在 RAG 评测中的角色，并知道从哪些核心指标开始搭建第一版评测集。
- **前置知识**: 了解 LLM、Embedding、向量检索、RAG 基本工作流。

## 2. 核心结论
- RAG 评测不能只看最终答案，要同时关注检索质量和生成质量。
- Ragas 的价值在于把主观体验转成一组可重复运行的评测指标。
- 第一版评测通常优先关注 `faithfulness`、`answer relevancy`、`context recall`。
- 没有高质量评测样本，再好的指标体系也会失真。

## 3. 原理拆解
- **关键概念**: RAG 评测通常拆成问题、检索上下文、模型回答、标准答案或参考事实。
- **运行机制**: 把样本数据整理成评测集后，Ragas 会基于指标函数对输出进行批量评估并产出分数。
- **图示说明**: 一个最基础的 RAG 评测闭环是“构造样本 -> 执行问答 -> 计算指标 -> 迭代系统”。

```mermaid
flowchart LR
    A["构造测试集"] --> B["运行 RAG 问答"]
    B --> C["计算评测指标"]
    C --> D["分析弱点"]
    D --> E["优化检索 / 生成"]
```

## 4. 实战步骤

### 4.1 环境准备
- 依赖版本: Python 3.9+、`ragas`、可选的 `datasets`
- 安装命令:

```bash
pip install ragas datasets
```

### 4.2 核心代码

```python
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_recall


dataset = Dataset.from_dict(
    {
        "question": ["什么是回归测试？"],
        "answer": ["回归测试用于确认已有功能在变更后仍然正常工作。"],
        "contexts": [["回归测试用于验证变更未破坏已有功能。"]],
        "ground_truth": ["回归测试用于验证系统变更后既有功能仍然正确。"],
    }
)

result = evaluate(
    dataset=dataset,
    metrics=[faithfulness, answer_relevancy, context_recall],
)

print(result)
```

### 4.3 如何验证
- 本地运行命令: 在具备依赖与模型配置的环境中运行评测脚本。
- 预期结果: 输出每个指标的分数，并能发现是“检索召回不足”还是“回答偏离上下文”。
- 失败时重点检查: 数据集字段名、上下文格式、模型依赖与 API 配置是否正确。

```bash
python rag_eval.py
```

## 5. 项目实践建议
- **适用场景**: 企业知识库问答、客服问答、内部助手、文档检索增强问答。
- **不适用场景**: 没有真实问题样本、没有业务口径、只想做一次性演示的阶段。
- **落地建议**: 先沉淀一小批高质量黄金样本，再逐渐扩展到更完整的评测基准集。
- **与其他方案对比**: 与纯人工抽样相比，Ragas 更适合持续集成、版本对比和批量回归。

## 6. 踩坑记录
- **常见问题**: 把低质量测试集拿来做模型优劣判断。
- **错误现象**: 分数变化很大，但团队无法从中得出可信结论。
- **定位方式**: 回看样本问题是否真实、标准答案是否明确、上下文是否足够代表业务。
- **解决方案**: 先修测试集质量，再解读模型分数；评测体系和测试数据要一起演进。

## 7. 面试高频 Q&A
### Q1: 为什么 RAG 评测不能只看最终答案是否“像是对的”？
### A1:
因为“看起来对”不代表可追溯、可稳定复现。RAG 系统既可能检索错，也可能生成时幻觉，必须把问题拆开评估。

### Q2: `faithfulness` 和 `context recall` 分别在解决什么问题？
### A2:
`faithfulness` 更关注回答是否忠于上下文，`context recall` 更关注检索阶段是否把需要的信息找回来了。

## 8. 延伸阅读
- [Ragas Introduction](https://docs.ragas.io/)
- [Ragas Get Started](https://docs.ragas.io/en/stable/getstarted/)
- [Ragas Quick Start](https://docs.ragas.io/en/stable/getstarted/quickstart/)

## 9. 关联内容
- 相关笔记: [AI 模型与评测 README](../../README.md)
- 相关代码: [ragas 目录](../)
- 相关测试: 后续可在 `projects/` 中补 RAG 回归评测脚本

---
[返回首页](../../../../README.md)
