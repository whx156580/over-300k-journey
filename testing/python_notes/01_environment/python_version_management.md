---
title: Python 多版本管理：pyenv、venv、conda
module: testing
area: python_notes
stack: python
level: basics
status: active
tags: [python, environment, pyenv, venv, conda]
updated: 2026-04-16
---

## 目录
- [为什么要学](#为什么要学)
- [工具对比](#工具对比)
- [实战步骤](#实战步骤)
- [验证清单](#验证清单)
- [截图清单](#截图清单)
- [易错点](#易错点)
- [Self-Check](#Self-Check)
- [参考答案](#参考答案)
- [参考链接](#参考链接)
- [版本记录](#版本记录)

## 为什么要学
- 测试工程常同时维护老系统和新项目，Python 版本隔离做不好就会出现解释器冲突、依赖污染和脚本不可复现。
- 掌握 pyenv、venv、conda 的组合关系后，可以做到“全局选版本、项目做隔离、数据科学场景管系统库”。
- 本节的目标不是背命令，而是建立“版本管理”和“环境隔离”这两层能力的分工意识。

## 工具对比
- `pyenv` 负责安装多个 Python 解释器并按目录切换版本，适合开发机统一管理。
- `venv` 是标准库方案，轻量、稳定、对纯 Python 项目足够好。
- `conda` 除了装 Python 还能装二进制依赖，更适合数据分析、AI、本地 C/C++ 扩展较多的场景。
- 常见组合是 `pyenv + venv`；如果团队已经统一到 Anaconda/Miniconda，则优先遵循团队习惯。

## 实战步骤
### 1. Windows：使用 pyenv-win 管理解释器

```powershell
pip install pyenv-win --user
setx PYENV "%USERPROFILE%\.pyenv\pyenv-win"
setx PATH "%USERPROFILE%\.pyenv\pyenv-win\bin;%USERPROFILE%\.pyenv\pyenv-win\shims;%PATH%"
pyenv install 3.11.9
pyenv global 3.11.9
python --version
```

逐行说明:
- 第 1 行安装 `pyenv-win`。
- 第 2 至 3 行把执行目录和 shim 目录加入环境变量。
- 第 4 行安装指定版本。
- 第 5 行设置全局版本。
- 第 6 行回显当前解释器版本，确认切换生效。

### 2. macOS：使用 Homebrew 安装 pyenv

```bash
brew update
brew install pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
exec "$SHELL"
pyenv install 3.10.14
pyenv local 3.10.14
python --version
```

逐行说明:
- 第 1 至 2 行安装 pyenv。
- 第 3 至 5 行把初始化逻辑写入 shell 配置。
- 第 6 行重新加载 shell。
- 第 7 至 9 行安装解释器、绑定当前目录版本并验证结果。

### 3. Linux：系统依赖 + pyenv

```bash
sudo apt update
sudo apt install -y build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev curl git
curl https://pyenv.run | bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc
pyenv install 3.9.19
pyenv shell 3.9.19
python --version
```

逐行说明:
- 第 1 至 2 行安装编译 Python 所需的系统依赖。
- 第 3 行执行官方安装脚本。
- 第 4 至 7 行把 pyenv 注入当前 shell。
- 第 8 至 10 行安装解释器、在当前终端切换版本并验证。

### 4. 项目级隔离：venv

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -c "import sys; print(sys.prefix)"
```

逐行说明:
- 第 1 行创建虚拟环境。
- 第 2 行激活环境；Windows 对应命令是 `.\.venv\Scripts\activate`。
- 第 3 行升级 pip，避免旧版解析器导致安装异常。
- 第 4 行输出当前环境前缀，用于确认已进入项目环境。

### 5. 用 Python 自检当前解释器和虚拟环境

```python hl_lines="5 9"
import sys
from pathlib import Path


def in_virtualenv() -> bool:
    return sys.prefix != getattr(sys, "base_prefix", sys.prefix)


executable = Path(sys.executable).name
print(sys.version.split()[0], executable, in_virtualenv())
```

关键行说明:
- 第 5 行通过 `sys.prefix` 和 `sys.base_prefix` 判断是否处于虚拟环境。
- 第 9 行输出版本、解释器文件名和布尔结果，适合放到排障脚本里。

## 验证清单
- 执行 `python --version`，确认输出与 `pyenv global/local/shell` 设定一致。
- 执行 `which python` 或 `where python`，检查路径是否落在期望的解释器目录或 `.venv` 目录。
- 在项目目录执行 `python -c "import sys; print(sys.prefix)"`，确认 `venv` 已隔离。

## 截图清单
- `images/python_version_management_01.png`: Windows 上配置 pyenv-win 与 PATH 的终端截图。
- `images/python_version_management_02.png`: macOS 上使用 `pyenv local` 绑定目录版本的截图。
- `images/python_version_management_03.png`: Linux 上编译依赖与切换版本的截图。

## 易错点
- Windows 上只装了 `pyenv-win` 但没有重新打开终端，`pyenv` 命令会提示找不到。
- Linux 缺少 `libssl-dev`、`zlib1g-dev` 等系统库时，`pyenv install` 通常会在编译阶段失败。
- 很多人把 `pyenv` 当成虚拟环境工具使用，结果同一版本的第三方依赖被项目间污染；记住它只负责解释器层。

## Self-Check
### 概念题
1. `pyenv`、`venv`、`conda` 分别解决哪一层问题？
2. 为什么团队里常推荐 `pyenv + venv` 这组搭配？
3. `pyenv local` 和 `pyenv global` 的作用域有什么区别？

### 编程题
1. 写一个脚本打印当前 Python 主版本号、可执行文件路径以及是否处于虚拟环境。
2. 如何让 Windows 下的项目固定使用 Python 3.11，并为仓库创建独立虚拟环境？

### 实战场景
1. 你的 UI 自动化仓库需要在本机同时维护 Python 3.8 和 Python 3.12，应该怎样设计开发机环境？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
`pyenv` 解决解释器版本切换，`venv` 解决项目级纯 Python 依赖隔离，`conda` 额外解决二进制依赖与跨语言包管理。遇到混合场景时先看团队基线，再决定组合方式。
讲解回看: [工具对比](#工具对比)

### 概念题 2
因为它把“安装多个解释器”和“给项目做隔离”拆成两层，职责清晰、迁移成本低，而且完全基于 Python 生态自身能力。
讲解回看: [为什么要学](#为什么要学)

### 概念题 3
`pyenv global` 设置全局默认版本，影响所有目录；`pyenv local` 只在当前项目目录写入 `.python-version`，更适合仓库级配置。
讲解回看: [实战步骤](#实战步骤)

### 编程题 1
可以直接复用“用 Python 自检当前解释器和虚拟环境”里的示例：`sys.version.split()[0]` 取版本，`sys.executable` 取路径，`sys.prefix != sys.base_prefix` 判断是否处于虚拟环境。
讲解回看: [实战步骤](#实战步骤)

### 编程题 2
先用 `pyenv install 3.11.x` 安装解释器，再在仓库目录执行 `pyenv local 3.11.x`，随后执行 `python -m venv .venv` 并激活。这样版本和依赖都被项目固定住了。
讲解回看: [验证清单](#验证清单)

### 实战场景 1
优先用 `pyenv` 安装两个解释器，每个仓库用 `pyenv local` 绑定到目标版本，再在项目里各自创建 `.venv`。这样升级某个项目时不会连带影响另一个项目。
讲解回看: [为什么要学](#为什么要学)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-16: 初版整理，补齐示例、自测题与落地建议。

---
[返回 Python 学习总览](../README.md)
