# 🚀 迈向 30W+ 复合型工程师：工程知识库

![Testing](https://img.shields.io/badge/Focus-Testing-blue)
![Frontend](https://img.shields.io/badge/Focus-Frontend-success)
![Backend](https://img.shields.io/badge/Focus-Backend-informational)
![AI](https://img.shields.io/badge/Focus-AI-orange)

> 这个仓库的目标，是把软件测试、前端开发、后端开发、AI 评测、AI 开发的技能，沉淀成一个能长期积累、持续复用的工程知识库。

---

<!-- PORTAL:START -->

## 门户首页

| 模块 | 领域数 | 笔记数 | 入口 | 搜索示例 |
| :--- | :--- | :--- | :--- | :--- |
| `testing` | 7 | 40 | [进入模块](./testing/README.md) | `python scripts/search_knowledge.py playwright --module testing` |
| `frontend` | 3 | 3 | [进入模块](./frontend/README.md) | `python scripts/search_knowledge.py react --module frontend` |
| `backend` | 3 | 3 | [进入模块](./backend/README.md) | `python scripts/search_knowledge.py mysql --module backend` |
| `ai` | 3 | 3 | [进入模块](./ai/README.md) | `python scripts/search_knowledge.py prompt --module ai` |

### 快速入口

- 知识汇总页: [knowledge_hub.md](./common/docs/indexes/knowledge_hub.md)
- 门户说明页: [portal_home.md](./common/docs/indexes/portal_home.md)
- 模板: [template.md](./common/docs/template.md)
- 结构说明: [project_structure.md](./common/docs/project_structure.md)

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
| 类型提示与静态检查 | `testing` | `python_notes` | `python` | 2026-04-16 | [testing/python_notes/04_progressive_topics/type_hints_and_static_checking.md](./testing/python_notes/04_progressive_topics/type_hints_and_static_checking.md) |
| 测试金字塔、pytest fixture、参数化与 CI | `testing` | `python_notes` | `python` | 2026-04-16 | [testing/python_notes/04_progressive_topics/testing_pyramid_and_pytest.md](./testing/python_notes/04_progressive_topics/testing_pyramid_and_pytest.md) |
| 打包发布：setuptools、wheel、twine 与私有 PyPI | `testing` | `python_notes` | `python` | 2026-04-16 | [testing/python_notes/04_progressive_topics/packaging_and_publishing.md](./testing/python_notes/04_progressive_topics/packaging_and_publishing.md) |
| 性能剖析 | `testing` | `python_notes` | `python` | 2026-04-16 | [testing/python_notes/04_progressive_topics/python_profiling.md](./testing/python_notes/04_progressive_topics/python_profiling.md) |
| 并发模型：线程、进程、协程与 GIL | `testing` | `python_notes` | `python` | 2026-04-16 | [testing/python_notes/04_progressive_topics/python_concurrency.md](./testing/python_notes/04_progressive_topics/python_concurrency.md) |
| Python 关键字全集 | `testing` | `python_notes` | `python` | 2026-04-16 | [testing/python_notes/04_progressive_topics/python_keywords.md](./testing/python_notes/04_progressive_topics/python_keywords.md) |
| 正则表达式与 re 模块 | `testing` | `python_notes` | `python` | 2026-04-16 | [testing/python_notes/04_progressive_topics/python_re.md](./testing/python_notes/04_progressive_topics/python_re.md) |
| 模块与包 | `testing` | `python_notes` | `python` | 2026-04-16 | [testing/python_notes/03_advanced_syntax/modules_and_packages.md](./testing/python_notes/03_advanced_syntax/modules_and_packages.md) |

<!-- PORTAL:END -->

## 它现在是什么

- 一个面向个人成长和团队复用的知识库仓库。
- 既能放笔记，也能放样例代码、测试脚本、题库、图示、导出工具。
- 强调“结构化沉淀”而不是“零散收藏”。

---

## 知识库组织规则

建议按下面这条路径来沉淀内容：

`模块 -> 领域 -> 技术栈 -> 内容层级 -> 笔记 / 代码 / 图片 / 题库`

每个技术栈目录，统一推荐使用下面五层：

- `basics/`：基础概念、环境搭建、第一份 Demo
- `advanced/`：原理、架构、性能优化、复杂场景
- `projects/`：实战案例、完整项目、复盘总结
- `interview/`：高频题、答题模板、知识回顾
- `assets/`：图片、流程图、附件

统一写作模板见 [common/docs/template.md](./common/docs/template.md)。

---

## 五大知识域

| 模块 | 你可以放什么 |
| :--- | :--- |
| [testing](./testing/README.md) | UI 自动化、接口测试、性能测试、移动端测试、AI 评测、测试策略 |
| [frontend](./frontend/README.md) | React/Vue/TypeScript、工程化、构建工具、性能优化 |
| [backend](./backend/README.md) | 分布式系统、数据库、中间件、系统设计、稳定性建设 |
| [ai](./ai/README.md) | Prompt、RAG、Agent、MLOps、数据集工程 |
| [common](./common/docs) | 规范文档、知识模板、题库、工具、检查清单 |

---

## 现在已经有的支撑能力

- [scripts/init_dirs.py](./scripts/init_dirs.py)：初始化知识库目录骨架
- [scripts/check_quality_gate.py](./scripts/check_quality_gate.py)：质量门禁自查脚本
- [scripts/build_knowledge_index.py](./scripts/build_knowledge_index.py)：自动生成知识库汇总首页
- [scripts/search_knowledge.py](./scripts/search_knowledge.py)：按关键词、模块、标签搜索知识笔记
- [common/tools/gen_radar.py](./common/tools/gen_radar.py)：能力雷达图生成
- [common/tools/gen_anki.py](./common/tools/gen_anki.py)：Markdown 问答导出为 Anki
- [common/tools/gen_pdf.py](./common/tools/gen_pdf.py)：合并 Markdown 准备导出 PDF
- [common/docs/capability_model.md](./common/docs/capability_model.md)：能力模型
- [common/docs/assessment_bank.md](./common/docs/assessment_bank.md)：评估题库

---

## 如何开始使用这个知识库

1. 运行 `python scripts/init_dirs.py`，补全知识库目录骨架。
2. 选择一个方向开始沉淀，例如：
   - `testing/ui/playwright/basics/`
   - `frontend/frameworks/react/advanced/`
   - `backend/database/mysql/projects/`
   - `testing/ai-eval/ragas/projects/`
   - `ai/llm-agent/agent/advanced/`
3. 新建笔记时使用 [common/docs/template.md](./common/docs/template.md)。
4. 有代码示例时，把代码和验证方式与笔记放在同一主题目录附近。
5. 定期运行导出工具，形成可复习资产。

```bash
python scripts/build_knowledge_index.py
python scripts/search_knowledge.py playwright
```

---

## 知识复利方式

- **输入**：从 [assessment_bank.md](./common/docs/assessment_bank.md) 里挑一个知识点深入学习
- **输出**：在对应模块目录下落一篇结构化笔记
- **验证**：补代码、样例、测试或图示
- **复习**：用 `gen_anki.py` 和 `gen_pdf.py` 把知识库转成复习材料

---

## 后续建议

下一步最值得做的是三件事：

1. 先把每个主模块补齐“索引页 README”。
2. 在你最熟的一两个技术栈里先沉淀 5 到 10 篇高质量笔记。
3. 再逐步补自动索引、站点化展示和全文检索能力。

---

© 2026 over-300k-journey
© 2026 迈向 30W+ 复合型人才之路 | [GitHub](https://github.com/whx156580/over-300k-journey)
🚀 30W+ 复合型人才模型，欢迎大家参与完善！
📚 项目文档，欢迎大家参与完善！
🛠️ 项目评估，欢迎大家参与完善！
📚 知识库录入标准，欢迎大家参与完善！
📝 代码规范，欢迎大家参与完善！
🤝 贡献指南，欢迎大家参与完善！
🔥 菜单导航系统，欢迎大家参与完善！
🚀 后续我会完善成一个在线学习项目，大家可以在项目中学习到最新的技术知识。
