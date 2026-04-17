---
title: 函数进阶与作用域 (Functions & Scopes)
module: testing
area: python_notes
stack: python
level: basics
status: active
tags: [python, function, scope, legb, closures, nonlocal]
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
- **问题场景**: 在复杂测试脚本中，变量名冲突导致数据被意外覆盖；或者需要通过“闭包”技术在多个测试步骤间共享某些不希望暴露为全局变量的状态。
- **学习目标**: 深度理解 Python 的 LEGB 作用域查找规则，掌握 `global` 与 `nonlocal` 的正确用法，并能编写具备状态保持能力的闭包函数。
- **前置知识**: [变量与数据类型](./variables_and_types.md)。

## 核心结论
- **LEGB 查找**: Python 按 **L**ocal (局部) -> **E**nclosing (嵌套) -> **G**lobal (全局) -> **B**uilt-in (内置) 的顺序检索变量。
- **闭包 (Closure)**: 内部函数引用了外部嵌套函数的变量，且该内部函数被返回时，会形成闭包，保留当时的上下文状态。
- **nonlocal**: 专门用于在嵌套函数中修改外部（但非全局）作用域的变量绑定。

## 原理拆解
- **名称空间 (Namespace)**: 变量名与对象的映射表。函数调用时会创建独立的局部名称空间，调用结束通常即销毁。
- **自由变量 (Free Variable)**: 在函数中使用但未在函数体中定义的变量（由闭包捕获）。

## 官方文档与兼容性
| 规则名称 | 官方出处 | PEP 链接 | 兼容性 |
| :--- | :--- | :--- | :--- |
| 作用域规则 | [Naming and binding](https://docs.python.org/3/reference/executionmodel.html#naming-and-binding) | N/A | Python 1.0+ |
| `nonlocal` 关键字 | [The nonlocal statement](https://docs.python.org/3/reference/simple_stmts.html#nonlocal) | [PEP 3104](https://peps.python.org/pep-3104/) | Python 3.0+ |
| 关键字限定参数 | [Function definitions](https://docs.python.org/3/reference/compound_stmts.html#function-definitions) | [PEP 3102](https://peps.python.org/pep-3102/) | Python 3.0+ |

## 代码示例

### 示例 1：LEGB 查找链深度演示
观察同名变量在不同作用域层级下的遮蔽 (Shadowing) 效应。

```python
# G: Global
x = "global"

def outer():
    # E: Enclosing
    x = "enclosing"
    
    def inner():
        # L: Local
        # 如果取消注释下一行，则会遮蔽 E 和 G
        # x = "local"
        return x
    
    return inner()

print(f"Result: {outer()}") # 应返回 "enclosing"
assert outer() == "enclosing"
```

### 示例 2：闭包与状态保持 (Counter)
利用闭包实现一个不需要全局变量、也不需要类的轻量级计数器。

```python
def make_counter(start: int = 0):
    """
    闭包示例：make_counter 的局部变量 count 被 inner 捕获。
    """
    count = start
    
    def increment():
        nonlocal count # 声明修改外部嵌套作用域的变量
        count += 1
        return count
    
    return increment

counter_a = make_counter(10)
print(f"A-1: {counter_a()}") # 11
print(f"A-2: {counter_a()}") # 12

counter_b = make_counter(0)
print(f"B-1: {counter_b()}") # 1
```

### 示例 3：关键字强制参数与默认值陷阱
演示如何通过 `*` 强制调用方使用关键字参数，并规避可变默认参数坑。

```python
def safe_append(item, target_list=None):
    """
    最佳实践：使用 None 作为默认值，避免共享同一个列表对象。
    """
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list

def config_runner(*, env="test", debug=False):
    """
    关键字强制参数：调用时必须写 env="prod"。
    """
    return f"Running {env} (debug={debug})"

# 验证
print(config_runner(env="staging"))
# config_runner("staging") # 会抛出 TypeError
```

## 性能基准测试
对比闭包访问与类实例属性访问的性能。

```python
import timeit

def benchmark_closure():
    def make_adder(x):
        def adder(y): return x + y
        return adder
    add_five = make_adder(5)
    return lambda: add_five(10)

class Adder:
    def __init__(self, x): self.x = x
    def add(self, y): return self.x + y

obj_adder = Adder(5)
benchmark_class = lambda: obj_adder.add(10)

t_closure = timeit.timeit(benchmark_closure(), number=1000000)
t_class = timeit.timeit(benchmark_class, number=1000000)

print(f"Closure Access: {t_closure:.4f}s")
print(f"Class Access: {t_class:.4f}s")
```

## 易错点与最佳实践
| 特性 | 常见陷阱 | 最佳实践 |
| :--- | :--- | :--- |
| **可变默认参数** | `def f(a=[])`，导致多次调用共享同一个 `a`。 | 始终使用 `None` 并在函数内初始化。 |
| **LEGB 遮蔽** | 局部变量名与内置函数（如 `list`, `sum`）重名。 | 避免使用 Python 关键字和高频内置函数名作为变量。 |
| **闭包循环捕获** | 在循环中创建闭包，所有闭包都引用了循环变量的最终值。 | 使用默认参数或 `partial` 固定当前循环值。 |

## Self-Check
1. 为什么在 `inner` 函数里可以直接读 `outer` 的变量，但修改它却必须加 `nonlocal`？
2. `global` 关键字在什么场景下应该被严格禁止？
3. 如何判断一个函数对象是否形成了闭包？（提示：查看 `__closure__` 属性）。

## 参考链接
- [Python Execution Model](https://docs.python.org/3/reference/executionmodel.html)
- [Closures in Python Explained](https://example.com)

---
[版本记录](./function_basics.md) | [返回首页](../README.md)
