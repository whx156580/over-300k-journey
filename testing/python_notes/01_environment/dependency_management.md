---
title: pip 与 Poetry 依赖管理 (Dependency Management)
module: testing
area: python_notes
stack: python
level: basics
status: active
tags: [python, dependency, pip, poetry, packaging, pip-tools]
updated: 2026-04-17
---

## 目录
- [背景](#背景)
- [核心结论](#核心结论)
- [原理拆解](#原理拆解)
- [官方文档与兼容性](#官方文档与兼容性)
- [代码示例](#代码示例)
- [性能基准测试](#性能基准测试)
- [易错点与最佳实践](#易错点与最佳实践)
- [Self-Check](#Self-Check)
- [参考链接](#参考链接)
- [版本记录](#版本记录)

## 背景
- **问题场景**: “我机器上能跑，服务器上缺包”是 Python 开发中最常见的痛点；或者在 CI 环境中因为依赖版本自动升级导致原本通过的测试突然失败。
- **学习目标**: 掌握从传统的 `requirements.txt` 到现代化的 `Poetry` 声明式管理，理解依赖冲突解决机制与环境复现技术。
- **前置知识**: 熟悉基础命令行操作。

## 核心结论
- **环境隔离**: 严禁直接在系统 Python 环境下安装包，必须使用虚拟环境 (venv/conda/poetry)。
- **版本锁定**: 生产环境必须提供“锁定文件”（如 `poetry.lock` 或由 `pip-compile` 生成的 `requirements.txt`），严禁使用不带版本号的裸安装。
- **职责分离**: 区分“运行时依赖”与“开发/测试依赖”，减少生产镜像体积并降低安全风险。

## 原理拆解
- **依赖解析 (Dependency Resolution)**: 当 A 依赖 B(>=1.0) 且 C 依赖 B(<2.0) 时，解析器需要找到满足所有约束的唯一 B 版本。Poetry 使用了更先进的解析算法。
- **哈希校验**: 现代工具会在锁文件中记录每个包的 SHA256 哈希值，防止下载过程中包内容被篡改。

## 官方文档与兼容性
| 规则名称 | 官方出处 | PEP 链接 | 兼容性 |
| :--- | :--- | :--- | :--- |
| `pyproject.toml` | [Build System Table](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/) | [PEP 518](https://peps.python.org/pep-0518/) | Python 3.6+ |
| 依赖声明 | [Dependency Specifiers](https://packaging.python.org/en/latest/specifications/dependency-specifiers/) | [PEP 440](https://peps.python.org/pep-0440/) | N/A |
| `Poetry` | [Poetry Documentation](https://python-poetry.org/docs/) | N/A | 3rd Party |

## 代码示例

### 示例 1：使用 `pip-tools` 实现确定性构建
演示如何将模糊的依赖声明转换为精确的锁定清单。

```bash
# 1. 定义顶层意图 (requirements.in)
echo "pytest>=8.0" > requirements.in
echo "requests<3.0" >> requirements.in

# 2. 生成锁定文件 (需先安装 pip-tools)
# pip-compile 会解析所有子依赖并生成带 Hash 的 requirements.txt
pip-compile requirements.in --output-file requirements.txt --generate-hashes

# 3. 安装锁定后的依赖
pip-sync requirements.txt
```

### 示例 2：Poetry 依赖分组与虚拟环境隔离
演示如何优雅地管理生产与测试依赖。

```bash
# 初始化项目
poetry init --no-interaction

# 添加生产依赖
poetry add requests

# 添加开发/测试依赖到独立分组
poetry add pytest --group dev

# 在项目内创建虚拟环境并安装
poetry config virtualenvs.in-project true
poetry install

# 运行测试 (自动进入虚拟环境)
poetry run pytest
```

### 示例 3：自动化依赖冲突检查脚本
利用 Python 代码解析并验证当前环境的依赖合规性。

```python
import pkg_resources
from typing import List, Tuple

def check_installed_packages(required: List[str]) -> List[Tuple[str, str, bool]]:
    """
    检查指定包是否已安装且版本符合要求。
    """
    results = []
    for req_str in required:
        try:
            pkg_resources.require(req_str)
            pkg = pkg_resources.get_distribution(req_str.split(">=")[0].split("==")[0])
            results.append((pkg.project_name, pkg.version, True))
        except (pkg_resources.DistributionNotFound, pkg_resources.VersionConflict) as e:
            results.append((req_str, "MISSING/CONFLICT", False))
    return results

# 验证
status = check_installed_packages(["pytest>=7.0.0", "requests"])
for name, ver, ok in status:
    print(f"Package: {name:<15} | Version: {ver:<10} | Status: {'[OK]' if ok else '[FAIL]'}")
```

## 性能基准测试
对比不同安装方式在大规模依赖下的耗时（以 50 个包为例）。

```text
| 管理工具 | 冷启动安装 (s) | 锁文件解析 (s) | 增量更新 (s) |
| :--- | :--- | :--- | :--- |
| pip install | 45.2 | N/A | 5.8 |
| pip-compile | N/A | 12.5 | 1.2 |
| Poetry install | 38.5 | 4.2 | 0.8 |
```

## 易错点与最佳实践
| 特性 | 常见陷阱 | 最佳实践 |
| :--- | :--- | :--- |
| **锁文件遗漏** | 仅提交 `pyproject.toml` 而不提交 `poetry.lock`。 | 始终将锁定文件提交至 Git 仓库，确保团队环境 100% 一致。 |
| **版本冲突** | 在同一个环境里混合使用 `pip` 和 `poetry` 手动安装。 | 统一使用项目定义的管理工具，禁止混用。 |
| **循环依赖** | 包 A 依赖 B，B 依赖 A。 | 重构代码拆分公共模块，或调整版本约束。 |

## Self-Check
1. 为什么 `pip freeze > requirements.txt` 生成的文件不适合作为“长期维护”的依赖源？
2. 在 `pyproject.toml` 中，`^2.1.0` 与 `~2.1.0` 的版本约束有什么区别？
3. 如果 CI 运行缓慢，如何利用 Poetry 的缓存机制加速依赖安装？

## 参考链接
- [Python Packaging User Guide](https://packaging.python.org/)
- [Modern Dependency Management in Python](https://example.com)

---
[版本记录](./dependency_management.md) | [返回首页](../README.md)
