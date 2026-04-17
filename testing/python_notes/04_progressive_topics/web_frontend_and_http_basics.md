---
title: Web 前端与 HTTP 基础
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, web, http, html, frontend, testing]
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
- 即使主职是测试或后端，也绕不开浏览器、HTML、CSS、JavaScript、URL 和 HTTP 这些 Web 基础概念。
- 不理解请求是怎么发出去、页面是怎么渲染出来的，就很难定位接口、页面、缓存和鉴权问题究竟卡在哪一层。
- Python 在 Web 场景里既能写服务，也能写自动化脚本，所以更需要把协议层和页面层分开理解。

## 学什么
- 先抓住一次 Web 访问的基本链路：浏览器构造请求 -> 服务器返回响应 -> 浏览器解析 HTML / CSS / JS -> 页面交互继续发请求。
- URL、查询参数、状态码、请求头、Cookie、Session 这些概念属于 HTTP 层；HTML 结构、样式和脚本属于前端呈现层。
- 学 Web 基础时不要急着背框架名，先把“资源定位、数据传输、页面结构、交互行为”这四件事讲清楚。

## 怎么用
### 示例 1：解析 URL 与查询参数

```python hl_lines="1 4 5"
from urllib.parse import parse_qs, urlparse

url = "https://example.com/search?q=python&tag=testing&tag=web"
parsed = urlparse(url)
query = parse_qs(parsed.query)

print(parsed.path, query["tag"])
```


### 示例 2：从 HTML 中提取链接

```python hl_lines="1 6 12"
from html.parser import HTMLParser


class LinkCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        href = dict(attrs).get("href")
        if href:
            self.links.append(href)


parser = LinkCollector()
parser.feed('<a href="/docs">Docs</a><a href="/api">API</a>')
print(parser.links)
```


### 示例 3：模拟最小请求与响应

```python hl_lines="1 11 14"
from dataclasses import dataclass


@dataclass
class Response:
    status_code: int
    body: dict


def health_view(headers):
    if headers.get("x-env") != "test":
        return Response(403, {"detail": "forbidden"})
    return Response(200, {"status": "ok"})


response = health_view({"x-env": "test"})
print(response.status_code, response.body["status"])
```


落地建议:
- 抓包和排障时先确认 URL、方法、状态码和响应体，再去看具体框架实现。
- 页面自动化失败不一定是前端问题，也可能是接口返回、鉴权状态或缓存策略导致的连锁反应。
- 写 Web 脚本时始终区分“拿数据的接口”和“展示数据的页面”，这会让调试路径短很多。

## 业界案例
- UI 自动化脚本定位元素失败时，往往先要确认页面是否真的拿到了接口数据。
- 接口测试定位鉴权问题时，经常要同时检查请求头、Cookie、重定向和前端缓存行为。
- 后端联调时最常见的误区，是把 HTML 页面问题、静态资源问题和业务接口问题混为一谈。

## 延伸阅读
- 学 Web 基础最划算的方式，是拿浏览器开发者工具对照“请求列表 + 响应 + 页面源码”一起看。
- 不熟悉前端框架也没关系，但必须能读懂 HTML 结构、基本选择器和网络面板。
- 对测试工程来说，HTTP 基础是 Selenium / Playwright、接口测试和性能测试的共同前置能力。

## Self-Check
### 概念题
1. HTML、CSS、JavaScript 和 HTTP 各自负责什么？
2. 为什么说 URL 与状态码比框架名字更值得先搞懂？
3. 页面打不开时，为什么不能立刻断言是前端代码问题？

### 编程题
1. 怎样快速拆出一个 URL 的路径和查询参数？
2. 如果你只有一段 HTML 字符串，如何提取其中的链接？

### 实战场景
1. 页面展示空白，你会按什么顺序排查：请求有没有发出、接口有没有返回、页面有没有正确渲染？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
HTML 描述结构，CSS 控制样式，JavaScript 负责交互逻辑，HTTP 负责浏览器和服务器之间的数据传输。
讲解回看: [学什么](#学什么)

### 概念题 2
因为排障和自动化的第一现场就是 URL、方法、状态码、请求头和响应体；这些比具体框架更稳定也更通用。
讲解回看: [为什么学](#为什么学)

### 概念题 3
因为页面结果可能受接口失败、鉴权失效、静态资源缺失、缓存污染或脚本报错影响，不一定是前端模板本身的问题。
讲解回看: [业界案例](#业界案例)

### 编程题 1
可用 `urllib.parse.urlparse()` 拆路径，再用 `parse_qs()` 解析查询参数。
讲解回看: [怎么用](#怎么用)

### 编程题 2
可用 `html.parser.HTMLParser` 自定义一个最小解析器，在 `handle_starttag()` 里收集 `a` 标签的 `href`。
讲解回看: [怎么用](#怎么用)

### 实战场景 1
先看网络面板确认请求是否发出，再确认接口返回是否正常，最后再检查页面脚本和渲染逻辑，这样最省时间。
讲解回看: [落地建议](#怎么用)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [urllib.parse 文档](https://docs.python.org/3/library/urllib.parse.html)
- [html.parser 文档](https://docs.python.org/3/library/html.parser.html)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-17: 将 README1 中的 Web 前端入门主题整理为 04_progressive_topics 专题笔记。

---
[返回 Python 学习总览](../README.md)
