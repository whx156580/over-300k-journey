import pytest
import sys
import importlib.util
import json
from datetime import datetime
from decimal import Decimal
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
target_file = current_dir / "structured_data_formats.py"
mod = load_module_from_path("data_format_logic", target_file)

def test_json_custom_serialization():
    """验证自定义类型的 JSON 序列化"""
    now = datetime(2026, 1, 1, 10, 0, 0)
    data = {"time": now, "price": Decimal("19.99")}
    res = mod.serialize_complex_data(data)
    
    parsed = json.loads(res)
    assert parsed["time"] == "2026-01-01T10:00:00"
    assert parsed["price"] == "19.99"

def test_csv_parsing():
    """验证 CSV 到字典的解析"""
    csv_text = "name,val\nAlice,10\nBob,20"
    res = mod.parse_csv_to_dicts(csv_text)
    assert len(res) == 2
    assert res[0]["name"] == "Alice"
    assert res[1]["val"] == "20"

def test_flat_to_nested_conversion():
    """验证扁平数据到嵌套结构的转换"""
    flat = [
        {"type": "A", "val": 1},
        {"type": "B", "val": 2},
        {"type": "A", "val": 3},
        {"val": 4} # 缺少 group_key
    ]
    nested = mod.convert_flat_to_nested(flat, "type")
    assert len(nested["A"]) == 2
    assert nested["B"][0]["val"] == 2
    assert nested["Other"][0]["val"] == 4

def test_json_ensure_ascii_logic():
    """验证中文字符不被转义"""
    data = {"msg": "你好"}
    res = mod.serialize_complex_data(data)
    assert "你好" in res
    assert "\\u" not in res

def test_json_unserializable_type():
    """验证无法序列化的类型触发 TypeError"""
    # 模拟一个既不是 datetime 也不是 Decimal 的对象
    class Unserializable: pass
    with pytest.raises(TypeError):
        mod.serialize_complex_data({"val": Unserializable()})
