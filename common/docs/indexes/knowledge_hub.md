# 知识库汇总首页

> 本页由 `python scripts/build_knowledge_index.py` 自动生成，用于汇总带标准元数据的知识笔记。

---

## 总览

- 已收录笔记数: **49**
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
- 笔记数: **40**

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
| Python 关键字全集 | `python` | `advanced` | python, keywords, syntax, parser, highlight | [testing/python_notes/04_progressive_topics/python_keywords.md](../../../testing/python_notes/04_progressive_topics/python_keywords.md) |
| 上下文管理器 | `python` | `advanced` | python, context-manager, with, contextlib, resource | [testing/python_notes/03_advanced_syntax/context_managers.md](../../../testing/python_notes/03_advanced_syntax/context_managers.md) |
| 并发模型：线程、进程、协程与 GIL | `python` | `advanced` | python, concurrency, threading, asyncio, multiprocessing | [testing/python_notes/04_progressive_topics/python_concurrency.md](../../../testing/python_notes/04_progressive_topics/python_concurrency.md) |
| 异常体系 | `python` | `advanced` | python, exception, raise-from, logging, error-handling | [testing/python_notes/03_advanced_syntax/exceptions.md](../../../testing/python_notes/03_advanced_syntax/exceptions.md) |
| 性能剖析 | `python` | `advanced` | python, profiling, timeit, cprofile, memory | [testing/python_notes/04_progressive_topics/python_profiling.md](../../../testing/python_notes/04_progressive_topics/python_profiling.md) |
| 打包发布：setuptools、wheel、twine 与私有 PyPI | `python` | `advanced` | python, packaging, wheel, twine, pep517 | [testing/python_notes/04_progressive_topics/packaging_and_publishing.md](../../../testing/python_notes/04_progressive_topics/packaging_and_publishing.md) |
| 模块与包 | `python` | `advanced` | python, module, package, import, zipapp | [testing/python_notes/03_advanced_syntax/modules_and_packages.md](../../../testing/python_notes/03_advanced_syntax/modules_and_packages.md) |
| 正则表达式与 re 模块 | `python` | `advanced` | python, regex, re, log-parsing, pattern | [testing/python_notes/04_progressive_topics/python_re.md](../../../testing/python_notes/04_progressive_topics/python_re.md) |
| 测试金字塔、pytest fixture、参数化与 CI | `python` | `advanced` | python, pytest, testing, mock, coverage | [testing/python_notes/04_progressive_topics/testing_pyramid_and_pytest.md](../../../testing/python_notes/04_progressive_topics/testing_pyramid_and_pytest.md) |
| 类型提示与静态检查 | `python` | `advanced` | python, typing, mypy, protocol, pydantic | [testing/python_notes/04_progressive_topics/type_hints_and_static_checking.md](../../../testing/python_notes/04_progressive_topics/type_hints_and_static_checking.md) |
| 装饰器 | `python` | `advanced` | python, decorator, wraps, class-decorator, aop | [testing/python_notes/03_advanced_syntax/decorators.md](../../../testing/python_notes/03_advanced_syntax/decorators.md) |
| 迭代器、生成器与 yield/send/throw/close | `python` | `advanced` | python, iterator, generator, yield, coroutine | [testing/python_notes/03_advanced_syntax/iterators_and_generators.md](../../../testing/python_notes/03_advanced_syntax/iterators_and_generators.md) |
| 面向对象 | `python` | `advanced` | python, oop, property, slots, mro | [testing/python_notes/03_advanced_syntax/object_oriented_programming.md](../../../testing/python_notes/03_advanced_syntax/object_oriented_programming.md) |
| Python 多版本管理：pyenv、venv、conda | `python` | `basics` | python, environment, pyenv, venv, conda | [testing/python_notes/01_environment/python_version_management.md](../../../testing/python_notes/01_environment/python_version_management.md) |
| VS Code + Pylance + Black + isort + flake8 一体化配置 | `python` | `basics` | python, vscode, pylance, black, flake8 | [testing/python_notes/01_environment/ide_setup.md](../../../testing/python_notes/01_environment/ide_setup.md) |
| pip 与 Poetry 依赖管理 | `python` | `basics` | python, dependency, pip, poetry, packaging | [testing/python_notes/01_environment/dependency_management.md](../../../testing/python_notes/01_environment/dependency_management.md) |
| 函数基础 | `python` | `basics` | python, function, scope, legb, kwargs | [testing/python_notes/02_basic_syntax/function_basics.md](../../../testing/python_notes/02_basic_syntax/function_basics.md) |
| 列表、元组、集合、字典 | `python` | `basics` | python, list, tuple, set, dict | [testing/python_notes/02_basic_syntax/collections.md](../../../testing/python_notes/02_basic_syntax/collections.md) |
| 变量与数据类型 | `python` | `basics` | python, variables, types, identity, annotations | [testing/python_notes/02_basic_syntax/variables_and_types.md](../../../testing/python_notes/02_basic_syntax/variables_and_types.md) |
| 字符串与常用方法 | `python` | `basics` | python, string, f-string, slice, raw-string | [testing/python_notes/02_basic_syntax/strings_and_methods.md](../../../testing/python_notes/02_basic_syntax/strings_and_methods.md) |
| 流程控制 | `python` | `basics` | python, flow-control, if, while, for | [testing/python_notes/02_basic_syntax/control_flow.md](../../../testing/python_notes/02_basic_syntax/control_flow.md) |
| 运算符与表达式 | `python` | `basics` | python, operators, expressions, comparison, bitwise | [testing/python_notes/02_basic_syntax/operators_and_expressions.md](../../../testing/python_notes/02_basic_syntax/operators_and_expressions.md) |

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
