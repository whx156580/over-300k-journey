import sys
import json
import os

def check_quality_gate():
    """
    模拟 MR 阶段的质量门禁检查逻辑。
    """
    print("🚀 Starting Quality Gate Check...")
    
    # 1. 检查测试通过率 (模拟从测试报告中读取)
    test_pass_rate = 1.0  # 目标 100%
    if test_pass_rate < 1.0:
        print("❌ Error: Test pass rate is below 100%.")
        sys.exit(1)
        
    # 2. 检查覆盖率 (目标：行 80%, 分支 75%)
    line_cov = 85.0
    branch_cov = 78.0
    if line_cov < 80 or branch_cov < 75:
        print(f"❌ Error: Coverage too low (Line: {line_cov}%, Branch: {branch_cov}%).")
        sys.exit(1)
        
    # 3. 检查缺陷
    high_defects = 0
    if high_defects > 0:
        print(f"❌ Error: Found {high_defects} Critical/High defects.")
        sys.exit(1)
        
    print("✅ Quality Gate Passed! Ready to Merge.")

if __name__ == "__main__":
    check_quality_gate()
