# Python 学习笔记体系

> 面向测试工程师、测试开发、自动化工程师，也兼顾 Python 初学者的主线学习笔记。当前内容统一收敛在 `01_environment` 到 `04_progressive_topics` 四个阶段目录中，不再维护额外的按天目录。

## 页内导航

[快速开始](#快速开始) | [课程主线总览](#课程主线总览) | [路线选择](#我该选哪条路线) | [学习里程碑](#学习里程碑--推荐练手项目) | [本轮补充清单](#本轮补充清单) | [推荐先读 6 篇](#推荐先读-6-篇) | [内容索引](#内容索引) | [一键初始化](#一键初始化)

## 这套笔记解决什么问题

- 它不是零散收藏夹，而是一条从“把环境配稳”到“把能力落到工程场景”的连续主线。
- 它不是只讲语法，也不是一上来就讲框架，而是把环境、基础语法、高级语法、工程专题串成一个可执行的学习路径。
- 它特别适合想把 Python 用到测试自动化、接口联调、数据处理、Web 服务、采集脚本和项目交付中的同学。

## 适合谁看

- 刚开始学 Python，希望有一条不绕路的主线。
- 已经会一点语法，但知识点比较散，想重新收拢成体系。
- 做测试开发、自动化测试、平台工具开发，想把 Python 学到“能稳定落地”的程度。
- 后面想转向数据分析、机器学习或 Web 开发，但希望先把语言根基和工程习惯打牢。

## 快速开始

如果你是第一次打开这个目录，建议先按下面的顺序进入：

1. [Python 生态全景与职业路线 (Python Landscape)](./01_environment/python_landscape_and_career_paths.md)：先看清 Python 能解决哪些工作问题，再决定后面的主攻方向。
2. [Python 多版本管理与虚拟环境 (Version Management)](./01_environment/python_version_management.md)：先把解释器、虚拟环境和版本切换这件事理顺。
3. [注释、输入输出与脚本入口 (I/O & Entry Point)](./02_basic_syntax/comments_and_input_output.md)：进入最小脚本闭环，先能写、能跑、能看结果。
4. [变量与数据类型 (Variables & Data Types)](./02_basic_syntax/variables_and_types.md)：把最常用的数据表示方式和命名习惯打稳。
5. [函数进阶与作用域 (Functions & Scopes)](./02_basic_syntax/function_basics.md)：从“能写几行代码”进入“能组织一个小脚本”。

走完这几篇之后，再回到这页，从“推荐学习路线图”或“三种选读方案”里挑自己的主线。

## 课程主线总览

| 阶段 | 目录 | 目标 | 预计时长 | 前置知识 |
| :--- | :--- | :--- | :--- | :--- |
| 环境篇 | `01_environment/` | 配好解释器、依赖管理和 IDE 调试体验 | 4-6 小时 | 基本命令行操作 |
| 基础语法篇 | `02_basic_syntax/` | 建立脚本结构、数据类型、流程控制、容器与函数基础 | 14-18 小时 | 环境篇 |
| 高级语法篇 | `03_advanced_syntax/` | 掌握迭代、装饰、上下文、OOP、文件与结构化数据处理 | 18-24 小时 | 基础语法篇 |
| 进阶专题篇 | `04_progressive_topics/` | 把 Python 能力落到正则、数据库、Web、采集、数据分析、机器学习、测试与项目交付 | 24-36 小时 | 高级语法篇 |

## 四个阶段分别解决什么问题

- `01_environment`：先解决“工具链是否稳定”。学完后你应该能独立安装与切换 Python、创建虚拟环境、安装依赖，并在 IDE 中调试最小脚本。
- `02_basic_syntax`：先解决“能不能顺畅写出小脚本”。学完后你应该能从零写出带输入输出、判断、循环、容器和函数的小工具脚本。
- `03_advanced_syntax`：先解决“能不能写出结构更清晰、更可复用的代码”。学完后你应该能把脚本拆成模块，处理文件和结构化数据，并理解装饰器、迭代器、上下文管理器和 OOP 基础。
- `04_progressive_topics`：先解决“能不能把语言能力落到真实工作”。学完后你应该能把 Python 用到日志分析、CLI 工具、数据库操作、Web 服务、采集脚本、数据分析、测试与项目交付。

## 推荐学习路线图

1. 第 1 站：先把 `01_environment` 跑通，确保解释器、虚拟环境、依赖管理和 IDE 调试体验稳定。
2. 第 2 站：在 `02_basic_syntax` 里完成“脚本入口与 I/O -> 变量 -> 运算符 -> 流程控制 -> 字符串 -> 容器 -> 函数”的最小闭环。
3. 第 3 站：进入 `03_advanced_syntax`，按“模块与抽象能力 -> 资源管理 -> 文件与结构化数据 -> OOP 与异常”的顺序补齐工程写法。
4. 第 4 站：回到 `04_progressive_topics`，优先挑 1-2 条和工作最相关的方向深挖，不建议一开始就把所有专题平铺扫完。
5. 第 5 站：每学完一个阶段，至少做一个自己的小脚本、小工具或小项目，把示例改造成真实场景。

如果你是业余时间学习，可以把这 5 站理解成一个 4-8 周的学习闭环；如果你是在工作中边用边学，也可以先从第 4 站进入，再回补前面的共同底座。

## 我该选哪条路线

- 如果你现在最常接触的是接口联调、自动化测试、测试工具、质量平台，先看“测试开发路线”。
- 如果你现在最常接触的是 CSV / JSON / SQL、报表、数据清洗、ETL，先看“数据方向路线”。
- 如果你还没完全确定方向，但希望先把 Python 语言和工程习惯打牢，先看“通用 Python 路线”。

## 三种选读方案

不管最后走哪条路线，`01_environment`、`02_basic_syntax`、`03_advanced_syntax` 都建议作为共同底座完整走一遍；真正的分流，主要发生在 `04_progressive_topics`。

### 方案：测试开发路线

- 适合人群：做接口自动化、测试框架、平台工具、质量平台相关工作的同学。
- 共同底座：`01_environment` 到 `03_advanced_syntax` 建议完整走完。
- 核心专题：
  - [标准库工具箱](./04_progressive_topics/standard_library_toolbox.md)
  - [配置分层、环境变量与密钥管理](./04_progressive_topics/configuration_and_secrets_management.md)
  - [Python 安全基础](./04_progressive_topics/python_security_basics.md)
  - [Python 安全进阶：反序列化、命令执行、供应链与审计](./04_progressive_topics/python_security_advanced.md)
  - [调试、traceback 与 Python 排障方法](./04_progressive_topics/debugging_and_troubleshooting.md)
  - [Python 常见坑位清单](./04_progressive_topics/common_python_pitfalls_checklist.md)
  - [HTTP 客户端、超时、重试与接口集成](./04_progressive_topics/http_client_and_api_integration.md)
  - [日志、CLI 与自动化脚本 (Logging & CLI Automation)](./04_progressive_topics/logging_and_cli_automation.md)
  - [可观测性：日志、指标与链路追踪](./04_progressive_topics/observability_logging_metrics_tracing.md)
  - [关系型数据库、MySQL 与 SQL 基础](./04_progressive_topics/relational_databases_and_sql.md)
  - [Python 数据库编程与 ETL 实战 (Database & ETL)](./04_progressive_topics/python_database_programming.md)
  - [SQLAlchemy ORM 与 Alembic 迁移 (DB Engineering)](./04_progressive_topics/sqlalchemy_and_alembic.md)
  - [Web 前端与 HTTP 基础](./04_progressive_topics/web_frontend_and_http_basics.md)
  - [Web 框架、Django / DRF 与服务交付](./04_progressive_topics/web_frameworks_and_api_delivery.md)
  - [FastAPI、ASGI 与接口服务交付](./04_progressive_topics/fastapi_and_asgi_delivery.md)
  - [FastAPI 进阶模式 (FastAPI Advanced Patterns)](./04_progressive_topics/fastapi_advanced_patterns.md)
  - [Redis 缓存与 Celery 异步任务 (Background Jobs)](./04_progressive_topics/redis_celery_and_background_jobs.md)
  - [测试金字塔、pytest fixture、参数化与 CI](./04_progressive_topics/testing_pyramid_and_pytest.md)
  - [测试工程进阶：conftest、分层、flaky 与契约测试](./04_progressive_topics/testing_engineering_advanced.md)
  - [pytest-asyncio 与性质测试入门](./04_progressive_topics/pytest_asyncio_and_property_based_testing.md)
  - [Ruff、Black、mypy、pytest 与 pre-commit 工具链](./04_progressive_topics/python_quality_toolchain.md)
  - [项目交付、Docker 与工程协作 (Project Delivery & Docker)](./04_progressive_topics/project_delivery_and_engineering_practice.md)
- 补充专题：
  - [面向 Python 工程的 Linux 与 Shell 基础](./04_progressive_topics/linux_shell_for_python.md)
  - [并发模型 (Concurrency Models)](./04_progressive_topics/python_concurrency.md)
  - [Asyncio 进阶：超时、限流与队列 (Asyncio Patterns)](./04_progressive_topics/asyncio_advanced_patterns.md)
  - [现代 Python 工具链：uv、PDM、Hatch 与 Nox](./04_progressive_topics/modern_python_tooling_uv_pdm_hatch_nox.md)
  - [内存排障：tracemalloc、gc 与对象增长](./04_progressive_topics/memory_profiling_tracemalloc_gc.md)
  - [办公文档、PDF、图像与消息自动化](./04_progressive_topics/office_and_document_automation.md)
  - [进阶专题篇 综合项目与交付练习](./04_progressive_topics/progressive_topics_integrated_projects.md)
  - [测试开发方向 Capstone Projects](./04_progressive_topics/testing_development_capstone_projects.md)
- 学完后的结果：能写稳脚本、能做接口联调、能搭基础测试工具和简单工程化交付链路。

### 方案：平台工具路线

- 适合人群：做内部平台、CLI 工具、任务执行平台、配置治理或自动化基础设施的同学。
- 共同底座：`01_environment` 到 `03_advanced_syntax` 建议完整走完。
- 核心专题：
  - [标准库工具箱](./04_progressive_topics/standard_library_toolbox.md)
  - [配置分层、环境变量与密钥管理](./04_progressive_topics/configuration_and_secrets_management.md)
  - [Python 安全基础](./04_progressive_topics/python_security_basics.md)
  - [Python 安全进阶：反序列化、命令执行、供应链与审计](./04_progressive_topics/python_security_advanced.md)
  - [日志、CLI 与自动化脚本 (Logging & CLI Automation)](./04_progressive_topics/logging_and_cli_automation.md)
  - [可观测性：日志、指标与链路追踪](./04_progressive_topics/observability_logging_metrics_tracing.md)
  - [并发模型 (Concurrency Models)](./04_progressive_topics/python_concurrency.md)
  - [Asyncio 进阶：超时、限流与队列 (Asyncio Patterns)](./04_progressive_topics/asyncio_advanced_patterns.md)
  - [Redis 缓存与 Celery 异步任务 (Background Jobs)](./04_progressive_topics/redis_celery_and_background_jobs.md)
  - [Ruff、Black、mypy、pytest 与 pre-commit 工具链](./04_progressive_topics/python_quality_toolchain.md)
  - [现代 Python 工具链：uv、PDM、Hatch 与 Nox](./04_progressive_topics/modern_python_tooling_uv_pdm_hatch_nox.md)
  - [项目交付、Docker 与工程协作 (Project Delivery & Docker)](./04_progressive_topics/project_delivery_and_engineering_practice.md)
- 补充专题：
  - [FastAPI、ASGI 与接口服务交付](./04_progressive_topics/fastapi_and_asgi_delivery.md)
  - [FastAPI 进阶模式 (FastAPI Advanced Patterns)](./04_progressive_topics/fastapi_advanced_patterns.md)
  - [打包发布：setuptools、wheel、twine 与私有 PyPI](./04_progressive_topics/packaging_and_publishing.md)
  - [SQLAlchemy ORM 与 Alembic 迁移 (DB Engineering)](./04_progressive_topics/sqlalchemy_and_alembic.md)
  - [平台工具方向 Capstone Projects](./04_progressive_topics/platform_tools_capstone_projects.md)
- 学完后的结果：能沉淀可复用工具入口、任务执行边界、配置治理与最小审计链路。

### 方案：数据方向路线

- 适合人群：做数据清洗、报表分析、ETL，或后续想转机器学习的同学。
- 共同底座：`01_environment` 到 `03_advanced_syntax` 建议完整走完。
- 核心专题：
  - [正则表达式进阶 (Regular Expressions)](./04_progressive_topics/python_re.md)
  - [标准库工具箱](./04_progressive_topics/standard_library_toolbox.md)
  - [文本编码与字节流 (Encoding & Bytes)](./03_advanced_syntax/bytes_encoding_and_text_files.md)
  - [关系型数据库、MySQL 与 SQL 基础](./04_progressive_topics/relational_databases_and_sql.md)
  - [Python 数据库编程与 ETL 实战 (Database & ETL)](./04_progressive_topics/python_database_programming.md)
  - [数据分析、NumPy / pandas 与可视化基础](./04_progressive_topics/data_analysis_and_visualization.md)
  - [机器学习入门与模型闭环](./04_progressive_topics/machine_learning_basics.md)
  - [Python 安全基础](./04_progressive_topics/python_security_basics.md)
  - [Python 安全进阶：反序列化、命令执行、供应链与审计](./04_progressive_topics/python_security_advanced.md)
- 补充专题：
  - [办公文档、PDF、图像与消息自动化](./04_progressive_topics/office_and_document_automation.md)
  - [面向 Python 工程的 Linux 与 Shell 基础](./04_progressive_topics/linux_shell_for_python.md)
  - [Web 前端与 HTTP 基础](./04_progressive_topics/web_frontend_and_http_basics.md)
  - [性能剖析](./04_progressive_topics/python_profiling.md)
  - [内存排障：tracemalloc、gc 与对象增长](./04_progressive_topics/memory_profiling_tracemalloc_gc.md)
  - [进阶专题篇 综合项目与交付练习](./04_progressive_topics/progressive_topics_integrated_projects.md)
  - [数据方向 Capstone Projects](./04_progressive_topics/data_capstone_projects.md)
- 学完后的结果：能完成 CSV / JSON / SQL 数据处理、分析脚本和最小建模闭环。

### 方案：通用 Python 路线

- 适合人群：还没完全确定方向，但想先把语言和工程习惯打牢的同学。
- 共同底座：`01_environment` 到 `03_advanced_syntax` 建议完整走完。
- 核心专题：
  - [标准库工具箱](./04_progressive_topics/standard_library_toolbox.md)
  - [日志、CLI 与自动化脚本 (Logging & CLI Automation)](./04_progressive_topics/logging_and_cli_automation.md)
  - [调试、traceback 与 Python 排障方法](./04_progressive_topics/debugging_and_troubleshooting.md)
  - [Python 常见坑位清单](./04_progressive_topics/common_python_pitfalls_checklist.md)
  - [面向 Python 工程的 Linux 与 Shell 基础](./04_progressive_topics/linux_shell_for_python.md)
  - [类型提示与静态检查](./04_progressive_topics/type_hints_and_static_checking.md)
  - [Ruff、Black、mypy、pytest 与 pre-commit 工具链](./04_progressive_topics/python_quality_toolchain.md)
  - [现代 Python 工具链：uv、PDM、Hatch 与 Nox](./04_progressive_topics/modern_python_tooling_uv_pdm_hatch_nox.md)
  - [Python 安全基础](./04_progressive_topics/python_security_basics.md)
  - [Python 安全进阶：反序列化、命令执行、供应链与审计](./04_progressive_topics/python_security_advanced.md)
  - [打包发布：setuptools、wheel、twine 与私有 PyPI](./04_progressive_topics/packaging_and_publishing.md)
  - [项目交付、Docker 与工程协作 (Project Delivery & Docker)](./04_progressive_topics/project_delivery_and_engineering_practice.md)
- 补充专题：
  - [Web 前端与 HTTP 基础](./04_progressive_topics/web_frontend_and_http_basics.md)
  - [关系型数据库、MySQL 与 SQL 基础](./04_progressive_topics/relational_databases_and_sql.md)
  - [数据分析、NumPy / pandas 与可视化基础](./04_progressive_topics/data_analysis_and_visualization.md)
  - [配置分层、环境变量与密钥管理](./04_progressive_topics/configuration_and_secrets_management.md)
  - [内存排障：tracemalloc、gc 与对象增长](./04_progressive_topics/memory_profiling_tracemalloc_gc.md)
  - [进阶专题篇 综合项目与交付练习](./04_progressive_topics/progressive_topics_integrated_projects.md)
  - [平台工具方向 Capstone Projects](./04_progressive_topics/platform_tools_capstone_projects.md)
- 学完后的结果：能独立完成结构清晰、可运行、可排障、可交付的小型 Python 工程。

## 学习里程碑 / 推荐练手项目

1. 学完 `01_environment`：至少完成一次本地 Python 安装、虚拟环境创建、依赖安装和 IDE 调试闭环。
2. 学完 `02_basic_syntax`：做一个带输入输出和流程控制的小脚本，比如日志筛选器、批量重命名工具、简单成绩统计器。
3. 学完 `03_advanced_syntax`：把脚本拆成 2-4 个模块，补上异常处理、JSON / CSV 读写，以及最基本的类封装。
4. 学完 `04_progressive_topics`：按自己的路线做一个岗位相关的小项目，比如接口测试工具、ETL 清洗脚本、CLI 自动化工具或最小 Web 服务。

## 本轮补充清单

- [x] 初学者补充：新增 [切片、解包与高频内置函数](./02_basic_syntax/slicing_unpacking_and_common_builtins.md)，把 `slice`、解包、`enumerate()`、`zip()`、`sorted()`、`any()`、`all()` 这类高频能力单独讲透。
- [x] 初学者补充：新增 [可变性、浅拷贝与深拷贝](./02_basic_syntax/mutability_and_copying.md)，补齐初学者最容易踩坑的“共享引用”和复制语义。
- [x] 进阶语法补充：新增 [dataclass、Enum 与结构化建模](./03_advanced_syntax/dataclasses_and_enum.md)，把常见数据模型写法从“字典堆着用”升级到“结构化表达”。
- [x] 进阶语法补充：新增 [编码、bytes 与文本文件处理](./03_advanced_syntax/bytes_encoding_and_text_files.md)，补齐字符串、字节流、文件编码和文本边界。
- [x] 从业者补充：新增 [asyncio 进阶：取消、超时、队列与限流](./04_progressive_topics/asyncio_advanced_patterns.md)，把协程从“会用 `gather()`”推进到“能处理真实异步边界”。
- [x] 从业者补充：新增 [FastAPI、ASGI 与接口服务交付](./04_progressive_topics/fastapi_and_asgi_delivery.md)，补齐 Python 服务端在现代接口项目里的常见交付形态。
- [x] 初学者补充：新增 [推导式与生成器表达式](./02_basic_syntax/comprehensions_and_generator_expressions.md)，补齐从循环累加到声明式构造集合的常用写法。
- [x] 初学者补充：新增 [breakpoint / pdb 基础](./03_advanced_syntax/breakpoint_and_pdb_basics.md)，让排障能力从 `print()` 过渡到断点与单步调试。
- [x] 通用排障补充：新增 [常见 Python 坑位清单](./04_progressive_topics/common_python_pitfalls_checklist.md)，把可变默认值、闭包绑定、路径与时区等问题收成复盘清单。
- [x] 从业者补充：新增 [SQLAlchemy 与 Alembic](./04_progressive_topics/sqlalchemy_and_alembic.md)，补齐 ORM、事务和迁移治理的基本工作流。
- [x] 从业者补充：新增 [Redis、Celery 与后台任务](./04_progressive_topics/redis_celery_and_background_jobs.md)，补齐缓存、队列和异步任务的工程配合方式。
- [x] 从业者补充：新增 [可观测性：日志、指标与链路追踪](./04_progressive_topics/observability_logging_metrics_tracing.md)，补齐线上排障时最关键的三类信号。
- [x] 从业者补充：新增 [现代 Python 工具链：uv / pdm / hatch / nox](./04_progressive_topics/modern_python_tooling_uv_pdm_hatch_nox.md)，补齐项目初始化、运行矩阵和工具选型视角。
- [x] 从业者补充：新增 [pytest-asyncio 与性质测试](./04_progressive_topics/pytest_asyncio_and_property_based_testing.md)，补齐异步接口和边界输入的验证方法。
- [x] 从业者补充：新增 [内存分析：tracemalloc / gc](./04_progressive_topics/memory_profiling_tracemalloc_gc.md)，补齐对象增长定位和泄漏排查入口。
- [x] 从业者补充：新增 [Python 安全基础](./04_progressive_topics/python_security_basics.md)，补齐密钥管理、注入防护、路径边界和最小权限的最低防守动作。
- [x] 练习闭环补充：新增 [环境篇 Mini Projects](./01_environment/environment_mini_projects.md)，把解释器、虚拟环境和启动说明变成可复现练习。
- [x] 练习闭环补充：新增 [基础语法篇 Mini Projects](./02_basic_syntax/basic_syntax_mini_projects.md)，把变量、循环、字符串、容器和函数串成小工具训练。
- [x] 练习闭环补充：新增 [高级语法篇 Mini Projects](./03_advanced_syntax/advanced_syntax_mini_projects.md)，把模块拆分、生成器、dataclass 和错误处理落到项目骨架里。
- [x] 练习闭环补充：新增 [进阶专题篇 综合项目](./04_progressive_topics/progressive_topics_integrated_projects.md)，把接口、异步、观测、测试和交付串成完整练习路线。
- [x] 从业者补充：新增 [FastAPI 进阶模式](./04_progressive_topics/fastapi_advanced_patterns.md)，把依赖注入、生命周期、异常治理和测试替身拉进真实服务骨架。
- [x] 从业者补充：新增 [Python 安全进阶](./04_progressive_topics/python_security_advanced.md)，把反序列化、命令执行、供应链和审计问题收成第二层防守清单。
- [x] Capstone 补充：新增 [测试开发方向 Capstone Projects](./04_progressive_topics/testing_development_capstone_projects.md)，把质量平台、smoke 服务和报告归档串成方向化综合项目。
- [x] Capstone 补充：新增 [数据方向 Capstone Projects](./04_progressive_topics/data_capstone_projects.md)，把数据流程、质量规则和分析交付串成方向化综合项目。
- [x] Capstone 补充：新增 [平台工具方向 Capstone Projects](./04_progressive_topics/platform_tools_capstone_projects.md)，把 CLI、任务平台和配置治理串成方向化综合项目。
- [ ] 深度补充：新增 [元编程与描述符协议](./03_advanced_syntax/metaprogramming_and_descriptors.md)，补齐底层机制剖析。
- [ ] 深度补充：新增 [内存管理与 GC 调优](./04_progressive_topics/memory_management_and_gc.md)，补齐内存模型与调优入口。
- [x] 结构修正：修复内容索引漏项，补回配置、调试、HTTP 客户端、质量工具链和测试工程进阶等专题入口。
- [x] 结构修正：修正总篇数统计，并同步 `Makefile` 入口说明，避免 README 与实际目录不一致。

## 当前覆盖范围

- 当前共有 4 个阶段、71 篇可校验笔记。
- `01_environment` 到 `04_progressive_topics` 已覆盖环境搭建、语言基础、高级语法，以及配置管理、调试排障、数据库、Web、采集、数据分析、机器学习、测试、性能、质量工具链、打包发布和项目交付等主题。

## 推荐先读 6 篇

- 如果你暂时不想完整浏览整份目录，可以先读下面这 6 篇，把“方向感 -> 环境 -> 脚本 -> 抽象 -> 工程入口”这条主线先跑通：

1. [Python 生态全景与职业路线 (Python Landscape)](./01_environment/python_landscape_and_career_paths.md)：先知道 Python 在不同岗位里怎么用。
2. [Python 多版本管理与虚拟环境 (Version Management)](./01_environment/python_version_management.md)：先把解释器、虚拟环境和版本切换理顺。
3. [注释、输入输出与脚本入口 (I/O & Entry Point)](./02_basic_syntax/comments_and_input_output.md)：先建立最小脚本闭环。
4. [变量与数据类型 (Variables & Data Types)](./02_basic_syntax/variables_and_types.md)：先把最常见的数据表示方式打稳。
5. [函数进阶与作用域 (Functions & Scopes)](./02_basic_syntax/function_basics.md)：先从“写几行代码”走到“组织一个小脚本”。
6. [日志、CLI 与自动化脚本 (Logging & CLI Automation)](./04_progressive_topics/logging_and_cli_automation.md)：提前看看 Python 在真实工作里怎样长成可复用工具。

## 内容索引

### 环境篇

| 主题 | 文件 | 说明 |
| :--- | :--- | :--- |
| Python 生态全景与职业路线 (Python Landscape) | [python_landscape_and_career_paths.md](./01_environment/python_landscape_and_career_paths.md) | 先建立能力地图，明确 Python 在不同岗位里的使用方式 |
| Python 多版本管理与虚拟环境 (Version Management) | [python_version_management.md](./01_environment/python_version_management.md) | 理清解释器、虚拟环境和版本切换 |
| pip 与 Poetry 依赖管理 (Dependency Management) | [dependency_management.md](./01_environment/dependency_management.md) | 解决安装依赖、锁版本、项目隔离的问题 |
| VS Code Python 开发环境一体化配置 (IDE Setup) | [ide_setup.md](./01_environment/ide_setup.md) | 补齐编辑、运行、调试、格式化体验 |
| 环境篇 Mini Projects (Environment Lab) | [environment_mini_projects.md](./01_environment/environment_mini_projects.md) | 把环境搭建变成可复现、可交接的动手闭环 |

### 基础语法篇

| 主题 | 文件 | 说明 |
| :--- | :--- | :--- |
| 注释、输入输出与脚本入口 (I/O & Entry Point) | [comments_and_input_output.md](./02_basic_syntax/comments_and_input_output.md) | 建立脚本最小闭环 |
| 变量与数据类型 (Variables & Data Types) | [variables_and_types.md](./02_basic_syntax/variables_and_types.md) | 理清对象、类型、可变性与命名习惯 |
| 运算符与表达式深度解析 (Operators & Expressions) | [operators_and_expressions.md](./02_basic_syntax/operators_and_expressions.md) | 掌握条件判断与计算表达 |
| 流程控制深度解析 (Flow Control) | [control_flow.md](./02_basic_syntax/control_flow.md) | 把 if / for / while / break / continue 用顺 |
| 字符串处理与常用方法 (String Processing) | [strings_and_methods.md](./02_basic_syntax/strings_and_methods.md) | 处理文本、格式化、切片和编码 |
| 核心容器：列表、元组、集合、字典 (Collections) | [collections.md](./02_basic_syntax/collections.md) | 理解最常用容器及其适用边界 |
| 推导式与生成器表达式 (Comprehensions & Generator Expressions) | [comprehensions_and_generator_expressions.md](./02_basic_syntax/comprehensions_and_generator_expressions.md) | 补齐推导式、生成器表达式和惰性迭代的常用写法 |
| 切片、解包与高频内置函数 (Slicing & Built-ins) | [slicing_unpacking_and_common_builtins.md](./02_basic_syntax/slicing_unpacking_and_common_builtins.md) | 把高频迭代写法、排序与聚合判断补成常用工具层 |
| 变量可变性与深浅拷贝 (Mutability & Copying) | [mutability_and_copying.md](./02_basic_syntax/mutability_and_copying.md) | 理清引用共享、复制语义和嵌套对象修改边界 |
| 函数进阶与作用域 (Functions & Scopes) | [function_basics.md](./02_basic_syntax/function_basics.md) | 进入参数、返回值、作用域与函数化封装 |
| 基础语法篇 Mini Projects (Basics Lab) | [basic_syntax_mini_projects.md](./02_basic_syntax/basic_syntax_mini_projects.md) | 把变量、循环、容器和函数串成能跑的小工具 |

### 高级语法篇

| 主题 | 文件 | 说明 |
| :--- | :--- | :--- |
| 模块与包进阶 (Modules & Packages) | [modules_and_packages.md](./03_advanced_syntax/modules_and_packages.md) | 把代码从单文件脚本升级为可组织的结构 |
| 迭代器与生成器 (Iterators & Generators) | [iterators_and_generators.md](./03_advanced_syntax/iterators_and_generators.md) | 理解惰性求值与迭代协议 |
| 函数式编程与递归 (Functional & Recursion) | [functional_programming_and_recursion.md](./03_advanced_syntax/functional_programming_and_recursion.md) | 补齐抽象能力与函数式思维 |
| 装饰器 (Decorators) | [decorators.md](./03_advanced_syntax/decorators.md) | 理解横切逻辑与函数增强 |
| 上下文管理器进阶 (Context Managers) | [context_managers.md](./03_advanced_syntax/context_managers.md) | 学会把资源申请与释放写稳 |
| 文件读写与路径进阶 (File I/O & Pathlib) | [file_io_and_pathlib.md](./03_advanced_syntax/file_io_and_pathlib.md) | 进入真实文件系统和路径处理 |
| 序列化与结构化数据 (JSON & CSV) | [structured_data_formats.md](./03_advanced_syntax/structured_data_formats.md) | 进入结构化数据交换 |
| 结构化建模进阶 (Dataclasses & Enum) | [dataclasses_and_enum.md](./03_advanced_syntax/dataclasses_and_enum.md) | 提升数据表达清晰度，减少裸字典和魔法字符串 |
| 文本编码与字节流 (Encoding & Bytes) | [bytes_encoding_and_text_files.md](./03_advanced_syntax/bytes_encoding_and_text_files.md) | 理解文本、字节流和文件编码之间的边界 |
| 面向对象 (Object-Oriented Programming) | [object_oriented_programming.md](./03_advanced_syntax/object_oriented_programming.md) | 理解类、对象、继承、封装与多态 |
| 异常体系 (Exception Handling) | [exceptions.md](./03_advanced_syntax/exceptions.md) | 补齐错误处理、排障与失败边界 |
| 断点调试与 pdb 进阶 (Debugging & PDB) | [breakpoint_and_pdb_basics.md](./03_advanced_syntax/breakpoint_and_pdb_basics.md) | 补齐从 print 到断点调试的交互式定位能力 |
| 高级语法篇 Mini Projects (Advanced Lab) | [advanced_syntax_mini_projects.md](./03_advanced_syntax/advanced_syntax_mini_projects.md) | 把模块、生成器和结构化对象练进小型工程脚手架 |
| 元编程与描述符协议 | [metaprogramming_and_descriptors.md](./03_advanced_syntax/metaprogramming_and_descriptors.md) | 理解 __new__、元类与描述符协议的底层魔法 |

### 进阶专题篇

| 主题 | 文件 | 说明 |
| :--- | :--- | :--- |
| 正则表达式进阶 (Regular Expressions) | [python_re.md](./04_progressive_topics/python_re.md) | 处理文本匹配、提取与替换 |
| Python 关键字全集 | [python_keywords.md](./04_progressive_topics/python_keywords.md) | 对语言关键字做统一回顾 |
| 标准库工具箱 | [standard_library_toolbox.md](./04_progressive_topics/standard_library_toolbox.md) | 补齐日常脚本最常用工具箱 |
| 配置分层、环境变量与密钥管理 | [configuration_and_secrets_management.md](./04_progressive_topics/configuration_and_secrets_management.md) | 管理多环境配置和敏感信息边界 |
| Python 安全基础 | [python_security_basics.md](./04_progressive_topics/python_security_basics.md) | 补齐输入边界、密钥管理、注入和路径安全的基础意识 |
| Python 安全进阶：反序列化、命令执行、供应链与审计 | [python_security_advanced.md](./04_progressive_topics/python_security_advanced.md) | 补齐反序列化、命令执行、供应链与审计治理的进阶视角 |
| 调试、traceback 与 Python 排障方法 | [debugging_and_troubleshooting.md](./04_progressive_topics/debugging_and_troubleshooting.md) | 建立排障证据链和最小复现思维 |
| Python 常见坑位清单 | [common_python_pitfalls_checklist.md](./04_progressive_topics/common_python_pitfalls_checklist.md) | 把高频坑位收成排查、复盘和 code review 清单 |
| HTTP 客户端、超时、重试与接口集成 | [http_client_and_api_integration.md](./04_progressive_topics/http_client_and_api_integration.md) | 把请求调用从“能发”提升到“更稳定可控” |
| 日志、CLI 与自动化脚本 (Logging & CLI Automation) | [logging_and_cli_automation.md](./04_progressive_topics/logging_and_cli_automation.md) | 让脚本更像可复用工具 |
| 可观测性：日志、指标与链路追踪 | [observability_logging_metrics_tracing.md](./04_progressive_topics/observability_logging_metrics_tracing.md) | 补齐日志、指标与链路追踪三件套的协作视角 |
| 面向 Python 工程的 Linux 与 Shell 基础 | [linux_shell_for_python.md](./04_progressive_topics/linux_shell_for_python.md) | 学会在真实运行环境里排障与协作 |
| 并发模型 (Concurrency Models) | [python_concurrency.md](./04_progressive_topics/python_concurrency.md) | 理解线程、进程、协程和适用边界 |
| Asyncio 进阶：超时、限流与队列 (Asyncio Patterns) | [asyncio_advanced_patterns.md](./04_progressive_topics/asyncio_advanced_patterns.md) | 补齐真实异步任务中的取消、背压和资源治理 |
| 办公文档、PDF、图像与消息自动化 | [office_and_document_automation.md](./04_progressive_topics/office_and_document_automation.md) | 进入测试报告和办公自动化场景 |
| 关系型数据库、MySQL 与 SQL 基础 | [relational_databases_and_sql.md](./04_progressive_topics/relational_databases_and_sql.md) | 打稳数据模型、SQL 和索引基础 |
| Python 数据库编程与 ETL 实战 (Database & ETL) | [python_database_programming.md](./04_progressive_topics/python_database_programming.md) | 把 Python 和数据库真正连起来 |
| SQLAlchemy ORM 与 Alembic 迁移 (DB Engineering) | [sqlalchemy_and_alembic.md](./04_progressive_topics/sqlalchemy_and_alembic.md) | 补齐 ORM、事务边界和迁移治理能力 |
| Web 前端与 HTTP 基础 | [web_frontend_and_http_basics.md](./04_progressive_topics/web_frontend_and_http_basics.md) | 理解请求、响应、页面和协议边界 |
| Web 框架、Django / DRF 与服务交付 | [web_frameworks_and_api_delivery.md](./04_progressive_topics/web_frameworks_and_api_delivery.md) | 进入接口服务、缓存、异步任务与上线 |
| FastAPI、ASGI 与接口服务交付 | [fastapi_and_asgi_delivery.md](./04_progressive_topics/fastapi_and_asgi_delivery.md) | 补齐现代 Python API 服务的常见交付路径 |
| FastAPI 进阶模式 (FastAPI Advanced Patterns) | [fastapi_advanced_patterns.md](./04_progressive_topics/fastapi_advanced_patterns.md) | 补齐依赖注入、生命周期、异常治理与测试替身的实战模式 |
| Redis 缓存与 Celery 异步任务 (Background Jobs) | [redis_celery_and_background_jobs.md](./04_progressive_topics/redis_celery_and_background_jobs.md) | 补齐缓存、队列与后台任务的常见工程模式 |
| 网络采集、浏览器自动化与 Scrapy 思维 | [data_collection_and_browser_automation.md](./04_progressive_topics/data_collection_and_browser_automation.md) | 进入采集、解析和浏览器自动化 |
| 数据分析、NumPy / pandas 与可视化基础 | [data_analysis_and_visualization.md](./04_progressive_topics/data_analysis_and_visualization.md) | 进入表格处理、聚合与图表表达 |
| 机器学习入门与模型闭环 | [machine_learning_basics.md](./04_progressive_topics/machine_learning_basics.md) | 建立训练、验证、评估的最小闭环 |
| 性能剖析 | [python_profiling.md](./04_progressive_topics/python_profiling.md) | 学会定位慢代码和资源瓶颈 |
| 内存排障：tracemalloc、gc 与对象增长 | [memory_profiling_tracemalloc_gc.md](./04_progressive_topics/memory_profiling_tracemalloc_gc.md) | 补齐内存增长定位、快照对比与 GC 排障方法 |
| 内存管理与 GC 调优 (Memory Management & GC) | [memory_management_and_gc.md](./04_progressive_topics/memory_management_and_gc.md) | 深入理解引用计数、分代回收与内存池机制 |
| 类型提示与静态检查 | [type_hints_and_static_checking.md](./04_progressive_topics/type_hints_and_static_checking.md) | 提升可维护性和静态可见性 |
| Ruff、Black、mypy、pytest 与 pre-commit 工具链 | [python_quality_toolchain.md](./04_progressive_topics/python_quality_toolchain.md) | 把规范、测试和类型检查前移到本地与 CI |
| 现代 Python 工具链：uv、PDM、Hatch 与 Nox | [modern_python_tooling_uv_pdm_hatch_nox.md](./04_progressive_topics/modern_python_tooling_uv_pdm_hatch_nox.md) | 补齐现代 Python 工具链的选型与协作方式 |
| 测试金字塔、pytest fixture、参数化与 CI | [testing_pyramid_and_pytest.md](./04_progressive_topics/testing_pyramid_and_pytest.md) | 回到测试工程最核心的验证能力 |
| 测试工程进阶：conftest、分层、flaky 与契约测试 | [testing_engineering_advanced.md](./04_progressive_topics/testing_engineering_advanced.md) | 把测试项目从“能跑”提升到“更稳、更可维护” |
| pytest-asyncio 与性质测试入门 | [pytest_asyncio_and_property_based_testing.md](./04_progressive_topics/pytest_asyncio_and_property_based_testing.md) | 补齐异步测试与性质测试的实战入口 |
| 打包发布：setuptools、wheel、twine 与私有 PyPI | [packaging_and_publishing.md](./04_progressive_topics/packaging_and_publishing.md) | 补齐包管理与分发视角 |
| 项目交付、Docker 与工程协作 (Project Delivery & Docker) | [project_delivery_and_engineering_practice.md](./04_progressive_topics/project_delivery_and_engineering_practice.md) | 把代码真正带到上线和协作场景 |
| 进阶专题篇 综合项目与交付练习 | [progressive_topics_integrated_projects.md](./04_progressive_topics/progressive_topics_integrated_projects.md) | 把接口、异步、测试、观测和交付串成综合项目训练 |
| 测试开发方向 Capstone Projects | [testing_development_capstone_projects.md](./04_progressive_topics/testing_development_capstone_projects.md) | 按测试开发方向给出质量平台与自动化服务的综合项目题 |
| 数据方向 Capstone Projects | [data_capstone_projects.md](./04_progressive_topics/data_capstone_projects.md) | 按数据方向给出数据流程、质量监控与分析交付的综合项目题 |
| 平台工具方向 Capstone Projects | [platform_tools_capstone_projects.md](./04_progressive_topics/platform_tools_capstone_projects.md) | 按平台工具方向给出 CLI、任务平台与配置治理的综合项目题 |

## 怎么使用这套笔记

1. 先看“快速开始”“推荐学习路线图”“三种选读方案”，再按主线阶段学习，不建议一上来只挑感兴趣的高级专题。
2. 每篇笔记先看目录，再看“为什么学”“学什么”“怎么用”，最后做 `Self-Check`。
3. 每学完一个主题，至少手敲一遍示例，并改成自己的场景。
4. 如果你是测试开发，优先把日志、CLI、数据库、Web、测试、项目交付这几组专题练熟。
5. 遇到不懂的地方，先最小复现，再回看对应主线阶段，不要直接跳去堆框架。

## 一键初始化

```bash
cd testing/python_notes
python -m pip install -r requirements.txt
pytest tests -q
```

## 工程化约定

- 所有笔记使用 GitHub Flavored Markdown。
- 每篇笔记都包含 front matter、目录锚点、Self-Check、参考答案、参考链接和版本记录。
- `tests/test_markdown_examples.py` 会执行所有 `python` 代码块，并使用独立编译标志，避免被测试文件自身的 future import 掩盖兼容性问题。
- 当前共有 4 个阶段目录、71 篇可校验笔记。
- 当前示例以 Python 3.8+ 为最低兼容目标；遇到 3.10+ 语法特性时会明确标注版本差异。
- `images/` 目录按“笔记名_序号.png”维护截图与示意图资源。
- 当前目录提供 [Makefile](./Makefile) 作为常用命令入口，可使用 `make install`、`make test`、`make lint`、`make format`、`make check`。

## 关联入口

- 示例校验脚本: [tests/test_markdown_examples.py](./tests/test_markdown_examples.py)
- 依赖清单: [requirements.txt](./requirements.txt)
- 常用命令: [Makefile](./Makefile)
- 结构清单: [manifest.json](./manifest.json)
- 知识汇总页: [../../common/docs/indexes/knowledge_hub.md](../../common/docs/indexes/knowledge_hub.md)
- 模板参考: [../../common/docs/template.md](../../common/docs/template.md)
