from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from common.tools.knowledge_base import load_knowledge_entries


README_PORTAL_START = "<!-- PORTAL:START -->"
README_PORTAL_END = "<!-- PORTAL:END -->"


def group_entries(entries):
    grouped: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
    for entry in entries:
        grouped[entry.module][entry.area].append(entry)
    return grouped


def module_tree_lines(entries, module_name: str) -> list[str]:
    area_to_stacks: dict[str, set[str]] = defaultdict(set)
    for entry in entries:
        if entry.module != module_name:
            continue
        area_to_stacks[entry.area].add(entry.stack)

    lines = [f"{module_name}/"]
    areas = sorted(area_to_stacks.items())
    for area_index, (area, stacks) in enumerate(areas):
        area_prefix = "└─" if area_index == len(areas) - 1 else "├─"
        lines.append(f"{area_prefix} {area}/")

        sorted_stacks = sorted(stack for stack in stacks if stack)
        for stack_index, stack in enumerate(sorted_stacks):
            indent = "   " if area_index == len(areas) - 1 else "│  "
            stack_prefix = "└─" if stack_index == len(sorted_stacks) - 1 else "├─"
            lines.append(f"{indent}{stack_prefix} {stack}/")

    return lines


def recent_entry_rows(entries, link_prefix: str, limit: int = 8) -> list[str]:
    ordered = sorted(
        entries,
        key=lambda entry: (
            entry.updated,
            entry.modified_at,
            entry.module,
            entry.area,
            entry.title,
        ),
        reverse=True,
    )[:limit]

    rows = [
        "| 标题 | 模块 | 领域 | 技术栈 | 更新时间 | 路径 |",
        "| :--- | :--- | :--- | :--- | :--- | :--- |",
    ]
    for entry in ordered:
        rows.append(
            f"| {entry.title} | `{entry.module}` | `{entry.area}` | `{entry.stack}` | "
            f"{entry.updated or datetime.fromtimestamp(entry.modified_at).strftime('%Y-%m-%d')} | "
            f"[{entry.relative_path}]({link_prefix}{entry.relative_path}) |"
        )
    return rows


def portal_lines(entries, link_prefix: str) -> list[str]:
    grouped = group_entries(entries)
    module_readmes = {
        "testing": f"{link_prefix}testing/README.md",
        "frontend": f"{link_prefix}frontend/README.md",
        "backend": f"{link_prefix}backend/README.md",
        "ai": f"{link_prefix}ai/README.md",
    }
    search_examples = {
        "testing": "playwright",
        "frontend": "react",
        "backend": "mysql",
        "ai": "prompt",
    }

    lines = [
        "## 门户首页",
        "",
        "| 模块 | 领域数 | 笔记数 | 入口 | 搜索示例 |",
        "| :--- | :--- | :--- | :--- | :--- |",
    ]

    for module_name in ("testing", "frontend", "backend", "ai"):
        area_map = grouped.get(module_name, {})
        note_count = sum(len(items) for items in area_map.values())
        lines.append(
            f"| `{module_name}` | {len(area_map)} | {note_count} | "
            f"[进入模块]({module_readmes[module_name]}) | "
            f"`python scripts/search_knowledge.py {search_examples[module_name]} --module {module_name}` |"
        )

    lines.extend(
        [
            "",
            "### 快速入口",
            "",
            f"- 知识汇总页: [knowledge_hub.md]({link_prefix}common/docs/indexes/knowledge_hub.md)",
            f"- 门户说明页: [portal_home.md]({link_prefix}common/docs/indexes/portal_home.md)",
            f"- 模板: [template.md]({link_prefix}common/docs/template.md)",
            f"- 结构说明: [project_structure.md]({link_prefix}common/docs/project_structure.md)",
            "",
            "### 每模块目录树",
            "",
        ]
    )

    for module_name in ("testing", "frontend", "backend", "ai"):
        lines.append(f"#### `{module_name}`")
        lines.append("")
        lines.append("```text")
        lines.extend(module_tree_lines(entries, module_name))
        lines.append("```")
        lines.append("")

    lines.extend(
        [
            "### 最近新增内容",
            "",
        ]
    )
    lines.extend(recent_entry_rows(entries, link_prefix))
    lines.append("")
    return lines


def write_portal_home(entries) -> Path:
    output = ROOT / "common" / "docs" / "indexes" / "portal_home.md"
    lines = [
        "# 知识库门户页",
        "",
        "> 本页由 `python scripts/build_knowledge_index.py` 自动生成，用于展示首页导航、模块目录树和最近新增内容。",
        "",
        "---",
        "",
    ]
    lines.extend(portal_lines(entries, "../../../"))
    output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return output


def update_root_readme(entries) -> Path:
    readme_path = ROOT / "README.md"
    content = readme_path.read_text(encoding="utf-8")
    start = content.find(README_PORTAL_START)
    end = content.find(README_PORTAL_END)
    if start == -1 or end == -1 or end < start:
        raise ValueError("README portal markers not found.")

    portal_block = "\n".join(portal_lines(entries, "./")).rstrip()
    new_content = (
        content[: start + len(README_PORTAL_START)]
        + "\n\n"
        + portal_block
        + "\n\n"
        + content[end:]
    )
    readme_path.write_text(new_content, encoding="utf-8")
    return readme_path


def build_knowledge_hub() -> Path:
    entries = load_knowledge_entries(ROOT)
    output = ROOT / "common" / "docs" / "indexes" / "knowledge_hub.md"

    grouped = group_entries(entries)

    lines: list[str] = [
        "# 知识库汇总首页",
        "",
        "> 本页由 `python scripts/build_knowledge_index.py` 自动生成，用于汇总带标准元数据的知识笔记。",
        "",
        "---",
        "",
        "## 总览",
        "",
        f"- 已收录笔记数: **{len(entries)}**",
        f"- 覆盖模块数: **{len(grouped)}**",
        "- 搜索入口: `python scripts/search_knowledge.py <关键词>`",
        "",
        "---",
        "",
        "## 模块索引",
        "",
    ]

    for module_name, area_map in grouped.items():
        lines.append(f"### `{module_name}`")
        lines.append("")
        lines.append(f"- 领域数: **{len(area_map)}**")
        lines.append(f"- 笔记数: **{sum(len(items) for items in area_map.values())}**")
        lines.append("")

        for area_name, items in sorted(area_map.items()):
            lines.append(f"#### `{area_name}`")
            lines.append("")
            lines.append("| 标题 | 技术栈 | 层级 | 标签 | 路径 |")
            lines.append("| :--- | :--- | :--- | :--- | :--- |")
            for item in items:
                tag_text = ", ".join(item.tags) if item.tags else "-"
                lines.append(
                    f"| {item.title} | `{item.stack}` | `{item.level}` | {tag_text} | "
                    f"[{item.relative_path}](../../../{item.relative_path}) |"
                )
            lines.append("")

    if not entries:
        lines.extend(
            [
                "当前还没有带标准元数据的知识笔记。",
                "",
                "你可以先使用 `common/docs/template.md` 新建第一篇内容，再重新运行生成脚本。",
                "",
            ]
        )

    output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return output


if __name__ == "__main__":
    entries = load_knowledge_entries(ROOT)
    hub_target = build_knowledge_hub()
    portal_target = write_portal_home(entries)
    readme_target = update_root_readme(entries)
    print(f"Knowledge hub generated at: {hub_target}")
    print(f"Portal home generated at: {portal_target}")
    print(f"README portal updated at: {readme_target}")
