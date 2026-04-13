# 🚀 迈向 30W+ 复合型人才：全栈开发 & 质量工程知识库

> 本项目是一个系统化的知识库，旨在帮助工程师构建从“纯测试”向“测试 + 前后端 + AI”复合型人才转型的核心竞争力。

---

## 🏗️ 项目目录结构 (Project Structure)

> **架构升级说明**: 本项目已从旧版散乱目录迁移至全新的五大核心模块架构。旧目录 (ai-dev, ai-eval, api, checklists, docs, snippets, tools, web) 已全部合并至对应模块中。

```text
.
├── 📂 testing/              # 软件测试模块 (Software Testing)
│   ├── 📁 ui/               # UI 自动化 (Playwright, Selenium)
│   ├── 📁 api/              # 接口自动化 (Pytest, Rest-Assured)
│   ├── 📁 mobile/           # 移动端测试 (Appium)
│   ├── 📁 performance/      # 性能压测 (K6, JMeter)
│   ├── 📁 ai-eval/          # AI 模型与 RAG 评测
│   └── 📁 strategy/         # 测试策略与质量度量
├── 📂 frontend/             # 前端开发模块 (Frontend Development)
│   ├── 📁 frameworks/       # React/Vue/跨端框架实战
│   ├── 📁 engineering/      # 构建工具、CI/CD 与工程化
│   └── 📁 performance/      # 前端性能监控与优化实践
├── 📂 backend/              # 后端开发模块 (Backend Development)
│   ├── 📁 distributed/      # 分布式、微服务与中间件
│   ├── 📁 database/         # 数据库设计、调优与事务
│   └── 📁 system-design/    # 高可用架构与系统设计
├── 📂 ai/                   # AI 开发模块 (AI Development)
│   ├── 📁 llm-agent/        # 大模型应用、Prompt 与 Agent
│   ├── 📁 mlops/            # 模型部署、监控与 MLOps
│   └── 📁 dataset/          # 数据管道与特征工程
├── 📂 common/               # 公共资源模块 (Shared Resources)
│   ├── 📁 checklists/       # 质量门禁与 Review 清单
│   ├── 📁 snippets/         # 高频代码片段库
│   ├── 📁 tools/            # 自研提效工具链
│   └── 📁 docs/             # 核心规范与评估体系
└── 📂 scripts/              # 自动化运维脚本
    └── 🛠️ init_dirs.py      # 目录结构一键初始化与 .gitkeep 补全
```

---

## ⚙️ 目录维护规范
- **.gitkeep**: 所有空目录必须包含 `.gitkeep` 文件，以确保目录结构能被 Git 追踪。
- **初始化**: 若本地目录缺失，请运行 `python scripts/init_dirs.py` 进行一键补全。
- **标准化**: 每一级子目录均应包含 `README.md` 说明文件。

---

## 🎯 模块职责说明 (Module Responsibilities)

| 模块名称 | 核心目标 | 交付物 |
| :--- | :--- | :--- |
| **软件测试** | 建立全链路质量保障体系，实现质量左移与右移 | 自动化脚本、压测报告、质量度量看板 |
| **前端开发** | 构建高性能、可维护的 UI 系统，提升用户体验 | 组件库、性能优化方案、监控体系 |
| **后端开发** | 设计高并发、高可用的分布式后台架构 | 系统架构图、数据库方案、微服务链 |
| **AI 开发** | 落地 AI 应用，通过智能化手段赋能业务与效率 | AI Agent、RAG 知识库、智能化测试工具 |

---

## 🛠️ 技术栈对应表 (Tech Stack Matrix)

| 维度 | 核心技术栈 | 进阶方向 |
| :--- | :--- | :--- |
| **测试** | Playwright, Pytest, K6, JMeter | 混沌工程, 流量录制回放, 智能回归 |
| **前端** | React/Vue3, TypeScript, Vite | 微前端, 视觉回归, 埋点监控 |
| **后端** | Go/Java, MySQL, Redis, Kafka | 分布式事务, K8s 治理, 领域建模 (DDD) |
| **AI** | LangChain, LlamaIndex, PyTorch | 模型微调 (SFT), Rerank, 智能化自愈 |

---

## �️ 菜单导航系统 (Menu System)

本项目配套完整的菜单导航，详见配置文件：[menu_config.json](./common/docs/menu_config.json)

- **能力评估**: [30W+ 复合型人才模型](./common/docs/capability_model.md)
- **实战练习**: [50+ 评估题库](./common/docs/assessment_bank.md)
- **贡献指南**: [知识库录入标准](./common/docs/contribution_guide.md)

---
© 2026 迈向 30W+ 复合型人才之路 | [GitHub](https://github.com/your-username/over-300k-journey)
