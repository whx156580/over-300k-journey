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
target_file = current_dir / "dependency_management.py"
mod = load_module_from_path("dep_mgmt_logic", target_file)

def test_check_package_status_installed():
    """验证已安装包的状态检查"""
    name, ver, ok = mod.check_package_status("pytest")
    assert name == "pytest"
    assert ok is True
    assert ver != "NOT_INSTALLED"

def test_check_package_status_missing():
    """验证未安装包的状态检查"""
    name, ver, ok = mod.check_package_status("non_existent_package_xyz")
    assert ok is False
    assert ver == "NOT_INSTALLED"

def test_parse_requirements_logic():
    """验证 requirements 解析逻辑"""
    content = """
    pytest>=8.0
    # This is a comment
    requests==2.31.0  # inline comment
    
    """
    expected = ["pytest>=8.0", "requests==2.31.0"]
    assert mod.parse_requirements(content) == expected

def test_poetry_line_generation():
    """验证 Poetry 依赖行生成"""
    line = mod.generate_poetry_dependency_line("fastapi", "0.100.0")
    assert line == 'fastapi = "^0.100.0"'

def test_version_comparison_logic():
    """验证简单的版本比较逻辑 (字符串比较)"""
    # 注意：字符串比较 '10.0' < '9.0' 是 False，但在某些场景下有效
    _, _, ok = mod.check_package_status("pytest", min_version="1.0.0")
    assert ok is True
