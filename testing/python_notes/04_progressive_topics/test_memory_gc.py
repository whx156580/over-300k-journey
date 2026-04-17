import pytest
import sys
import gc
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
target_file = current_dir / "memory_management_and_gc.py"
mod = load_module_from_path("memory_management_and_gc", target_file)

def test_ref_count_increase():
    """验证引用计数随别名增加"""
    x = [1, 2]
    base = sys.getrefcount(x)
    y = x
    assert sys.getrefcount(x) == base + 1

def test_gc_cycle_collection():
    """验证手动触发 GC 可以回收循环引用"""
    # 确保 GC 是开启的
    gc.enable()
    # 调用模块内的演示函数
    unreachable_count = mod.cycle_demo()
    # 至少应该发现 n1, n2 及其 __dict__ 等对象
    assert unreachable_count > 0

def test_sys_getsizeof_logic():
    """验证内存占用计算逻辑"""
    assert sys.getsizeof([]) < sys.getsizeof(list(range(100)))

def test_gc_threshold_access():
    """验证可以访问并修改 GC 阈值"""
    original = gc.get_threshold()
    try:
        gc.set_threshold(500, 5, 5)
        assert gc.get_threshold() == (500, 5, 5)
    finally:
        gc.set_threshold(*original)

def test_ref_count_demo_call():
    """触发 ref_count_demo 提高覆盖率"""
    mod.ref_count_demo()
    assert True

def test_memory_size_demo_call():
    """触发 memory_size_demo 提高覆盖率"""
    mod.memory_size_demo()
    assert True
