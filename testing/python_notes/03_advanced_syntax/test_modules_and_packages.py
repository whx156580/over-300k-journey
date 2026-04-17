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
target_file = current_dir / "modules_and_packages.py"
mod = load_module_from_path("module_logic", target_file)

def test_dynamic_plugin_success():
    """验证动态导入标准库成功"""
    res = mod.run_plugin_func("math", "sqrt", 16)
    assert res == 4.0

def test_dynamic_plugin_import_error():
    """验证导入不存在模块的错误处理"""
    res = mod.run_plugin_func("non_existent_module_xyz", "func")
    assert "Error" in res

def test_dynamic_plugin_attr_error():
    """验证模块内不存在函数的错误处理"""
    res = mod.run_plugin_func("math", "non_existent_func")
    assert "Error" in res

def test_module_caching_check():
    """验证模块缓存检查逻辑"""
    import sys
    assert mod.is_module_cached("sys") is True
    # 假设一个从未导入过的名字
    assert mod.is_module_cached("very_unlikely_module_name") is False

def test_all_declaration():
    """验证 __all__ 声明的存在"""
    assert hasattr(mod, "__all__")
    assert "InternalClient" in mod.__all__

def test_internal_client_logic():
    """验证模拟的客户端逻辑"""
    client = mod.InternalClient()
    assert client.query() == "data"
