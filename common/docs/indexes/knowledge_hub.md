# 知识库汇总首页

> 本页由 `python scripts/build_knowledge_index.py` 自动生成，用于汇总带标准元数据的知识笔记。

---

## 总览

- 已收录笔记数: **98**
- 覆盖模块数: **4**
- 搜索入口: `python scripts/search_knowledge.py <关键词>`

---

## 模块索引

### `ai`

- 领域数: **3**
- 笔记数: **3**

#### `dataset`

| 标题 | 技术栈 | 层级 | 标签 | 路径 |
| :--- | :--- | :--- | :--- | :--- |
| 数据集清洗基础 | `cleaning` | `basics` | dataset, cleaning, ai, data-quality | [ai/dataset/cleaning/basics/dataset_cleaning_basics.md](../../../ai/dataset/cleaning/basics/dataset_cleaning_basics.md) |

#### `llm-agent`

| 标题 | 技术栈 | 层级 | 标签 | 路径 |
| :--- | :--- | :--- | :--- | :--- |
| Prompt 设计基础 | `prompt` | `basics` | prompt, llm, ai, instruction, context | [ai/llm-agent/prompt/basics/prompt_design_basics.md](../../../ai/llm-agent/prompt/basics/prompt_design_basics.md) |

#### `mlops`

| 标题 | 技术栈 | 层级 | 标签 | 路径 |
| :--- | :--- | :--- | :--- | :--- |
| 模型部署流水线基础 | `deployment` | `basics` | mlops, deployment, model-serving, ai | [ai/mlops/deployment/basics/model_deployment_pipeline_basics.md](../../../ai/mlops/deployment/basics/model_deployment_pipeline_basics.md) |

### `backend`

- 领域数: **3**
- 笔记数: **3**

#### `database`

| 标题 | 技术栈 | 层级 | 标签 | 路径 |
| :--- | :--- | :--- | :--- | :--- |
| MySQL 索引设计基础 | `mysql` | `basics` | mysql, backend, index, query-optimization | [backend/database/mysql/basics/mysql_index_design_basics.md](../../../backend/database/mysql/basics/mysql_index_design_basics.md) |

#### `distributed`

| 标题 | 技术栈 | 层级 | 标签 | 路径 |
| :--- | :--- | :--- | :--- | :--- |
| 缓存击穿、穿透与雪崩基础 | `caching` | `basics` | backend, cache, redis, high-concurrency, resilience | [backend/distributed/caching/basics/cache_breakdown_penetration_avalanche.md](../../../backend/distributed/caching/basics/cache_breakdown_penetration_avalanche.md) |

#### `system-design`

| 标题 | 技术栈 | 层级 | 标签 | 路径 |
| :--- | :--- | :--- | :--- | :--- |
| 高可用与降级设计基础 | `high-availability` | `basics` | backend, system-design, high-availability, degradation, resilience | [backend/system-design/high-availability/basics/high_availability_and_degradation_basics.md](../../../backend/system-design/high-availability/basics/high_availability_and_degradation_basics.md) |

### `frontend`

- 领域数: **3**
- 笔记数: **3**

#### `engineering`

| 标题 | 技术栈 | 层级 | 标签 | 路径 |
| :--- | :--- | :--- | :--- | :--- |
| Vite 从本地开发到生产构建的流水线基础 | `build-tools` | `basics` | vite, frontend-engineering, build, bundling | [frontend/engineering/build-tools/basics/vite_dev_to_build_pipeline.md](../../../frontend/engineering/build-tools/basics/vite_dev_to_build_pipeline.md) |

#### `frameworks`

| 标题 | 技术栈 | 层级 | 标签 | 路径 |
| :--- | :--- | :--- | :--- | :--- |
| React 状态提升与组件通信基础 | `react` | `basics` | react, state, props, component-communication | [frontend/frameworks/react/basics/react_state_and_component_communication.md](../../../frontend/frameworks/react/basics/react_state_and_component_communication.md) |

