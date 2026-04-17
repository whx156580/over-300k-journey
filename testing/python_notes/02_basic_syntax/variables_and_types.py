from typing import List, Optional, Any

# --- 示例 1: 内存引用与身份追踪 ---

def reference_demo() -> bool:
    """演示变量重新绑定逻辑"""
    a = [1, 2]
    b = a
    # 修改 a 指向的对象
    a.append(3)
    # b 也会变化，因为指向同一个对象
    if b != [1, 2, 3]: return False
    
    # 重新绑定 a
    a = [4, 5]
    # b 保持不变，指向旧对象
    return b == [1, 2, 3] and (a is not b)

# --- 示例 2: 强类型实验 ---

def type_safety_demo(val: Any) -> str:
    """演示显式类型转换的重要性"""
    try:
        # 故意触发 TypeError
        return "Value: " + val
    except TypeError:
        return "Value: " + str(val)

# --- 示例 3: 类型注解实战 ---

def process_items(items: List[int], prefix: Optional[str] = None) -> List[str]:
    """
    处理整数列表，应用类型注解。
    """
    p = prefix if prefix is not None else "ITEM"
    return [f"{p}_{i}" for i in items]

if __name__ == "__main__":
    print(f"Reference logic OK: {reference_demo()}")
    print(f"Type safety: {type_safety_demo(100)}")
    print(f"Typed output: {process_items([1, 2], prefix='TEST')}")
