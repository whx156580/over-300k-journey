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
    expect(page).to_have_title("Playwright", timeout=10000)
    
    print("\n✅ Playwright environment is working correctly!")
