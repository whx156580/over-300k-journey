import pytest
from common.tools.salary_calculator import calculate_salary_premium

@pytest.mark.unit
def test_calculate_salary_premium_standard():
    # Given: 输入基础薪资与技能列表
    base_salary = 200000
    skills = ["Playwright", "AI-Eval"]
    
    # When: 执行计算逻辑
    result = calculate_salary_premium(base_salary, skills)
    
    # Then: 验证结果是否符合预期 (1 + 0.2 + 0.3 = 1.5)
    assert result == 300000

@pytest.mark.unit
def test_calculate_salary_premium_invalid_input():
    # Given: 异常的基础薪资
    base_salary = -1000
    skills = []
    
    # When & Then: 验证是否抛出指定异常
    with pytest.raises(ValueError, match="Base salary must be positive"):
        calculate_salary_premium(base_salary, skills)

@pytest.mark.unit
@pytest.mark.parametrize("skills, expected_premium", [
    (["K6"], 1.15),
    ([], 1.0),
    (["Unknown"], 1.0)
])
def test_calculate_salary_premium_multi_scenarios(skills, expected_premium):
    # Given: 不同技能组合
    base = 100
    
    # When: 执行计算
    result = calculate_salary_premium(base, skills)
    
    # Then: 断言溢价倍数
    assert result == pytest.approx(base * expected_premium)
