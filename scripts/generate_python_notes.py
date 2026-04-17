from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parent.parent
ROOT = PROJECT_ROOT / "testing" / "python_notes"
MANIFEST_PATH = ROOT / "manifest.json"

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.tools.knowledge_base import parse_front_matter


@dataclass(frozen=True)
class StageConfig:
    directory: str
    title: str
    goal: str
    duration: str
    prerequisite: str


def load_manifest() -> dict[str, object]:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


MANIFEST = load_manifest()
STAGES = tuple(StageConfig(**stage) for stage in MANIFEST["stages"])
INDEX_DESCRIPTIONS = {
    stage: [(item["filename"], item["description"]) for item in items]
    for stage, items in MANIFEST["index_descriptions"].items()
}
QUICK_START = [(item["path"], item["description"]) for item in MANIFEST["quick_start"]]
RECOMMENDED_FIRST = [(item["path"], item["description"]) for item in MANIFEST["recommended_first"]]
SUPPLEMENT_CHECKLIST = list(MANIFEST["supplement_checklist"])
ROUTE_DEFINITIONS = dict(MANIFEST["route_definitions"])
PYTHON_NOTES_REQUIREMENTS = "\n".join(MANIFEST["requirements"]) + "\n"
PYTHON_NOTES_MAKEFILE = "\n".join(MANIFEST["makefile_lines"]) + "\n"


@dataclass(frozen=True)
class NoteEntry:
    relative_path: str
    stage: str
    title: str


def write(relative_path: str, content: str) -> None:
    path = ROOT / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def discover_note_entries() -> dict[str, NoteEntry]:
    entries: dict[str, NoteEntry] = {}
    for stage in STAGES:
        stage_dir = ROOT / stage.directory
        for note_path in sorted(stage_dir.glob("*.md")):
            if note_path.name.lower() == "readme.md":
                continue
            metadata, _ = parse_front_matter(note_path.read_text(encoding="utf-8"))
            title = str(metadata.get("title", note_path.stem))
            relative_path = note_path.relative_to(ROOT).as_posix()
            entries[relative_path] = NoteEntry(relative_path=relative_path, stage=stage.directory, title=title)
    return entries


def expected_note_paths() -> set[str]:
    paths: set[str] = set()
    for stage in STAGES:
        for filename, _ in INDEX_DESCRIPTIONS[stage.directory]:
            paths.add(f"{stage.directory}/{filename}")
    return paths


def referenced_note_paths() -> set[str]:
    paths = {path for path, _ in QUICK_START}
    paths.update(path for path, _ in RECOMMENDED_FIRST)
    for route in ROUTE_DEFINITIONS.values():
        paths.update(route["core"])
        paths.update(route["extra"])
    return paths


def validate_structure(entries: dict[str, NoteEntry]) -> None:
    actual_paths = set(entries)
    expected_paths = expected_note_paths()
    referenced_paths = referenced_note_paths()

    missing = sorted(expected_paths - actual_paths)
    extra = sorted(actual_paths - expected_paths)
    broken_references = sorted(referenced_paths - actual_paths)
    if missing or extra:
        details: list[str] = []
        if missing:
            details.append("Missing note files:\n- " + "\n- ".join(missing))
        if extra:
            details.append("Unexpected note files:\n- " + "\n- ".join(extra))
        raise ValueError("\n\n".join(details))
    if broken_references:
        raise ValueError("Manifest references missing note files:\n- " + "\n- ".join(broken_references))


def stage_note_mapping_literal() -> str:
    lines = ["STAGE_DIRECTORIES = {"]
    for stage in STAGES:
        lines.append(f'    "{stage.directory}": {{')
        for filename, _ in INDEX_DESCRIPTIONS[stage.directory]:
            lines.append(f'        "{filename}",')
        lines.append("    },")
    lines.append("}")
    return "\n".join(lines)


def note_link(entries: dict[str, NoteEntry], relative_path: str) -> str:
    return f"[{entries[relative_path].title}](./{relative_path})"


