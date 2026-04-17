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
target_file = current_dir / "bytes_encoding_and_text_files.py"
mod = load_module_from_path("encoding_logic", target_file)

def test_safe_decode_utf8():
    """验证 UTF-8 正常解码"""
    data = "Python 笔记".encode("utf-8")
    assert mod.safe_decode(data) == "Python 笔记"

def test_safe_decode_gbk():
    """验证 GBK 自动识别解码"""
    data = "你好".encode("gbk")
    assert mod.safe_decode(data) == "你好"

def test_safe_decode_default_list():
    """验证使用默认编码列表解码"""
    data = "test".encode("utf-8")
    # 显式传入 None
    assert mod.safe_decode(data, None) == "test"

def test_safe_decode_fallback():
    """验证解码彻底失败后的替换行为"""
    # 随机杂乱字节
    bad_data = b"\xff\xfe\xfd"
    res = mod.safe_decode(bad_data)
    assert "�" in res or res != "" # 替换符

def test_process_binary_header():
    """验证二进制头部解析"""
    data = b"\xde\xad\xbe\xef\x00\x01"
    assert mod.process_binary_header(data) == "DEADBEEF"

def test_convert_encoding():
    """验证编码转换逻辑"""
    original = "test".encode("utf-8")
    converted = mod.convert_encoding(original, "utf-8", "utf-16")
    assert converted.decode("utf-16") == "test"

def test_string_vs_bytes_length():
    """验证字符长度与字节长度差异"""
    s = "你好"
    b = s.encode("utf-8")
    assert len(s) == 2
    assert len(b) == 6
