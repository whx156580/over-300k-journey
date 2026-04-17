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
target_file = current_dir / "collections.py"
mod = load_module_from_path("collection_logic", target_file)

def test_environment_comparison():
    """验证集合差集与交集逻辑"""
    p = {"db=p", "opt=1"}
    s = {"db=p", "opt=2"}
    s_only, common = mod.compare_environments(p, s)
    assert s_only == {"opt=2"}
    assert common == {"db=p"}

def test_config_merging():
    """验证字典合并逻辑"""
    base = {"a": 1, "b": 2}
    user = {"b": 3, "c": 4}
    final = mod.merge_configs(base, user)
    assert final == {"a": 1, "b": 3, "c": 4}

def test_status_counting():
    """验证状态计数逻辑"""
    data = ["P", "F", "P", "S"]
    counts = mod.count_statuses(data)
    assert counts == {"P": 2, "F": 1, "S": 1}

def test_test_result_named_tuple():
    """验证具名元组访问逻辑"""
    tr = mod.TestResult(101, "FAIL", 1.2)
    assert tr.case_id == 101
    assert tr.status == "FAIL"
    assert tr[2] == 1.2
    assert "Case 101: FAIL (1.2s)" in mod.get_formatted_result(tr)

def test_dict_ordering_guarantee():
    """验证 Python 3.7+ 字典保持插入顺序"""
    d = {}
    d["z"] = 1
    d["a"] = 2
    d["m"] = 3
    keys = list(d.keys())
    assert keys == ["z", "a", "m"]

def test_set_performance_logic():
    """验证文档中提到的集合查找 $O(1)$ 逻辑"""
    import timeit
    n = 1000
    l = list(range(n))
    s = set(range(n))
    # 集合查找应快于列表查找
    t_l = timeit.timeit(lambda: 999 in l, number=1000)
    t_s = timeit.timeit(lambda: 999 in s, number=1000)
    assert t_s < t_l
