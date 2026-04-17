import io
import sys
from typing import Dict, Any, Optional

# --- 示例 1: 结构化输出与重定向 ---

def get_status_report(name: str, status: str) -> str:
    """
    生成格式化的状态报告。
    """
    buffer = io.StringIO()
    # 演示 sep, end, file 参数
    print(f"[{name.upper()}]", status, sep=" -> ", end="", file=buffer)
    return buffer.getvalue()

# --- 示例 2: 类型安全的交互式输入解析 ---

def parse_input_config(raw_input: str) -> Optional[Dict[str, int]]:
    """
    解析用户输入的配置字符串（模拟 input() 后的处理）。
    格式预期: "age,retry"
    """
    try:
        parts = [p.strip() for p in raw_input.split(",")]
        if len(parts) != 2:
            return None
        return {
            "age": int(parts[0]),
            "retry": int(parts[1])
        }
    except (ValueError, IndexError):
        return None

# --- 示例 3: 模块入口逻辑 ---

def business_logic():
    """模拟核心业务逻辑"""
    return "SUCCESS"

def main_entry(args):
    """模拟 main 函数调度"""
    if "--debug" in args:
        print("DEBUG MODE ON")
    return business_logic()

if __name__ == "__main__":
    # 仅演示，实际运行需 python 脚本名.py
    print(f"Report: {get_status_report('smoke', 'passed')}")
    print(f"Config: {parse_input_config(' 25 , 3 ')}")
