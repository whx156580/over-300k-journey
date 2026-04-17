# 知识库门户页

> 本页由 `python scripts/build_knowledge_index.py` 自动生成，用于展示首页导航、模块目录树和最近新增内容。

---

## 门户首页

| 模块 | 领域数 | 笔记数 | 入口 | 搜索示例 |
| :--- | :--- | :--- | :--- | :--- |
| `testing` | 7 | 89 | [进入模块](../../../testing/README.md) | `python scripts/search_knowledge.py playwright --module testing` |
| `frontend` | 3 | 3 | [进入模块](../../../frontend/README.md) | `python scripts/search_knowledge.py react --module frontend` |
| `backend` | 3 | 3 | [进入模块](../../../backend/README.md) | `python scripts/search_knowledge.py mysql --module backend` |
| `ai` | 3 | 3 | [进入模块](../../../ai/README.md) | `python scripts/search_knowledge.py prompt --module ai` |

### 快速入口

- 知识汇总页: [knowledge_hub.md](../../../common/docs/indexes/knowledge_hub.md)
- 门户说明页: [portal_home.md](../../../common/docs/indexes/portal_home.md)
- 模板: [template.md](../../../common/docs/template.md)
- 结构说明: [project_structure.md](../../../common/docs/project_structure.md)

### 每模块目录树

#### `testing`

```text
testing/
├─ ai-eval/
│  └─ ragas/
├─ api/
│  └─ pytest/
├─ mobile/
│  └─ appium/
├─ performance/
│  └─ k6/
├─ python_notes/
│  └─ python/
├─ strategy/
│  ├─ methodologies/
│  └─ quality-gates/
└─ ui/
   └─ playwright/
```

#### `frontend`

```text
frontend/
├─ engineering/
│  └─ build-tools/
├─ frameworks/
│  └─ react/
└─ performance/
   └─ web-vitals/
```

#### `backend`

```text
backend/
├─ database/
│  └─ mysql/
├─ distributed/
│  └─ caching/
└─ system-design/
   └─ high-availability/
```

#### `ai`

```text
ai/
├─ dataset/
│  └─ cleaning/
├─ llm-agent/
│  └─ prompt/
└─ mlops/
   └─ deployment/
```

### 最近新增内容

| 标题 | 模块 | 领域 | 技术栈 | 更新时间 | 路径 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Redis 缓存与 Celery 异步任务 (Background Jobs) | `testing` | `python_notes` | `python` | 2026-04-17 | [testing/python_notes/04_progressive_topics/redis_celery_and_background_jobs.md](../../../testing/python_notes/04_progressive_topics/redis_celery_and_background_jobs.md) |
| SQLAlchemy ORM 与 Alembic 迁移 (DB Engineering) | `testing` | `python_notes` | `python` | 2026-04-17 | [testing/python_notes/04_progressive_topics/sqlalchemy_and_alembic.md](../../../testing/python_notes/04_progressive_topics/sqlalchemy_and_alembic.md) |
| Asyncio 进阶：超时、限流与队列 (Asyncio Patterns) | `testing` | `python_notes` | `python` | 2026-04-17 | [testing/python_notes/04_progressive_topics/asyncio_advanced_patterns.md](../../../testing/python_notes/04_progressive_topics/asyncio_advanced_patterns.md) |
| 高级语法篇 Mini Projects (Advanced Lab) | `testing` | `python_notes` | `python` | 2026-04-17 | [testing/python_notes/03_advanced_syntax/advanced_syntax_mini_projects.md](../../../testing/python_notes/03_advanced_syntax/advanced_syntax_mini_projects.md) |
| 断点调试与 pdb 进阶 (Debugging & PDB) | `testing` | `python_notes` | `python` | 2026-04-17 | [testing/python_notes/03_advanced_syntax/breakpoint_and_pdb_basics.md](../../../testing/python_notes/03_advanced_syntax/breakpoint_and_pdb_basics.md) |
| 函数式编程与递归 (Functional & Recursion) | `testing` | `python_notes` | `python` | 2026-04-17 | [testing/python_notes/03_advanced_syntax/functional_programming_and_recursion.md](../../../testing/python_notes/03_advanced_syntax/functional_programming_and_recursion.md) |
| 文本编码与字节流 (Encoding & Bytes) | `testing` | `python_notes` | `python` | 2026-04-17 | [testing/python_notes/03_advanced_syntax/bytes_encoding_and_text_files.md](../../../testing/python_notes/03_advanced_syntax/bytes_encoding_and_text_files.md) |
| 结构化建模进阶 (Dataclasses & Enum) | `testing` | `python_notes` | `python` | 2026-04-17 | [testing/python_notes/03_advanced_syntax/dataclasses_and_enum.md](../../../testing/python_notes/03_advanced_syntax/dataclasses_and_enum.md) |
