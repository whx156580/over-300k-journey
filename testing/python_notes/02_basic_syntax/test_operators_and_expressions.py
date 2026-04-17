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
target_file = current_dir / "operators_and_expressions.py"
mod = load_module_from_path("op_logic", target_file)

def test_extract_score_success():
    """验证海象运算符提取逻辑"""
    assert mod.extract_and_validate_score("final score:88") == 88

def test_extract_score_out_of_range():
    """验证链式比较边界"""
    assert mod.extract_and_validate_score("score:105") is None
    assert mod.extract_and_validate_score("score:-5") is None

def test_get_username_valid():
    """验证逻辑短路正常获取名称"""
    u = mod.MockUser("Bob")
    assert mod.get_username(u) == "Bob"

def test_get_username_none():
    """验证逻辑短路保护 None 并设置默认值"""
    assert mod.get_username(None) == "Guest"

def test_toggle_permission_logic():
    """验证位运算翻转逻辑"""
    READ = 0b01
    WRITE = 0b10
    current = READ
    # 开启写权限
    current = mod.toggle_permission(current, WRITE)
    assert current == 0b11
    # 关闭写权限
    current = mod.toggle_permission(current, WRITE)
    assert current == READ

def test_truthy_values_behavior():
    """验证 Python 特有的 or/and 返回值行为"""
    # or 返回第一个真值
    assert ([] or [1, 2]) == [1, 2]
    # and 返回第一个假值，若全为真则返回最后一个
    assert ([1] and [2, 3]) == [2, 3]
    assert (0 and 100) == 0
