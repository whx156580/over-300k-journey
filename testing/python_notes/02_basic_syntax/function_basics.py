from typing import List, Optional, Callable

# --- 示例 1: LEGB 作用域与遮蔽 ---

def scope_demo() -> str:
    """演示 Enclosing 作用域查找"""
    value = "enclosing"
    
    def inner():
        # 查找顺序: Local -> Enclosing (value) -> Global
        return value
        
    return inner()

# --- 示例 2: 闭包与 nonlocal 状态保持 ---

def make_counter(start: int = 0) -> Callable[[], int]:
    """
    创建一个计数器闭包。
    """
    count = start
    
    def increment() -> int:
        nonlocal count
        count += 1
        return count
        
    return increment

# --- 示例 3: 默认参数陷阱修复与强制关键字 ---

def safe_append(item: str, target: Optional[List[str]] = None) -> List[str]:
    """
    修复可变默认参数坑。
    """
    if target is None:
        target = []
    target.append(item)
    return target

def run_test(*, env: str = "test") -> str:
    """
    强制使用关键字参数。
    """
    return f"Running in {env}"

if __name__ == "__main__":
    # 验证闭包
    c = make_counter(10)
    print(f"Counter: {c()}, {c()}")
    
    # 验证关键字参数
    print(run_test(env="prod"))
    # run_test("prod") # TypeError