def render_stage_overview_rows() -> list[str]:
    lines = [
        "| 阶段 | 目录 | 目标 | 预计时长 | 前置知识 |",
        "| :--- | :--- | :--- | :--- | :--- |",
    ]
    for stage in STAGES:
        lines.append(
            f"| {stage.title} | `{stage.directory}/` | {stage.goal} | {stage.duration} | {stage.prerequisite} |"
        )
    return lines


def render_route_links(entries: dict[str, NoteEntry], relative_paths: list[str]) -> list[str]:
    return [f"  - {note_link(entries, path)}" for path in relative_paths]


def render_content_index(stage: StageConfig, entries: dict[str, NoteEntry]) -> list[str]:
    lines = [
        f"### {stage.title}",
        "",
        "| 主题 | 文件 | 说明 |",
        "| :--- | :--- | :--- |",
    ]
    for filename, description in INDEX_DESCRIPTIONS[stage.directory]:
        relative_path = f"{stage.directory}/{filename}"
        lines.append(
            f"| {entries[relative_path].title} | [{filename}](./{relative_path}) | {description} |"
        )
    lines.append("")
    return lines


def build_readme(entries: dict[str, NoteEntry]) -> None:
    total_notes = len(entries)
    lines = [
        "# Python 学习笔记体系",
        "",
        "> 面向测试工程师、测试开发、自动化工程师，也兼顾 Python 初学者的主线学习笔记。当前内容统一收敛在 `01_environment` 到 `04_progressive_topics` 四个阶段目录中，不再维护额外的按天目录。",
        "",
        "## 页内导航",
        "",
        "[快速开始](#快速开始) | [课程主线总览](#课程主线总览) | [路线选择](#我该选哪条路线) | [学习里程碑](#学习里程碑--推荐练手项目) | [本轮补充清单](#本轮补充清单) | [推荐先读 6 篇](#推荐先读-6-篇) | [内容索引](#内容索引) | [一键初始化](#一键初始化)",
        "",
        "## 这套笔记解决什么问题",
        "",
        "- 它不是零散收藏夹，而是一条从“把环境配稳”到“把能力落到工程场景”的连续主线。",
        "- 它不是只讲语法，也不是一上来就讲框架，而是把环境、基础语法、高级语法、工程专题串成一个可执行的学习路径。",
        "- 它特别适合想把 Python 用到测试自动化、接口联调、数据处理、Web 服务、采集脚本和项目交付中的同学。",
        "",
        "## 适合谁看",
        "",
        "- 刚开始学 Python，希望有一条不绕路的主线。",
        "- 已经会一点语法，但知识点比较散，想重新收拢成体系。",
        "- 做测试开发、自动化测试、平台工具开发，想把 Python 学到“能稳定落地”的程度。",
        "- 后面想转向数据分析、机器学习或 Web 开发，但希望先把语言根基和工程习惯打牢。",
        "",
        "## 快速开始",
        "",
        "如果你是第一次打开这个目录，建议先按下面的顺序进入：",
        "",
    ]
    for index, (relative_path, description) in enumerate(QUICK_START, start=1):
        lines.append(f"{index}. {note_link(entries, relative_path)}：{description}")
    lines.extend(
        [
            "",
            "走完这几篇之后，再回到这页，从“推荐学习路线图”或“三种选读方案”里挑自己的主线。",
            "",
            "## 课程主线总览",
            "",
        ]
    )
    lines.extend(render_stage_overview_rows())
    lines.extend(
        [
            "",
            "## 四个阶段分别解决什么问题",
            "",
            "- `01_environment`：先解决“工具链是否稳定”。学完后你应该能独立安装与切换 Python、创建虚拟环境、安装依赖，并在 IDE 中调试最小脚本。",
            "- `02_basic_syntax`：先解决“能不能顺畅写出小脚本”。学完后你应该能从零写出带输入输出、判断、循环、容器和函数的小工具脚本。",
            "- `03_advanced_syntax`：先解决“能不能写出结构更清晰、更可复用的代码”。学完后你应该能把脚本拆成模块，处理文件和结构化数据，并理解装饰器、迭代器、上下文管理器和 OOP 基础。",
            "- `04_progressive_topics`：先解决“能不能把语言能力落到真实工作”。学完后你应该能把 Python 用到日志分析、CLI 工具、数据库操作、Web 服务、采集脚本、数据分析、测试与项目交付。",
            "",
            "## 推荐学习路线图",
            "",
            "1. 第 1 站：先把 `01_environment` 跑通，确保解释器、虚拟环境、依赖管理和 IDE 调试体验稳定。",
            "2. 第 2 站：在 `02_basic_syntax` 里完成“脚本入口与 I/O -> 变量 -> 运算符 -> 流程控制 -> 字符串 -> 容器 -> 函数”的最小闭环。",
            "3. 第 3 站：进入 `03_advanced_syntax`，按“模块与抽象能力 -> 资源管理 -> 文件与结构化数据 -> OOP 与异常”的顺序补齐工程写法。",
            "4. 第 4 站：回到 `04_progressive_topics`，优先挑 1-2 条和工作最相关的方向深挖，不建议一开始就把所有专题平铺扫完。",
            "5. 第 5 站：每学完一个阶段，至少做一个自己的小脚本、小工具或小项目，把示例改造成真实场景。",
            "",
            "如果你是业余时间学习，可以把这 5 站理解成一个 4-8 周的学习闭环；如果你是在工作中边用边学，也可以先从第 4 站进入，再回补前面的共同底座。",
            "",
            "## 我该选哪条路线",
            "",
            "- 如果你现在最常接触的是接口联调、自动化测试、测试工具、质量平台，先看“测试开发路线”。",
            "- 如果你现在最常接触的是 CSV / JSON / SQL、报表、数据清洗、ETL，先看“数据方向路线”。",
            "- 如果你还没完全确定方向，但希望先把 Python 语言和工程习惯打牢，先看“通用 Python 路线”。",
            "",
            "## 三种选读方案",
            "",
            "不管最后走哪条路线，`01_environment`、`02_basic_syntax`、`03_advanced_syntax` 都建议作为共同底座完整走一遍；真正的分流，主要发生在 `04_progressive_topics`。",
            "",
        ]
    )
    for route_name, config in ROUTE_DEFINITIONS.items():
        lines.append(f"### 方案：{route_name}")
        lines.append("")
        lines.append(f"- 适合人群：{config['audience']}")
        lines.append("- 共同底座：`01_environment` 到 `03_advanced_syntax` 建议完整走完。")
        lines.append("- 核心专题：")
        lines.extend(render_route_links(entries, config["core"]))
        lines.append("- 补充专题：")
        lines.extend(render_route_links(entries, config["extra"]))
        lines.append(f"- 学完后的结果：{config['result']}")
        lines.append("")
    lines.extend(
        [
            "## 学习里程碑 / 推荐练手项目",
            "",
            "1. 学完 `01_environment`：至少完成一次本地 Python 安装、虚拟环境创建、依赖安装和 IDE 调试闭环。",
            "2. 学完 `02_basic_syntax`：做一个带输入输出和流程控制的小脚本，比如日志筛选器、批量重命名工具、简单成绩统计器。",
            "3. 学完 `03_advanced_syntax`：把脚本拆成 2-4 个模块，补上异常处理、JSON / CSV 读写，以及最基本的类封装。",
            "4. 学完 `04_progressive_topics`：按自己的路线做一个岗位相关的小项目，比如接口测试工具、ETL 清洗脚本、CLI 自动化工具或最小 Web 服务。",
            "",
            "## 本轮补充清单",
            "",
        ]
    )
    lines.extend(SUPPLEMENT_CHECKLIST)
    lines.extend(
        [
            "",
            "## 当前覆盖范围",
            "",
            f"- 当前共有 4 个阶段、{total_notes} 篇可校验笔记。",
            "- `01_environment` 到 `04_progressive_topics` 已覆盖环境搭建、语言基础、高级语法，以及配置管理、调试排障、数据库、Web、采集、数据分析、机器学习、测试、性能、质量工具链、打包发布和项目交付等主题。",
            "",
            "## 推荐先读 6 篇",
            "",
            "- 如果你暂时不想完整浏览整份目录，可以先读下面这 6 篇，把“方向感 -> 环境 -> 脚本 -> 抽象 -> 工程入口”这条主线先跑通：",
            "",
        ]
    )
    for index, (relative_path, description) in enumerate(RECOMMENDED_FIRST, start=1):
        lines.append(f"{index}. {note_link(entries, relative_path)}：{description}")
    lines.extend(["", "## 内容索引", ""])
    for stage in STAGES:
        lines.extend(render_content_index(stage, entries))
    lines.extend(
        [
            "## 怎么使用这套笔记",
            "",
            "1. 先看“快速开始”“推荐学习路线图”“三种选读方案”，再按主线阶段学习，不建议一上来只挑感兴趣的高级专题。",
            "2. 每篇笔记先看目录，再看“为什么学”“学什么”“怎么用”，最后做 `Self-Check`。",
            "3. 每学完一个主题，至少手敲一遍示例，并改成自己的场景。",
            "4. 如果你是测试开发，优先把日志、CLI、数据库、Web、测试、项目交付这几组专题练熟。",
            "5. 遇到不懂的地方，先最小复现，再回看对应主线阶段，不要直接跳去堆框架。",
            "",
            "## 一键初始化",
            "",
            "```bash",
            "cd testing/python_notes",
            "python -m pip install -r requirements.txt",
            "pytest tests -q",
            "```",
            "",
            "## 工程化约定",
            "",
            "- 所有笔记使用 GitHub Flavored Markdown。",
            "- 每篇笔记都包含 front matter、目录锚点、Self-Check、参考答案、参考链接和版本记录。",
            "- `tests/test_markdown_examples.py` 会执行所有 `python` 代码块，并使用独立编译标志，避免被测试文件自身的 future import 掩盖兼容性问题。",
            f"- 当前共有 4 个阶段目录、{total_notes} 篇可校验笔记。",
            "- 当前示例以 Python 3.8+ 为最低兼容目标；遇到 3.10+ 语法特性时会明确标注版本差异。",
            "- `images/` 目录按“笔记名_序号.png”维护截图与示意图资源。",
            "- 当前目录提供 [Makefile](./Makefile) 作为常用命令入口，可使用 `make install`、`make test`、`make lint`、`make format`、`make check`。",
            "",
            "## 关联入口",
            "",
            "- 示例校验脚本: [tests/test_markdown_examples.py](./tests/test_markdown_examples.py)",
            "- 依赖清单: [requirements.txt](./requirements.txt)",
            "- 常用命令: [Makefile](./Makefile)",
            "- 结构清单: [manifest.json](./manifest.json)",
            "- 知识汇总页: [../../common/docs/indexes/knowledge_hub.md](../../common/docs/indexes/knowledge_hub.md)",
            "- 模板参考: [../../common/docs/template.md](../../common/docs/template.md)",
        ]
    )
    write("README.md", "\n".join(lines).rstrip() + "\n")


