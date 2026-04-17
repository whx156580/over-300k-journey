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
target_file = current_dir / "python_version_management.py"
mod = load_module_from_path("version_mgmt_logic", target_file)

def test_get_env_details_structure():
    """验证环境详情字典结构"""
    details = mod.get_env_details()
    assert "version" in details
    assert "executable" in details
    assert "is_venv" in details
    assert isinstance(details["is_venv"], bool)

def test_is_safe_to_run_boolean():
    """验证安全检查返回布尔值"""
    res = mod.is_safe_to_run()
    assert isinstance(res, bool)

def test_get_venv_path_default():
    """验证 venv 路径生成逻辑"""
    expected = Path.cwd() / ".venv"
    assert mod.get_venv_path() == expected

def test_get_venv_path_custom():
    """验证自定义 venv 名称路径生成"""
    assert mod.get_venv_path("myenv") == Path.cwd() / "myenv"

def test_sys_path_contains_site_packages():
    """验证 sys.path 是否包含典型的 Python 库路径"""
    paths_str = "|".join(sys.path)
    assert "site-packages" in paths_str or "dist-packages" in paths_str or "lib-python" in paths_str
