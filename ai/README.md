# 🤖 AI 开发模块

> 这里承接 Prompt、RAG、Agent、MLOps 和数据集工程相关知识，并接入统一模板、自动汇总与搜索体系。

---

## 导航入口

- 自动汇总首页: [knowledge_hub.md](../common/docs/indexes/knowledge_hub.md)
- 搜索入口: `python scripts/search_knowledge.py <关键词> --module ai`
- 写作模板: [template.md](../common/docs/template.md)

---

## 模块索引

| 知识域 | 入口 | 已收录内容 |
| :--- | :--- | :--- |
| LLM 与 Agent | [llm-agent/README.md](./llm-agent/README.md) | Prompt 设计基础 |
| MLOps | [mlops/README.md](./mlops/README.md) | 模型部署流水线基础 |
| 数据集工程 | [dataset/README.md](./dataset/README.md) | 数据集清洗基础 |

---

## 如何继续补内容

1. 在对应目录创建带元数据的 `.md` 笔记。
2. 运行 `python scripts/build_knowledge_index.py` 更新汇总页。
3. 使用 `python scripts/search_knowledge.py prompt --module ai` 验证检索结果。

---
[返回首页](../README.md)
