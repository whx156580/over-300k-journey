# 🛡️ 软件测试模块 (Software Testing)

> **核心目标**: 建立全链路质量保障体系，实现质量左移与右移。

## 📁 目录结构与技术栈 (Structure & Tech Stacks)

本项目采用三级目录管理，确保不同技术栈的实现隔离、结构清晰：

### 🎨 UI 自动化测试 (UI Testing)
- **[ui/playwright/](./ui/playwright)**: Playwright 测试脚本、Page Object Model 与配置。
- **[ui/selenium/](./ui/selenium)**: Selenium WebDriver 脚本、驱动配置与测试数据。

### ⚙️ 接口自动化测试 (API Testing)
- **[api/pytest/](./api/pytest)**: 基于 Pytest 的接口自动化框架与插件。
- **[api/rest-assured/](./api/rest-assured)**: 基于 Rest-Assured 的 Java 接口测试方案。

### 📱 移动端测试 (Mobile Testing)
- **[mobile/appium/](./mobile/appium)**: Appium 自动化脚本、设备配置与多端兼容。

### ⚡ 性能测试 (Performance Testing)
- **[performance/k6/](./performance/k6)**: K6 性能压测脚本与指标监控。
- **[performance/jmeter/](./performance/jmeter)**: JMeter 压测方案与结果分析。

### 🤖 AI 模型与评测 (AI Evaluation)
- **[ai-eval/ragas/](./ai-eval/ragas)**: RAG 应用的自动化评估。
- **[ai-eval/deepeval/](./ai-eval/deepeval)**: 深度学习模型评测实践。

### 🧠 测试策略 (Testing Strategy)
- **[strategy/](./strategy)**: 测试策略、缺陷分析、质量度量看板。

---
[返回首页](../README.md) | [查看菜单](../common/docs/menu_config.json)
