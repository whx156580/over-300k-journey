---
title: 并发模型 (Concurrency Models)
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, concurrency, threading, multiprocessing, asyncio, gil]
updated: 2026-04-17
---

## 目录
- [背景](#背景)
- [核心结论](#核心结论)
- [原理拆解](#原理拆解)
- [官方文档与兼容性](#官方文档与兼容性)
- [代码示例](#代码示例)
- [性能基准测试](#性能基准测试)
- [易错点与最佳实践](#易错点与最佳实践)
- [Self-Check](#Self-Check)
- [参考链接](#参考链接)
- [版本记录](#版本记录)

## 背景
- **问题场景**: 自动化测试中需要并发运行数千个测试用例、处理大量日志解析、或者构建高并发的模拟服务端。
- **学习目标**: 理解 GIL 的局限性，掌握线程、进程、协程的选型逻辑，能够处理并发中的资源竞争与同步问题。
- **前置知识**: [函数基础](../02_basic_syntax/function_basics.md)、[异常处理](../03_advanced_syntax/exceptions.md)。

## 核心结论
- **线程 (Threading)**: 适合 I/O 密集型任务（如 HTTP 请求），受 GIL 限制无法利用多核 CPU。
- **进程 (Multiprocessing)**: 适合 CPU 密集型任务（如复杂计算），拥有独立内存空间，利用多核。
- **协程 (Asyncio)**: 适合极高并发的 I/O 任务，单线程内切换，开销极低，但需配合异步库。

## 原理拆解
- **GIL (Global Interpreter Lock)**: CPython 的全局解释器锁，确保同一时刻只有一个线程执行字节码。
- **上下文切换**: 线程/进程切换由 OS 调度，协程切换由程序（事件循环）控制。

## 官方文档与兼容性
| 规则名称 | 官方出处 | PEP 链接 | 兼容性 |
| :--- | :--- | :--- | :--- |
| `threading` | [threading — Thread-based parallelism](https://docs.python.org/3/library/threading.html) | N/A | Python 1.5+ |
| `multiprocessing` | [multiprocessing — Process-based parallelism](https://docs.python.org/3/library/multiprocessing.html) | [PEP 371](https://peps.python.org/pep-0371/) | Python 2.6+ |
| `asyncio` | [asyncio — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html) | [PEP 3156](https://peps.python.org/pep-3156/) | Python 3.4+ |
| `TaskGroup` | [Task Groups](https://docs.python.org/3/library/asyncio-task.html#task-groups) | [PEP 654](https://peps.python.org/pep-0654/) | Python 3.11+ |

## 代码示例

### 示例 1：线程安全计数器 (Threading + Lock)
演示多线程下的资源竞争及如何使用锁保证原子操作。

```python
import threading
from concurrent.futures import ThreadPoolExecutor

class SafeCounter:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            # 临界区操作
            curr = self.value
            self.value = curr + 1

counter = SafeCounter()
with ThreadPoolExecutor(max_workers=10) as executor:
    for _ in range(1000):
        executor.submit(counter.increment)

print(f"Final count: {counter.value}") # 应为 1000
```

### 示例 2：海量数据并行处理 (Multiprocessing)
利用进程池加速 CPU 密集型计算（如生成大量哈希）。

```python
import hashlib
from multiprocessing import Pool, cpu_count

def heavy_compute(data: int) -> str:
    """CPU 密集型：多次哈希计算"""
    res = str(data)
    for _ in range(10000):
        res = hashlib.sha256(res.encode()).hexdigest()
    return res

if __name__ == "__main__":
    tasks = range(100)
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(heavy_compute, tasks)
    print(f"Computed {len(results)} hashes using {cpu_count()} cores.")
```

### 示例 3：高并发异步请求 (Asyncio + Timeout)
演示如何使用 `asyncio` 管理并发任务并设置超时。

```python
import asyncio

async def fetch_api(task_id: int, delay: float):
    print(f"Task {task_id} starting...")
    await asyncio.sleep(delay)
    if delay > 2.0:
        raise asyncio.TimeoutError(f"Task {task_id} exceeded time limit")
    return f"Result {task_id}"

async def main():
    tasks = [
        fetch_api(1, 1.0),
        fetch_api(2, 3.0), # 故意超时
    ]
    # return_exceptions=True 允许部分失败不影响整体
    results = await asyncio.gather(*tasks, return_exceptions=True)
    print(f"Async Results: {results}")

if __name__ == "__main__":
    asyncio.run(main())
```

## 性能基准测试
对比不同模型在 I/O 密集型任务中的表现。

```python
import time
import threading
import asyncio

def io_bound_task():
    time.sleep(0.1)

async def async_io_task():
    await asyncio.sleep(0.1)

def test_threading():
    threads = [threading.Thread(target=io_bound_task) for _ in range(50)]
    start = time.perf_counter()
    for t in threads: t.start()
    for t in threads: t.join()
    return time.perf_counter() - start

async def test_asyncio():
    start = time.perf_counter()
    await asyncio.gather(*(async_io_task() for _ in range(50)))
    return time.perf_counter() - start

print(f"Threading time: {test_threading():.4f}s")
print(f"Asyncio time: {asyncio.run(test_asyncio()):.4f}s")
```

## 易错点与最佳实践
| 特性 | 常见陷阱 | 最佳实践 |
| :--- | :--- | :--- |
| **线程** | 在多线程中直接修改共享列表/字典，导致数据不一致。 | 始终使用 `threading.Lock` 或 `queue.Queue` 进行同步。 |
| **进程** | 忘记在 Windows 下使用 `if __name__ == "__main__":` 保护。 | 必须使用入口保护，防止子进程递归导入。 |
| **协程** | 在 `async` 函数中使用同步 `time.sleep()` 阻塞整个事件循环。 | 始终使用 `await asyncio.sleep()`。 |

## Self-Check
1. 为什么计算密集型任务在 Python 线程中运行可能比单线程还慢？
2. `asyncio.gather` 与 `asyncio.wait` 的主要区别是什么？
3. 如何在进程间共享大型 NumPy 数组而无需复制内存？

## 参考链接
- [Python Concurrency Docs](https://docs.python.org/3/library/concurrency.html)
- [Modern Asyncio with Python 3.11+](https://example.com)

---
[版本记录](./python_concurrency.md) | [返回首页](../README.md)
