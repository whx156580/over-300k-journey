import sys
import gc
import time

# --- 示例 1: 引用计数实验 ---

def ref_count_demo() -> None:
    """观察引用的变化"""
    a = [1, 2, 3]
    # sys.getrefcount(a) 会暂时增加一次引用
    c1 = sys.getrefcount(a)
    
    b = a
    c2 = sys.getrefcount(a)
    
    # 存入列表
    container = [a]
    c3 = sys.getrefcount(a)
    
    print(f"Initial: {c1}, After alias: {c2}, Inside list: {c3}")

# --- 示例 2: 循环引用与手动 GC ---

class Node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.next = None

def cycle_demo() -> int:
    """演示循环引用的清理"""
    n1 = Node("n1")
    n2 = Node("n2")
    n1.next = n2
    n2.next = n1
    
    # 删除外部引用
    del n1, n2
    
    # 强制执行回收，并返回发现的不可达对象数
    return gc.collect()

# --- 示例 3: 内存池分配观测 ---

def memory_size_demo() -> None:
    """展示不同规模对象的内存占用"""
    # 探测 Pymalloc 的边界行为
    empty = sys.getsizeof([])
    one = sys.getsizeof([1])
    many = sys.getsizeof(list(range(100)))
    print(f"Empty: {empty}, One: {one}, Many(100): {many}")

if __name__ == "__main__":
    ref_count_demo()
    found = cycle_demo()
    print(f"GC found {found} unreachable objects in cycle.")
    memory_size_demo()
