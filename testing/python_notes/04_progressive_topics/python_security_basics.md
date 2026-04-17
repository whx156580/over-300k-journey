---
title: Python 安全基础
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, security, secrets, validation, sql-injection, path-traversal]
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
- Python 很适合快速写脚本、做后台工具和接口服务，但“写得快”也意味着更容易把敏感信息、拼接命令、宽松反序列化之类的问题一并带进生产环境。
- 很多安全问题不是高深漏洞，而是日常工程细节失守，比如把密钥打进日志、直接拼 SQL、把用户输入当路径、把不可信数据喂给解释器。
- 对 Python 从业者来说，安全基础不是单独的安全岗位知识，而是写脚本、做接口、跑任务时都应该默认带上的判断框架。

## 学什么
- 先建立最常见的风险地图：敏感信息泄露、注入问题、路径穿越、不安全反序列化、依赖风险、权限边界和审计缺口。
- 再把每类问题拆成“危险信号、常见触发点、最低限度的防守动作”，不要只停在“知道有这个名词”。
- 最后形成一个实用习惯：默认不信任外部输入，默认对敏感数据做脱敏，默认给数据库和文件系统操作加边界。

## 怎么用
### 示例 1：密钥读取后只保留必要暴露面

```python hl_lines="1 5 8"
import os


os.environ["API_TOKEN"] = "sk-demo-token"
token = os.environ["API_TOKEN"]
masked = token[:2] + "***" + token[-2:]

print(bool(token), masked)
```


### 示例 2：数据库查询优先使用参数化，而不是字符串拼接

```python hl_lines="5 8 11"
import sqlite3


conn = sqlite3.connect(":memory:")
conn.execute("create table users(name text)")
conn.execute("insert into users(name) values (?)", ("alice",))

unsafe_input = "alice' OR 1=1 --"
count = conn.execute(
    "select count(*) from users where name = ?",
    (unsafe_input,),
).fetchone()[0]

print(count)
conn.close()
```


### 示例 3：文件路径在访问前先收口到允许目录

```python hl_lines="4 7 9"
from pathlib import Path


base_dir = Path("workspace").resolve()
candidate = (base_dir / "reports" / "daily.txt").resolve()

is_safe = candidate.is_relative_to(base_dir)

print(is_safe, candidate.parts[-2:])
```


安全排查清单:
- 外部输入是否直接进入了 `eval()`、模板渲染、SQL、shell 命令或文件路径？
- 敏感信息是否出现在日志、异常信息、截图、测试样例或配置仓库里？
- 依赖是否有版本锁定、升级节奏和漏洞扫描入口？
- 后台任务、脚本执行账号和数据库账号是否拿了“够用就好”的权限，而不是默认给满？
- 反序列化、YAML / pickle / 自定义对象加载是否明确区分了可信与不可信来源？

## 业界案例
- 内部脚本为了图快，把数据库 where 条件直接用 f-string 拼起来，功能能跑，但一旦输入来自工单系统或网页参数，就把注入风险带进了生产。
- 导出报表脚本把用户传入的文件名直接和目标目录拼接，结果 `../` 类路径绕过导致覆盖了不该动的文件。
- 排障时为了方便，把完整请求体和所有请求头打进日志，最终把 token、cookie 和手机号都留在了日志平台里。

## 延伸阅读
- 安全学习最怕“只记概念，不记落地动作”。建议你每学一个工程主题，就顺手问自己三件事：输入是否可信、数据是否敏感、边界是否可控。
- 如果你已经在做 Web 服务，可以把这篇和 `configuration_and_secrets_management.md`、`sqlalchemy_and_alembic.md`、`observability_logging_metrics_tracing.md` 连起来看。
- 如果你主要写脚本和自动化，也别觉得安全离自己远。脚本往往权限更大、审计更少，一旦出问题反而更难排查。

## Self-Check
1. 为什么“只会写功能，不会给输入加边界”会在 Python 项目里特别危险？
2. 为什么参数化查询比字符串拼接更安全？它解决的是哪类风险？
3. 处理上传路径、导出路径或用户给出的文件名时，最低限度应该做什么检查？

## 参考答案
1. 因为 Python 很适合快速接外部输入，脚本、接口、任务和工具都可能直接消费用户数据；如果默认信任输入，就容易引入注入、路径穿越和反序列化风险。
2. 参数化查询会把“SQL 结构”和“用户值”分开处理，避免输入被解释成 SQL 语法的一部分，主要防的是 SQL 注入。
3. 至少要把目标路径收口到允许目录、规范化后再检查边界，并避免直接信任用户传来的相对路径或文件名。

## 参考链接
- [Python `sqlite3` 文档](https://docs.python.org/3/library/sqlite3.html)
- [Python `pathlib` 文档](https://docs.python.org/3/library/pathlib.html)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)

## 版本记录
- 2026-04-17：首版，补齐 Python 从业者常见安全风险与最低防守动作。
