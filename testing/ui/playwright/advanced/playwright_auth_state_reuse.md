---
title: Playwright 登录态复用与鉴权状态管理
module: testing
area: ui
stack: playwright
level: advanced
status: active
tags: [playwright, auth, storage-state, ui-testing, login]
updated: 2026-04-16
---

## 1. 背景
- **问题场景**: 大量 UI 用例都从登录页开始，会让回归脚本慢、脆弱、重复。
- **学习目标**: 理解如何把“登录一次”改造成“复用鉴权状态”，提升用例执行效率与稳定性。
- **前置知识**: 了解 Cookie、Local Storage、Session 和 Playwright Context。

## 2. 核心结论
- 大多数回归用例不需要重复验证登录流程本身。
- Playwright 的 `storage_state` 能把登录后的状态持久化，供后续用例复用。
- 登录流程验证应该保留少量专项用例，普通业务回归则复用状态即可。
- 状态复用不是为了偷懒，而是为了让用例更聚焦于真实业务路径。

## 3. 原理拆解
- **关键概念**: `storage_state` 会序列化 Cookie 和本地存储，新的 Browser Context 可直接加载这些状态。
- **运行机制**: 先由单独脚本或前置步骤完成登录，再导出状态文件，后续测试复用该状态进入业务页面。
- **图示说明**: 状态复用把“登录动作”从每条用例里抽离成一次性前置准备。

```mermaid
flowchart LR
    A["专项登录脚本"] --> B["生成 storage state"]
    B --> C["业务回归用例加载状态"]
    C --> D["直接进入业务页面"]
```

## 4. 实战步骤

### 4.1 环境准备
- 依赖版本: `pytest-playwright`
- 安装命令:

```bash
pip install pytest-playwright
playwright install chromium
```

### 4.2 核心代码

```python
from playwright.sync_api import sync_playwright


def save_auth_state():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://example.com/login")
        page.get_by_label("用户名").fill("demo_user")
        page.get_by_label("密码").fill("demo_password")
        page.get_by_role("button", name="登录").click()
        page.context.storage_state(path="auth_state.json")
        browser.close()
```

```python
import pytest
from playwright.sync_api import expect


@pytest.mark.ui
def test_order_list(page):
    page.context.storage_state(path="auth_state.json")
    page.goto("https://example.com/orders")
    expect(page.get_by_role("heading", name="订单列表")).to_be_visible()
```

### 4.3 如何验证
- 本地运行命令: 先生成状态文件，再运行相关 UI 用例。
- 预期结果: 测试可跳过登录页，直接进入业务页执行断言。
- 失败时重点检查: 登录状态是否过期、权限是否变化、状态文件是否和当前环境匹配。

```bash
python save_auth_state.py
pytest testing/ui/playwright/test_e2e_journey.py -q
```

## 5. 项目实践建议
- **适用场景**: 中后台系统、大量需要登录后才能访问的业务页面回归。
- **不适用场景**: 登录流程本身就是被测重点，或鉴权逻辑变化极频繁的场景。
- **落地建议**: 将登录专项测试和业务回归测试拆分成两类流水线。
- **与其他方案对比**: 与每条用例都走登录流程相比，状态复用能显著降低执行时间和环境依赖。

## 6. 踩坑记录
- **常见问题**: 直接复用过期状态文件。
- **错误现象**: 用例随机跳回登录页，或者在 CI 中大量出现 401 / 403。
- **定位方式**: 检查 Cookie 生命周期、租户环境差异、角色权限是否变化。
- **解决方案**: 为状态文件增加失效重建机制，并区分不同环境与不同角色状态。

## 7. 面试高频 Q&A
### Q1: 为什么 UI 自动化里要区分“登录测试”和“登录态复用”？
### A1:
因为它们验证目标不同。登录测试验证鉴权流程本身，登录态复用则是为了让业务回归更聚焦、更高效。

### Q2: 状态复用最大的风险是什么？
### A2:
最大的风险是状态文件过期、权限变化或环境不匹配，导致用例表现不稳定甚至掩盖真实问题。

## 8. 延伸阅读
- [Playwright Authentication](https://playwright.dev/python/docs/auth)
- [Playwright Browser Contexts](https://playwright.dev/python/docs/browser-contexts)
- [Playwright Test Isolation](https://playwright.dev/python/docs/browser-contexts#isolation)

## 9. 关联内容
- 相关笔记: [Playwright 网络拦截与接口 Mock](./playwright_network_mocking_and_route.md)
- 相关代码: [test_playwright_smoke.py](../test_playwright_smoke.py)
- 相关测试: 后续可在 `projects/` 中补多角色状态管理

---
[返回首页](../../../../README.md)
