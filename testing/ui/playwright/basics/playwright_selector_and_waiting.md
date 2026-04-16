---
title: Playwright 选择器与自动等待基础
module: testing
area: ui
stack: playwright
level: basics
status: active
tags: [playwright, ui-testing, locator, auto-wait]
updated: 2026-04-16
---

## 1. 背景
- **问题场景**: Web 页面越来越动态，元素会延迟渲染、状态会异步变化，传统脚本容易出现找不到元素或偶发失败。
- **学习目标**: 理解 Playwright 为什么强调 Locator 和自动等待，并能写出更稳定的 UI 自动化脚本。
- **前置知识**: 了解 HTML、DOM、基本断言和 Pytest 用法。

## 2. 核心结论
- Playwright 更推荐使用 `Locator` 和语义化选择器，而不是脆弱的 CSS 路径。
- 大多数点击、输入、断言场景都自带自动等待，不应滥用 `sleep` 或 `wait_for_timeout`。
- 选择器优先级通常是: `get_by_role` > `get_by_label` > `get_by_text` > 稳定 `data-testid`。
- UI 自动化稳定性的关键不是“等更久”，而是“等正确的状态”。

## 3. 原理拆解
- **关键概念**: Locator 是延迟求值的元素定位器，每次操作前都会重新解析元素状态。
- **运行机制**: 点击、输入、断言前，Playwright 会检查元素是否存在、可见、可交互、稳定。
- **图示说明**: 下面这个流程说明了一个点击动作在执行前会经过哪些检查。

```mermaid
flowchart LR
    A["定位元素 Locator"] --> B["检查元素存在"]
    B --> C["检查可见/可交互"]
    C --> D["执行点击/输入"]
    D --> E["断言结果"]
```

## 4. 实战步骤

### 4.1 环境准备
- 依赖版本: Python 3.9+、`pytest-playwright`
- 安装命令:

```bash
pip install pytest-playwright
playwright install chromium
```

### 4.2 核心代码

```python
import pytest
from playwright.sync_api import Page, expect


@pytest.mark.ui
def test_login_form(page: Page):
    page.goto("https://example.com/login")

    page.get_by_label("用户名").fill("demo_user")
    page.get_by_label("密码").fill("demo_password")
    page.get_by_role("button", name="登录").click()

    expect(page.get_by_role("heading", name="控制台")).to_be_visible()
```

### 4.3 如何验证
- 本地运行命令: `pytest testing/ui/playwright/test_playwright_smoke.py -q`
- 预期结果: 页面可成功打开，断言命中目标标题或目标元素。
- 失败时重点检查: 浏览器是否已安装、页面选择器是否稳定、测试环境网络是否可用。

```bash
pytest testing/ui/playwright/test_playwright_smoke.py -q
```

## 5. 项目实践建议
- **适用场景**: 中后台、B 端系统、需要跨浏览器回归验证的 Web 产品。
- **不适用场景**: 页面结构极不稳定且没有稳定标识的原型阶段页面。
- **落地建议**: 与开发约定 `data-testid` 或语义化标签，减少脚本和页面结构的强耦合。
- **与其他方案对比**: 与依赖显式等待的旧式 WebDriver 脚本相比，Playwright 的自动等待更适合现代前端异步渲染场景。

## 6. 踩坑记录
- **常见问题**: 直接使用固定等待时间。
- **错误现象**: 本地偶尔通过，CI 上经常失败，表现为元素未出现或状态不正确。
- **定位方式**: 打开 Trace、截图、视频，确认失败时元素状态是否真的满足操作条件。
- **解决方案**: 优先改为等待具体状态，例如 `to_be_visible()`、`to_have_url()`、`to_contain_text()`。

## 7. 面试高频 Q&A
### Q1: Playwright 的自动等待到底解决了什么核心问题？
### A1:
它解决的是“脚本执行速度快于页面状态变化”的问题。相比简单睡眠，自动等待会围绕元素状态和断言目标来判断时机，因此更稳定也更高效。

### Q2: 为什么推荐优先使用 `get_by_role`？
### A2:
因为它更接近真实用户访问语义，既能提升选择器可读性，也通常比依赖 DOM 层级的 CSS 选择器更稳定。

## 8. 延伸阅读
- [Playwright Python 文档](https://playwright.dev/python/docs/intro)
- [Playwright Page Object Models](https://playwright.dev/python/docs/pom)
- [Playwright Frames](https://playwright.dev/python/docs/frames)

## 9. 关联内容
- 相关笔记: [Playwright 环境搭建与初探](../playwright_env_setup.md)
- 相关代码: [test_playwright_smoke.py](../test_playwright_smoke.py)
- 相关测试: [test_e2e_journey.py](../test_e2e_journey.py)

---
[返回首页](../../../../README.md)
