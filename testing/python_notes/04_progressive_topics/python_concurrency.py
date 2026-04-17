import threading
import hashlib
import asyncio
import time
from multiprocessing import Pool, cpu_count
from concurrent.futures import ThreadPoolExecutor
from typing import List, Any

# --- 示例 1: 线程安全计数器 (Threading + Lock) ---

class SafeCounter:
    """
    线程安全计数器。
    原理: 使用 threading.Lock 保护共享资源。
    """
    def __init__(self) -> None:
        self.value = 0
        self._lock = threading.Lock()

    def increment(self) -> None:
        with self._lock:
            curr = self.value
            self.value = curr + 1

# --- 示例 2: 并行哈希计算 (Multiprocessing) ---

def heavy_compute(data: int) -> str:
    """
    CPU 密集型任务：计算多次哈希。
    """
    res = str(data)
    for _ in range(5000):
        res = hashlib.sha256(res.encode()).hexdigest()
    return res

# --- 示例 3: 异步 API 请求模拟 (Asyncio) ---

async def fetch_api(task_id: int, delay: float) -> str:
    """
    异步 I/O 模拟。
    """
    await asyncio.sleep(delay)
    if delay > 2.0:
        raise asyncio.TimeoutError(f"Task {task_id} timeout")
    return f"Result {task_id}"

async def run_parallel_requests() -> List[Any]:
    tasks = [
        fetch_api(1, 0.1),
        fetch_api(2, 0.2),
        fetch_api(3, 2.5), # 故意设置超时逻辑触发
    ]
    # return_exceptions=True 捕获异常而不中断整体
    return await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    # 线程测试
    counter = SafeCounter()
    with ThreadPoolExecutor(max_workers=5) as executor:
        for _ in range(100):
            executor.submit(counter.increment)
    print(f"Threads: final count {counter.value}")

    # 进程测试
    with Pool(processes=2) as pool:
        results = pool.map(heavy_compute, range(5))
    print(f"Processes: computed {len(results)} hashes")

    # 协程测试
    loop_results = asyncio.run(run_parallel_requests())
    print(f"Asyncio: results {loop_results}")
