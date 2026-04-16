# ⚙️ 后端开发模块

> 这里承接分布式、中间件、数据库与系统设计相关知识，并接入统一模板、自动汇总与搜索体系。

---

## 导航入口

- 自动汇总首页: [knowledge_hub.md](../common/docs/indexes/knowledge_hub.md)
- 搜索入口: `python scripts/search_knowledge.py <关键词> --module backend`
- 写作模板: [template.md](../common/docs/template.md)

---

## 模块索引

| 知识域 | 入口 | 已收录内容 |
| :--- | :--- | :--- |
| 分布式 | [distributed/README.md](./distributed/README.md) | 缓存击穿、穿透与雪崩基础 |
| 数据库 | [database/README.md](./database/README.md) | MySQL 索引设计基础 |
| 系统设计 | [system-design/README.md](./system-design/README.md) | 高可用与降级设计基础 |

---

## 如何继续补内容

1. 在对应目录创建带元数据的 `.md` 笔记。
2. 运行 `python scripts/build_knowledge_index.py` 更新汇总页。
3. 使用 `python scripts/search_knowledge.py mysql --module backend` 验证检索结果。

---
[返回首页](../README.md)
