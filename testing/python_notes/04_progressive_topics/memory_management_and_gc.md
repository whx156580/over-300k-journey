---
title: 内存管理与 GC 调优 (Memory Management & GC)
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, memory, gc, reference-counting, performance]
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
- **问题场景**: 自动化任务长时间运行导致内存泄漏、大数据处理脚本频繁触发 Full GC 导致系统停顿。
- **学习目标**: 深入理解 CPython 内存分配模型，掌握引用计数与分代回收的底层机制，能够通过 `gc` 和 `sys` 模块进行线上故障排查与性能调优。
- **前置知识**: [性能剖析](./python_profiling.md)。

## 核心结论
- **双重机制**: CPython 核心是引用计数 (Reference Counting)，辅以分代回收 (Generational GC) 解决循环引用。
- **内存池 (Pymalloc)**: 针对 <= 512 字节的小对象使用专用 Arena/Pool 机制，减少系统调用。
- **不可达对象**: GC 主要针对“不可达”的循环引用对象。

## 原理拆解
- **引用计数**: 每个对象头部的 `ob_refcnt`。优点是实时释放，缺点是无法处理 $A \leftrightarrow B$ 这种闭环。
- **三代回收**: 
    - **第 0 代**: 扫描频率最高，存放新创建对象。
    - **第 1 代**: 第 0 代扫描后存活的对象进入。
    - **第 2 代**: Full GC，扫描频率最低，存放长期存活对象。

## 官方文档与兼容性
| 规则名称 | 官方出处 | PEP 链接 | 兼容性 |
| :--- | :--- | :--- | :--- |
| `gc` 模块 | [gc — Garbage Collector interface](https://docs.python.org/3/library/gc.html) | N/A | Python 2.0+ |
| 内存池机制 | [Memory Management](https://docs.python.org/3/c-api/memory.html) | [PEP 445](https://peps.python.org/pep-0445/) | Python 3.4+ |
| `sys.getrefcount` | [sys 模块](https://docs.python.org/3/library/sys.html#sys.getrefcount) | N/A | Python 1.5+ |

## 代码示例

### 示例 1：引用计数实验
观察对象引用的增加与销毁。

```python
import sys

def ref_count_demo():
    a = [1, 2, 3]
    print(f"Initial ref count: {sys.getrefcount(a)}") # getrefcount 本身会增加一次临时引用
    
    b = a
    print(f"After alias: {sys.getrefcount(a)}")
    
    c = [a]
    print(f"Inside list: {sys.getrefcount(a)}")
    
    del b
    print(f"After del alias: {sys.getrefcount(a)}")

ref_count_demo()
```

### 示例 2：循环引用与手动 GC
演示即便 `del` 了变量，循环引用仍会导致对象驻留在内存，直到 GC 介入。

```python
import gc

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

def cycle_demo():
    n1 = Node("n1")
    n2 = Node("n2")
    n1.next = n2
    n2.next = n1 # 形成循环引用
    
    print(f"GC threshold: {gc.get_threshold()}")
    del n1, n2 # 引用计数减 1，但由于互相引用，计数不为 0
    
    # 强制执行第 0 代回收
    unreachable = gc.collect(0)
    print(f"Unreachable objects found: {unreachable}")

cycle_demo()
```

### 示例 3：内存池观测 (sys.getsizeof)
理解小对象分配优化。

```python
import sys

# 空列表与含少量元素的列表
empty_list = []
small_list = [1]
large_list = list(range(1000))

print(f"Empty list size: {sys.getsizeof(empty_list)} bytes")
print(f"Small list size: {sys.getsizeof(small_list)} bytes")
print(f"Large list size: {sys.getsizeof(large_list)} bytes")
```

## 性能基准测试
演示禁用 GC 与手动触发 GC 对大批量任务的影响。

```python
import gc
import time

def generate_garbage():
    for _ in range(100000):
        # 产生带循环引用的对象
        a = {}
        b = {}
        a['b'] = b
        b['a'] = a

start = time.perf_counter()
gc.disable() # 临时禁用以观察内存压力
generate_garbage()
mid = time.perf_counter()
gc.enable()
gc.collect() # 手动清理
end = time.perf_counter()

print(f"Generate time (GC disabled): {mid - start:.4f}s")
print(f"Cleanup time: {end - mid:.4f}s")
```

## 易错点与最佳实践
| 特性 | 常见陷阱 | 最佳实践 |
| :--- | :--- | :--- |
| **循环引用** | 在长期运行的队列消费中，对象间互相持有导致 OOM。 | 使用 `weakref` (弱引用) 打断循环。 |
| **大对象清理** | 认为 `del obj` 就会立即释放大内存。 | `del` 只是删除引用，如需立即归还 OS，有时需调用 `gc.collect()`。 |
| **GC 频繁停顿** | 产生大量小对象导致第 0 代回收频繁。 | 调整 `gc.set_threshold` 或重用对象池。 |

## Self-Check
1. `sys.getrefcount(obj)` 返回的结果为什么总比预想的多 1？
2. 什么是“孤岛” (Island of isolation)？它是如何产生的？
3. `weakref.ref` 与普通引用在 GC 时有什么本质区别？

## 参考链接
- [Python Garbage Collection Internals](https://example.com)
- [CPython Memory Allocator Source](https://github.com/python/cpython/blob/main/Objects/obmalloc.c)

---
[版本记录](./memory_management_and_gc.md) | [返回首页](../README.md)
