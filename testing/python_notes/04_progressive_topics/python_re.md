---
title: 正则表达式与 re 模块
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, regex, re, log-parsing, pattern]
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
- 测试工程经常要处理日志、接口报文、批量文本清洗和字段抽取，正则是非常高频的工具。
- 会写简单正则不够，真正落地时更重要的是知道如何控制可读性、贪婪行为和命名分组。
- 掌握 `re` 后，你可以更稳定地做日志解析、结果校验和模糊匹配断言。

## 学什么
- 元字符：`.`、`*`、`+`、`?`、`[]`、`()`、`{m,n}`、`^`、`$` 等。
- 贪婪与非贪婪匹配的差异，以及如何通过 `?` 控制。
- 捕获分组、命名分组、前向断言与常用 API：`search`、`findall`、`sub`、`compile`。

## 怎么用
### 核心代码：日志解析

```python hl_lines="3 8 10 11"
import re

pattern = re.compile(
    r"^(?P<level>INFO|ERROR)\s+user=(?P<user>\w+)\s+cost=(?P<cost>\d+)ms$"
)

line = "ERROR user=alice cost=128ms"
match = pattern.search(line)

assert match is not None
print(match.group("level"))
print(match.groupdict())
```


### 进阶技巧：非贪婪匹配与前向断言

```python hl_lines="4 5"
import re

html = "<title>alpha</title><title>beta</title>"
titles = re.findall(r"<title>(.*?)</title>", html)
digits_before_ms = re.findall(r"\d+(?=ms)", "cost=18ms retry=2")

print(titles)
print(digits_before_ms)
```


落地建议:
- 高频模式先 `compile()`，避免重复解析。
- 对复杂正则配上命名分组和注释，降低后续维护成本。
- 遇到结构化数据（JSON、HTML、XML）时，优先考虑专门解析器，正则只作为补充工具。

## 业界案例
- 日志平台常用正则从文本行中抽出 trace_id、状态码、耗时和用户标识。
- 接口测试会用正则校验时间戳、订单号、脱敏手机号等动态字段。
- CI 流水线里经常用正则从命令行输出中提取失败摘要或覆盖率数字。

## 延伸阅读
- [Python re 文档](https://docs.python.org/3/library/re.html)
- [Regex101 交互式调试工具](https://regex101.com/)
- 优先使用原始字符串书写模式，降低转义噪音。

## Self-Check
### 概念题
1. 什么是贪婪匹配，为什么 HTML 场景里经常要改成非贪婪？
2. 命名分组相比普通分组有什么优势？
3. 前向断言适合解决什么问题？

### 编程题
1. 怎样从一行日志里提取 `level`、`user` 和 `cost` 三个字段？
2. 如何匹配多个 `<title>...</title>` 标签中的内容而不过度吞噬文本？

### 实战场景
1. 你要在 CI 输出里提取覆盖率百分比和失败用例名，为什么正则合适，但也不能滥用？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
贪婪匹配会尽可能多地吞字符，HTML 中容易一下子跨过多个标签；改成 `.*?` 这样的非贪婪写法后，通常更容易只拿到最近的匹配。
讲解回看: [学什么](#学什么)

### 概念题 2
它让提取结果带上语义名称，调用时可用 `group("name")` 或 `groupdict()`，可读性和维护性都更好。
讲解回看: [怎么用](#怎么用)

### 概念题 3
它适合“只在某个后缀条件成立时匹配当前内容，但不把后缀吃掉”的场景，例如匹配 `ms` 前面的数字。
讲解回看: [学什么](#学什么)

### 编程题 1
可以用命名分组的 `re.compile()` 模式，然后通过 `match.groupdict()` 一次拿到结构化字典。
讲解回看: [怎么用](#怎么用)

### 编程题 2
使用非贪婪模式 `r"<title>(.*?)</title>"`，而不是默认的贪婪 `.*`。
讲解回看: [怎么用](#怎么用)

### 实战场景 1
因为终端输出本质上是文本，正则提取很方便；但如果源数据已经是 JSON、XML 或 HTML，就应优先使用结构化解析器，避免脆弱模式。
讲解回看: [业界案例](#业界案例)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-16: 初版整理，补齐示例、自测题与落地建议。

---
[返回 Python 学习总览](../README.md)
