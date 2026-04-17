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
target_file = current_dir / "comments_and_input_output.py"
mod = load_module_from_path("io_logic", target_file)

def test_status_report_formatting():
    """验证报告生成格式"""
    res = mod.get_status_report("api", "failed")
    assert res == "[API] -> failed"

def test_parse_input_config_success():
    """验证合规输入的解析"""
    data = mod.parse_input_config(" 30, 5 ")
    assert data == {"age": 30, "retry": 5}

def test_parse_input_config_failure():
    """验证异常输入的解析"""
    assert mod.parse_input_config("invalid") is None
    assert mod.parse_input_config("30, abc") is None

def test_main_entry_logic(capsys):
    """验证入口函数的调度逻辑"""
    res = mod.main_entry(["--debug"])
    assert res == "SUCCESS"
    captured = capsys.readouterr()
    assert "DEBUG MODE ON" in captured.out

def test_docstring_presence():
    """验证核心函数包含文档字符串"""
    assert mod.get_status_report.__doc__ is not None
    assert "生成格式化的状态报告" in mod.get_status_report.__doc__
