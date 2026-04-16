---
title: 并发模型：线程、进程、协程与 GIL
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, concurrency, threading, asyncio, multiprocessing]
updated: 2026-04-16
---

## 目录
- [为什么学](#为什么学)
- [学什么](#学什么)
- [怎么用](#怎么用)
- [业界案例](#业界案例)
- [延伸阅读](#延伸阅读)
- [Self-Check](#Self-Check)
- [参考答案](#参考答案)
- [参考链接](#参考链接)
- [版本记录](#版本记录)

## 为什么学
- 测试工程会同时面对 I/O 密集型任务、CPU 密集型任务和高并发调度问题，单靠同步脚本很快就会遇到瓶颈。
- 理解线程、进程、协程和 GIL 的边界，能帮助你选择正确模型，而不是盲目“并发化”。
- 本节重点是“什么时候该用什么”，而不只是会写几个 API 调用。

## 学什么
- 线程适合 I/O 密集型任务；进程适合 CPU 密集型任务；协程适合大量可挂起的异步 I/O 任务。
- CPython 的 GIL 限制了同一进程内多个线程并行执行 Python 字节码，但不阻止 I/O 并发。
- `multiprocessing`、`concurrent.futures`、`asyncio` 是最常见的三套工程化入口。

## 怎么用
### 示例 1：ThreadPoolExecutor

```python hl_lines="5 9"
from concurrent.futures import ThreadPoolExecutor
import time


def fetch(name: str) -> str:
    time.sleep(0.01)
    return f"done:{name}"


with ThreadPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(fetch, ["api", "ui", "perf"]))

print(results)
```


### 示例 2：asyncio 事件循环

```python hl_lines="4 8 12"
import asyncio


async def fetch(name: str) -> str:
    await asyncio.sleep(0.01)
    return f"async:{name}"


async def main() -> None:
    results = await asyncio.gather(fetch("a"), fetch("b"))
    print(results)


asyncio.run(main())
```


### 示例 3：进程池入口示意

```python hl_lines="8 9"
from concurrent.futures import ProcessPoolExecutor


def square(value: int) -> int:
    return value * value


if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=2) as executor:
        print(list(executor.map(square, [1, 2, 3])))
else:
    print("process example skipped in imported mode")
```


选型口诀:
- I/O 密集：优先线程或协程。
- CPU 密集：优先进程。
- 数量巨大且大多在等待：优先协程。

## 业界案例
- 批量接口巡检、批量页面冒烟、批量文件上传下载通常适合线程池或协程。
- 压测数据预处理、日志大规模解析、图像对比等 CPU 密集任务更适合进程池。
- 异步爬虫、消息消费、WebSocket 监听这类高连接数场景通常会选 asyncio。

## 延伸阅读
- [asyncio 文档](https://docs.python.org/3/library/asyncio.html)
- [concurrent.futures 文档](https://docs.python.org/3/library/concurrent.futures.html)
- 选型时先看任务类型，再看团队维护成本和生态配套。

## Self-Check
### 概念题
1. GIL 为什么不意味着“Python 线程没用”？
2. 线程、进程、协程三者最核心的选择依据是什么？
3. `asyncio` 的事件循环在做什么？

### 编程题
1. 如何快速把多个 I/O 任务并发执行起来？
2. 为什么进程池示例常写在 `if __name__ == "__main__":` 里？

### 实战场景
1. 你要同时跑 300 个接口健康检查，每个请求都要等待网络返回，最先考虑哪种并发模型？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
因为 GIL 主要限制的是同一时刻执行 Python 字节码的线程数量，但 I/O 等待期间线程仍然可以切换，所以线程对 I/O 密集任务依然有效。
讲解回看: [学什么](#学什么)

### 概念题 2
看任务是 I/O 密集还是 CPU 密集，以及任务规模和调用栈是否天然适合异步。线程偏 I/O，进程偏 CPU，协程偏海量可挂起 I/O。
讲解回看: [学什么](#学什么)

### 概念题 3
它负责调度协程，在它们遇到 `await` 可挂起点时切换执行，让单线程也能高效处理大量并发 I/O 任务。
讲解回看: [怎么用](#怎么用)

### 编程题 1
同步代码可先用 `ThreadPoolExecutor`；异步代码可用 `asyncio.gather()` 同时等待多个协程结果。
讲解回看: [怎么用](#怎么用)

### 编程题 2
尤其在 Windows 上，子进程会重新导入主模块。加这层保护可以避免递归创建进程和入口重复执行。
讲解回看: [怎么用](#怎么用)

### 实战场景 1
优先考虑线程池或 asyncio，因为这类任务主要卡在网络 I/O。是否选协程，再看现有代码栈是不是异步友好。
讲解回看: [业界案例](#业界案例)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-16: 初版整理，补齐示例、自测题与落地建议。

---
[返回 Python 学习总览](../README.md)
