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
target_file = current_dir / "comprehensions_and_generator_expressions.py"
mod = load_module_from_path("comprehensions", target_file)

def test_transpose_matrix():
    """验证矩阵转置逻辑"""
    matrix = [[1, 2, 3], [4, 5, 6]]
    expected = [[1, 4], [2, 5], [3, 6]]
    assert mod.transpose_matrix(matrix) == expected
    assert mod.transpose_matrix([]) == []

def test_build_grade_map():
    """验证等级映射逻辑"""
    scores = {"A": 100, "B": 59, "C": 60}
    expected = {"A": "PASS", "B": "FAIL", "C": "PASS"}
    assert mod.build_grade_map(scores) == expected

def test_flatten_suites():
    """验证列表拍平逻辑"""
    suites = [["t1", "t2"], ["t3"]]
    assert mod.flatten_suites(suites) == ["t1", "t2", "t3"]
    assert mod.flatten_suites([]) == []

def test_generator_memory_efficiency():
    """验证生成器表达式的内存占用远小于大列表"""
    import sys
    n = 10000
    list_obj = [i for i in range(n)]
    gen_obj = (i for i in range(n))
    # 列表占用 KB 级别，生成器仅 Bytes 级别
    assert sys.getsizeof(gen_obj) < sys.getsizeof(list_obj) / 10

def test_set_comprehension_deduplication():
    """验证集合推导式的自动去重特性"""
    data = ["test", "test", "prod"]
    unique = {x for x in data}
    assert unique == {"test", "prod"}
