---
title: Web 框架、Django / DRF 与服务交付
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, web, django, drf, api, celery, cache]
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
- Web 框架主题把 HTTP、路由、模板、数据库、认证、缓存、异步任务和上线交付真正串成一条业务链路。
- 测试开发在做接口测试、自动化平台、后台管理系统时，迟早都要面对 Django / DRF 这类服务端框架。
- 如果只会敲命令而不理解请求生命周期、配置入口和服务依赖，项目一复杂就很难排障。

## 学什么
- 先把 Web 应用拆成“配置与启动、路由与视图、数据模型、认证与会话、接口序列化、缓存与异步任务、发布与监控”几层。
- Django 更偏“完整框架”，适合快速搭后台、管理端和中小型业务系统；DRF 则是在 Django 之上把接口开发、认证、分页、序列化这些能力标准化。
- Web 框架学习不能只盯着 happy path，还要同时考虑迁移、静态资源、日志、单元测试、缓存一致性和失败降级。

## 怎么用
### 示例 1：用数据结构梳理一个最小 Web 应用

```python hl_lines="4 14 19"
from dataclasses import dataclass


@dataclass
class Route:
    path: str
    view_name: str
    methods: tuple


routes = [
    Route("/health/", "health_check", ("GET",)),
    Route("/api/reports/", "report_list", ("GET", "POST")),
]
route_map = {route.path: route.view_name for route in routes}

print(route_map["/health/"], routes[1].methods)
```


### 示例 2：模拟一个最小 API 序列化与校验流程

```python hl_lines="1 6 18"
from dataclasses import dataclass, asdict


@dataclass
class Report:
    name: str
    passed: int


def validate_payload(payload):
    if not payload.get("name"):
        raise ValueError("name is required")
    if payload.get("passed", -1) < 0:
        raise ValueError("passed must be >= 0")
    return Report(name=payload["name"], passed=payload["passed"])


report = validate_payload({"name": "smoke", "passed": 12})
print(asdict(report))
```


### 示例 3：把缓存与异步任务配置拆开表达

```python hl_lines="2 8 13"
service_config = {
    "cache": {"backend": "redis", "ttl_seconds": 300},
    "tasks": {
        "send_daily_report": {"queue": "default", "interval_seconds": 600},
        "sync_metrics": {"queue": "analytics", "interval_seconds": 60},
    },
}

task_names = sorted(service_config["tasks"])
cache_ttl = service_config["cache"]["ttl_seconds"]
print(task_names, cache_ttl)
```


落地建议:
- 先跑通“启动服务 -> 发请求 -> 看日志 -> 看数据库 / 响应”的最小链路，再逐步加认证、缓存、Celery 和三方平台。
- 接口和页面要拆开调试，别把模板问题、接口问题、认证问题和缓存问题混成一团。
- 项目一旦进入多人协作，就要把配置入口、依赖服务、迁移步骤、回滚方式写成清单。

## 业界案例
- 内部管理平台通常会同时用到 Django Admin、业务模型、REST 接口和后台异步任务。
- 前后端分离项目常见问题不是接口“不会写”，而是序列化边界、鉴权方式、缓存策略和错误码约定不一致。
- 项目上线前最容易暴露的问题往往是静态资源、数据库迁移、配置缺失和后台任务没跟着部署。

## 延伸阅读
- 先掌握请求生命周期和配置入口，再看 DRF、缓存、消息队列和中间件扩展，学习曲线会平很多。
- Django 学习最怕“只会改业务代码”，却说不清 `settings`、`urls`、`views`、`models`、`serializers`、`tasks` 分别放什么。
- 服务端框架本质上是在帮你组织复杂度，但复杂度并不会消失，所以日志、测试、配置和部署同样重要。

## Self-Check
### 概念题
1. Django、DRF、缓存和异步任务分别解决的是哪一层问题？
2. 为什么说 Web 框架排障时要优先看配置、请求生命周期和依赖服务？
3. Session、Token、缓存和数据库各自更适合存什么？

### 编程题
1. 写一个最小路由表结构，表达页面路由和接口路由的区别。
2. 写一个最小校验函数，把请求字典校验后转换成统一的数据结构。

### 实战场景
1. 你接手一个 Django 项目，接口 200 但页面是空的，你会按什么顺序检查路由、接口、模板、静态资源和缓存？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
Django 负责项目骨架和服务端组织，DRF 负责接口层标准化，缓存负责读性能与热点数据，异步任务负责把长耗时动作从请求链路里拆出去。
讲解回看: [学什么](#学什么)

### 概念题 2
因为框架问题经常不是业务逻辑本身错了，而是配置入口、服务依赖、路由绑定或中间件顺序出了问题。
讲解回看: [为什么学](#为什么学)

### 概念题 3
Session / Token 更偏身份与会话，缓存更偏可重建的热点数据，数据库负责持久化业务真相。
讲解回看: [怎么用](#怎么用)

### 编程题 1
可以用 `dataclass` 或字典列表表达 `path`、`view_name` 和 `methods`，先把请求入口梳理清楚再谈框架细节。
讲解回看: [怎么用](#怎么用)

### 编程题 2
先判断必填字段，再校验类型与边界，最后转换成统一对象或字典，这就是最小序列化思路。
讲解回看: [怎么用](#怎么用)

### 实战场景 1
先确认请求是否真的拿到正确数据，再确认模板 / 前端是否正确消费，之后再检查静态资源和缓存污染。
讲解回看: [落地建议](#怎么用)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [Django 官方文档](https://docs.djangoproject.com/)
- [Django REST framework 文档](https://www.django-rest-framework.org/)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-17: 将 README1 中的 Django、DRF、缓存、异步任务、单元测试与项目上线主题折叠进主线路径专题。

---
[返回 Python 学习总览](../README.md)
