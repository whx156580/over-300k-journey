# Python 学习笔记体系

> 面向测试工程师的 Python 系统学习路径，覆盖环境搭建、语言基础、高级语法与工程化专题。

## 学习路径

| 阶段 | 目录 | 目标 | 预计时长 | 前置知识 |
| :--- | :--- | :--- | :--- | :--- |
| 环境篇 | `01_environment/` | 配好解释器、依赖管理和 IDE 调试体验 | 4-6 小时 | 基本命令行操作 |
| 基础语法篇 | `02_basic_syntax/` | 建立数据类型、流程控制、容器与函数基础 | 10-14 小时 | 环境篇 |
| 高级语法篇 | `03_advanced_syntax/` | 掌握生成器、装饰器、上下文管理器、OOP 与异常体系 | 12-16 小时 | 基础语法篇 |
| 进阶专题篇 | `04_progressive_topics/` | 把 Python 能力落到并发、性能、类型、测试与发布链路 | 14-20 小时 | 高级语法篇 |

## 建议学习顺序

1. 先把环境篇走通，确保解释器、依赖与编辑器体验稳定。
2. 基础语法篇按“变量 -> 运算符 -> 流程控制 -> 字符串 -> 容器 -> 函数”的顺序推进。
3. 高级语法篇重点理解“抽象边界”和“资源管理”，不要只背语法。
4. 进阶专题篇按工作场景挑重点，测试工程优先看正则、并发、测试金字塔与类型检查。

## 内容索引

### 环境篇

| 主题 | 文件 |
| :--- | :--- |
| Python 多版本管理 | [python_version_management.md](./01_environment/python_version_management.md) |
| pip 与 Poetry 依赖管理 | [dependency_management.md](./01_environment/dependency_management.md) |
| VS Code 一体化配置 | [ide_setup.md](./01_environment/ide_setup.md) |

### 基础语法篇

| 主题 | 文件 |
| :--- | :--- |
| 变量与数据类型 | [variables_and_types.md](./02_basic_syntax/variables_and_types.md) |
| 运算符与表达式 | [operators_and_expressions.md](./02_basic_syntax/operators_and_expressions.md) |
| 流程控制 | [control_flow.md](./02_basic_syntax/control_flow.md) |
| 字符串与常用方法 | [strings_and_methods.md](./02_basic_syntax/strings_and_methods.md) |
| 列表、元组、集合、字典 | [collections.md](./02_basic_syntax/collections.md) |
| 函数基础 | [function_basics.md](./02_basic_syntax/function_basics.md) |

### 高级语法篇

| 主题 | 文件 |
| :--- | :--- |
| 迭代器、生成器与 yield/send/throw/close | [iterators_and_generators.md](./03_advanced_syntax/iterators_and_generators.md) |
| 装饰器 | [decorators.md](./03_advanced_syntax/decorators.md) |
| 上下文管理器 | [context_managers.md](./03_advanced_syntax/context_managers.md) |
| 面向对象 | [object_oriented_programming.md](./03_advanced_syntax/object_oriented_programming.md) |
| 异常体系 | [exceptions.md](./03_advanced_syntax/exceptions.md) |
| 模块与包 | [modules_and_packages.md](./03_advanced_syntax/modules_and_packages.md) |

### 进阶专题篇

| 主题 | 文件 |
| :--- | :--- |
| 正则表达式与 re 模块 | [python_re.md](./04_progressive_topics/python_re.md) |
| Python 关键字全集 | [python_keywords.md](./04_progressive_topics/python_keywords.md) |
| 并发模型 | [python_concurrency.md](./04_progressive_topics/python_concurrency.md) |
| 性能剖析 | [python_profiling.md](./04_progressive_topics/python_profiling.md) |
| 类型提示与静态检查 | [type_hints_and_static_checking.md](./04_progressive_topics/type_hints_and_static_checking.md) |
| 测试金字塔与 Pytest | [testing_pyramid_and_pytest.md](./04_progressive_topics/testing_pyramid_and_pytest.md) |
| 打包发布 | [packaging_and_publishing.md](./04_progressive_topics/packaging_and_publishing.md) |

## 一键初始化

```bash
cd testing/python_notes
python -m pip install -r requirements.txt
pytest tests -q
```

## 工程化约定

- 所有笔记使用 GitHub Flavored Markdown。
- 每篇笔记都包含 front matter、目录锚点、Self-Check、参考答案、参考链接和版本记录。
- 代码块优先保证“可读、可运行、可复制”，测试脚本会执行所有 `python` 代码块。
- `images/` 目录按“笔记名_序号.png”维护截图与示意图资源。
- 根目录 `Makefile` 提供 `install`、`serve`、`test`、`lint`、`format` 等命令入口。

## 关联入口

- 示例校验脚本: [tests/test_markdown_examples.py](./tests/test_markdown_examples.py)
- 依赖清单: [requirements.txt](./requirements.txt)
- 常用命令: [Makefile](./Makefile)
- 知识汇总页: [../../common/docs/indexes/knowledge_hub.md](../../common/docs/indexes/knowledge_hub.md)
- 模板参考: [../../common/docs/template.md](../../common/docs/template.md)