#### `performance`

| 标题 | 技术栈 | 层级 | 标签 | 路径 |
| :--- | :--- | :--- | :--- | :--- |
| Web Vitals 与前端性能预算基础 | `web-vitals` | `basics` | web-vitals, frontend-performance, lcp, inp, cls | [frontend/performance/web-vitals/basics/web_vitals_and_performance_budget.md](../../../frontend/performance/web-vitals/basics/web_vitals_and_performance_budget.md) |

### `testing`

- 领域数: **7**
- 笔记数: **89**

#### `ai-eval`

| 标题 | 技术栈 | 层级 | 标签 | 路径 |
| :--- | :--- | :--- | :--- | :--- |
| RAG 检索阶段指标设计 | `ragas` | `advanced` | ragas, ai-eval, rag, retrieval, recall, precision | [testing/ai-eval/ragas/advanced/rag_retrieval_metric_design.md](../../../testing/ai-eval/ragas/advanced/rag_retrieval_metric_design.md) |
| RAG 黄金测试集构建方法 | `ragas` | `advanced` | ragas, ai-eval, rag, dataset, benchmark, testset | [testing/ai-eval/ragas/advanced/rag_gold_dataset_construction.md](../../../testing/ai-eval/ragas/advanced/rag_gold_dataset_construction.md) |
| 使用 Ragas 建立 RAG 评测基础 | `ragas` | `basics` | ragas, ai-eval, rag, faithfulness, context-recall | [testing/ai-eval/ragas/basics/ragas_rag_evaluation_basics.md](../../../testing/ai-eval/ragas/basics/ragas_rag_evaluation_basics.md) |

#### `api`

| 标题 | 技术栈 | 层级 | 标签 | 路径 |
| :--- | :--- | :--- | :--- | :--- |
| 使用 Pytest 做 OpenAPI Schema 校验 | `pytest` | `advanced` | pytest, api-testing, openapi, schema, contract | [testing/api/pytest/advanced/openapi_schema_validation_with_pytest.md](../../../testing/api/pytest/advanced/openapi_schema_validation_with_pytest.md) |
| 接口鉴权与签名测试设计 | `pytest` | `advanced` | pytest, api-testing, auth, signature, security | [testing/api/pytest/advanced/authentication_and_signature_testing.md](../../../testing/api/pytest/advanced/authentication_and_signature_testing.md) |
| 使用 Pytest 做接口契约测试基础 | `pytest` | `basics` | pytest, api-testing, contract-testing, requests | [testing/api/pytest/basics/api_contract_testing_with_pytest.md](../../../testing/api/pytest/basics/api_contract_testing_with_pytest.md) |

#### `mobile`

| 标题 | 技术栈 | 层级 | 标签 | 路径 |
| :--- | :--- | :--- | :--- | :--- |
| Appium 会话管理与 Capability 设计 | `appium` | `advanced` | appium, mobile-testing, capability, session, device | [testing/mobile/appium/advanced/appium_session_and_capability_design.md](../../../testing/mobile/appium/advanced/appium_session_and_capability_design.md) |
| Appium 等待机制与稳定性设计 | `appium` | `advanced` | appium, mobile-testing, wait, stability, flakiness | [testing/mobile/appium/advanced/appium_waiting_and_stability_patterns.md](../../../testing/mobile/appium/advanced/appium_waiting_and_stability_patterns.md) |
| Appium 元素定位策略基础 | `appium` | `basics` | appium, mobile-testing, locator, uiautomator2 | [testing/mobile/appium/basics/appium_locator_strategy_basics.md](../../../testing/mobile/appium/basics/appium_locator_strategy_basics.md) |

#### `performance`

