import pytest
import sys
import importlib.util
import json
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
target_file = current_dir / "environment_mini_projects.py"
mod = load_module_from_path("env_lab_logic", target_file)

def test_get_env_report_structure():
    """验证环境报告包含核心字段"""
    report = mod.get_env_report()
    assert "python_ver" in report
    assert "is_venv" in report
    assert isinstance(report["is_venv"], bool)

def test_bootstrap_vscode_settings_logic(tmp_path):
    """验证配置初始化逻辑生成正确文件"""
    settings_file = mod.bootstrap_vscode_settings(tmp_path)
    assert settings_file.exists()
    assert settings_file.name == "settings.json"
    
    with open(settings_file, "r") as f:
        data = json.load(f)
    assert data["editor.formatOnSave"] is True

def test_pytest_presence_in_report():
    """验证报告中能正确检测到 pytest (当前测试环境下应为 True)"""
    report = mod.get_env_report()
    assert report["pytest_installed"] is True
