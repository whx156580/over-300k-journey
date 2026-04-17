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
target_file = current_dir / "slicing_unpacking_and_common_builtins.py"
mod = load_module_from_path("builtin_logic", target_file)

def test_extract_key_metrics_success():
    """验证星号解包逻辑"""
    h, m, t = mod.extract_key_metrics([1, 2, 3, 4, 5])
    assert h == 1
    assert m == [2, 3, 4]
    assert t == 5

def test_extract_key_metrics_error():
    """验证解包长度不足报错"""
    with pytest.raises(ValueError, match="Data must have at least 2 elements"):
        mod.extract_key_metrics([1])

def test_get_indexed_pairs():
    """验证 enumerate + zip 组合逻辑"""
    res = mod.get_indexed_pairs(["k1", "k2"], [100, 200])
    assert res == ["1: k1=100", "2: k2=200"]

def test_sort_and_check():
    """验证排序与 all() 检查逻辑"""
    items = [{"v": 30}, {"v": 10}, {"v": 20}]
    res = mod.sort_and_check(items, "v")
    assert res is True
    assert items[0]["v"] == 10
    assert items[2]["v"] == 30

def test_any_all_logic():
    """验证 any/all 核心行为"""
    assert any([False, True, False]) is True
    assert all([True, True, True]) is True
    assert all([True, False]) is False

def test_slicing_behavior():
    """验证切片反转与跨度"""
    s = "python"
    assert s[::-1] == "nohtyp"
    assert s[::2] == "pto"
