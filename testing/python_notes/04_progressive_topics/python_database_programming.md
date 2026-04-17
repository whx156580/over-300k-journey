---
title: Python 数据库编程与 ETL 实战 (Database & ETL)
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, database, sqlite, etl, transactions, sql-injection]
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
- **问题场景**: 自动化测试需要验证接口操作是否真实写入数据库；或者需要从生产环境导出一批脱敏数据用于压测；或者需要构建每日测试结果报表流水线（ETL）。
- **学习目标**: 掌握 DB-API 2.0 规范，理解事务控制与连接管理，学会使用参数化查询防御 SQL 注入，并能处理海量数据的批量写入。
- **前置知识**: [异常处理](../03_advanced_syntax/exceptions.md)、[上下文管理器](../03_advanced_syntax/context_managers.md)。

## 核心结论
- **参数化查询**: 严禁使用字符串拼接构建 SQL，必须通过 `execute(sql, params)` 占位符防止 SQL 注入。
- **事务一致性**: 涉及写操作必须显式执行 `commit()` 或在上下文管理器中自动提交，报错时执行 `rollback()`。
- **批量提效**: 使用 `executemany()` 替代循环 `execute()`，可将写入性能提升 10 倍以上。

## 原理拆解
- **DB-API 2.0**: Python 官方定义的通用数据库接口规范（PEP 249），无论底层是 MySQL、PostgreSQL 还是 SQLite，API 调用逻辑高度一致。
- **游标 (Cursor)**: 用于执行命令并管理结果集的临时句柄，支持流式读取（fetchone/fetchmany）避免内存爆满。

## 官方文档与兼容性
| 规则名称 | 官方出处 | PEP 链接 | 兼容性 |
| :--- | :--- | :--- | :--- |
| DB-API 2.0 | [Database API Specification](https://peps.python.org/pep-0249/) | [PEP 249](https://peps.python.org/pep-0249/) | Python 1.0+ |
| `sqlite3` 模块 | [sqlite3 — DB-API 2.0 interface](https://docs.python.org/3/library/sqlite3.html) | N/A | Python 2.5+ |

## 代码示例

### 示例 1：防御 SQL 注入的参数化查询
演示正确使用占位符与处理字典化结果。

```python
import sqlite3

def get_user_data(user_id: int):
    # 使用 :memory: 建立内存数据库进行演示
    with sqlite3.connect(":memory:") as conn:
        conn.row_factory = sqlite3.Row # 使结果支持字段名访问
        cursor = conn.cursor()
        
        # 初始化表
        cursor.execute("CREATE TABLE users (id INT, name TEXT)")
        # 批量插入测试数据
        cursor.execute("INSERT INTO users VALUES (?, ?)", (1, "QA_Admin"))
        
        # 安全查询：使用 ? 占位符
        query = "SELECT * FROM users WHERE id = ?"
        cursor.execute(query, (user_id,))
        
        row = cursor.fetchone()
        return dict(row) if row else None

print(f"User 1: {get_user_data(1)}")
assert get_user_data(1)["name"] == "QA_Admin"
```

### 示例 2：高性能批量写入 (ETL 核心)
对比单条插入与 `executemany` 的性能。

```python
import sqlite3

def batch_insert_logs(logs: list):
    with sqlite3.connect(":memory:") as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE logs (level TEXT, msg TEXT)")
        
        # 高效批量插入
        cursor.executemany("INSERT INTO logs VALUES (?, ?)", logs)
        conn.commit()
        
        cursor.execute("SELECT count(*) FROM logs")
        return cursor.fetchone()[0]

test_logs = [("INFO", f"Task {i}") for i in range(100)]
count = batch_insert_logs(test_logs)
print(f"Inserted {count} rows.")
assert count == 100
```

### 示例 3：事务原子性与异常回滚
演示在报错时如何保护数据一致性。

```python
import sqlite3

def transfer_points(from_id, to_id, amount):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE account (id INT, balance INT)")
    cursor.execute("INSERT INTO account VALUES (1, 100), (2, 100)")
    
    try:
        # 扣钱
        cursor.execute("UPDATE account SET balance = balance - ? WHERE id = ?", (amount, from_id))
        # 模拟中间报错
        raise RuntimeError("Network Error during transfer")
        # 加钱
        cursor.execute("UPDATE account SET balance = balance + ? WHERE id = ?", (amount, to_id))
        conn.commit()
    except Exception as e:
        print(f"Transaction failed, rolling back: {e}")
        conn.rollback() # 撤销所有操作
    finally:
        cursor.execute("SELECT sum(balance) FROM account")
        total = cursor.fetchone()[0]
        conn.close()
        return total

# 总金额应仍为 200，证明回滚成功
assert transfer_points(1, 2, 50) == 200
```

## 性能基准测试
对比单条 `execute` 与 `executemany` 在插入 1000 条数据时的耗时。

```python
import timeit
import sqlite3

def setup_db():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE test (v INT)")
    return conn

def slow_insert(conn, data):
    for x in data:
        conn.execute("INSERT INTO test VALUES (?)", (x,))

def fast_insert(conn, data):
    conn.executemany("INSERT INTO test VALUES (?)", [(x,) for x in data])

data = list(range(1000))
conn = setup_db()

t1 = timeit.timeit(lambda: slow_insert(conn, data), number=10)
t2 = timeit.timeit(lambda: fast_insert(conn, data), number=10)

print(f"Loop Execute: {t1/10:.4f}s")
print(f"Executemany: {t2/10:.4f}s")
print(f"Speedup: {t1/t2:.1f}x")
```

## 易错点与最佳实践
| 特性 | 常见陷阱 | 最佳实践 |
| :--- | :--- | :--- |
| **SQL 注入** | `execute(f"SELECT * FROM u WHERE id={uid}")`。 | 始终使用 `execute(sql, (uid,))`。 |
| **连接泄漏** | 打开连接后未显式 `close()`。 | 使用 `with` 语句或 `contextlib` 自动化管理。 |
| **大结果集** | `fetchall()` 直接加载百万行数据到内存。 | 使用 `cursor` 迭代器或 `fetchmany(size)` 分批读取。 |

## Self-Check
1. 为什么在 `sqlite3` 中，即便使用了 `with` 语句，有时仍需显式调用 `conn.commit()`？
2. 什么是“雪花 ID”或“分布式自增 ID”？在 ETL 场景下如何保证主键不冲突？
3. `cursor.rowcount` 返回的是查询到的行数还是受影响的行数？

## 参考链接
- [Python Database Topic Guide](https://docs.python.org/3/library/database.html)
- [SQLite Tutorial for Testers](https://example.com)

---
[版本记录](./python_database_programming.md) | [返回首页](../README.md)
