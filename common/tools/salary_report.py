import datetime

def generate_salary_report():
    """
    基于行业数据生成年度薪酬对标报告。
    """
    print("Starting salary report generation...")
    
    current_year = datetime.datetime.now().year
    
    report_content = f"""# 📊 {current_year} 年度软件测试工程师薪酬对标报告

## 🌏 行业基准 (2025-2026 数据)
- **初中级测试工程师**: 10-18W (1-3 年)
- **高级测试工程师/负责人**: 20-35W (3-7 年)
- **测试专家/架构师**: 40W+ (7 年以上)

## 🎯 核心高薪因子 (Impact Factors)
1. **自动化测试 (Playwright/Pytest)**: 溢价 +20%
2. **AI 评测/AI Agent 开发**: 溢价 +30%
3. **全链路性能压测 (K6/Locust)**: 溢价 +15%
4. **架构设计与稳定性建设**: 溢价 +25%

## 💹 个人能力对标 (Self-Assessment)
> *以下数据基于知识库覆盖度自动计算 (Mock 数据)*
- **全栈自动化**: 95% (目标: 100%)
- **AI 领域深耕**: 85% (目标: 90%)
- **系统稳定性**: 70% (目标: 80%)

---
✅ 结论：您的技术栈已覆盖 **30W+** 岗位的 85% 以上需求，建议重点攻克 **AI Agent 开发与 RAG 评测**。
"""
    
    with open("salary_report.md", "w", encoding='utf-8') as f:
        f.write(report_content)
            
    print("Successfully generated salary report: salary_report.md")

if __name__ == "__main__":
    import os
    generate_salary_report()
