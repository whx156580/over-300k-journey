---
title: 项目交付、Docker 与工程协作 (Project Delivery & Docker)
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, delivery, docker, ci-cd, makefile, collaboration]
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
- **问题场景**: 开发者本地运行正常的脚本，推送到 CI 服务器或生产环境后因为缺少依赖、路径不一致或 Python 版本冲突而崩溃；或者团队协作时，每个人启动服务的命令都不统一，导致交接极其困难。
- **学习目标**: 掌握 Docker 容器化技术实现环境一致性，利用 Makefile 自动化常用工程任务，建立结构化的发布检查清单。
- **前置知识**: [FastAPI 进阶模式](./fastapi_advanced_patterns.md)。

## 核心结论
- **环境隔离**: Docker 是解决“我机器上能跑”问题的终极方案，通过镜像封装系统级依赖。
- **自动化入口**: Makefile 或任务运行器应作为项目的“唯一入口”，屏蔽复杂的 CLI 参数。
- **质量门禁**: 交付不只是代码，还包括通过所有 Lint、类型检查和覆盖率达标的测试。

## 原理拆解
- **容器层级**: Docker 利用 Linux Namespace 实现进程隔离，利用 UnionFS 实现镜像分层。
- **工程化闭环**: 源码 -> 构建 (Build) -> 验证 (Test) -> 发布 (Ship) -> 运行 (Run) 的标准化链路。

## 官方文档与兼容性
| 规则名称 | 官方出处 | PEP 链接 | 兼容性 |
| :--- | :--- | :--- | :--- |
| Dockerfile 指南 | [Dockerfile reference](https://docs.docker.com/engine/reference/builder/) | N/A | Cross-platform |
| Twelve-Factor | [The Twelve-Factor App](https://12factor.net/) | N/A | Methodology |
| Makefile | [GNU Make Manual](https://www.gnu.org/software/make/manual/) | N/A | Unix-like/Win |

## 代码示例

### 示例 1：标准化多阶段构建 (Dockerfile)
演示如何构建体积精简、安全性高的生产级镜像。

```dockerfile
# 第一阶段：构建依赖
FROM python:3.11-slim as builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# 第二阶段：运行环境
FROM python:3.11-slim
WORKDIR /app
# 仅拷贝必要文件，减少镜像体积
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "main.py"]
```

### 示例 2：工程任务自动化 (Makefile)
通过 Makefile 统一团队的操作入口，避免记忆复杂的 pytest 或 flake8 命令。

```makefile
# 定义变量
PYTHON = python
PYTEST = pytest --cov=.

.PHONY: install test lint check

install:
	pip install -r requirements.txt

test:
	$(PYTEST)

lint:
	flake8 .
	mypy .

check: lint test
	@echo "All quality gates passed!"
```

### 示例 3：结构化发布门禁 (Checklist Logic)
使用 Python 脚本自动化执行发布前的合规性检查。

```python
def check_release_readiness(metrics: dict) -> bool:
    """
    检查发布就绪状态：测试通过、覆盖率达标、无高危漏洞。
    """
    gates = {
        "tests": metrics.get("tests_passed", False),
        "coverage": metrics.get("coverage_pct", 0) >= 90,
        "security": metrics.get("vulnerabilities", 1) == 0
    }
    
    can_ship = all(gates.values())
    if not can_ship:
        failed = [k for k, v in gates.items() if not v]
        print(f"Release BLOCKED by: {failed}")
    return can_ship

# 验证
res = check_release_readiness({"tests_passed": True, "coverage_pct": 95, "vulnerabilities": 0})
assert res is True
```

## 性能基准测试
对比不同基础镜像（Alpine vs Slim）的构建耗时与镜像体积。

```text
| 基础镜像 | 构建耗时 (Build Time) | 镜像体积 (Size) | 备注 |
| :--- | :--- | :--- | :--- |
| python:3.11 | 45s | 920MB | 包含完整编译工具，适合开发 |
| python:3.11-slim | 30s | 120MB | 推荐生产使用，体积适中 |
| python:3.11-alpine | 60s+ | 50MB | 编译依赖慢，可能存在 glibc 兼容问题 |
```

## 易错点与最佳实践
| 特性 | 常见陷阱 | 最佳实践 |
| :--- | :--- | :--- |
| **敏感信息** | 将 API Key 硬编码在 Dockerfile 中。 | 使用 `ENV` 或 `docker secret`，生产环境通过环境变量注入。 |
| **依赖锁死** | `requirements.txt` 不带版本号。 | 使用 `pip-compile` 或 `poetry` 生成带 Hash 的锁文件。 |
| **忽略 .dockerignore** | 镜像中包含了大量的 `.git`, `__pycache__` 或本地虚拟环境。 | 编写 `.dockerignore` 显式排除无关文件。 |

## Self-Check
1. 为什么在 CI 流水线中推荐使用 `pip install --frozen-lockfile` 类似的确定性安装命令？
2. `ENTRYPOINT` 与 `CMD` 在 Dockerfile 中的主要区别是什么？
3. Makefile 中的 `.PHONY` 标签有什么作用？

## 参考链接
- [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Python Project Structure Best Practices](https://example.com)

---
[版本记录](./project_delivery_and_engineering_practice.md) | [返回首页](../README.md)
