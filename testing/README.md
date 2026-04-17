# 🛡️ 软件测试模块

> 这里承接 UI 自动化、接口测试、性能测试、移动端测试、AI 评测和测试策略六大知识域。

---

## 导航入口

- 自动汇总首页: [knowledge_hub.md](../common/docs/indexes/knowledge_hub.md)
- 搜索入口: `python scripts/search_knowledge.py <关键词>`
- 写作模板: [template.md](../common/docs/template.md)
- 测试策略总览: [test_strategy.md](./strategy/test_strategy.md)

---

## 模块索引

| 知识域 | 入口 | 已补充内容 |
| :--- | :--- | :--- |
| UI 自动化 | [ui/README.md](./ui/README.md) | 选择器与等待、网络 Mock、登录态复用 |
| 接口测试 | [api/README.md](./api/README.md) | 契约测试、Schema 校验、鉴权测试 |
| 性能测试 | [performance/README.md](./performance/README.md) | 基础压测、场景建模、容量预估 |
| 移动端测试 | [mobile/README.md](./mobile/README.md) | 定位策略、会话管理、稳定性设计 |
| AI 评测 | [ai-eval/README.md](./ai-eval/README.md) | RAG 基础、检索指标、黄金测试集 |
| Python 笔记 | [python_notes/README.md](./python_notes/README.md) | 环境管理、基础语法、高级特性、工程专题 |
| 测试策略 | [strategy/README.md](./strategy/README.md) | 风险驱动、分层回归、质量门禁 |

---

## 推荐学习顺序

1. 先看 [strategy/README.md](./strategy/README.md)，建立测试分层、风险和门禁意识。
2. 再补 UI、API、性能、移动端的单项能力。
3. 最后进入 [ai-eval/README.md](./ai-eval/README.md)，把传统测试能力延伸到 LLM / RAG 评测。

---

## 如何继续往里加内容

1. 找到对应目录，例如 `testing/ui/playwright/advanced/`
2. 复制 [template.md](../common/docs/template.md) 的结构
3. 补齐标准元数据
4. 写完后运行:

```bash
python scripts/build_knowledge_index.py
python scripts/search_knowledge.py playwright
```

---
[返回首页](../README.md) | [查看索引说明](../common/docs/indexes/README.md)
