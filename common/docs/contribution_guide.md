# 📚 知识库贡献与维护指南 (Contribution & Maintenance Guide)

> 本指南旨在规范 **迈向 30W+ 软件测试工程师** 知识库的内容录入、分类、审核及维护流程，确保知识的可复用性、可搜索性及技术深度。

---

## 📑 1. 内容分类体系 (Classification)

知识库采用 **“模块 -> 技术方向 -> 技术栈 -> 四级阶段”** 的分层管理体系：

### 1.1 模块与技术栈矩阵 (Example: Testing)
| 技术方向 (Area) | 核心技术栈 (Tech Stacks) | 存放路径 |
| :--- | :--- | :--- |
| **UI 自动化** | Playwright, Selenium | `testing/ui/{stack}` |
| **接口自动化** | Pytest, Rest-assured | `testing/api/{stack}` |
| **性能压测** | K6, JMeter | `testing/performance/{stack}` |
| **移动端测试** | Appium | `testing/mobile/{stack}` |
| **AI 评测** | Ragas, DeepEval | `testing/ai-eval/{stack}` |

### 1.2 四级阶段划分
每个技术栈内部均按照以下阶段组织内容：
- **基础 (Basic)**: 语法、环境搭建、核心 API。
- **进阶 (Advanced)**: 架构设计、插件开发、性能调优。
- **实战 (Project)**: 真实项目案例、CI/CD 集成。
- **面试 (Interview)**: 高频真题、原理解析。

### 📂 辅助目录
- `/common/snippets`: 通用脚本片段 (Python, JS, Shell 等)。
- `/common/checklists`: 质量检查单、发布清单、Review 清单。
- `/common/tools`: 自动化脚本、提效工具。
- `/common/docs`: 行业报告、索引文档、规范指南。

---

## 📋 2. 信息录入标准 (Standard)

### 2.1 笔记标准模板 (Standard Template)
每篇笔记必须遵循 [标准模板](../docs/template.md)，包含：
- **背景 (Background)**: 业务场景与核心痛点。
- **原理 (Principles)**: 技术方案的核心逻辑 (推荐使用 Mermaid 图示)。
- **实战步骤 (Implementation)**: 可直接运行的代码块 + 环境依赖。
- **踩坑记录 (Pitfalls)**: 具体的错误信息及解决方案。
- **面试高频 Q&A**: 至少 2 个高频问题，并采用 `### Q:` 和 `### A:` 格式以便 Anki 导出。

### 2.2 代码片段标准
- **自包含性**: 每一段核心代码应具备独立运行的能力或配套单元测试。
- **单测覆盖**: 存放在 `/snippets` 或 `/project` 下的代码需包含对应的 `tests/`。
- **禁止敏感信息**: 严禁提交 API Key、Token 或公司内网地址。

### 2.3 命名约定 (Naming Convention)
- **文件夹/文件**: 采用 `snake_case` (小写字母 + 下划线)，例如 `playwright_parallel_execution.md`。
- **资源引用**: 图片存放于 `./assets/` 目录下，并使用相对路径引用。

---

## 🛠️ 3. 审核机制 (Review Mechanism)

### 第一阶段：自查 (Self-Check)
- [ ] 运行 `pytest` 或 `npm test` 确保代码 100% 通过。
- [ ] 本地检查 Markdown 预览效果，确保 Mermaid 图形显示正常。
- [ ] 确保无 404 死链。

### 第二阶段：同级 Review (Peer Review)
- [ ] 提交 Pull Request 后，由另一名成员检查技术准确性。
- [ ] 重点检查：方案是否具有普遍参考意义？是否有过度设计的嫌疑？

### 第三阶段：归档 (Archive)
- [ ] 合并 PR 后，运行 `tools/gen_anki.py` 同步面试题。
- [ ] 运行 `tools/gen_pdf.py` 更新全量知识册。
- [ ] 更新根目录 `README.md` 的索引链接。

---

## 🔄 4. 维护与更新策略 (Maintenance)

### 4.1 定期回顾
- **季度审视**: 每季度末对“进阶”和“实战”内容进行技术迭代检查 (如工具版本升级)。
- **归档机制**: 将过时的技术方案移动至 `archive/` 目录，避免误导。

### 4.2 自动化监控
- **链接检查**: GitHub Actions 每周自动运行 `links.yml` 检测死链。
- **CI 测试**: 每次提交代码自动触发 `tests.yml` 验证脚本可用性。

### 4.3 搜索与索引优化
- **关键词标签**: 在笔记头部使用 YAML Front Matter 标记关键词，方便未来扩展全文搜索。

---
[返回首页](../README.md)
