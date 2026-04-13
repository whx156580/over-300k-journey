# 🚀 迈向 30W+ 复合型人才：全栈开发 & 质量工程知识库

![Testing](https://img.shields.io/badge/Focus-FullStack_Quality-blue)
![AI](https://img.shields.io/badge/AI-LLM_Evaluation-orange)
![License](https://img.shields.io/badge/Content-Knowledge_Base-green)

> **不仅是笔记，更是通往高级/专家级工程师的职业进化引擎。**

---

## 🛡️ 测试体系与质量红线 (Testing System)
本项目建立了严密的自动化测试体系，确保每一行代码均经过严格校验：
- **测试策略**: [全链路测试计划](./testing/strategy/test_strategy.md)
- **质量门禁**: 强制要求通过率 100%，行覆盖率 ≥ 80%，禁止合并含 High 缺陷代码。
- **自动化运行**: 运行 `pytest` 执行单元/集成测试，运行 `python scripts/check_quality_gate.py` 进行门禁自查。

---

## 🚀 快速开始 (Quick Start)
1. **环境初始化**: 运行 `python scripts/init_dirs.py` 自动补全本地物理目录及 `.gitkeep` 占位文件。
2. **安装依赖**: 执行 `pip install -r requirements.txt -i http://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn` 安装。
3. **能力评估**: 阅读 [30W+ 复合型人才模型](./common/docs/capability_model.md) 并使用 [自评脚本](./common/tools/gen_radar.py) 生成您的能力雷达图。
4. **按需学习**: 根据雷达图短板，进入 `testing/` 或 `frontend/backend/ai/` 模块进行针对性实战。

---

## 🏗️ 项目目录结构 (Project Structure)

> **架构升级说明**: 本项目已从旧版散乱目录迁移至全新的五大核心模块架构。旧目录已全部合并至对应模块中。
> **CI/CD 说明**: `.github/` 目录下的自动化工作流配置文件已本地化，不随仓库分发。

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
- **初始化**: 若本地目录缺失或需要重置，请执行 `python scripts/init_dirs.py`。
- **标准化**: 每一级子目录均应包含 `README.md` 说明文件。

---

## 🎯 模块职责说明 (Module Responsibilities)

| 模块名称 | 核心目标 | 交付物 |
| :--- | :--- | :--- |
| **软件测试** | 建立全链路质量保障体系，实现质量左移与右移 | 自动化脚本、压测报告、质量度量看板 |
| **前端开发** | 构建高性能、可维护的 UI 系统，提升用户体验 | 组件库、性能优化方案、监控体系 |
| **后端开发** | 设计高并发、高可用的分布式后台架构 | 系统架构图、数据库方案、微服务链 |
| **AI 开发** | 落地 AI 应用，通过智能化手段赋能业务与效率 | AI Agent、RAG 知识库、智能化测试工具 |
| **运维脚本** | 提供项目结构维护、环境补全等自动化能力 | [init_dirs.py](./scripts/init_dirs.py) |

---

## 🛠️ 全景技术索引 (Knowledge Index)

| 维度 | 核心实战 (点击直达) | 进阶方向 |
| :--- | :--- | :--- |
| **测试工程** | [UI 自动化](./testing/ui) \| [API 自动化](./testing/api) \| [性能压测](./testing/performance) | 混沌工程, 流量回放 |
| **前端开发** | [核心框架](./frontend/frameworks) \| [工程化](./frontend/engineering) \| [性能优化](./frontend/performance) | 微前端, 视觉回归 |
| **后端开发** | [分布式系统](./backend/distributed) \| [数据库实战](./backend/database) \| [架构设计](./backend/system-design) | K8s 治理, DDD |
| **AI 领域** | [LLM & Agent](./ai/llm-agent) \| [MLOps](./ai/mlops) \| [数据管道](./ai/dataset) | 模型微调, 智能化自愈 |

---

## 💎 知识复利策略 (Knowledge Compounding)
- **输入**: 每日攻克一个 [评估题库](./common/docs/assessment_bank.md) 中的核心知识点。
- **输出**: 在对应目录下新增笔记，并运行 [gen_pdf.py](./common/tools/gen_pdf.py) 导出为个人资产。
- **内化**: 每周末通过 [gen_anki.py](./common/tools/gen_anki.py) 导出题库，利用碎片时间完成记忆闭环。

---

## 🗺️ 菜单导航系统 (Menu System)

本项目配套完整的菜单导航，详见配置文件：[menu_config.json](./common/docs/menu_config.json)

- **能力评估**: [30W+ 复合型人才模型](./common/docs/capability_model.md)
- **实战练习**: [50+ 评估题库](./common/docs/assessment_bank.md)
- **贡献指南**: [知识库录入标准](./common/docs/contribution_guide.md)

---
© 2026 迈向 30W+ 复合型人才之路 | [GitHub](https://github.com/whx156580/over-300k-journey)


