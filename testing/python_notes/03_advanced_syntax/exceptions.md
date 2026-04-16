---
title: 异常体系
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, exception, raise-from, logging, error-handling]
updated: 2026-04-16
---

## 目录
- [概念](#概念)
- [核心机制](#核心机制)
- [代码示例](#代码示例)
- [易错点](#易错点)
- [小练习](#小练习)
- [Self-Check](#Self-Check)
- [参考答案](#参考答案)
- [参考链接](#参考链接)
- [版本记录](#版本记录)

## 概念
- 异常是 Python 里表达错误路径的正式机制，不是“程序崩了以后才会看到的附属产物”。
- 设计异常时要考虑可读性、可恢复性和排障上下文，而不是只图省事地 `except Exception`。
- 自定义异常和异常链能让定位问题时保留更多业务语义。

## 核心机制
- 内置异常按层级组织，`BaseException` 在最顶层，业务代码通常只处理 `Exception` 体系。
- `raise` 抛出异常，`raise from` 用于显式建立异常链。
- `try/except/else/finally` 分别用于捕获、正常分支、以及清理收尾。
- 日志记录异常时优先使用 `logger.exception` 或 `exc_info=True`，不要吞掉关键信息。

## 代码示例
### 示例 1：自定义异常

```python hl_lines="1 6"
class ValidationError(Exception):
    """Raised when input payload is invalid."""


def validate_age(age: int) -> None:
    if age < 0:
        raise ValidationError("age must be non-negative")


validate_age(1)
print("ok")
```


### 示例 2：`raise from`

```python hl_lines="4 5 10"
def parse_port(value: str) -> int:
    try:
        return int(value)
    except ValueError as error:
        raise ValueError(f"invalid port: {value}") from error


try:
    parse_port("abc")
except ValueError as exc:
    print(type(exc.__cause__).__name__)
```


### 示例 3：日志记录最佳实践

```python hl_lines="7 9"
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    raise RuntimeError("network timeout")
except RuntimeError:
    logger.exception("request failed")
```

## 易错点
- 直接 `except Exception: pass` 会吞掉错误，让问题在更远的地方以更隐蔽的方式爆出来。
- 把业务校验错误和系统错误混在同一个异常类型里，会让调用方难以决定是否可重试。
- 日志里只记录“失败了”而不带异常栈，等于放弃了最重要的排障线索。

## 小练习
1. 为配置加载逻辑定义一个自定义异常，表达“必填字段缺失”。
2. 把底层 `KeyError` 包装成更易懂的业务异常，并保留原始异常链。
3. 写一个 `try/except/finally` 示例，验证 finally 始终执行。


建议先手写一遍，再对照“参考答案”检查抽象边界是否清晰。

## Self-Check
### 概念题
1. 为什么业务代码通常只捕获 `Exception` 体系，而不去捕获 `BaseException`？
2. `raise from` 相比直接重新抛异常，多了什么价值？
3. 为什么“异常日志要带栈信息”是基本要求？

### 编程题
1. 如何把 `KeyError` 包装成更易懂的配置异常？
2. 如何在记录日志时自动附带当前异常栈？

### 实战场景
1. 在自动化测试框架里，哪些异常应该被重试，哪些应该直接失败？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
因为 `BaseException` 还包含 `SystemExit`、`KeyboardInterrupt` 等系统级信号，业务代码不应该随意吞掉这些退出机制。
讲解回看: [核心机制](#核心机制)

### 概念题 2
它显式保留了底层异常作为 `__cause__`，方便你同时看到业务语义和原始错误来源。
讲解回看: [核心机制](#核心机制)

### 概念题 3
因为没有栈就很难知道错误是在哪一层、哪条路径发生的。只靠一条字符串日志通常无法复盘完整上下文。
讲解回看: [概念](#概念)

### 编程题 1
在 `except KeyError as error` 中抛出自定义异常，并用 `raise ConfigError(...) from error` 保留原始因果关系。
讲解回看: [代码示例](#代码示例)

### 编程题 2
在 `except` 块中调用 `logger.exception("...")`，或者 `logger.error("...", exc_info=True)`。
讲解回看: [代码示例](#代码示例)

### 实战场景 1
网络抖动、临时超时等可恢复错误可以考虑重试；断言失败、数据不合法、配置缺失等确定性错误应直接失败并尽快暴露。
讲解回看: [易错点](#易错点)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-16: 初版整理，补齐示例、自测题与落地建议。

---
[返回 Python 学习总览](../README.md)