| 标题 | 技术栈 | 层级 | 标签 | 路径 |
| :--- | :--- | :--- | :--- | :--- |
| k6 阶梯加压与场景建模 | `k6` | `advanced` | k6, performance-testing, scenario, stages, workload | [testing/performance/k6/advanced/k6_stage_and_scenario_design.md](../../../testing/performance/k6/advanced/k6_stage_and_scenario_design.md) |
| 性能阈值设计与容量预估基础 | `k6` | `advanced` | k6, performance-testing, threshold, capacity, p95 | [testing/performance/k6/advanced/performance_thresholds_and_capacity_estimation.md](../../../testing/performance/k6/advanced/performance_thresholds_and_capacity_estimation.md) |
| 使用 k6 建立性能测试基础模型 | `k6` | `basics` | k6, performance-testing, load-testing, threshold | [testing/performance/k6/basics/k6_load_testing_basics.md](../../../testing/performance/k6/basics/k6_load_testing_basics.md) |

#### `python_notes`

| 标题 | 技术栈 | 层级 | 标签 | 路径 |
| :--- | :--- | :--- | :--- | :--- |
| Asyncio 进阶：超时、限流与队列 (Asyncio Patterns) | `python` | `advanced` | python, asyncio, concurrency, timeout, semaphore, queue | [testing/python_notes/04_progressive_topics/asyncio_advanced_patterns.md](../../../testing/python_notes/04_progressive_topics/asyncio_advanced_patterns.md) |
| FastAPI 进阶模式 (FastAPI Advanced Patterns) | `python` | `advanced` | python, fastapi, dependency-injection, lifespan, middleware, testing | [testing/python_notes/04_progressive_topics/fastapi_advanced_patterns.md](../../../testing/python_notes/04_progressive_topics/fastapi_advanced_patterns.md) |
| FastAPI、ASGI 与接口服务交付 | `python` | `advanced` | python, fastapi, asgi, uvicorn, api, delivery | [testing/python_notes/04_progressive_topics/fastapi_and_asgi_delivery.md](../../../testing/python_notes/04_progressive_topics/fastapi_and_asgi_delivery.md) |
| HTTP 客户端、超时、重试与接口集成 | `python` | `advanced` | python, http, api, timeout, retry, integration | [testing/python_notes/04_progressive_topics/http_client_and_api_integration.md](../../../testing/python_notes/04_progressive_topics/http_client_and_api_integration.md) |
| Python 关键字全集 | `python` | `advanced` | python, keywords, syntax, parser, highlight | [testing/python_notes/04_progressive_topics/python_keywords.md](../../../testing/python_notes/04_progressive_topics/python_keywords.md) |
| Python 安全基础 | `python` | `advanced` | python, security, secrets, validation, sql-injection, path-traversal | [testing/python_notes/04_progressive_topics/python_security_basics.md](../../../testing/python_notes/04_progressive_topics/python_security_basics.md) |
| Python 安全进阶：反序列化、命令执行、供应链与审计 | `python` | `advanced` | python, security, deserialization, subprocess, audit, supply-chain | [testing/python_notes/04_progressive_topics/python_security_advanced.md](../../../testing/python_notes/04_progressive_topics/python_security_advanced.md) |
| Python 常见坑位清单 | `python` | `advanced` | python, pitfalls, defaults, late-binding, imports, truthiness | [testing/python_notes/04_progressive_topics/common_python_pitfalls_checklist.md](../../../testing/python_notes/04_progressive_topics/common_python_pitfalls_checklist.md) |
| Python 数据库编程与 ETL 实战 (Database & ETL) | `python` | `advanced` | python, database, sqlite, etl, transactions, sql-injection | [testing/python_notes/04_progressive_topics/python_database_programming.md](../../../testing/python_notes/04_progressive_topics/python_database_programming.md) |
| Redis 缓存与 Celery 异步任务 (Background Jobs) | `python` | `advanced` | python, redis, celery, background-jobs, cache, idempotency | [testing/python_notes/04_progressive_topics/redis_celery_and_background_jobs.md](../../../testing/python_notes/04_progressive_topics/redis_celery_and_background_jobs.md) |
| Ruff、Black、mypy、pytest 与 pre-commit 工具链 | `python` | `advanced` | python, ruff, black, mypy, pytest, pre-commit | [testing/python_notes/04_progressive_topics/python_quality_toolchain.md](../../../testing/python_notes/04_progressive_topics/python_quality_toolchain.md) |
| SQLAlchemy ORM 与 Alembic 迁移 (DB Engineering) | `python` | `advanced` | python, sqlalchemy, alembic, orm, database, migration, transaction | [testing/python_notes/04_progressive_topics/sqlalchemy_and_alembic.md](../../../testing/python_notes/04_progressive_topics/sqlalchemy_and_alembic.md) |
| Web 前端与 HTTP 基础 | `python` | `advanced` | python, web, http, html, frontend, testing | [testing/python_notes/04_progressive_topics/web_frontend_and_http_basics.md](../../../testing/python_notes/04_progressive_topics/web_frontend_and_http_basics.md) |
| Web 框架、Django / DRF 与服务交付 | `python` | `advanced` | python, web, django, drf, api, celery, cache | [testing/python_notes/04_progressive_topics/web_frameworks_and_api_delivery.md](../../../testing/python_notes/04_progressive_topics/web_frameworks_and_api_delivery.md) |
| pytest-asyncio 与性质测试入门 | `python` | `advanced` | python, pytest, asyncio, hypothesis, property-based-testing | [testing/python_notes/04_progressive_topics/pytest_asyncio_and_property_based_testing.md](../../../testing/python_notes/04_progressive_topics/pytest_asyncio_and_property_based_testing.md) |
| 上下文管理器进阶 (Context Managers) | `python` | `advanced` | python, context-manager, with, contextlib, resource-management | [testing/python_notes/03_advanced_syntax/context_managers.md](../../../testing/python_notes/03_advanced_syntax/context_managers.md) |
| 元编程与描述符协议 | `python` | `advanced` | python, metaprogramming, metaclass, descriptors, magic-methods | [testing/python_notes/03_advanced_syntax/metaprogramming_and_descriptors.md](../../../testing/python_notes/03_advanced_syntax/metaprogramming_and_descriptors.md) |
| 关系型数据库、MySQL 与 SQL 基础 | `python` | `advanced` | python, database, sql, mysql, sqlite | [testing/python_notes/04_progressive_topics/relational_databases_and_sql.md](../../../testing/python_notes/04_progressive_topics/relational_databases_and_sql.md) |
| 内存排障：tracemalloc、gc 与对象增长 | `python` | `advanced` | python, memory, tracemalloc, gc, profiling, leak | [testing/python_notes/04_progressive_topics/memory_profiling_tracemalloc_gc.md](../../../testing/python_notes/04_progressive_topics/memory_profiling_tracemalloc_gc.md) |
| 内存管理与 GC 调优 (Memory Management & GC) | `python` | `advanced` | python, memory, gc, reference-counting, performance | [testing/python_notes/04_progressive_topics/memory_management_and_gc.md](../../../testing/python_notes/04_progressive_topics/memory_management_and_gc.md) |
| 函数式编程与递归 (Functional & Recursion) | `python` | `advanced` | python, functional, lambda, partial, recursion, lru_cache | [testing/python_notes/03_advanced_syntax/functional_programming_and_recursion.md](../../../testing/python_notes/03_advanced_syntax/functional_programming_and_recursion.md) |
| 办公文档、PDF、图像与消息自动化 | `python` | `advanced` | python, automation, office, pdf, image, email | [testing/python_notes/04_progressive_topics/office_and_document_automation.md](../../../testing/python_notes/04_progressive_topics/office_and_document_automation.md) |
| 可观测性：日志、指标与链路追踪 | `python` | `advanced` | python, observability, logging, metrics, tracing, opentelemetry | [testing/python_notes/04_progressive_topics/observability_logging_metrics_tracing.md](../../../testing/python_notes/04_progressive_topics/observability_logging_metrics_tracing.md) |
| 平台工具方向 Capstone Projects | `python` | `advanced` | python, capstone, platform, tools, cli, automation | [testing/python_notes/04_progressive_topics/platform_tools_capstone_projects.md](../../../testing/python_notes/04_progressive_topics/platform_tools_capstone_projects.md) |
| 并发模型 (Concurrency Models) | `python` | `advanced` | python, concurrency, threading, multiprocessing, asyncio, gil | [testing/python_notes/04_progressive_topics/python_concurrency.md](../../../testing/python_notes/04_progressive_topics/python_concurrency.md) |
| 序列化与结构化数据 (JSON & CSV) | `python` | `advanced` | python, serialization, json, csv, orjson, data-exchange | [testing/python_notes/03_advanced_syntax/structured_data_formats.md](../../../testing/python_notes/03_advanced_syntax/structured_data_formats.md) |
| 异常体系 (Exception Handling) | `python` | `advanced` | python, exception, raise-from, context-manager, error-handling | [testing/python_notes/03_advanced_syntax/exceptions.md](../../../testing/python_notes/03_advanced_syntax/exceptions.md) |
| 性能剖析 | `python` | `advanced` | python, profiling, timeit, cprofile, memory | [testing/python_notes/04_progressive_topics/python_profiling.md](../../../testing/python_notes/04_progressive_topics/python_profiling.md) |
| 打包发布：setuptools、wheel、twine 与私有 PyPI | `python` | `advanced` | python, packaging, wheel, twine, pep517 | [testing/python_notes/04_progressive_topics/packaging_and_publishing.md](../../../testing/python_notes/04_progressive_topics/packaging_and_publishing.md) |
| 数据分析、NumPy / pandas 与可视化基础 | `python` | `advanced` | python, data-analysis, numpy, pandas, visualization | [testing/python_notes/04_progressive_topics/data_analysis_and_visualization.md](../../../testing/python_notes/04_progressive_topics/data_analysis_and_visualization.md) |
| 数据方向 Capstone Projects | `python` | `advanced` | python, capstone, data, pipeline, validation, projects | [testing/python_notes/04_progressive_topics/data_capstone_projects.md](../../../testing/python_notes/04_progressive_topics/data_capstone_projects.md) |
| 文件读写与路径进阶 (File I/O & Pathlib) | `python` | `advanced` | python, file-io, pathlib, stream, encoding, shutil | [testing/python_notes/03_advanced_syntax/file_io_and_pathlib.md](../../../testing/python_notes/03_advanced_syntax/file_io_and_pathlib.md) |
| 文本编码与字节流 (Encoding & Bytes) | `python` | `advanced` | python, bytes, encoding, utf8, unicode, io | [testing/python_notes/03_advanced_syntax/bytes_encoding_and_text_files.md](../../../testing/python_notes/03_advanced_syntax/bytes_encoding_and_text_files.md) |
| 断点调试与 pdb 进阶 (Debugging & PDB) | `python` | `advanced` | python, breakpoint, pdb, debugging, interactive, traceback | [testing/python_notes/03_advanced_syntax/breakpoint_and_pdb_basics.md](../../../testing/python_notes/03_advanced_syntax/breakpoint_and_pdb_basics.md) |
| 日志、CLI 与自动化脚本 (Logging & CLI Automation) | `python` | `advanced` | python, logging, cli, click, automation, subprocess | [testing/python_notes/04_progressive_topics/logging_and_cli_automation.md](../../../testing/python_notes/04_progressive_topics/logging_and_cli_automation.md) |
| 机器学习入门与模型闭环 | `python` | `advanced` | python, machine-learning, scikit-learn, evaluation, model | [testing/python_notes/04_progressive_topics/machine_learning_basics.md](../../../testing/python_notes/04_progressive_topics/machine_learning_basics.md) |
| 标准库工具箱 | `python` | `advanced` | python, stdlib, datetime, collections, itertools, deque | [testing/python_notes/04_progressive_topics/standard_library_toolbox.md](../../../testing/python_notes/04_progressive_topics/standard_library_toolbox.md) |
| 模块与包进阶 (Modules & Packages) | `python` | `advanced` | python, module, package, import, importlib, zipapp | [testing/python_notes/03_advanced_syntax/modules_and_packages.md](../../../testing/python_notes/03_advanced_syntax/modules_and_packages.md) |
| 正则表达式进阶 (Regular Expressions) | `python` | `advanced` | python, regex, re, log-parsing, performance | [testing/python_notes/04_progressive_topics/python_re.md](../../../testing/python_notes/04_progressive_topics/python_re.md) |
| 测试工程进阶：conftest、分层、flaky 与契约测试 | `python` | `advanced` | python, pytest, conftest, flaky, contract-testing | [testing/python_notes/04_progressive_topics/testing_engineering_advanced.md](../../../testing/python_notes/04_progressive_topics/testing_engineering_advanced.md) |
| 测试开发方向 Capstone Projects | `python` | `advanced` | python, capstone, testing, qa, automation, projects | [testing/python_notes/04_progressive_topics/testing_development_capstone_projects.md](../../../testing/python_notes/04_progressive_topics/testing_development_capstone_projects.md) |
| 测试金字塔、pytest fixture、参数化与 CI | `python` | `advanced` | python, pytest, testing, mock, coverage | [testing/python_notes/04_progressive_topics/testing_pyramid_and_pytest.md](../../../testing/python_notes/04_progressive_topics/testing_pyramid_and_pytest.md) |
| 现代 Python 工具链：uv、PDM、Hatch 与 Nox | `python` | `advanced` | python, uv, pdm, hatch, nox, tooling, pyproject | [testing/python_notes/04_progressive_topics/modern_python_tooling_uv_pdm_hatch_nox.md](../../../testing/python_notes/04_progressive_topics/modern_python_tooling_uv_pdm_hatch_nox.md) |
| 类型提示与静态检查 | `python` | `advanced` | python, typing, mypy, protocol, pydantic | [testing/python_notes/04_progressive_topics/type_hints_and_static_checking.md](../../../testing/python_notes/04_progressive_topics/type_hints_and_static_checking.md) |
| 结构化建模进阶 (Dataclasses & Enum) | `python` | `advanced` | python, dataclass, enum, post_init, frozen, modeling | [testing/python_notes/03_advanced_syntax/dataclasses_and_enum.md](../../../testing/python_notes/03_advanced_syntax/dataclasses_and_enum.md) |
| 网络采集、浏览器自动化与 Scrapy 思维 | `python` | `advanced` | python, scraping, selenium, scrapy, html, automation | [testing/python_notes/04_progressive_topics/data_collection_and_browser_automation.md](../../../testing/python_notes/04_progressive_topics/data_collection_and_browser_automation.md) |
| 装饰器 (Decorators) | `python` | `advanced` | python, decorator, wraps, closures, aop | [testing/python_notes/03_advanced_syntax/decorators.md](../../../testing/python_notes/03_advanced_syntax/decorators.md) |
| 调试、traceback 与 Python 排障方法 | `python` | `advanced` | python, debugging, traceback, troubleshooting, logging | [testing/python_notes/04_progressive_topics/debugging_and_troubleshooting.md](../../../testing/python_notes/04_progressive_topics/debugging_and_troubleshooting.md) |
| 进阶专题篇 综合项目与交付练习 | `python` | `advanced` | python, practice, projects, integration, delivery | [testing/python_notes/04_progressive_topics/progressive_topics_integrated_projects.md](../../../testing/python_notes/04_progressive_topics/progressive_topics_integrated_projects.md) |
| 迭代器与生成器 (Iterators & Generators) | `python` | `advanced` | python, iterator, generator, yield, coroutines | [testing/python_notes/03_advanced_syntax/iterators_and_generators.md](../../../testing/python_notes/03_advanced_syntax/iterators_and_generators.md) |
| 配置分层、环境变量与密钥管理 | `python` | `advanced` | python, config, env, secrets, deployment | [testing/python_notes/04_progressive_topics/configuration_and_secrets_management.md](../../../testing/python_notes/04_progressive_topics/configuration_and_secrets_management.md) |
| 面向 Python 工程的 Linux 与 Shell 基础 | `python` | `advanced` | python, linux, shell, subprocess, environment | [testing/python_notes/04_progressive_topics/linux_shell_for_python.md](../../../testing/python_notes/04_progressive_topics/linux_shell_for_python.md) |
| 面向对象 (Object-Oriented Programming) | `python` | `advanced` | python, oop, mro, abc, slots, property | [testing/python_notes/03_advanced_syntax/object_oriented_programming.md](../../../testing/python_notes/03_advanced_syntax/object_oriented_programming.md) |
| 项目交付、Docker 与工程协作 (Project Delivery & Docker) | `python` | `advanced` | python, delivery, docker, ci-cd, makefile, collaboration | [testing/python_notes/04_progressive_topics/project_delivery_and_engineering_practice.md](../../../testing/python_notes/04_progressive_topics/project_delivery_and_engineering_practice.md) |
| 高级语法篇 Mini Projects (Advanced Lab) | `python` | `advanced` | python, project, advanced, lab, engineering | [testing/python_notes/03_advanced_syntax/advanced_syntax_mini_projects.md](../../../testing/python_notes/03_advanced_syntax/advanced_syntax_mini_projects.md) |
| Python 多版本管理与虚拟环境 (Version Management) | `python` | `basics` | python, environment, pyenv, venv, conda, isolation | [testing/python_notes/01_environment/python_version_management.md](../../../testing/python_notes/01_environment/python_version_management.md) |
| Python 生态全景与职业路线 (Python Landscape) | `python` | `basics` | python, career, ecosystem, roadmap, testing-dev | [testing/python_notes/01_environment/python_landscape_and_career_paths.md](../../../testing/python_notes/01_environment/python_landscape_and_career_paths.md) |
| VS Code Python 开发环境一体化配置 (IDE Setup) | `python` | `basics` | python, vscode, black, flake8, mypy, isort, debug | [testing/python_notes/01_environment/ide_setup.md](../../../testing/python_notes/01_environment/ide_setup.md) |
| pip 与 Poetry 依赖管理 (Dependency Management) | `python` | `basics` | python, dependency, pip, poetry, packaging, pip-tools | [testing/python_notes/01_environment/dependency_management.md](../../../testing/python_notes/01_environment/dependency_management.md) |
| 函数进阶与作用域 (Functions & Scopes) | `python` | `basics` | python, function, scope, legb, closures, nonlocal | [testing/python_notes/02_basic_syntax/function_basics.md](../../../testing/python_notes/02_basic_syntax/function_basics.md) |
| 切片、解包与高频内置函数 (Slicing & Built-ins) | `python` | `basics` | python, slice, unpacking, built-ins, enumerate, zip, sorted | [testing/python_notes/02_basic_syntax/slicing_unpacking_and_common_builtins.md](../../../testing/python_notes/02_basic_syntax/slicing_unpacking_and_common_builtins.md) |
| 变量与数据类型 (Variables & Data Types) | `python` | `basics` | python, variables, types, objects, type-hints | [testing/python_notes/02_basic_syntax/variables_and_types.md](../../../testing/python_notes/02_basic_syntax/variables_and_types.md) |
| 变量可变性与深浅拷贝 (Mutability & Copying) | `python` | `basics` | python, mutability, copy, deepcopy, references | [testing/python_notes/02_basic_syntax/mutability_and_copying.md](../../../testing/python_notes/02_basic_syntax/mutability_and_copying.md) |
| 字符串处理与常用方法 (String Processing) | `python` | `basics` | python, string, f-string, slice, unicode, performance | [testing/python_notes/02_basic_syntax/strings_and_methods.md](../../../testing/python_notes/02_basic_syntax/strings_and_methods.md) |
| 推导式与生成器表达式 (Comprehensions & Generator Expressions) | `python` | `basics` | python, comprehension, generator, list, dict, performance | [testing/python_notes/02_basic_syntax/comprehensions_and_generator_expressions.md](../../../testing/python_notes/02_basic_syntax/comprehensions_and_generator_expressions.md) |
| 核心容器：列表、元组、集合、字典 (Collections) | `python` | `basics` | python, list, dict, set, tuple, performance | [testing/python_notes/02_basic_syntax/collections.md](../../../testing/python_notes/02_basic_syntax/collections.md) |
| 注释、输入输出与脚本入口 (I/O & Entry Point) | `python` | `basics` | python, input, output, comments, script-structure, main | [testing/python_notes/02_basic_syntax/comments_and_input_output.md](../../../testing/python_notes/02_basic_syntax/comments_and_input_output.md) |
| 流程控制深度解析 (Flow Control) | `python` | `basics` | python, flow-control, match-case, for-else, loops, performance | [testing/python_notes/02_basic_syntax/control_flow.md](../../../testing/python_notes/02_basic_syntax/control_flow.md) |
| 环境篇 Mini Projects (Environment Lab) | `python` | `basics` | python, project, environment, lab, setup | [testing/python_notes/01_environment/environment_mini_projects.md](../../../testing/python_notes/01_environment/environment_mini_projects.md) |
| 运算符与表达式深度解析 (Operators & Expressions) | `python` | `basics` | python, operators, walrus, short-circuit, bitwise, logic | [testing/python_notes/02_basic_syntax/operators_and_expressions.md](../../../testing/python_notes/02_basic_syntax/operators_and_expressions.md) |
| 基础语法篇 Mini Projects (Basics Lab) | `python` | `beginner` | python, project, basics, lab, exercise | [testing/python_notes/02_basic_syntax/basic_syntax_mini_projects.md](../../../testing/python_notes/02_basic_syntax/basic_syntax_mini_projects.md) |

