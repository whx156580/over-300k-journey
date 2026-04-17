import sys
import datetime
from typing import Dict, Any

# --- 示例 1: 自动化 Hook 接管断点 ---

def custom_debug_hook(*args: Any, **kwargs: Any) -> None:
    """
    不进入交互模式，仅记录快照。
    """
    frame = sys._getframe(1)
    # 模拟发送快照到监控系统
    snapshot = {
        "time": datetime.datetime.now().isoformat(),
        "line": frame.f_lineno,
        "locals": {k: str(v) for k, v in frame.f_locals.items() if not k.startswith("__")}
    }
    print(f"[SNAPSHOT] {snapshot}")

def run_business_logic(val: int):
    # 临时重定向断点
    old_hook = sys.breakpointhook
    sys.breakpointhook = custom_debug_hook
    
    x = val * 2
    breakpoint() # 触发自定义 hook
    
    sys.breakpointhook = old_hook
    return x

# --- 示例 2: 事后调试逻辑 ---

def buggy_calc(a: int, b: int) -> int:
    return a // b # 当 b=0 时触发 ZeroDivisionError

if __name__ == "__main__":
    print(f"Logic result: {run_business_logic(21)}")
    
    try:
        buggy_calc(10, 0)
    except ZeroDivisionError:
        print("Exception caught. In real scenario, use pdb.post_mortem() here.")
