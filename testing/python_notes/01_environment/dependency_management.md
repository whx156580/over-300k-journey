---
title: pip 与 Poetry 依赖管理
module: testing
area: python_notes
stack: python
level: basics
status: active
tags: [python, dependency, pip, poetry, packaging]
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
- 测试仓库通常既有运行时依赖，也有格式化、静态检查和调试依赖，依赖管理混乱时最先坏掉的往往是 CI。
- 理解 `requirements.txt`、`constraints.txt`、`pyproject.toml` 与锁文件的分工，能让环境初始化更稳定，也更方便团队协作。
- 本节重点不是二选一，而是学会在不同项目成熟度下选择 `pip` 或 `Poetry` 的维护方式。

## 工具对比
- `pip` 是默认安装器，简单、兼容性广，适合脚本仓库或已有传统 `requirements.txt` 的项目。
- `Poetry` 把依赖声明、版本约束、构建配置统一到 `pyproject.toml`，更适合新项目或需要清晰锁文件的场景。
- `requirements.txt` 适合作为部署清单，`pyproject.toml` 更适合作为项目声明文件。
- 如果团队已经在 CI、部署平台和内部模板里统一使用某一种方案，优先跟随团队基线，减少维护分叉。

## 实战步骤
### 1. `pip` 初始化与常用命令

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install requests pytest
pip freeze > requirements.txt
pip install -r requirements.txt
```

逐行说明:
- 第 1 至 2 行准备隔离环境。
- 第 3 行升级 pip。
- 第 4 行安装业务与测试依赖。
- 第 5 行冻结当前环境，生成可复现清单。
- 第 6 行验证清单可被重新安装。

### 2. `Poetry` 初始化与常用命令

```bash
curl -sSL https://install.python-poetry.org | python3 -
poetry new demo_project
cd demo_project
poetry add requests
poetry add --group dev pytest black
poetry install
poetry run pytest
```

逐行说明:
- 第 1 行安装 Poetry。
- 第 2 至 3 行创建项目并进入目录。
- 第 4 行安装运行时依赖。
- 第 5 行安装开发依赖。
- 第 6 行根据锁文件装齐依赖。
- 第 7 行通过 `poetry run` 在项目环境里执行命令。

### 3. `requirements.txt` 与 `pyproject.toml` 的互转

```bash
poetry export -f requirements.txt --output requirements.txt --without-hashes
pip install pip-tools
pip-compile pyproject.toml --output-file requirements.txt
pip install -r requirements.txt
```

逐行说明:
- 第 1 行把 Poetry 依赖导出为传统清单，便于部署平台复用。
- 第 2 至 3 行使用 `pip-tools` 从项目声明生成固定依赖。
- 第 4 行用生成结果恢复环境。

### 4. 版本锁定与镜像配置

```bash
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip config set install.trusted-host pypi.tuna.tsinghua.edu.cn
poetry config virtualenvs.in-project true
poetry config repositories.company https://pypi.example.com/simple/
```

逐行说明:
- 前两行给 pip 设置镜像和可信主机，适合网络较慢时提速。
- 第 3 行让 Poetry 把虚拟环境放在项目目录，降低排障成本。
- 第 4 行演示如何注册私有源。

### 5. 用 Python 解析 requirements 内容

```python hl_lines="7 8"
requirements_text = """
pytest==8.3.2
requests>=2.32,<3.0
black==24.8.0
""".strip()

parsed = [line for line in requirements_text.splitlines() if line and not line.startswith("#")]
print(parsed)
assert "pytest==8.3.2" in parsed
```

关键行说明:
- 第 7 行过滤空行和注释，适合写依赖检查脚本。
- 第 8 行用断言保证关键依赖没有丢失。

## 验证清单
- 在空目录里执行 `pip install -r requirements.txt`，确认可以一次性装齐依赖。
- 执行 `poetry lock --no-update` 或 `poetry install`，确认锁文件和依赖声明一致。
- 在 CI 中固定使用 `requirements.txt` 或 `poetry.lock`，避免开发机和流水线使用不同来源。

## 截图清单
- `images/dependency_management_01.png`: `pip freeze` 与 `requirements.txt` 生成过程截图。
- `images/dependency_management_02.png`: Poetry 初始化、添加依赖与锁文件变化截图。
- `images/dependency_management_03.png`: 镜像配置和私有源配置示意图。

## 易错点
- 只提交 `pyproject.toml` 不提交 `poetry.lock`，会导致不同机器解析出不同依赖树。
- 把 `pip freeze` 的结果直接当成长期维护清单，容易把临时工具和无关依赖一起固化进去。
- 镜像配置后忘了同步到 CI，结果本地能装、流水线超时失败。

## Self-Check
### 概念题
1. `requirements.txt`、`pyproject.toml`、锁文件三者的职责分别是什么？
2. 为什么新项目常更推荐 Poetry，而不是只靠 `pip freeze`？
3. 什么情况下 `pip` 仍然是更合适的选择？

### 编程题
1. 如何从 Poetry 项目导出部署用 `requirements.txt`？
2. 如何快速检查一个 `requirements.txt` 文本里是否包含 `pytest`？

### 实战场景
1. 团队里既有老仓库，也准备启动一个新的 Python 自动化项目，该如何选择依赖管理策略？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
`requirements.txt` 更像可安装清单，`pyproject.toml` 是项目声明，锁文件记录被解析后的精确依赖树。三者一起用时，声明文件描述意图，锁文件保证复现，部署清单方便执行。
讲解回看: [工具对比](#工具对比)

### 概念题 2
因为 Poetry 把依赖声明、分组、构建元数据和锁文件管理统一起来，更适合长期维护；`pip freeze` 更像当前环境快照，表达能力弱。
讲解回看: [为什么要学](#为什么要学)

### 概念题 3
脚本仓库、历史项目、部署平台只认 `requirements.txt`，或团队已有完整 `pip + constraints` 规范时，继续使用 `pip` 往往成本更低。
讲解回看: [工具对比](#工具对比)

### 编程题 1
执行 `poetry export -f requirements.txt --output requirements.txt --without-hashes`。如果部署平台不理解 Poetry，这一步非常常见。
讲解回看: [实战步骤](#实战步骤)

### 编程题 2
可以像本节示例一样按行切分、过滤空行，再用 `any(line.startswith("pytest"))` 或 `"pytest==..." in parsed` 做断言。
讲解回看: [实战步骤](#实战步骤)

### 实战场景 1
老仓库优先延续现有 `requirements.txt`，减少迁移风险；新仓库可直接使用 Poetry 或 `pip-tools + pyproject.toml`，同时在 CI 里统一锁文件与导出策略。
讲解回看: [验证清单](#验证清单)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-16: 初版整理，补齐示例、自测题与落地建议。

---
[返回 Python 学习总览](../README.md)
