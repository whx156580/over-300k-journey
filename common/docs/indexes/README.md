# 索引与搜索

> 这里是知识库的导航入口，负责承接“自动汇总首页”和“本地搜索入口”。

---

## 自动汇总首页

- 汇总页文件: [knowledge_hub.md](./knowledge_hub.md)
- 生成命令: `python scripts/build_knowledge_index.py`

这个汇总页会扫描带标准元数据的知识笔记，并按模块、领域、技术栈自动生成导航表。

---

## 搜索入口

- 搜索命令: `python scripts/search_knowledge.py <关键词>`

常用示例:

```bash
python scripts/search_knowledge.py playwright
python scripts/search_knowledge.py contract --module testing --area api
python scripts/search_knowledge.py rag --stack ragas
python scripts/search_knowledge.py appium --json
```

支持的筛选参数:

- `--module`
- `--area`
- `--stack`
- `--tag`
- `--limit`
- `--json`

---

[返回首页](../../../README.md)
