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
target_file = current_dir / "function_basics.py"
mod = load_module_from_path("function_basics", target_file)

def test_scope_logic():
    """验证 LEGB 查找逻辑"""
    assert mod.scope_demo() == "enclosing"

def test_closure_counter():
    """验证闭包计数器独立性与状态保持"""
    c1 = mod.make_counter(0)
    c2 = mod.make_counter(100)
    
    assert c1() == 1
    assert c1() == 2
    assert c2() == 101
    assert c1() == 3

def test_safe_append_isolation():
    """验证默认参数隔离逻辑"""
    l1 = mod.safe_append("a")
    l2 = mod.safe_append("b")
    assert l1 == ["a"]
    assert l2 == ["b"]
    assert l1 is not l2

def test_keyword_only_args():
    """验证强制关键字参数约束"""
    assert mod.run_test(env="prod") == "Running in prod"
    with pytest.raises(TypeError):
        mod.run_test("prod") # type: ignore

def test_closure_internal_check():
    """验证函数对象包含闭包单元"""
    c = mod.make_counter(0)
    # 查看内部函数的闭包单元
    assert c.__closure__ is not None
    assert len(c.__closure__) == 1
    # 验证闭包单元中的值
    assert c.__closure__[0].cell_contents == 0
    c()
    assert c.__closure__[0].cell_contents == 1
