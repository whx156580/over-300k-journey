---
title: 基础语法篇 Mini Projects (Basics Lab)
module: testing
area: python_notes
stack: python
level: beginner
status: active
tags: [python, project, basics, lab, exercise]
updated: 2026-04-17
---

## 目录
- [背景](#背景)
- [核心结论](#核心结论)
- [项目 1: Expense Tracker (数据汇总器)](#项目-1-expense-tracker-数据汇总器)
- [项目 2: Filename Normalizer (文本处理器)](#项目-2-filename-normalizer-文本处理器)
- [项目 3: Quiz Scorer (逻辑封装器)](#项目-3-quiz-scorer-逻辑封装器)
- [官方文档与兼容性](#官方文档与兼容性)
- [代码示例](#代码示例)
- [验收标准](#验收标准)
- [易错点与最佳实践](#易错点与最佳实践)
- [Self-Check](#Self-Check)
- [参考链接](#参考链接)
- [版本记录](#版本记录)

## 背景
- **问题场景**: 初学者往往“看书都懂，上手就懵”，无法将零散的变量、循环、判断组合成解决实际问题的工具；或者编写的脚本逻辑混乱，难以维护和测试。
- **学习目标**: 掌握基础语法的综合应用，学会“分解问题 -> 设计结构 -> 编写实现 -> 自动化验证”的开发全流程。
- **前置知识**: [02 基础语法](./) 全系列笔记。

## 核心结论
- **数据结构即模型**: 选择合适的容器（如字典列表）是编写简洁代码的前提。
- **预览机制**: 涉及修改文件或大量数据的脚本，必须先实现“预览 (Preview)”模式。
- **函数收口**: 重复出现的处理逻辑应封装为函数，保持脚本主流程清晰。

## 项目 1: Expense Tracker (数据汇总器)
实现一个消费记录分析工具：
1.  **输入**: 包含日期、分类、金额的字典列表。
2.  **处理**: 计算总支出、平均支出，并按分类进行统计。
3.  **输出**: 格式化的控制台报表。

## 项目 2: Filename Normalizer (文本处理器)
编写一个文件名批量规范化工具：
1.  **输入**: 原始文件名列表（含空格、大写、特殊字符）。
2.  **规则**: 转换为全小写、空格转下划线、移除多余点号。
3.  **输出**: 展示“原始名 -> 目标名”的对比预览。

## 项目 3: Quiz Scorer (逻辑封装器)
构建一个自动化的选择题评分系统：
1.  **数据**: 标准答案字典与学生提交答案字典。
2.  **校验**: 计算得分、记录错题 ID。
3.  **等级**: 根据得分率自动判定 A/B/C 等级。

## 官方文档与兼容性
| 规则名称 | 官方出处 | 链接 | 兼容性 |
| :--- | :--- | :--- | :--- |
| `statistics` | [Mathematical statistics functions](https://docs.python.org/3/library/statistics.html) | N/A | Python 3.4+ |
| `dict.items()` | [Dictionary methods](https://docs.python.org/3/library/stdtypes.html#dict.items) | N/A | Python 1.0+ |

## 代码示例

### 示例 1：Expense Tracker 核心逻辑
演示如何利用字典和 `sum` 进行数据聚合。

```python
def analyze_expenses(records: list):
    """
    聚合消费数据。
    """
    total = sum(r["amount"] for r in records)
    categories = {}
    for r in records:
        cat = r["category"]
        categories[cat] = categories.get(cat, 0) + r["amount"]
        
    return {
        "total": total,
        "avg": total / len(records) if records else 0,
        "by_category": categories
    }

# 验证
test_data = [{"category": "food", "amount": 10}, {"category": "food", "amount": 20}]
res = analyze_expenses(test_data)
assert res["total"] == 30 and res["by_category"]["food"] == 30
```

### 示例 2：Filename Normalizer 核心实现
演示字符串清洗与列表推导式的结合。

```python
def get_rename_preview(filenames: list) -> list:
    """
    生成重命名预览。
    """
    return [
        (old, old.strip().lower().replace(" ", "_"))
        for old in filenames
    ]

# 验证
files = [" REPORT 01.txt ", "notes.md"]
preview = get_rename_preview(files)
assert preview[0][1] == "report_01.txt"
```

## 验收标准
- [ ] 所有脚本均使用 `if __name__ == "__main__":` 保护。
- [ ] 逻辑函数与输入输出边界层（print/input）明确分离。
- [ ] 至少针对“空列表”和“异常类型”进行了边界处理。

## 易错点与最佳实践
| 特性 | 常见陷阱 | 最佳实践 |
| :--- | :--- | :--- |
| **浮点精度** | 直接打印 `0.1 + 0.2` 导致报表显示长尾数字。 | 使用 `round(val, 2)` 或 f-string 精度控制。 |
| **字典覆盖** | 在汇总统计时直接赋值 `d[k] = v` 而不检查键是否存在。 | 使用 `d.get(k, 0)` 或 `defaultdict`。 |
| **死循环** | 在 `while` 模拟交互时缺少退出指令。 | 显式检查 `"exit"` 或 `"q"`。 |

## Self-Check
1. 如何将 `analyze_expenses` 的输出结果按金额从高到低排序？
2. 在项目 2 中，如果两个原始文件名不同但规范化后重名了，应该如何处理冲突？
3. 为什么在项目 3 中建议将“标准答案”设为常量（全大写命名）？

## 参考链接
- [Python Standard Library by Example](https://example.com)
- [Clean Code in Python: Chapter 2 - Pythonic Code](https://example.com)

---
[版本记录](./basic_syntax_mini_projects.md) | [返回首页](../README.md)
