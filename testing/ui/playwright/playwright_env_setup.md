# 🎭 Playwright 环境搭建与初探 (Basic)

> **背景**: 现代 Web 应用复杂度日益增加，传统的 Selenium 在处理异步加载、Shadow DOM 和多端同步时力不从心。Playwright 作为新一代自动化工具，提供了更快的速度、更稳定的自动等待机制及强大的浏览器上下文隔离。

---

## 📖 背景 (Background)
- **业务痛点**: Selenium 脚本执行慢、易掉链（Flaky）、环境配置复杂。
- **解决方案**: 使用 Playwright 提供的统一 API 操控 Chromium, WebKit 和 Firefox，实现极速、稳定的 UI 自动化。

## 🔬 原理 (Principles)
- **核心架构**: 基于 CDP (Chrome DevTools Protocol) 协议，通过 WebSocket 直接驱动浏览器引擎，比 HTTP 协议更高效。
- **自动等待**: 默认在执行操作（如点击）前自动检查元素的可交互性（Visible, Stable, Enabled）。

## 🚀 实战步骤 (Implementation)

### 1. 环境准备
确保已安装 Python 3.8+。建议使用虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# .\venv\Scripts\activate  # Windows
```

### 2. 安装 Playwright
```bash
pip install pytest-playwright
playwright install chromium  # 安装浏览器二进制文件
```

### 3. 核心代码示例
本项目已配套冒烟测试脚本 [test_playwright_smoke.py](./test_playwright_smoke.py)，您可以直接运行：
```python
import pytest
from playwright.sync_api import Page, expect

@pytest.mark.ui
@pytest.mark.unit
def test_playwright_setup_smoke(page: Page):
    """
    Given: 用户访问知识库 GitHub 页面 (冒烟测试)
    """
    page.goto("https://github.com/microsoft/playwright")
    
    # When: 检查页面标题
    # Then: 验证包含 Playwright 关键字
    expect(page).to_have_title("Playwright")
    
    print("\n✅ Playwright environment is working correctly!")
```

### 4. 运行测试
```bash
# 运行配套的冒烟测试脚本
pytest testing/ui/playwright/test_playwright_smoke.py --headed
```

## ⚠️ 踩坑记录 (Pitfalls)
- **常见错误**: `Executable doesn't exist`
- **解决方案**: 忘记运行 `playwright install`。这是 Playwright 的独立步骤，仅安装 Python 包是不够的。
- **网络问题**: 国内下载浏览器驱动慢。建议配置镜像或使用代理。

## ❓ 面试高频 Q&A (Interview Q&A)
- **Q1**: Playwright 与 Selenium 的最大区别是什么？
- **A1**: Selenium 基于 HTTP 协议，每个操作都是一次请求/响应；Playwright 基于 WebSocket，长连接实时驱动，且原生支持自动等待，稳定性极高。
- **Q2**: 什么是 Browser Context？
- **A2**: 类似于浏览器的无痕窗口。它允许你在同一个浏览器实例下创建多个完全隔离的环境，极大地节省了测试启动时间。

## 🔗 参考链接 (References)
- [Playwright Python 官方文档](https://playwright.dev/python/docs/intro)
- [Pytest-Playwright 插件指南](https://github.com/microsoft/playwright-pytest)

---
[返回首页](../../../README.md) | [查看目录](../README.md)
