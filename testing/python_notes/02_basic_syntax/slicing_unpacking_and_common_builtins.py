from typing import List, Tuple, Any, Dict

# --- 示例 1: 扩展解包 ---

def extract_key_metrics(data: List[Any]) -> Tuple[Any, List[Any], Any]:
    """
    使用星号语法解包序列。
    """
    if len(data) < 2:
        raise ValueError("Data must have at least 2 elements")
    head, *middle, tail = data
    return head, middle, tail

# --- 示例 2: 组合遍历 ---

def get_indexed_pairs(keys: List[str], values: List[Any]) -> List[str]:
    """
    组合使用 enumerate 和 zip。
    """
    return [
        f"{i}: {k}={v}" 
        for i, (k, v) in enumerate(zip(keys, values), start=1)
    ]

# --- 示例 3: 复杂排序与判定 ---

def sort_and_check(items: List[Dict[str, Any]], key_name: str) -> bool:
    """
    按指定键排序，并检查是否所有值都符合要求。
    """
    # 原地排序示例
    items.sort(key=lambda x: x.get(key_name, 0))
    # all() 配合生成器表达式
    return all(isinstance(item.get(key_name), (int, float)) for item in items)

if __name__ == "__main__":
    # 验证解包
    print(f"Metrics: {extract_key_metrics([1, 2, 3, 4])}")
    
    # 验证组合遍历
    print(f"Pairs: {get_indexed_pairs(['a', 'b'], [10, 20])}")
    
    # 验证排序
    data = [{"v": 10}, {"v": 5}]
    print(f"All valid? {sort_and_check(data, 'v')}, Data: {data}")
