---
title: 流程控制深度解析 (Flow Control)
module: testing
area: python_notes
stack: python
level: basics
status: active
tags: [python, flow-control, match-case, for-else, loops, performance]
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
- **问题场景**: 自动化测试需要根据接口返回的状态码执行不同的断言分支；或者需要不断轮询（Polling）某个任务直到成功或超时；或者在多级嵌套循环中高效查找目标。
- **学习目标**: 掌握 `if-elif-else` 的短路逻辑，熟练运用 `for-else` 搜索模式，并掌握 Python 3.10+ 的结构化模式匹配 (`match-case`)。
- **前置知识**: [核心容器](./collections.md)。

## 核心结论
- **短路逻辑**: `if A or B` 如果 A 为真，B 将不再执行。这常用于防御式编程（如检查对象是否为 None 再访问属性）。
- **Else 子句**: `for-else` 的 `else` 块只有在循环**正常结束**（未触发 `break`）时才会运行。
- **Match-Case**: 这是处理复杂条件分支（如状态分发）的最优选，支持模式解构和守卫条件。

## 原理拆解
- **迭代器协议**: `for` 循环底层通过调用 `iter()` 获取迭代器，并不断调用 `next()` 直到捕获 `StopIteration`。
- **真值测试**: Python 中 `0`, `""`, `[]`, `{}`, `None` 均为假 (False)，其余多为真。

## 官方文档与兼容性
| 规则名称 | 官方出处 | PEP 链接 | 兼容性 |
| :--- | :--- | :--- | :--- |
| 控制流教程 | [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) | N/A | Python 1.0+ |
| 模式匹配 | [Structural Pattern Matching](https://docs.python.org/3/reference/compound_stmts.html#match) | [PEP 634](https://peps.python.org/pep-0634/) | Python 3.10+ |
| `for-else` | [The for statement](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement) | N/A | Python 1.0+ |

## 代码示例

### 示例 1：智能轮询与 `while-else` (Timeout)
模拟等待后台任务完成，结合 `break` 和 `else` 区分“成功退出”与“超时失败”。

```python
import time
import random

def poll_task_status(max_retries=5):
    """
    演示 while-else：如果循环正常耗尽（即超时），执行 else 逻辑。
    """
    retries = 0
    while retries < max_retries:
        # 模拟状态检查
        status = random.choice(["PENDING", "RUNNING", "SUCCESS"])
        print(f"Retry {retries}: Status is {status}")
        
        if status == "SUCCESS":
            print("Task completed successfully!")
            break # 正常退出循环，跳过 else
        
        retries += 1
        time.sleep(0.01)
    else:
        # 只有在 while 条件变为假（即达到 max_retries）时才执行
        raise TimeoutError("Task timed out after maximum retries")

# poll_task_status()
```

### 示例 2：结构化模式匹配 (Match-Case)
处理复杂的 API 响应分发，支持多值匹配和守卫。

```python
def handle_api_response(response: dict):
    """
    Python 3.10+ match-case 示例。
    """
    match response:
        case {"status": 200, "data": data}:
            return f"Success with: {data}"
        case {"status": 401 | 403}:
            return "Auth Error: Access Denied"
        case {"status": code} if code >= 500:
            return f"Server Error: {code}"
        case _:
            return "Unknown Response Format"

# 验证
print(handle_api_response({"status": 200, "data": "OK"}))
assert "Auth Error" in handle_api_response({"status": 403})
```

### 示例 3：双重循环下的 `continue` 与 `break`
演示在处理测试矩阵（环境 x 用例）时如何跳过特定组合。

```python
envs = ["dev", "test", "prod"]
cases = ["smoke", "stress", "perf"]

results = []
for env in envs:
    if env == "prod":
        continue # 生产环境不跑这些实验性用例
        
    for case in cases:
        if env == "dev" and case == "perf":
            break # 开发环境不跑性能测试，跳出内层循环
        results.append(f"{env}_{case}")

print(f"Matrix run: {results}")
assert "prod_smoke" not in results
```

## 性能基准测试
对比不同循环方式在大数据量下的执行效率。

```python
import timeit

data = list(range(10000))

def loop_filter():
    res = []
    for x in data:
        if x % 2 == 0: res.append(x)
    return res

def comp_filter():
    return [x for x in data if x % 2 == 0]

t_loop = timeit.timeit(loop_filter, number=1000)
t_comp = timeit.timeit(comp_filter, number=1000)

print(f"Standard Loop: {t_loop:.4f}s")
print(f"Comprehension: {t_comp:.4f}s")
print(f"Efficiency gain: {(t_loop - t_comp) / t_loop * 100:.1f}%")
```

## 易错点与最佳实践
| 特性 | 常见陷阱 | 最佳实践 |
| :--- | :--- | :--- |
| **可变性** | 在 `for` 循环中通过 `remove()` 修改正在遍历的列表。 | 遍历副本 `for x in data[:]` 或使用推导式。 |
| **死循环** | `while True` 忘记更新条件变量。 | 始终结合 `timeout` 或计数器机制。 |
| **else 误区** | 认为 `if-else` 的 `else` 和 `for-else` 逻辑一样。 | 记住 `for-else` 中的 `else` 是“无 break 补丁”。 |

## Self-Check
1. `if not my_list:` 这种写法相比 `if len(my_list) == 0:` 有什么优势？
2. 为什么在 Python 3.10 之前，我们通常用字典来模拟 `switch-case`？
3. `break` 只能跳出当前层循环吗？如何一次性跳出双重嵌套循环？（提示：通过异常或标志变量）。

## 参考链接
- [Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
- [PEP 634: Structural Pattern Matching](https://peps.python.org/pep-0634/)

---
[版本记录](./control_flow.md) | [返回首页](../README.md)
