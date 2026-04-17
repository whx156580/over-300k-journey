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
target_file = current_dir / "strings_and_methods.py"
mod = load_module_from_path("string_logic", target_file)

def test_format_test_summary():
    """验证 f-string 格式化输出"""
    res = mod.format_test_summary("Test", 10, 1.556)
    assert "Test           " in res # 15 chars left aligned
    assert "   10" in res # 5 chars right aligned
    assert "1.56s" in res # 2 decimal precision

def test_get_filename_from_path():
    """验证 raw string 路径解析"""
    path = r"D:\workspace\python\readme.md"
    assert mod.get_filename_from_path(path) == "readme.md"

def test_join_logs():
    """验证 join 拼接逻辑"""
    lines = ["A", "B", "C"]
    assert mod.join_logs(lines) == "A\nB\nC"
    assert mod.join_logs([]) == ""

def test_string_immutability():
    """验证字符串不可变性 (Python 核心行为)"""
    s = "hello"
    with pytest.raises(TypeError):
        s[0] = "H" # type: ignore

def test_raw_string_length():
    """验证 raw string 不转义行为"""
    s_normal = "\n"
    s_raw = r"\n"
    assert len(s_normal) == 1
    assert len(s_raw) == 2

def test_remove_prefix_behavior():
    """验证 Python 3.9+ removeprefix 行为"""
    s = "http://example.com"
    # 模拟 removeprefix (兼容 3.8)
    if hasattr(s, "removeprefix"):
        assert s.removeprefix("http://") == "example.com"
    else:
        prefix = "http://"
        assert (s[len(prefix):] if s.startswith(prefix) else s) == "example.com"
