def calculate_salary_premium(base_salary, skills):
    """
    核心业务逻辑：根据掌握的技能计算薪资溢价。
    """
    if base_salary <= 0:
        raise ValueError("Base salary must be positive")
    
    premium = 0
    if "Playwright" in skills:
        premium += 0.20
    if "AI-Eval" in skills:
        premium += 0.30
    if "K6" in skills:
        premium += 0.15
        
    return base_salary * (1 + premium)
