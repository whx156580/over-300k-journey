---
title: 现代 Python 工具链：uv、PDM、Hatch 与 Nox
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, uv, pdm, hatch, nox, tooling, pyproject]
updated: 2026-04-17
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
- 现在的 Python 工程化已经不只是一句“用 pip 装依赖”，越来越多团队把依赖解析、虚拟环境、构建发布和任务编排统一到更现代的工具链里。
- `uv`、`PDM`、`Hatch`、`Nox` 这类工具，解决的是速度、隔离、任务矩阵和多版本验证这类更偏工程协作的问题。
- 如果你是从业者，只会 `pip install -r requirements.txt` 已经不太够了，至少要能看懂团队为什么选择这些工具。

## 学什么
- `uv` 更强调快和统一入口，`PDM`、`Hatch` 更偏项目与包管理，`Nox` 更适合定义多环境自动化任务。
- 现代工具链通常围绕 `pyproject.toml` 组织配置，而不是把依赖和构建逻辑分散在多个文件里。
- 真正要学的不是“谁最潮”，而是项目怎么统一依赖、虚拟环境、命令入口和多版本验证。

## 怎么用
### 示例 1：先把工具职责映射清楚

```python hl_lines="2 8"
tool_roles = {
    "uv": "fast dependency and environment workflow",
    "pdm": "project dependency management",
    "hatch": "project and build workflow",
    "nox": "automation sessions across environments"
}

print(sorted(tool_roles))
print(tool_roles["nox"])
```


### 示例 2：统一任务矩阵表达

```python hl_lines="2 7"
sessions = {
    "lint": ["ruff", "mypy"],
    "test-py39": ["pytest"],
    "test-py311": ["pytest"]
}

print(len(sessions), sessions["lint"][0])
```


### 示例 3：把 `pyproject` 关注点结构化

```python hl_lines="2 7"
pyproject_focus = {
    "dependencies": ["requests", "pydantic"],
    "dev_dependencies": ["pytest", "ruff"],
    "requires_python": ">=3.9"
}

print(pyproject_focus["requires_python"], len(pyproject_focus["dev_dependencies"]))
```


落地建议:
- 先统一一个主入口，再决定是否引入更多工具，不要多个工具同时半吊子落地。
- 无论选哪个工具，最关键的是团队成员都能复现同一套环境和命令。
- 多 Python 版本验证场景里，`Nox` 或类似任务编排工具的收益通常会非常高。

## 业界案例
- 工具仓库和 SDK 项目常需要在多个 Python 版本上跑测试，单靠手动切环境会越来越痛苦。
- 现代依赖工具的最大收益之一，是把“环境到底怎么建出来的”写成可执行配置，而不是口口相传。
- 很多团队换工具失败，不是工具不好，而是没有先统一使用边界和仓库约定。

## 延伸阅读
- 这类工具没有唯一标准答案，关键是团队是否已经统一到某一种工作流。
- 如果项目已经用传统 `pip + venv + tox` 跑得很稳，也不必为了新而新；重点是能否低摩擦复现环境。
- 真正值得投入的是减少环境漂移、缩短安装时间和统一命令入口，而不是追逐工具名词。

## Self-Check
### 概念题
1. 为什么现代 Python 工具链越来越围绕 `pyproject.toml`？
2. `uv`、`PDM` / `Hatch`、`Nox` 解决的问题大致有什么不同？
3. 为什么说工具选型重点不在“谁更新”，而在“谁更适合团队工作流”？

### 编程题
1. 如何把依赖、开发依赖和 Python 版本要求结构化表达出来？
2. 如何表达一个最小的多环境任务矩阵？

### 实战场景
1. 你的团队同时要支持 Python 3.9 和 3.11，还要统一依赖安装和测试命令，你会优先补哪类工具能力？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
因为它能把依赖、构建、工具配置尽量收敛到一个项目入口，减少配置分散和环境漂移。
讲解回看: [学什么](#学什么)

### 概念题 2
`uv` 更偏统一且快速的依赖 / 环境工作流，`PDM` / `Hatch` 更偏项目与包管理，`Nox` 更偏任务矩阵和多环境自动化。
讲解回看: [学什么](#学什么)

### 概念题 3
因为工具再先进，如果团队里没有统一命令、统一环境和统一维护方式，最后还是会回到混乱。
讲解回看: [为什么学](#为什么学)

### 编程题 1
可以先用字典或 `pyproject` 配置模型收敛依赖、开发依赖和 Python 版本要求。
讲解回看: [代码示例](#代码示例)

### 编程题 2
可以先用 `session -> commands` 这样的映射结构表达，再映射到 `Nox` 或其他自动化工具。
讲解回看: [代码示例](#代码示例)

### 实战场景 1
我会优先补统一依赖入口和多环境任务编排能力，也就是依赖管理工具加多版本自动化执行工具。
讲解回看: [业界案例](#业界案例)

## 参考链接
- [uv 文档](https://docs.astral.sh/uv/)
- [PDM 文档](https://pdm-project.org/)
- [Hatch 文档](https://hatch.pypa.io/)
- [Nox 文档](https://nox.thea.codes/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-17: 新增“现代 Python 工具链：uv、PDM、Hatch 与 Nox”，补齐 Python 从业者常见工程化工具认知。

---
[返回 Python 学习总览](../README.md)
