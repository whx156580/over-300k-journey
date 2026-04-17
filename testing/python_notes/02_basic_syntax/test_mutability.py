import pytest
import sys
import importlib.util
import copy
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
target_file = current_dir / "mutability_and_copying.py"
mod = load_module_from_path("mutability_logic", target_file)

def test_alias_behavior():
    """验证别名修改影响原对象"""
    assert mod.alias_demo() is True

def test_shallow_copy_demo_call():
    """触发模块内的浅拷贝演示逻辑"""
    res = mod.shallow_copy_demo()
    assert res["data"] == [1, 2, 3]

def test_deep_copy_demo_call():
    """触发模块内的深拷贝演示逻辑"""
    res = mod.deep_copy_demo()
    assert res["data"] == [1, 2]

def test_shallow_copy_isolation_outer():
    """验证浅拷贝顶层隔离"""
    d = {"a": 1}
    c = copy.copy(d)
    c["a"] = 2
    assert d["a"] == 1
    assert d is not c

def test_shallow_copy_shared_inner():
    """验证浅拷贝共享嵌套对象"""
    original = {"data": [1]}
    shallow = mod.copy.copy(original)
    shallow["data"].append(2)
    assert original["data"] == [1, 2]
    assert original["data"] is shallow["data"]

def test_deep_copy_full_isolation():
    """验证深拷贝完全隔离嵌套对象"""
    original = {"data": [1]}
    deep = mod.copy.deepcopy(original)
    deep["data"].append(2)
    assert original["data"] == [1]
    assert original["data"] is not deep["data"]

def test_immutable_types_copy():
    """验证不可变类型的拷贝行为 (通常返回原对象)"""
    s = "hello"
    sc = copy.copy(s)
    sd = copy.deepcopy(s)
    assert s is sc is sd
    
    t = (1, 2)
    tc = copy.copy(t)
    assert t is tc

def test_tuple_with_mutable_element():
    """验证包含可变元素的元组在深拷贝时的行为"""
    t = (1, [2])
    td = copy.deepcopy(t)
    assert t is not td
    assert t[1] is not td[1]
    td[1].append(3)
    assert len(t[1]) == 1