#### `strategy`

| 标题 | 技术栈 | 层级 | 标签 | 路径 |
| :--- | :--- | :--- | :--- | :--- |
| 测试金字塔与回归集分层策略 | `methodologies` | `advanced` | testing-strategy, testing-pyramid, regression, layering | [testing/strategy/methodologies/testing_pyramid_and_regression_layering.md](../../../testing/strategy/methodologies/testing_pyramid_and_regression_layering.md) |
| 基于风险的测试方法基础 | `methodologies` | `basics` | testing-strategy, risk-based-testing, prioritization, quality | [testing/strategy/methodologies/risk_based_testing_basics.md](../../../testing/strategy/methodologies/risk_based_testing_basics.md) |
| 质量门禁设计与发布准入策略 | `quality-gates` | `advanced` | testing-strategy, quality-gate, release, coverage, defect | [testing/strategy/quality-gates/quality_gate_design_and_release_entry.md](../../../testing/strategy/quality-gates/quality_gate_design_and_release_entry.md) |

#### `ui`

| 标题 | 技术栈 | 层级 | 标签 | 路径 |
| :--- | :--- | :--- | :--- | :--- |
| Playwright 登录态复用与鉴权状态管理 | `playwright` | `advanced` | playwright, auth, storage-state, ui-testing, login | [testing/ui/playwright/advanced/playwright_auth_state_reuse.md](../../../testing/ui/playwright/advanced/playwright_auth_state_reuse.md) |
| Playwright 网络拦截与接口 Mock | `playwright` | `advanced` | playwright, ui-testing, network, mock, route | [testing/ui/playwright/advanced/playwright_network_mocking_and_route.md](../../../testing/ui/playwright/advanced/playwright_network_mocking_and_route.md) |
| Playwright 选择器与自动等待基础 | `playwright` | `basics` | playwright, ui-testing, locator, auto-wait | [testing/ui/playwright/basics/playwright_selector_and_waiting.md](../../../testing/ui/playwright/basics/playwright_selector_and_waiting.md) |
