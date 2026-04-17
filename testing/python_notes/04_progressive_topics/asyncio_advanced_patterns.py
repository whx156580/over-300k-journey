import asyncio
import time
from typing import List, Optional, Any

# --- 示例 1: 超时与取消 ---

async def slow_task(duration: float) -> str:
    """模拟一个可能被取消的耗时任务"""
    try:
        await asyncio.sleep(duration)
        return "COMPLETED"
    except asyncio.CancelledError:
        # 清理逻辑
        return "CLEANED_UP"

# --- 示例 2: 信号量限流 ---

async def limited_worker(sem: asyncio.Semaphore, job_id: int) -> int:
    """受限并发的工作协程"""
    async with sem:
        await asyncio.sleep(0.01) # 模拟工作
        return job_id * 2

# --- 示例 3: 生产者-消费者队列 ---

async def producer(queue: asyncio.Queue, items: List[Any]):
    for item in items:
        await queue.put(item)
    await queue.put(None) # 结束标志

async def consumer(queue: asyncio.Queue, results: List[Any]):
    while True:
        item = await queue.get()
        if item is None:
            queue.task_done()
            break
        results.append(f"processed_{item}")
        queue.task_done()

if __name__ == "__main__":
    # 演示 1
    async def demo_timeout():
        try:
            res = await asyncio.wait_for(slow_task(1.0), timeout=0.1)
            print(f"Result: {res}")
        except asyncio.TimeoutError:
            print("Caught Timeout!")

    asyncio.run(demo_timeout())
