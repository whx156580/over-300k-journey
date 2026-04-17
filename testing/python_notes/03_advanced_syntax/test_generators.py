import pytest
import sys
import importlib.util
import itertools
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
target_file = current_dir / "iterators_and_generators.py"
mod = load_module_from_path("iterators_and_generators", target_file)

def test_log_pipeline():
    """验证日志流水线过滤逻辑"""
    pipeline = mod.error_filter(mod.log_stream())
    results = list(itertools.islice(pipeline, 2))
    assert len(results) == 2
    assert all("[CRITICAL]" in r for r in results)
    assert "ERROR" in results[0]

def test_smart_accumulator():
    """验证双向通信生成器的累加与重置功能"""
    gen = mod.smart_accumulator()
    assert next(gen) == 0 # 初始值
    assert gen.send(5) == 5
    assert gen.send(10) == 15
    assert gen.send("reset") == 0
    assert gen.send(7) == 7

def test_accumulator_type_error():
    """验证非预激调用 send 的错误 (Python 核心机制)"""
    gen = mod.smart_accumulator()
    with pytest.raises(TypeError, match="can't send non-None value to a just-started generator"):
        gen.send(10)

def test_resource_manager_safety():
    """验证生成器 close 时触发 finally 逻辑"""
    # 由于 resource_manager 内部只打印，我们通过外部观察其是否正常结束
    gen = mod.resource_manager("TEST")
    assert next(gen) == "HANDLE_TEST"
    gen.close()
    with pytest.raises(StopIteration):
        next(gen)

def test_memory_efficiency_logic():
    """验证生成器表达式的内存优势逻辑"""
    import sys
    n = 1000
    list_obj = [i for i in range(n)]
    gen_obj = (i for i in range(n))
    assert sys.getsizeof(gen_obj) < sys.getsizeof(list_obj)
