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
target_file = current_dir / "asyncio_advanced_patterns.py"
mod = load_module_from_path("asyncio_logic", target_file)

@pytest.mark.asyncio
async def test_slow_task_timeout():
    """验证超时引发 TimeoutError"""
    with pytest.raises(asyncio.TimeoutError):
        await asyncio.wait_for(mod.slow_task(1.0), timeout=0.01)

@pytest.mark.asyncio
async def test_slow_task_cancellation():
    """验证取消信号能被捕获并处理"""
    task = asyncio.create_task(mod.slow_task(1.0))
    await asyncio.sleep(0.01)
    task.cancel()
    res = await task
    # 注意：在我的实现中，CancelledError 被捕获并返回了字符串
    assert res == "CLEANED_UP"

@pytest.mark.asyncio
async def test_semaphore_limit():
    """验证信号量限制下的并发行为"""
    sem = asyncio.Semaphore(2)
    tasks = [mod.limited_worker(sem, i) for i in range(5)]
    results = await asyncio.gather(*tasks)
    assert len(results) == 5
    assert results[0] == 0
    assert results[4] == 8

@pytest.mark.asyncio
async def test_producer_consumer_queue():
    """验证队列的生产消费完整链路"""
    q = asyncio.Queue()
    results = []
    items = ["a", "b", "c"]
    
    await asyncio.gather(
        mod.producer(q, items),
        mod.consumer(q, results)
    )
    
    assert results == ["processed_a", "processed_b", "processed_c"]
    assert q.empty()

@pytest.mark.asyncio
async def test_wait_for_success():
    """验证正常完成的任务"""
    res = await asyncio.wait_for(mod.slow_task(0.01), timeout=0.1)
    assert res == "COMPLETED"
