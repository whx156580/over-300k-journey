# 🎨 前端开发模块

> 这里承接前端框架、工程化和性能优化三大知识域，并接入统一模板、自动汇总与搜索体系。

---

## 导航入口

- 自动汇总首页: [knowledge_hub.md](../common/docs/indexes/knowledge_hub.md)
- 搜索入口: `python scripts/search_knowledge.py <关键词> --module frontend`
- 写作模板: [template.md](../common/docs/template.md)

---

## 模块索引

| 知识域 | 入口 | 已收录内容 |
| :--- | :--- | :--- |
| 框架 | [frameworks/README.md](./frameworks/README.md) | React 状态提升与组件通信基础 |
| 工程化 | [engineering/README.md](./engineering/README.md) | Vite 从本地开发到生产构建的流水线基础 |
| 性能优化 | [performance/README.md](./performance/README.md) | Web Vitals 与前端性能预算基础 |

---

## 如何继续补内容

1. 在对应目录创建带元数据的 `.md` 笔记。
2. 运行 `python scripts/build_knowledge_index.py` 更新汇总页。
3. 使用 `python scripts/search_knowledge.py react --module frontend` 验证检索结果。

---
[返回首页](../README.md)
