from functools import partial, lru_cache
from typing import List, Dict, Any, Union

# --- 示例 1: 复杂对象排序 ---

def sort_test_results(results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    按耗时升序、优先级降序排序。
    """
    # 使用 lambda 定义复合 key
    return sorted(results, key=lambda x: (x.get("cost", 0), -x.get("prio", 0)))

# --- 示例 2: 函数工厂 (Partial) ---

def api_request(base_url: str, method: str, endpoint: str) -> str:
    """模拟基础请求函数"""
    return f"{method} {base_url}/{endpoint}"

def create_get_client(base_url: str):
    """
    创建一个固定为 GET 方法的客户端。
    """
    return partial(api_request, base_url, "GET")

# --- 示例 3: 递归处理 ---

def sum_nested_list(data: Union[List, int]) -> int:
    """
    递归计算嵌套列表中所有数字的和。
    """
    if isinstance(data, int):
        return data
    total = 0
    for item in data:
        total += sum_nested_list(item)
    return total

# --- 示例 4: 记忆化递归 ---

@lru_cache(maxsize=128)
def cached_fibonacci(n: int) -> int:
    """带缓存的斐波那契数列"""
    if n < 2: return n
    return cached_fibonacci(n-1) + cached_fibonacci(n-2)

if __name__ == "__main__":
    # 验证排序
    items = [{"cost": 1.0, "prio": 1}, {"cost": 1.0, "prio": 2}]
    print(f"Sorted: {sort_test_results(items)}")
    
    # 验证工厂
    client = create_get_client("https://api.com")
    print(f"Request: {client('users')}")
    
    # 验证递归
    print(f"Sum: {sum_nested_list([1, [2, [3, 4]], 5])}")
    print(f"Fib(10): {cached_fibonacci(10)}")
