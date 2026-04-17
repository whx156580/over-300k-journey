---
title: 关系型数据库、MySQL 与 SQL 基础
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, database, sql, mysql, sqlite]
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
- 数据库是后端系统、报表系统、自动化平台和数据分析链路的共同底座，测试开发也离不开它。
- 真正有用的数据库能力，不是会背几条 SQL，而是能把数据模型、查询语义、索引和事务放在一起理解。
- 一旦数据库和 SQL 基础稳了，排查脏数据、验证接口副作用、分析慢查询都会轻松很多。

## 学什么
- 先建立表、行、列、主键、外键、约束、索引和事务这些核心心智模型，再去记 DDL / DML / DQL / DCL 语句。
- MySQL 是常见生产数据库，`sqlite3` 则是练习 SQL 语义的低成本入口。先在 sqlite 跑通，再迁移到 MySQL 语境，学习效率更高。
- SQL 不只是“把数据查出来”，还包含建模、聚合、过滤、排序、连接、权限和执行计划这些工程问题。

## 怎么用
### 示例 1：建表、插数与关联查询

```python hl_lines="1 10 17"
import sqlite3

with sqlite3.connect(":memory:") as connection:
    connection.executescript(
        """
        create table team(id integer primary key, name text);
        create table report(team_id integer, passed integer);
        insert into team values (1, 'qa'), (2, 'backend');
        insert into report values (1, 12), (1, 10), (2, 8);
        """
    )
    rows = connection.execute(
        """
        select team.name, sum(report.passed) as total
        from team
        join report on team.id = report.team_id
        group by team.name
        order by team.name
        """
    ).fetchall()

print(rows)
```


### 示例 2：用事务保证原子性

```python hl_lines="1 6 9"
import sqlite3

with sqlite3.connect(":memory:") as connection:
    connection.execute("create table task(name text unique)")
    try:
        with connection:
            connection.execute("insert into task values (?)", ("smoke",))
            connection.execute("insert into task values (?)", ("smoke",))
    except sqlite3.IntegrityError:
        pass
    count = connection.execute("select count(*) from task").fetchone()[0]

print(count)
```


### 示例 3：查看查询计划

```python hl_lines="1 6 9"
import sqlite3

with sqlite3.connect(":memory:") as connection:
    connection.execute("create table event(level text, created_at text)")
    connection.execute("create index idx_event_level on event(level)")
    plan = connection.execute(
        "explain query plan select * from event where level = ?",
        ("ERROR",),
    ).fetchall()

print(plan[0][3])
```


落地建议:
- 先画数据关系，再写 SQL；先写最小样本，再上真实数据量。
- 涉及多步写入时，把事务边界想清楚，不要默认数据库会替你兜底。
- 学索引时不要只记“建索引会更快”，要结合过滤条件、排序和执行计划一起看。

## 业界案例
- 接口测试校验落库结果时，经常要自己写 SQL 验证幂等性、状态流转和聚合结果。
- 中后台报表系统通常离不开多表关联、分组统计和索引优化。
- 线上慢查询排查时，问题往往不在 SQL 语法对不对，而在查询条件、索引设计和返回数据量。

## 延伸阅读
- 先把 `SELECT ... FROM ... WHERE ... GROUP BY ... ORDER BY ...` 这条主线练熟，再扩展到视图、存储过程和权限控制。
- MySQL 与 sqlite 在函数、类型系统和优化器上有差异，迁移时要回到官方文档确认。
- SQL 学习最有效的方法永远是“小数据集 + 明确输出预期 + 自己解释执行过程”。

## Self-Check
### 概念题
1. 为什么数据库学习一定要把数据模型和 SQL 放在一起看？
2. 事务要解决的核心问题是什么？
3. 索引为什么不能简单理解为“越多越好”？

### 编程题
1. 怎样快速验证一条 SQL 的聚合结果是否符合预期？
2. 如何在练习阶段低成本观察一条查询的执行计划？

### 实战场景
1. 某条接口调用后数据库里写了三张表，但其中一张写失败了。你会从哪些事务和数据一致性问题入手排查？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
因为 SQL 只是操作数据模型的语言。你如果不知道表之间的关系和约束，就很难写出可靠的查询和更新语句。
讲解回看: [为什么学](#为什么学)

### 概念题 2
事务要保证一组操作要么全部成功、要么全部失败，从而避免只写了一半的数据状态。
讲解回看: [怎么用](#怎么用)

### 概念题 3
因为索引会增加写入成本和存储占用，建错位置还可能让优化器选出并不理想的计划。
讲解回看: [落地建议](#怎么用)

### 编程题 1
准备一小批可手算的样本数据，执行 SQL 后把结果和你自己算出来的预期值逐项对比。
讲解回看: [怎么用](#怎么用)

### 编程题 2
用 sqlite 的 `EXPLAIN QUERY PLAN` 或 MySQL 的 `EXPLAIN`，先看查询是否走到了你预期的索引与扫描方式。
讲解回看: [怎么用](#怎么用)

### 实战场景 1
先确认是否显式开启事务，再检查失败语句是否触发回滚，以及三张表之间是否存在必须同步提交的业务约束。
讲解回看: [业界案例](#业界案例)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [sqlite3 文档](https://docs.python.org/3/library/sqlite3.html)
- [MySQL 文档](https://dev.mysql.com/doc/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-17: 将 README1 中的数据库、SQL、索引与 MySQL 入门主题折叠进主路径专题。

---
[返回 Python 学习总览](../README.md)
