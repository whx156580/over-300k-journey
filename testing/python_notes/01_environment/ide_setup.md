---
title: VS Code + Pylance + Black + isort + flake8 一体化配置
module: testing
area: python_notes
stack: python
level: basics
status: active
tags: [python, vscode, pylance, black, flake8]
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
- 写测试代码时，问题往往不是“不会写”，而是跳转、提示、格式化、调试和静态检查没有串起来。
- 把 VS Code 调整成“保存即格式化、写代码就有类型提示、点调试就能进断点”的状态，能显著降低学习成本。
- 本节的目标是形成一套仓库可复制的 `.vscode` 模板，而不是只在个人电脑里临时点选配置。

## 工具对比
- `Pylance` 提供类型推断、跳转与补全，是 VS Code 里 Python 开发体验的核心。
- `Black` 负责无争议格式化，`isort` 负责导入排序，`flake8` 负责最基础的规范和语法风险检查。
- 调试配置最好和仓库一起提交，这样新成员拉下代码就能直接复用。

## 实战步骤
### 1. 安装扩展

- Python
- Pylance
- Black Formatter
- isort
- Flake8

### 2. 推荐的 `.vscode/settings.json`

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": "explicit"
  },
  "python.analysis.typeCheckingMode": "basic",
  "python.analysis.autoImportCompletions": true,
  "editor.defaultFormatter": "ms-python.black-formatter",
  "flake8.args": ["--max-line-length=88"],
  "isort.args": ["--profile", "black"]
}
```

关键字段说明:
- `python.defaultInterpreterPath`: 固定工作区解释器。
- `editor.formatOnSave`: 保存时自动格式化。
- `source.organizeImports`: 保存时触发 import 排序。
- `python.analysis.typeCheckingMode`: 推荐从 `basic` 起步，再逐步切到 `strict`。

### 3. 推荐的 `.vscode/launch.json`

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

字段说明:
- `program`: 当前打开的文件。
- `console`: 在集成终端执行，便于观察标准输出。
- `justMyCode`: 默认只调试业务代码，先降低干扰。

### 4. 断点调试示范

```python hl_lines="2 4 8"
def divide(total: int, count: int) -> float:
    if count == 0:
        raise ValueError("count must not be zero")
    return total / count


if __name__ == "__main__":
    result = divide(42, 6)
    print(result)
```

调试建议:
- 在第 2 行与第 8 行打断点，观察参数、返回值和异常分支。
- 如果你要调试 Pytest，用 `module: pytest` 的配置比直接跑脚本更方便。

### 5. 用 Python 生成一份 settings 模板

```python hl_lines="3 9"
import json

settings = {
    "editor.formatOnSave": True,
    "python.analysis.typeCheckingMode": "basic",
    "editor.defaultFormatter": "ms-python.black-formatter",
}

print(json.dumps(settings, ensure_ascii=False, indent=2))
assert settings["editor.formatOnSave"] is True
```

关键行说明:
- 第 3 至 7 行演示如何在脚本里生成配置片段。
- 第 9 行可作为初始化脚本的最小验收断言。

## 验证清单
- 打开任意 Python 文件，保存时确认 Black 和 isort 自动生效。
- 故意写一个未使用变量或语法错误，确认 Flake8/Pylance 能在编辑器里直接提示。
- 按 `F5` 启动当前文件调试，确认断点命中、变量面板可查看局部变量。

## 截图清单
- `images/ide_setup_01.png`: VS Code 扩展安装与解释器选择界面截图。
- `images/ide_setup_02.png`: `.vscode/settings.json` 配置与保存即格式化效果截图。
- `images/ide_setup_03.png`: `launch.json` 断点调试过程截图。

## 易错点
- 解释器路径写死为类 Unix 路径后，Windows 成员打开仓库会提示找不到 Python；需要按团队平台选择模板或使用变量。
- 同时启用多个 Formatter 会导致保存时格式来回抖动，最后很难定位是谁在改文件。
- `flake8`、`black`、`isort` 版本不一致时，常出现“格式化通过但 lint 失败”的现象，最好在仓库里锁版本。

## Self-Check
### 概念题
1. 为什么推荐把 `.vscode/settings.json` 和 `launch.json` 一起提交到仓库？
2. `Pylance`、`Black`、`flake8` 各自解决什么问题？
3. `basic` 类型检查模式为什么适合作为起点？

### 编程题
1. 如何让保存文件时自动排序 import 并运行 Black？
2. 如何验证当前工作区是否真的在使用 `.venv` 里的解释器？

### 实战场景
1. 团队里有人保存代码会自动格式化，有人不会，最终 PR 里全是无意义 diff，怎么收敛？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
因为它们属于团队开发体验的一部分。把它们跟代码一起版本化，能让新成员拉库后立刻获得统一的格式化、提示和调试行为。
讲解回看: [为什么要学](#为什么要学)

### 概念题 2
`Pylance` 负责智能提示与类型分析，`Black` 负责代码格式统一，`flake8` 负责基础规范和语法风险检查。它们互补而不是互相替代。
讲解回看: [工具对比](#工具对比)

### 概念题 3
因为它能先暴露明显类型问题，又不会像 `strict` 那样一下子引入过多告警，适合学习阶段和存量项目渐进接入。
讲解回看: [实战步骤](#实战步骤)

### 编程题 1
在 `settings.json` 中开启 `editor.formatOnSave`，并在 `editor.codeActionsOnSave` 里设置 `source.organizeImports`，同时把默认格式化器指向 `ms-python.black-formatter`。
讲解回看: [实战步骤](#实战步骤)

### 编程题 2
可以在终端运行 `python -c "import sys; print(sys.executable)"`，也可以直接在 VS Code 右下角查看当前解释器路径是否落在 `.venv` 中。
讲解回看: [验证清单](#验证清单)

### 实战场景 1
把 `.vscode` 模板、`requirements.txt` 和 CI 检查一起提交。开发机靠格式化器降低成本，CI 用 `black --check` 和 `flake8` 执行兜底，形成统一闭环。
讲解回看: [验证清单](#验证清单)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-16: 初版整理，补齐示例、自测题与落地建议。

---
[返回 Python 学习总览](../README.md)
