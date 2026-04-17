import pytest
import sys
import importlib.util
from pathlib import Path

# 确保项目根目录在路径中
ROOT = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(ROOT))

def load_module_from_path(module_name: str, file_path: Path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module
    raise ImportError(f"Could not load module {module_name} at {file_path}")

# 加载目标模块
current_dir = Path(__file__).resolve().parent
target_file = current_dir / "functional_programming_and_recursion.py"
mod = load_module_from_path("functional_logic", target_file)

def test_sort_test_results_logic():
    """验证复合排序逻辑"""
    data = [
        {"name": "A", "cost": 2.0, "prio": 1},
        {"name": "B", "cost": 1.0, "prio": 1},
        {"name": "C", "cost": 1.0, "prio": 2}
    ]
    res = mod.sort_test_results(data)
    # B 和 C 耗时相同，C 优先级高 (-2 < -1)，排在前面
    assert res[0]["name"] == "C"
    assert res[1]["name"] == "B"
    assert res[2]["name"] == "A"

def test_partial_client_factory():
    """验证 partial 生成的客户端"""
    client = mod.create_get_client("http://test.io")
    assert client("health") == "GET http://test.io/health"

def test_sum_nested_list_recursion():
    """验证递归求和逻辑"""
    assert mod.sum_nested_list([1, [2, 3], 4]) == 10
    assert mod.sum_nested_list([]) == 0
    assert mod.sum_nested_list(5) == 5

def test_cached_fibonacci_correctness():
    """验证斐波那契计算正确性"""
    assert mod.cached_fibonacci(0) == 0
    assert mod.cached_fibonacci(1) == 1
    assert mod.cached_fibonacci(10) == 55

def test_lru_cache_efficiency():
    """验证 lru_cache 缓存命中情况 (间接通过调用次数或速度)"""
    # 第一次计算
    res1 = mod.cached_fibonacci(20)
    # 第二次应瞬间完成
    res2 = mod.cached_fibonacci(20)
    assert res1 == res2
    # 检查缓存统计信息 (如果可用)
    info = mod.cached_fibonacci.cache_info()
    assert info.hits > 0
