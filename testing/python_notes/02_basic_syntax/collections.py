from typing import List, Dict, Set, Tuple, NamedTuple, Any
from collections import defaultdict

# --- 示例 1: 集合运算与环境对比 ---

def compare_environments(prod: Set[str], staging: Set[str]) -> Tuple[Set[str], Set[str]]:
    """对比生产与预发布环境的配置差异"""
    staging_only = staging - prod
    common = prod & staging
    return staging_only, common

# --- 示例 2: 字典高级操作 ---

def merge_configs(base: Dict[str, Any], user: Dict[str, Any]) -> Dict[str, Any]:
    """合并配置，用户配置覆盖基础配置"""
    # 使用 Python 3.9+ 联合运算符
    return base | user

def count_statuses(results: List[str]) -> Dict[str, int]:
    """使用 defaultdict 进行状态计数"""
    counter = defaultdict(int)
    for status in results:
        counter[status] += 1
    return dict(counter)

# --- 示例 3: 具名元组 (NamedTuple) ---

class TestResult(NamedTuple):
    case_id: int
    status: str
    duration: float

def get_formatted_result(res: TestResult) -> str:
    """展示具名元组的字段访问"""
    return f"Case {res.case_id}: {res.status} ({res.duration}s)"

if __name__ == "__main__":
    # 集合验证
    s1 = {"a", "b"}
    s2 = {"b", "c"}
    print(f"Compare: {compare_environments(s1, s2)}")
    
    # 字典验证
    print(f"Merged: {merge_configs({'r': 1}, {'r': 2, 'e': 'dev'})}")
    print(f"Counts: {count_statuses(['P', 'F', 'P'])}")
    
    # 元组验证
    tr = TestResult(1, "PASS", 0.5)
    print(get_formatted_result(tr))
