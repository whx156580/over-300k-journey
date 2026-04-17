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
target_file = current_dir / "breakpoint_and_pdb_basics.py"
mod = load_module_from_path("debug_logic", target_file)

def test_custom_hook_execution(capsys):
    """验证断点 hook 是否被正确调用并输出快照"""
    res = mod.run_business_logic(5)
    assert res == 10
    captured = capsys.readouterr()
    assert "[SNAPSHOT]" in captured.out
    assert "'x': '10'" in captured.out

def test_buggy_calc_error():
    """验证除零错误正常抛出"""
    with pytest.raises(ZeroDivisionError):
        mod.buggy_calc(1, 0)

def test_breakpointhook_reset():
    """验证 hook 在逻辑执行后被还原 (通过测试模块环境判断)"""
    original = sys.breakpointhook
    mod.run_business_logic(1)
    assert sys.breakpointhook == original

def test_pdb_module_presence():
    """验证调试核心库可用"""
    import pdb
    assert hasattr(pdb, "set_trace")
    assert hasattr(pdb, "post_mortem")
