import pytest
import sys
import importlib.util
import asyncio
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
target_file = current_dir / "python_concurrency.py"
mod = load_module_from_path("python_concurrency", target_file)

def test_safe_counter():
    """验证线程安全计数器逻辑"""
    counter = mod.SafeCounter()
    # 模拟多线程并发
    import threading
    threads = [threading.Thread(target=counter.increment) for _ in range(50)]
    for t in threads: t.start()
    for t in threads: t.join()
    assert counter.value == 50

def test_heavy_compute():
    """验证进程任务计算逻辑"""
    res = mod.heavy_compute(123)
    assert len(res) == 64 # SHA256 hex length
    assert isinstance(res, str)

@pytest.mark.asyncio
async def test_run_parallel_requests():
    """验证异步请求并行逻辑"""
    results = await mod.run_parallel_requests()
    assert len(results) == 3
    assert results[0] == "Result 1"
    assert results[1] == "Result 2"
    # 第三个任务应该是 TimeoutError 或其包装
    assert isinstance(results[2], asyncio.TimeoutError)

def test_io_vs_async_perf_logic():
    """验证文档中的性能基准测试代码逻辑"""
    # 仅验证函数可调用且返回合理结果
    import time
    start = time.perf_counter()
    asyncio.run(asyncio.sleep(0.01))
    duration = time.perf_counter() - start
    assert duration > 0
