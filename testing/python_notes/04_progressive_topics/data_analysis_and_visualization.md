---
title: 数据分析、NumPy / pandas 与可视化基础
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, data-analysis, numpy, pandas, visualization]
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
- 数据分析主题让 Python 从“能写脚本”走到“能解释数据、看趋势、做决策支持”。
- 对测试工程来说，回归结果、性能指标、缺陷统计和业务日志，最终都要落回数据清洗、聚合和可视化。
- 这部分的关键从来不是记住多少 API，而是看懂数据结构、变换路径和结果校验。

## 学什么
- 先把数组、表格、索引、缺失值、分组聚合、合并关联和可视化表达这些基本心智模型立住。
- NumPy 更偏数值数组和向量化思维，pandas 更偏带标签的表格处理，图表库则负责把结果转成可读输出。
- 分析流程通常是“取数 -> 清洗 -> 变换 -> 聚合 -> 可视化 -> 解释结果”，每一步都需要回验。

## 怎么用
### 示例 1：先用纯 Python 跑通聚合思路

```python hl_lines="2 5 8"
rows = [
    {"team": "qa", "passed": 12},
    {"team": "qa", "passed": 10},
    {"team": "dev", "passed": 9},
]
summary = {}
for row in rows:
    summary.setdefault(row["team"], 0)
    summary[row["team"]] += row["passed"]

print(summary)
```


### 示例 2：可选地用 pandas 表达同样的表格变换

```python hl_lines="1 4 8"
try:
    import pandas as pd
except ImportError:
    print("install pandas before running the full data-analysis workflow")
else:
    frame = pd.DataFrame(
        [{"team": "qa", "passed": 12}, {"team": "qa", "passed": 10}, {"team": "dev", "passed": 9}]
    )
    grouped = frame.groupby("team", as_index=False)["passed"].sum()
    print(grouped.to_dict(orient="records"))
```


### 示例 3：用最小文本图表达可视化思维

```python hl_lines="3 6"
summary = {"qa": 22, "dev": 9}
lines = []
for team, value in sorted(summary.items()):
    lines.append(f"{team}: {'#' * value}")

print("\n".join(lines))
```


落地建议:
- 每一步变换后都先看样本头部、列名、行数和关键统计量，不要把数据处理做成黑箱。
- 画图前先确认缺失值、异常值和分组逻辑，否则图再漂亮也可能是错的。
- 学 NumPy / pandas 最稳的方式，是先用纯 Python 手算一遍，再对照库的结果验证自己理解。

## 业界案例
- 测试日报会先聚合通过率、失败原因和执行时长，再画趋势图发给团队。
- 线上质量分析常从日志 / 数据库取数，清洗出关键字段后再分组比较不同版本差异。
- 数据分析工作里最常见的问题不是“不会画图”，而是分组口径、时间窗口和异常样本没定义清楚。

## 延伸阅读
- 先把 `groupby`、`merge`、筛选和排序吃透，再去补更复杂的窗口函数、透视表和高级可视化。
- 分析结果一定要能回溯到原始样本，否则图表越多越难知道错在哪。
- 数组、表格和图表只是表达层，真正重要的是你能不能解释业务含义和风险边界。

## Self-Check
### 概念题
1. NumPy、pandas 和可视化工具分别在分析链路里承担什么角色？
2. 为什么说数据分析里最危险的不是 API 不会用，而是数据口径不一致？
3. 缺失值、异常值和重复值为什么必须在画图前处理？

### 编程题
1. 写一个最小聚合脚本，统计不同团队的通过数总和。
2. 写一个最小文本图，把聚合结果展示出来。

### 实战场景
1. 你要分析最近一周自动化执行结果的失败趋势，应该如何拆分“取数、清洗、聚合、图表、解释”这几步？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
NumPy 偏数组与数值计算，pandas 偏表格与标签化数据处理，可视化工具负责把聚合后的结果变成可读表达。
讲解回看: [学什么](#学什么)

### 概念题 2
因为数据口径一旦错了，后面的聚合、图表和结论都会一起偏掉，甚至比代码报错更难发现。
讲解回看: [为什么学](#为什么学)

### 概念题 3
因为这些脏数据会直接改变聚合结果和图形外观，让结论看起来合理但其实不可信。
讲解回看: [落地建议](#怎么用)

### 编程题 1
先用字典按组累计，确保你能口述每一步逻辑；之后再迁移到 pandas 的 `groupby()`。
讲解回看: [怎么用](#怎么用)

### 编程题 2
文本图的核心是把数值映射到统一符号长度，这能帮你先确认图表表达是否和数据一致。
讲解回看: [怎么用](#怎么用)

### 实战场景 1
先定义时间窗口和失败口径，再取数清洗，之后做分组聚合和图表展示，最后回到原始样本解释异常峰值。
讲解回看: [业界案例](#业界案例)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [NumPy 文档](https://numpy.org/doc/)
- [pandas 文档](https://pandas.pydata.org/docs/)
- [Matplotlib 文档](https://matplotlib.org/stable/users/index.html)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-17: 将 README1 中的数据分析、NumPy、pandas 与可视化主题折叠进主线路径专题。

---
[返回 Python 学习总览](../README.md)
