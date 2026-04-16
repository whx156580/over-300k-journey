---
title: Python 关键字全集
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, keywords, syntax, parser, highlight]
updated: 2026-04-16
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
- 关键字是语言语法的地基。很多看似“记不住”的语法，其实都围绕关键字的语义边界展开。
- 测试工程里做代码生成、AST 分析、关键字高亮或样例审查时，理解关键字集合很有帮助。
- 随着 Python 版本演进，关键字也会变化，例如 `match`、`case` 就是较新的语法关键字。

## 学什么
- Python 3.12 常见关键字包括 `False`、`None`、`True`、`and`、`as`、`assert`、`async`、`await`、`break`、`class`、`continue`、`def`、`del`、`elif`、`else`、`except`、`finally`、`for`、`from`、`global`、`if`、`import`、`in`、`is`、`lambda`、`nonlocal`、`not`、`or`、`pass`、`raise`、`return`、`try`、`while`、`with`、`yield`。
- 版本差异重点关注 `async` / `await`、`match` / `case` 等在新语法里引入的保留字或软关键字。
- 关键字高亮通常来自词法分析器，它会把这些保留字映射到特定 token 类型，再交给编辑器着色。

## 怎么用
### 用标准库查看关键字列表

```python hl_lines="3 5"
import keyword

words = keyword.kwlist
print(len(words))
print(words[:10])
print("async" in words, "await" in words)
```


### 判断一个标识符是否与关键字冲突

```python hl_lines="4"
import keyword

candidates = ["status", "class", "case", "yield_value"]
conflicts = [name for name in candidates if keyword.iskeyword(name)]

print(conflicts)
```


学习建议:
- 不必死记硬背全部列表，但要知道哪些关键字承载控制流、定义、导入、异常和异步语义。
- 对版本敏感语法要结合当前解释器版本学习，不要混用旧语法与新语法。
- 关键字不能直接作为变量名；如果业务字段撞名，可通过后缀 `_` 规避，如 `class_`。

## 业界案例
- 代码生成器在输出 Python 变量名时，需要先检查是否撞上关键字。
- 语法高亮器和 LSP 服务器会基于关键字与上下文做 token 分类。
- 版本升级时，团队脚本可能因为新关键字保留而出现命名冲突，需要批量修复。

## 延伸阅读
- [keyword 模块文档](https://docs.python.org/3/library/keyword.html)
- [Python 词法分析文档](https://docs.python.org/3/reference/lexical_analysis.html)
- 关注 `match` / `case` 这类新语法的版本边界。

## Self-Check
### 概念题
1. 关键字和普通标识符的根本区别是什么？
2. 为什么说某些关键字会受版本影响？
3. 编辑器里的关键字高亮大致是如何工作的？

### 编程题
1. 如何检查一个名字是否是 Python 关键字？
2. 如果业务字段恰好叫 `class`，变量名该如何处理？

### 实战场景
1. 团队有一套模板脚本会根据 JSON 字段名自动生成 Python 模型，为什么要先做关键字检查？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
关键字是解释器保留给语法结构的词，不能随意作为变量、函数或类名使用；普通标识符则由开发者自由定义。
讲解回看: [学什么](#学什么)

### 概念题 2
因为随着语法演进，解释器可能把原本普通的词升级为关键字或软关键字。升级 Python 版本前，需要注意兼容性变化。
讲解回看: [为什么学](#为什么学)

### 概念题 3
词法分析器会扫描源码，把关键字标成特定 token 类型；编辑器再根据主题把这些 token 渲染成不同颜色。
讲解回看: [学什么](#学什么)

### 编程题 1
使用标准库 `keyword.iskeyword(name)`。如果返回 `True`，就应该避免直接拿它做标识符。
讲解回看: [怎么用](#怎么用)

### 编程题 2
常见做法是加下划线后缀，例如 `class_`，既避开关键字冲突，又保留业务含义。
讲解回看: [怎么用](#怎么用)

### 实战场景 1
因为字段名可能正好是 `class`、`from`、`global` 等关键字，不做检查就会生成无法运行的代码。生成器应在输出前自动规避这些名字。
讲解回看: [业界案例](#业界案例)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-16: 初版整理，补齐示例、自测题与落地建议。

---
[返回 Python 学习总览](../README.md)
