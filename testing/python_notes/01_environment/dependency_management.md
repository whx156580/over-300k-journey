# 📦 pip 与 poetry 依赖管理 (Dependency Management)

[TOC]

## 📖 背景 (Background)
Python 依赖管理长期以来较为松散，`requirements.txt` 无法解决依赖冲突和确定性构建问题。
- **业务痛点**: 依赖库 A 需要 B>=1.0，库 C 需要 B<1.0，`pip` 容易出现冲突。
- **解决方案**: 使用现代工具如 `Poetry` 进行锁版本管理。

## 🔬 原理 (Principles)
- **pip**: 扁平化安装，依赖关系由开发者手动维护。
- **Poetry**: 基于 `pyproject.toml` (PEP 518)，提供确定性解析器，通过 `poetry.lock` 锁定全链路依赖版本。

## 🚀 实战步骤 (Implementation)

### 1. pip 加速镜像配置
```bash
# 临时加速
pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
# 永久配置
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### 2. Poetry 初始化与常用命令
```bash
# 安装
curl -sSL https://install.python-poetry.org | python3 -
# 项目初始化
poetry init
# 添加依赖并自动创建虚拟环境
poetry add requests
# 进入环境
poetry shell
```

### 3. 互转操作
```bash
# 从 Poetry 导出 requirements.txt
poetry export -f requirements.txt --output requirements.txt
# 从 requirements.txt 批量安装
pip install -r requirements.txt
```

## ⚠️ 踩坑记录 (Pitfalls)
- **Poetry 环境位置**: 默认在系统目录。建议配置 `poetry config virtualenvs.in-project true` 将虚拟环境放在项目根目录。
- **依赖冲突**: Poetry 遇到版本不兼容会报错中止，需手动在 `pyproject.toml` 中放宽版本限制。

## ❓ Self-Check 清单
1. **概念题**: `poetry.lock` 文件的核心作用是什么？
2. **编程题**: 编写一个命令，列出当前 pip 环境中所有已安装包的许可证。
3. **实战场景**: 团队协作时，新成员拉取代码后应该执行什么命令来保证环境一致？

## 🔗 参考链接 (References)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [PyPI Mirror List](https://pypi.org/mirrors)

---
**版本记录**: v1.0 | 2026-04-13
