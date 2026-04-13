# 🔢 变量与核心数据类型 (Variables & Types)

[TOC]

## 📖 背景 (Background)
Python 是动态强类型语言。理解其对象引用机制和类型标注是编写稳健代码的基础。
- **业务痛点**: 类型混淆导致的运行时错误（如 `TypeError`）。
- **解决方案**: 使用类型标注 (Type Hints) 和明确的比较逻辑。

## 🔬 语法规则 (Rules)
- **动态类型**: 变量无需声明，运行时绑定对象。
- **引用机制**: 变量名是指向内存中对象的标签。
- **is vs ==**: `==` 比较值是否相等，`is` 比较内存地址（身份）是否相同。

## 🚀 代码示例 (Implementation)

### 1. 类型标注 (Python 3.5+)
```python
age: int = 25
name: str = "Alice"
is_expert: bool = True

def greet(user: str) -> str:
    return f"Hello, {user}"
```

### 2. 比较逻辑
```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True (值相等)
print(a is b)  # False (不同对象)
print(a is c)  # True (同一引用)
```

## ⚠️ 易错点 (Pitfalls)
- **不可变对象缓存**: 小整数（-5 到 256）在 Python 中会被重用，因此 `a = 10; b = 10; a is b` 为 True，但这不适用于大整数或复杂对象。
- **类型覆盖**: 变量可以随时指向不同类型，但在实战中应尽量保持单一职责。

## ❓ Self-Check 清单
1. **概念题**: 为什么说 Python 是“强类型”但又是“动态类型”的？
2. **编程题**: 编写一个函数，接受一个参数并打印其类型和内存地址。
3. **实战场景**: 在什么情况下必须使用 `is None` 而不是 `== None`？

---
**版本记录**: v1.0 | 2026-04-13
