# 💻 VS Code 一体化调试与工程化配置 (IDE Setup)

[TOC]

## 📖 背景 (Background)
高效的开发离不开强大的 IDE 支持。VS Code 配合 Pylance 和静态检查工具可以大幅提升代码质量。
- **业务痛点**: 代码格式不统一、调试效率低、拼写错误。
- **解决方案**: 配置统一的 `.vscode` 模板与格式化工具链。

## 🔬 原理 (Principles)
- **Pylance**: 基于 Pyright 的语言服务器，提供类型检查和感知。
- **Linting (flake8)**: 语法错误检查。
- **Formatting (Black/isort)**: 自动对齐与导入排序。

## 🚀 实战步骤 (Implementation)

### 1. 核心扩展安装
- Python (Microsoft)
- Pylance (Microsoft)
- Black Formatter

### 2. 项目配置 (.vscode/settings.json)
```json
{
    "python.defaultInterpreterPath": ".venv/bin/python",
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "ms-python.black-formatter",
    "python.analysis.typeCheckingMode": "basic",
    "isort.args": ["--profile", "black"],
    "flake8.args": ["--max-line-length=88"]
}
```

### 3. 断点调试 (.vscode/launch.json)
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true
        }
    ]
}
```

## ⚠️ 踩坑记录 (Pitfalls)
- **解释器未选对**: 右下角显示全局 Python 而非 `.venv`。需手动点击切换。
- **冲突**: 同时开启多个 Formatter 会导致格式互跳。

## ❓ Self-Check 清单
1. **概念题**: Pylance 的 "Strict" 模式与 "Basic" 模式有何区别？
2. **编程题**: 创建一个包含拼写错误和格式混乱的代码文件，使用快捷键自动修复它。
3. **实战场景**: 如何配置 VS Code 使得每次保存文件时自动删除未使用的 import 语句？

## 🔗 参考链接 (References)
- [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [Black Formatter Guide](https://black.readthedocs.io/en/stable/)

---
**版本记录**: v1.0 | 2026-04-13
