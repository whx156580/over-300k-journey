---
title: 办公文档、PDF、图像与消息自动化
module: testing
area: python_notes
stack: python
level: advanced
status: active
tags: [python, automation, office, pdf, image, email]
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
- Excel、Word、PDF、图像和邮件这些能力，经常出现在测试报告、办公流转、批处理和运维通知链路里。
- 这类主题的难点不在于“会不会调一个 API”，而在于你是否理解文件格式边界、可选依赖、编码和附件生命周期。
- 只要把这些能力收敛成脚本，很多重复性手工操作都能变成稳定可复用的小工具。

## 学什么
- 先分清标准库和第三方库的边界。`email`、`pathlib`、`mimetypes` 属于标准库；Excel、Word、PDF、图像往往需要额外安装专用库。
- 文件自动化最重要的是“输入格式 -> 处理动作 -> 输出格式”的链路，不要把解析、业务规则和导出混成一坨。
- 办公自动化任务通常要配套目录约定、命名规范、失败重试和人工兜底，否则脚本只会把错误批量放大。

## 怎么用
### 示例 1：检测常见可选依赖是否已安装

```python hl_lines="1 10"
OPTIONAL_IMPORTS = {
    "openpyxl": "openpyxl",
    "python-docx": "docx",
    "python-pptx": "pptx",
    "pypdf": "pypdf",
    "pillow": "PIL",
}

available = []
for package_name, module_name in OPTIONAL_IMPORTS.items():
    try:
        __import__(module_name)
    except ImportError:
        continue
    available.append(package_name)

print(sorted(available))
```


### 示例 2：用标准库构造带附件的邮件对象

```python hl_lines="1 7 11"
from email.message import EmailMessage

message = EmailMessage()
message["Subject"] = "Daily Report"
message["To"] = "qa@example.com"
message["From"] = "bot@example.com"
message.set_content("Smoke suite passed.")
message.add_attachment(
    b"status,passed\nsmoke,12\n",
    maintype="text",
    subtype="csv",
    filename="summary.csv",
)

print(message["Subject"], len(message.get_payload()))
```


### 示例 3：按文件后缀规划处理链路

```python hl_lines="3 9"
from pathlib import Path

HANDLERS = {
    ".xlsx": "openpyxl",
    ".docx": "python-docx",
    ".pdf": "pypdf",
    ".png": "pillow",
}

files = [Path("daily.xlsx"), Path("summary.pdf"), Path("avatar.png"), Path("mail.txt")]
plan = {file.name: HANDLERS.get(file.suffix, "manual-check") for file in files}
print(plan["daily.xlsx"], plan["mail.txt"])
```


落地建议:
- 先验证依赖和最小文件样本，再扩展到真实业务目录，别一上来就跑全量目录。
- 自动化处理文档时要显式区分“只读源文件”和“生成产物目录”，避免误覆盖原始资料。
- 消息通知脚本要保留失败日志和降级路径，例如先写本地草稿、再尝试真正发送。

## 业界案例
- 测试日报常见链路是 CSV / Excel 汇总 -> 图表截图或图片导出 -> 邮件发送给团队。
- 回归结果归档会涉及 PDF 合并、图片比对、日志打包和按日期目录归类。
- 业务运营脚本经常需要按模板生成 Word / PPT，再通过邮件或 IM 机器人分发。

## 延伸阅读
- 如果需求只是简单表格交换，优先考虑 CSV；只有在必须保留公式、样式、多工作表时再上 Excel 专用库。
- 面对 PDF、Office 这类复杂格式时，先用官方文档的最小示例确认能力边界，再决定是否继续投入。
- 消息通知能力要和日志、重试、幂等一起看，不能孤立设计。

## Self-Check
### 概念题
1. 办公自动化脚本最常见的风险点有哪些？
2. 为什么要先区分标准库能力和第三方依赖？
3. 什么时候应该优先使用 CSV 而不是 Excel？

### 编程题
1. 怎样在脚本启动时快速检测某个第三方文档库是否可用？
2. 如何用标准库构造一封带附件的邮件对象？

### 实战场景
1. 你要把测试结果导出成表格并按天归档，再把摘要发邮件给团队，应该如何拆分脚本职责？

先独立作答，再对照下方的“参考答案”和对应章节复盘。

## 参考答案
### 概念题 1
依赖缺失、文件格式不兼容、路径覆盖原件、附件过大、命名不规范和通知失败无兜底，都是常见风险。
讲解回看: [为什么学](#为什么学)

### 概念题 2
因为它直接决定安装成本、部署复杂度和可移植性。先吃透标准库，再按需要引入第三方库，脚本会更稳。
讲解回看: [学什么](#学什么)

### 概念题 3
当你只需要二维表格数据交换，不依赖样式、公式和复杂工作簿结构时，CSV 更轻、更通用，也更适合自动化链路。
讲解回看: [学什么](#学什么)

### 编程题 1
可在脚本入口用 `__import__()` 或直接 `import` 包一层 `try/except ImportError`，先把环境问题暴露出来。
讲解回看: [怎么用](#怎么用)

### 编程题 2
使用 `email.message.EmailMessage`，先设置主题、收件人和正文，再通过 `add_attachment()` 附加内容。
讲解回看: [怎么用](#怎么用)

### 实战场景 1
建议拆成“采集与汇总”“文件导出”“通知发送”三层。这样每层都能单独验证，也便于失败后局部重试。
讲解回看: [业界案例](#业界案例)

## 参考链接
- [Python 官方文档](https://docs.python.org/3/)
- [email.message 文档](https://docs.python.org/3/library/email.message.html)
- [本仓库知识模板](../../common/docs/template.md)

## 版本记录
- 2026-04-17: 将 README1 中的 Office / PDF / 图像 / 消息自动化主题并入 04_progressive_topics。

---
[返回 Python 学习总览](../README.md)
