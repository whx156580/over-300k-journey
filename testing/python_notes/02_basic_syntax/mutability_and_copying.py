import copy
from typing import Any, List, Dict

# --- 示例 1: 引用别名与原地修改 ---

def alias_demo() -> bool:
    """演示赋值操作仅创建引用别名"""
    a = [1, 2, 3]
    b = a
    b.append(4)
    # 修改 b 实际上修改了 a 共同指向的对象
    return a == [1, 2, 3, 4] and (a is b)

# --- 示例 2: 浅拷贝 (Shallow Copy) ---

def shallow_copy_demo() -> Dict[str, Any]:
    """演示浅拷贝在处理嵌套对象时的行为"""
    original = {"meta": "v1", "data": [1, 2]}
    shallow = copy.copy(original)
    
    # 修改顶层不可变对象
    shallow["meta"] = "v2"
    # 修改嵌套可变对象
    shallow["data"].append(3)
    
    return original # {"meta": "v1", "data": [1, 2, 3]}

# --- 示例 3: 深拷贝 (Deep Copy) ---

def deep_copy_demo() -> Dict[str, Any]:
    """演示深拷贝实现完全隔离"""
    original = {"meta": "v1", "data": [1, 2]}
    deep = copy.deepcopy(original)
    
    deep["meta"] = "v2"
    deep["data"].append(3)
    
    return original # {"meta": "v1", "data": [1, 2]}

if __name__ == "__main__":
    print(f"Alias logic check: {alias_demo()}")
    print(f"Shallow impact on original: {shallow_copy_demo()}")
    print(f"Deep isolation check: {deep_copy_demo()}")