def build_requirements() -> None:
    write("requirements.txt", PYTHON_NOTES_REQUIREMENTS)


def build_makefile() -> None:
    write("Makefile", PYTHON_NOTES_MAKEFILE)


def build_test_script() -> None:
    lines = [
        "from __future__ import annotations",
        "",
        "import re",
        "from pathlib import Path",
        "",
        "",
        "ROOT = Path(__file__).resolve().parent.parent",
        stage_note_mapping_literal(),
        'REQUIRED_HEADINGS = (',
        '    "## 目录",',
        '    "## Self-Check",',
        '    "## 参考答案",',
        '    "## 参考链接",',
        '    "## 版本记录",',
        ")",
        "FRONT_MATTER_KEYS = (",
        '    "title:",',
        '    "module:",',
        '    "area:",',
        '    "stack:",',
        '    "level:",',
        '    "status:",',
        '    "tags:",',
        '    "updated:",',
        ")",
        'PYTHON_BLOCK_PATTERN = re.compile(r"```python[^\\n]*\\n(.*?)```", re.DOTALL)',
        "",
        "",
        "def iter_note_files() -> list[Path]:",
        "    files: list[Path] = []",
        "    for directory in STAGE_DIRECTORIES:",
        "        stage_dir = ROOT / directory",
        '        files.extend(sorted(path for path in stage_dir.rglob("*.md") if "images" not in path.parts))',
        "    return files",
        "",
        "",
        "def test_expected_files_exist() -> None:",
        "    for directory, expected in STAGE_DIRECTORIES.items():",
        '        actual_names = {path.name for path in (ROOT / directory).glob("*.md")}',
        "        assert actual_names == expected",
        "",
        "",
        "def test_images_directories_exist() -> None:",
        "    for directory in STAGE_DIRECTORIES:",
        '        image_dir = ROOT / directory / "images"',
        "        assert image_dir.is_dir()",
        '        assert (image_dir / "README.md").exists()',
        "",
        "",
        "def test_note_front_matter_and_headings() -> None:",
        "    files = iter_note_files()",
        "    expected_count = sum(len(files) for files in STAGE_DIRECTORIES.values())",
        "    assert len(files) == expected_count",
        "",
        "    for note_file in files:",
        '        content = note_file.read_text(encoding="utf-8")',
        '        assert content.startswith("---\\n"), note_file',
        "        for key in FRONT_MATTER_KEYS:",
        '            assert key in content, f"{note_file} missing {key}"',
        "        for heading in REQUIRED_HEADINGS:",
        '            assert heading in content, f"{note_file} missing {heading}"',
        "",
        "",
        "def test_python_code_blocks_compile_and_run() -> None:",
        "    for note_file in iter_note_files():",
        '        content = note_file.read_text(encoding="utf-8")',
        "        blocks = PYTHON_BLOCK_PATTERN.findall(content)",
        '        assert blocks, f"{note_file} has no python code blocks"',
        "",
        "        for block in blocks:",
        '            namespace = {"__name__": "__markdown_example__"}',
        '            code = compile(block, str(note_file), "exec", dont_inherit=True)',
        "            exec(code, namespace, namespace)",
        "",
    ]
    content = "\n".join(lines)
    write("tests/test_markdown_examples.py", content)


def build_image_readmes() -> None:
    for stage in STAGES:
        image_dir = ROOT / stage.directory / "images"
        image_dir.mkdir(parents=True, exist_ok=True)
        image_files = sorted(
            path.name for path in image_dir.iterdir() if path.is_file() and path.name.lower() != "readme.md"
        )
        content_lines = [
            "# Images",
            "",
            "本目录用于保存该阶段笔记配套截图与示意图资源。",
            "",
            "命名约定:",
        ]
        if image_files:
            content_lines.extend(f"- `{name}`" for name in image_files)
        else:
            content_lines.append("- 当前阶段暂无截图资源")
        content_lines.extend(
            [
                "",
                "建议规范:",
                "- PNG 格式",
                "- 建议按照 4K 截图后再缩放到 50%",
                "- 一张图只表达一个关键步骤，优先展示命令、输出和关键配置项",
            ]
        )
        write(f"{stage.directory}/images/README.md", "\n".join(content_lines) + "\n")


def main() -> None:
    entries = discover_note_entries()
    validate_structure(entries)
    build_readme(entries)
    build_requirements()
    build_makefile()
    build_test_script()
    build_image_readmes()
    print(f"python_notes scaffolding synced: {len(entries)} notes")


if __name__ == "__main__":
    main()
