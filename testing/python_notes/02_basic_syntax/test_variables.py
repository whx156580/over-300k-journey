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
target_file = current_dir / "variables_and_types.py"
mod = load_module_from_path("variable_logic", target_file)

def test_reference_logic():
    """验证引用绑定与重新绑定逻辑"""
    assert mod.reference_demo() is True

def test_type_safety_str_int():
    """验证字符串与整数拼接的异常处理"""
    assert mod.type_safety_demo(123) == "Value: 123"
    assert mod.type_safety_demo("abc") == "Value: abc"

def test_process_items_with_prefix():
    """验证带前缀的类型化处理"""
    assert mod.process_items([1], "A") == ["A_1"]

def test_process_items_default_prefix():
    """验证默认前缀逻辑"""
    assert mod.process_items([1]) == ["ITEM_1"]

def test_small_int_interning():
    """验证小整数对象池机制"""
    a = 256
    b = 256
    assert a is b
    
    # 较大整数在脚本不同位置定义时通常不是同一个对象
    # 注意：在某些交互式环境或编译器优化下，结果可能有差异
    x = 1000
    y = 1000
    # 在同一个作用域内，编译器可能会优化
    assert x is y or x == y

def test_identity_vs_equality():
    """验证值相等与身份相等区别"""
    l1 = [1, 2]
    l2 = [1, 2]
    assert l1 == l2
    assert l1 is not l2
