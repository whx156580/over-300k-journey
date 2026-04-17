---
title: 网络采集、浏览器自动化与 Scrapy 思维
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, scraping, selenium, scrapy, html, automation]
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
- 网络采集把 HTTP、HTML 解析、等待策略、任务调度和数据清洗真正连成了一条流水线。
- 即使你不做传统爬虫，这类能力在页面诊断、接口联调、数据补录和自动化测试里也非常常见。
- 采集主题最大的价值，不是“拿到页面源码”，而是知道失败点究竟在请求、解析、浏览器还是数据清洗。

## 学什么
- 先分清静态采集、接口采集和浏览器自动化这三种场景，不同场景对应的工具、成本和稳定性完全不同。
- 一个完整采集链路通常包含“目标识别、请求发起、解析提取、去重清洗、存储落地、调度与重试、合法性边界”。
- Selenium 和 Scrapy 不是互相替代关系，前者更偏动态页面与浏览器行为，后者更偏批量采集、调度与管道化处理。

## 怎么用
### 示例 1：解析最小 HTML 列表并提取链接

```python hl_lines="1 8 20"
from html.parser import HTMLParser
from urllib.parse import urljoin


class LinkParser(HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        href = dict(attrs).get("href")
        if href:
            self.links.append(urljoin(self.base_url, href))


parser = LinkParser("https://example.com/reports/")
parser.feed('<a href="daily.html">daily</a><a href="/api/status">status</a>')
print(parser.links)
```


### 示例 2：用队列表达一个最小采集调度器

```python hl_lines="1 6 16"
from collections import deque
from urllib.parse import urljoin


seed = "https://example.com/"
queue = deque([seed])
visited = set()

while queue:
    current = queue.popleft()
    if current in visited:
        continue
    visited.add(current)
    if current == seed:
        queue.append(urljoin(current, "docs/"))
        queue.append(urljoin(current, "reports/"))

print(sorted(visited))
```


### 示例 3：用显式等待思路模拟浏览器自动化

```python hl_lines="1 5 13"
import time


def wait_until(predicate, timeout=0.2, interval=0.01):
    deadline = time.time() + timeout
    while time.time() < deadline:
        if predicate():
            return True
        time.sleep(interval)
    return False


state = {"ready": False}
state["ready"] = True
print(wait_until(lambda: state["ready"]))
```


落地建议:
- 先确定能不能直接拿接口数据，实在不行再上浏览器自动化，别一开始就把成本打满。
- 动态页面要把“页面加载、元素出现、网络请求完成、登录态有效”拆成独立等待条件。
- 采集完的数据必须做去重、字段校验和失败记录，否则后面分析阶段会被脏数据反噬。

## 业界案例
- 页面自动化测试常会先抓接口列表或 DOM 结构，再决定是走接口断言还是浏览器行为回放。
- 数据运营脚本会先采静态页面或接口，再批量清洗、去重并落到数据库或 CSV。
- 浏览器自动化最常见的误区，是把“页面没出来”和“元素定位错了”混成一个问题排查。

## 延伸阅读
- Scrapy 的真正价值在于“调度 + 去重 + 管道”，不只是能发 HTTP 请求。
- Selenium / Playwright 的稳定性，往往由等待策略、登录态复用和失败截图决定。
- 采集主题永远要先确认合法性、频率控制和 robots 边界，别把技术可行当成业务可做。

## Self-Check
### 概念题
1. 静态采集、接口采集和浏览器自动化分别适合什么场景？
2. 为什么采集脚本要把请求失败、解析失败和清洗失败分开记录？
3. Scrapy 的调度能力为什么比“for 循环发请求”更像工程资产？

### 编程题
1. 写一个最小 HTML 解析器，把页面中的链接提取成绝对路径。
2. 写一个最小等待函数，模拟浏览器等待元素出现的思路。

### 实战场景
1. 你要每天抓一个需要登录的后台页面，并抽取其中的报表数据，你会怎么决定是走接口、走 Selenium，还是两者混合？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
静态采集适合直接拿 HTML，接口采集适合数据已通过 HTTP 返回，浏览器自动化适合必须执行脚本、依赖登录态或复杂交互的页面。
讲解回看: [学什么](#学什么)

### 概念题 2
因为三类失败的修复路径完全不同，混在一起会让排障成本直线上升。
讲解回看: [为什么学](#为什么学)

### 概念题 3
因为工程化采集不仅要发请求，还要解决队列、去重、重试、限速、管道和失败恢复。
讲解回看: [延伸阅读](#延伸阅读)

### 编程题 1
可以自定义 `HTMLParser`，在 `handle_starttag()` 中收集 `a` 标签的 `href`，再用 `urljoin()` 转成绝对地址。
讲解回看: [怎么用](#怎么用)

### 编程题 2
核心是持续轮询一个条件，在超时前不断检查状态，这和 Selenium / Playwright 的显式等待思路一致。
讲解回看: [怎么用](#怎么用)

### 实战场景 1
先优先查网络面板能否直接拿到接口数据；如果必须执行脚本或依赖页面状态，再引入浏览器自动化，并把登录态与等待策略单独管理。
讲解回看: [落地建议](#怎么用)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [html.parser 文档](https://docs.python.org/3/library/html.parser.html)
- [Selenium 文档](https://www.selenium.dev/documentation/)
- [Scrapy 文档](https://docs.scrapy.org/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-17: 将 README1 中的网络采集、Selenium 与 Scrapy 相关主题折叠进主线路径专题。

---
[返回 Python 学习总览](../README.md)
