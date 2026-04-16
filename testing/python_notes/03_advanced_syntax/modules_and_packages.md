---
title: 模块与包
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, module, package, import, zipapp]
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
- 模块是单个 `.py` 文件，包是可以组织多个模块的目录结构。
- 合理的包结构能让测试工具、业务封装和共享能力边界更清晰，也能减少循环导入。
- 理解绝对导入、相对导入、命名空间包和打包入口，是项目工程化的重要基础。

## 核心机制
- `__init__.py` 常用于标记传统包、暴露公共 API 或执行轻量初始化。
- 绝对导入从项目根包开始写路径，清晰稳定；相对导入更适合包内部协作。
- `__all__` 可以控制 `from package import *` 暴露的名称，但团队代码里仍应少用星号导入。
- `zipapp` 可以把一个可执行包目录打成单文件归档，便于分发命令行工具。

## 代码示例
### 示例 1：动态导入标准库模块

```python hl_lines="3"
import importlib

json_module = importlib.import_module("json")
print(json_module.dumps({"status": "ok"}, sort_keys=True))
```


### 示例 2：定义 `__all__`

```python hl_lines="1"
__all__ = ["build_message"]


def build_message(name: str) -> str:
    return f"hello, {name}"


print(build_message("qa"))
```


### 示例 3：用 `zipapp` 生成可执行包

```python hl_lines="7 9 10"
import tempfile
import zipapp
from pathlib import Path

with tempfile.TemporaryDirectory() as temp_dir:
    root = Path(temp_dir) / "demo_app"
    root.mkdir()
    (root / "__main__.py").write_text('print("zipapp ready")\n', encoding="utf-8")
    target = Path(temp_dir) / "demo.pyz"
    zipapp.create_archive(root, target)
    print(target.exists())
```

## 易错点
- 随意在脚本根目录里使用相对导入，脱离包上下文运行时很容易直接报错。
- 在 `__init__.py` 里放太重的初始化逻辑，会让导入成本和副作用都变大。
- 循环导入往往不是导入语法本身的问题，而是模块职责拆分不清。

## 小练习
1. 设计一个 `client/` 包，对外只暴露 `HttpClient`。
2. 尝试把一个最小命令行脚本打成 `.pyz` 文件。
3. 把散落在脚本里的工具函数整理到包结构中，并改成绝对导入。


建议先手写一遍，再对照“参考答案”检查抽象边界是否清晰。

## Self-Check
### 概念题
1. 模块和包的最小区别是什么？
2. 绝对导入和相对导入各自适合什么场景？
3. `__all__` 真正控制的是什么？

### 编程题
1. 如何把一个目录快速打成可执行 `.pyz` 文件？
2. 为什么很多团队会在包根目录的 `__init__.py` 里只做轻量暴露？

### 实战场景
1. 你的自动化项目里既有 API 客户端、页面对象、公共断言、数据工厂，为什么应该尽早整理成包？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
模块通常是一个 `.py` 文件；包是组织多个模块的目录结构，能表达更清晰的命名空间和层次关系。
讲解回看: [概念](#概念)

### 概念题 2
绝对导入更清晰稳定，适合跨包依赖；相对导入适合包内部相邻模块协作，但不宜过深或过度复杂。
讲解回看: [核心机制](#核心机制)

### 概念题 3
它主要控制 `from module import *` 时可导出的名称集合，是一种 API 暴露声明，而不是访问权限控制。
讲解回看: [核心机制](#核心机制)

### 编程题 1
准备好包含 `__main__.py` 的目录后，调用 `zipapp.create_archive(source_dir, target_path)` 即可生成归档。
讲解回看: [代码示例](#代码示例)

### 编程题 2
因为这样导入成本更稳定，也更容易控制对外 API，避免引入复杂副作用和循环依赖。
讲解回看: [易错点](#易错点)

### 实战场景 1
因为包结构能明确模块边界，减少脚本式堆叠造成的循环依赖，也方便团队逐步演进到可测试、可分发、可复用的工程结构。
讲解回看: [概念](#概念)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-16: 初版整理，补齐示例、自测题与落地建议。

---
[返回 Python 学习总览](../README.md)
