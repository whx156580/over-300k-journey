---
title: Ruff、Black、mypy、pytest 与 pre-commit 工具链
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, ruff, black, mypy, pytest, pre-commit]
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
- 从业者真正痛苦的往往不是“不会写”，而是代码风格不统一、提交前漏跑测试、类型问题到线上才暴露。
- 质量工具链的目标不是增加流程负担，而是把低级错误前移到本地保存、提交和 PR 阶段。
- 对测试仓库和工具仓库来说，代码质量基线越稳定，协作成本越低，排障和重构都会轻松很多。

## 学什么
- `Ruff` 负责 lint 和一部分自动修复，`Black` 负责格式化，`mypy` 负责静态类型检查，`pytest` 负责行为验证。
- `pre-commit` 的价值是把这些检查挂到提交流程里，避免“我本地忘了跑”变成团队噪音。
- 本地、CI 和仓库配置要尽量统一，不然就会出现“本地能过、流水线失败”的反复摩擦。

## 怎么用
### 示例 1：在 `pyproject.toml` 里统一工具配置

```toml
[tool.ruff]
line-length = 100
target-version = "py39"

[tool.black]
line-length = 100

[tool.pytest.ini_options]
addopts = "-q"

[tool.mypy]
python_version = "3.9"
strict = true
```


### 示例 2：用 `pre-commit` 把检查挂到提交前

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.9
    hooks:
      - id: ruff
      - id: ruff-format
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.11.2
    hooks:
      - id: mypy
```


### 示例 3：在 CI 里固定执行顺序

```yaml
name: quality-gate
on: [push, pull_request]
jobs:
  checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: python -m pip install -r requirements.txt
      - run: ruff check .
      - run: black --check .
      - run: mypy .
      - run: pytest -q
```


### 示例 4：把质量门禁结果结构化

```python hl_lines="7 8"
quality_report = {
    "ruff": True,
    "black": True,
    "mypy": False,
    "pytest": True,
}

passed = all(quality_report.values())
failed_items = [name for name, ok in quality_report.items() if not ok]
print(passed, failed_items)
```


落地建议:
- 新仓库优先把工具配置放到 `pyproject.toml`，减少配置分散。
- 团队基线建议先落 `ruff + pytest`，再逐步加 `mypy` 和更严格的 pre-commit 检查。
- 本地与 CI 用同一套命令和同一份配置，能显著降低“环境口径不同”带来的噪音。

## 业界案例
- 很多 Python 团队把风格检查、类型检查和单元测试前移到 PR 阶段，只让主干分支接收已经过基础质量门禁的代码。
- 工具仓库和测试框架项目一旦缺少统一 lint 与 format 规则，review 很快就会被格式和命名问题淹没。
- `mypy` 最适合先落在工具层、SDK 层和公共函数层，这些位置的类型收益往往最高。

## 延伸阅读
- 质量工具链不是越多越好，而是要按团队成熟度分层推进。
- 如果大家经常绕开 pre-commit，往往不是人不配合，而是钩子太慢、误报太多或规则不清楚。
- 最理想的状态不是“所有人都记得手动执行”，而是“大家几乎不需要记”。

## Self-Check
### 概念题
1. Ruff、Black、mypy、pytest 各自主要解决哪类问题？
2. 为什么说 pre-commit 的价值不只是“自动跑命令”？
3. 为什么质量工具链需要本地和 CI 配置尽量统一？

### 编程题
1. 如何把 lint、format、type-check 和 test 的基础配置收敛到一个项目入口？
2. 为什么团队引入 `mypy` 时更适合渐进推进，而不是一步到位全仓严格模式？

### 实战场景
1. 团队经常出现“代码能跑但风格不统一、提交后 CI 才发现问题”，你会怎么设计最小质量工具链？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
Ruff 偏代码规范与潜在问题发现，Black 偏格式统一，mypy 偏静态类型约束，pytest 偏行为验证。
讲解回看: [学什么](#学什么)

### 概念题 2
它把团队约定前移到提交动作本身，让低成本问题更早失败，也减少“靠人记住流程”的不稳定性。
讲解回看: [为什么学](#为什么学)

### 概念题 3
因为如果两边命令、版本或规则不同，就会出现本地通过但 CI 失败，反而增加协作摩擦。
讲解回看: [怎么用](#怎么用)

### 编程题 1
可以优先把工具配置放进 `pyproject.toml`，再用 pre-commit 和 CI 统一执行入口。
讲解回看: [怎么用](#怎么用)

### 编程题 2
因为类型历史债务通常较多，直接全仓严格模式会让规则阻力大于收益；分层推进更容易稳定落地。
讲解回看: [业界案例](#业界案例)

### 实战场景 1
先落 `ruff + pytest + pre-commit` 做最小门禁，再按团队成熟度补 `black` 和 `mypy`，并保证本地与 CI 口径一致。
讲解回看: [落地建议](#怎么用)

## 参考链接
- [Ruff 文档](https://docs.astral.sh/ruff/)
- [Black 文档](https://black.readthedocs.io/)
- [mypy 文档](https://mypy.readthedocs.io/)
- [pre-commit 文档](https://pre-commit.com/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-17: 初版整理，补充 Python 常见质量工具链设计骨架。

---
[返回 Python 学习总览](../README.md)
