---
title: 面向 Python 工程的 Linux 与 Shell 基础
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, linux, shell, subprocess, environment]
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
- Python 真正进入工程环境后，几乎总要和 Linux、Shell、环境变量、进程、日志文件这些系统能力打交道。
- 很多“脚本明明能跑，线上却不工作”的问题，本质上不是 Python 语法，而是工作目录、权限、路径、依赖和子进程边界没处理好。
- 对测试开发来说，Linux 基础也是 CI、容器、远程执行和日志排障的共同前置。

## 学什么
- 先搞清 `PATH`、当前工作目录、环境变量、标准输入输出、退出码这些最基础的运行时概念。
- Shell 负责把命令组织起来；Python 则更适合承载复杂逻辑、数据处理和错误控制，两者不要互相替代。
- 进程调用要优先考虑参数安全、超时、输出采集和失败回传，而不是只看“命令有没有执行”。

## 怎么用
### 示例 1：读取环境变量并构造路径

```python hl_lines="1 5 7"
import os
from pathlib import Path

workspace = Path.cwd()
env_name = os.getenv("APP_ENV", "local")
log_dir = workspace / "logs" / env_name

print(workspace.name, log_dir.as_posix().endswith(env_name))
```


### 示例 2：安全执行子进程命令

```python hl_lines="1 5 10"
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "-c", "print('shell-ok')"],
    capture_output=True,
    text=True,
    check=True,
)

print(result.stdout.strip(), result.returncode)
```


### 示例 3：检查 PATH 与命令入口

```python hl_lines="1 4 8"
import os

path_segments = [segment for segment in os.getenv("PATH", "").split(os.pathsep) if segment]
python_like_segments = [segment for segment in path_segments if "python" in segment.lower()]

print(len(path_segments) > 0, len(python_like_segments) >= 0)
```


落地建议:
- 需要调用外部命令时，优先传参数列表，不拼接整段 shell 字符串。
- 任何依赖当前目录的脚本，都要明确工作目录基准，最好用 `Path(__file__)` 或统一入口管理。
- 线上排障时把“环境变量、可执行文件路径、用户权限、日志目录”列成固定检查清单，会比临场猜快很多。

## 业界案例
- CI 脚本最常见的问题之一是本地工作目录和流水线工作目录不同，导致相对路径失效。
- 自动化平台调用 `pytest`、浏览器驱动或数据库客户端时，经常要用 `subprocess` 接管退出码和输出。
- 线上任务明明“没有报错”，但产物目录为空，通常要回到权限、环境变量和日志路径去排查。

## 延伸阅读
- 先用 Python 把复杂业务逻辑写清楚，再决定是否用 Shell 包一层调度，不要反过来。
- Windows 和 Linux 在路径分隔符、权限和默认编码上有差异，写工具脚本时要尽量用跨平台 API。
- 系统层问题最怕“盲猜”，最好把常见排障动作做成可重复的自查脚本。

## Self-Check
### 概念题
1. 为什么工作目录和环境变量会直接影响 Python 脚本行为？
2. 什么时候应该优先用 Python 而不是继续堆 Shell？
3. 为什么子进程调用要显式处理退出码和输出？

### 编程题
1. 怎样安全执行一个外部命令并拿到标准输出？
2. 如何检查当前环境里的 `PATH` 是否包含你预期的命令入口？

### 实战场景
1. 脚本在本地能跑，在 CI 上却报“文件不存在”，你第一轮会检查哪些系统层信息？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
因为脚本能否找到配置文件、日志目录和外部命令，很大程度取决于当前目录和环境变量是否符合预期。
讲解回看: [学什么](#学什么)

### 概念题 2
当逻辑涉及数据结构、错误处理、重试、解析和跨平台兼容时，应优先用 Python；Shell 更适合薄薄一层调度。
讲解回看: [延伸阅读](#延伸阅读)

### 概念题 3
因为真正的成功标准不是“命令好像执行了”，而是退出码、输出内容和副作用都符合预期。
讲解回看: [怎么用](#怎么用)

### 编程题 1
使用 `subprocess.run()`，传入参数列表并开启 `capture_output=True`、`text=True`，必要时再加 `check=True`。
讲解回看: [怎么用](#怎么用)

### 编程题 2
读取 `os.getenv("PATH")`，按 `os.pathsep` 拆开后逐段检查，必要时可和预期路径做包含比对。
讲解回看: [怎么用](#怎么用)

### 实战场景 1
先看工作目录、相对路径基准、环境变量、产物目录权限、子进程退出码和日志输出，再去怀疑业务逻辑。
讲解回看: [业界案例](#业界案例)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [subprocess 文档](https://docs.python.org/3/library/subprocess.html)
- [pathlib 文档](https://docs.python.org/3/library/pathlib.html)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-17: 将 README1 中的 Linux / Shell 主题整理为 Python 工程配套专题。

---
[返回 Python 学习总览](../README.md)
