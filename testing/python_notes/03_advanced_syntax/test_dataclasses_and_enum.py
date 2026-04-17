import pytest
import sys
import importlib.util
from dataclasses import is_dataclass
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
target_file = current_dir / "dataclasses_and_enum.md" # 错误：应该是 .py
# 纠正：
target_file = current_dir / "dataclasses_and_enum.py"
mod = load_module_from_path("modeling_logic", target_file)

def test_case_meta_frozen():
    """验证 frozen=True 保证不可变"""
    meta = mod.CaseMeta(id=1, author="tester")
    with pytest.raises(Exception): # 准确应为 FrozenInstanceError
        meta.id = 2 # type: ignore

def test_test_result_post_init_validation():
    """验证 __post_init__ 校验逻辑"""
    meta = mod.CaseMeta(1, "qa")
    with pytest.raises(ValueError, match="Duration cannot be negative"):
        mod.TestResult(meta=meta, duration=-1.0)

def test_test_result_default_factory():
    """验证 default_factory 保证实例间列表隔离"""
    meta = mod.CaseMeta(1, "qa")
    r1 = mod.TestResult(meta=meta)
    r2 = mod.TestResult(meta=meta)
    r1.tags.append("smoke")
    assert "smoke" not in r2.tags

def test_enum_comparison():
    """验证 Enum 成员比较"""
    status = mod.RunStatus.PASSED
    assert status == mod.RunStatus.PASSED
    assert status is mod.RunStatus.PASSED

def test_result_to_json_ready():
    """验证业务字典转换逻辑"""
    meta = mod.CaseMeta(10, "admin")
    res = mod.TestResult(meta=meta, status=mod.RunStatus.FAILED)
    json_data = mod.result_to_json_ready(res)
    
    assert json_data["status"] == "FAILED"
    assert json_data["meta"]["id"] == 10
    assert isinstance(json_data, dict)

def test_is_dataclass_check():
    """验证装饰器生效"""
    assert is_dataclass(mod.TestResult)
    assert is_dataclass(mod.CaseMeta)
