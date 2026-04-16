---
title: 打包发布：setuptools、wheel、twine 与私有 PyPI
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, packaging, wheel, twine, pep517]
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
- 当脚本开始被多个仓库复用时，复制粘贴会迅速变成维护噩梦，打包发布是把代码升级为可分发能力的关键一步。
- 理解构建、分发、安装三个阶段的边界，能帮助你在工具脚本、SDK 和测试框架之间形成稳定交付链路。
- 即使不公开发布到 PyPI，私有源和内部包管理在团队协作中也非常常见。

## 学什么
- `pyproject.toml`、PEP 517、PEP 518 负责描述构建后端和项目元数据。
- `wheel` 是常见二进制分发格式，`twine` 负责安全上传构建产物。
- 语义化版本号通过 `MAJOR.MINOR.PATCH` 表达兼容性变化，是团队发布协作的基础语言。

## 怎么用
### 示例 1：最小 `pyproject.toml`

```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "qa-tools"
version = "0.1.0"
description = "Utilities for test automation"
requires-python = ">=3.8"
```


### 示例 2：版本号校验脚本

```python hl_lines="4 6 7"
import re

version = "1.4.2"
pattern = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")
match = pattern.match(version)

assert match is not None
print(tuple(int(part) for part in match.groups()))
```


### 示例 3：构建与发布命令

```bash
python -m pip install --upgrade build twine
python -m build
twine check dist/*
twine upload --repository-url https://pypi.example.com/simple/ dist/*
```


发布建议:
- 新项目优先用 `pyproject.toml`，避免旧式 `setup.py` 配置分散。
- 先在测试环境或私有源验证安装链路，再决定是否提升版本并正式发布。
- 对外发布遵循语义化版本；对内发布也建议保留清晰版本节奏和变更记录。

## 业界案例
- 团队会把公共 API 客户端、测试数据工具和报告 SDK 打成内部包，供多个仓库复用。
- CI 常在打 tag 后自动构建 wheel，并发布到私有 PyPI 或制品仓库。
- 版本号语义清晰时，调用方能更快判断升级是否涉及破坏性变更。

## 延伸阅读
- [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [PEP 517](https://peps.python.org/pep-0517/)
- [PEP 518](https://peps.python.org/pep-0518/)

## Self-Check
### 概念题
1. 构建、分发、安装三个阶段分别关注什么？
2. 为什么现代 Python 项目更推荐 `pyproject.toml`？
3. 语义化版本号里何时应该升级主版本？

### 编程题
1. 如何在脚本里粗略校验一个版本号是否符合 `MAJOR.MINOR.PATCH`？
2. 构建 wheel 并检查发布包通常需要哪几步？

### 实战场景
1. 你们团队有多个自动化仓库都在复制同一套公共工具函数，什么时候该考虑打包发布？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
构建生成可分发产物，分发负责把产物上传到仓库，安装则是调用方从仓库拉取并装到环境里。三者是相邻但不同的链路阶段。
讲解回看: [为什么学](#为什么学)

### 概念题 2
因为它把构建系统和项目元数据集中到一个标准文件里，更符合新工具链，也更容易被生态统一识别。
讲解回看: [学什么](#学什么)

### 概念题 3
当你引入不向后兼容的变更时，应该提升主版本号。新增兼容功能升次版本，兼容性修复升补丁版本。
讲解回看: [学什么](#学什么)

### 编程题 1
可以像示例 2 那样用正则 `^(\d+)\.(\d+)\.(\d+)$` 匹配，再把各段转成整数。
讲解回看: [怎么用](#怎么用)

### 编程题 2
先安装 `build` 和 `twine`，执行 `python -m build` 构建产物，再用 `twine check dist/*` 做基础校验，最后上传到目标仓库。
讲解回看: [怎么用](#怎么用)

### 实战场景 1
当重复代码已经开始频繁同步、修一个地方要到处手改时，就应该考虑抽出公共包并通过版本发布统一分发，减少维护分叉。
讲解回看: [业界案例](#业界案例)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-16: 初版整理，补齐示例、自测题与落地建议。

---
[返回 Python 学习总览](../README.md)
