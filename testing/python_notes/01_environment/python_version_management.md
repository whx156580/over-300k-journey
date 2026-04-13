# 🐍 Python 多版本管理 (pyenv, venv, conda)

[TOC]

## 📖 背景 (Background)
在软件开发中，不同项目往往依赖不同版本的 Python。直接在系统全局安装多个版本会导致路径冲突、库污染等问题。
- **业务痛点**: 项目 A 需 Python 3.7，项目 B 需 3.10，全局环境切换困难。
- **解决方案**: 使用管理工具实现版本隔离与平滑切换。

## 🔬 原理 (Principles)
- **pyenv**: 通过修改 `PATH` 环境变量，拦截 Python 命令调用（Shim 机制）。
- **venv**: Python 内置，通过在项目目录创建符号链接实现轻量级隔离。
- **conda**: 二进制包管理器，不仅管理 Python，还管理非 Python 依赖（如 C 库）。

## 🚀 实战步骤 (Implementation)

### 1. Windows 平台: pyenv-win
```powershell
# 安装
pip install pyenv-win --user
# 配置环境变量 (手动添加至用户变量 PATH)
# %USERPROFILE%\.pyenv\pyenv-win\bin
# %USERPROFILE%\.pyenv\pyenv-win\shims

# 安装指定版本
pyenv install 3.10.11
# 全局切换
pyenv global 3.10.11
```

### 2. macOS/Linux: pyenv
```bash
# 使用 Homebrew 安装
brew install pyenv
# 写入 shell 配置文件 (.zshrc 或 .bashrc)
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# 安装并局部应用
pyenv install 3.9.16
pyenv local 3.9.16
```

### 3. 轻量级隔离: venv
```bash
# 创建虚拟环境
python -m venv .venv
# 激活 (Windows)
.\.venv\Scripts\activate
# 激活 (Unix)
source .venv/bin/activate
```

## ⚠️ 踩坑记录 (Pitfalls)
- **SSL 错误**: Windows 下 `pyenv install` 可能因证书问题失败。需手动下载安装包放至 `.pyenv/pyenv-win/install_cache`。
- **编译依赖**: Linux 下安装 Python 前需安装 `build-essential`, `libssl-dev` 等。

## ❓ Self-Check 清单
1. **概念题**: pyenv 的 Shim 机制是如何工作的？
2. **编程题**: 编写一个脚本，检测当前环境是否处于虚拟环境中。
3. **实战场景**: 如果项目需要集成 C++ 编译的库，你会选择哪种管理工具？为什么？

## 🔗 参考链接 (References)
- [pyenv GitHub](https://github.com/pyenv/pyenv)
- [Python venv Docs](https://docs.python.org/3/library/venv.html)

---
**版本记录**: v1.0 | 2026-04-13
