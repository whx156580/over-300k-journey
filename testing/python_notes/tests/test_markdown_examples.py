from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
NOTE_DIRECTORIES = (
    "01_environment",
    "02_basic_syntax",
    "03_advanced_syntax",
    "04_progressive_topics",
)
EXPECTED_FILES = {
    "01_environment": {
        "dependency_management.md",
        "ide_setup.md",
        "python_version_management.md",
    },
    "02_basic_syntax": {
        "collections.md",
        "control_flow.md",
        "function_basics.md",
        "operators_and_expressions.md",
        "strings_and_methods.md",
        "variables_and_types.md",
    },
    "03_advanced_syntax": {
        "context_managers.md",
        "decorators.md",
        "exceptions.md",
        "iterators_and_generators.md",
        "modules_and_packages.md",
        "object_oriented_programming.md",
    },
    "04_progressive_topics": {
        "packaging_and_publishing.md",
        "python_concurrency.md",
        "python_keywords.md",
        "python_profiling.md",
        "python_re.md",
        "testing_pyramid_and_pytest.md",
        "type_hints_and_static_checking.md",
    },
}
REQUIRED_HEADINGS = (
    "## 目录",
    "## Self-Check",
    "## 参考答案",
    "## 参考链接",
    "## 版本记录",
)
FRONT_MATTER_KEYS = (
    "title:",
    "module:",
    "area:",
    "stack:",
    "level:",
    "status:",
    "tags:",
    "updated:",
)
PYTHON_BLOCK_PATTERN = re.compile(r"```python[^\n]*\n(.*?)```", re.DOTALL)


def iter_note_files() -> list[Path]:
    files: list[Path] = []
    for directory in NOTE_DIRECTORIES:
        files.extend(sorted((ROOT / directory).glob("*.md")))
    return files


def test_expected_files_exist() -> None:
    for directory, expected_names in EXPECTED_FILES.items():
        actual_names = {path.name for path in (ROOT / directory).glob("*.md")}
        assert actual_names == expected_names


def test_images_directories_exist() -> None:
    for directory in NOTE_DIRECTORIES:
        image_dir = ROOT / directory / "images"
        assert image_dir.is_dir()
        assert (image_dir / "README.md").exists()


def test_note_front_matter_and_headings() -> None:
    files = iter_note_files()
    assert len(files) == 22

    for note_file in files:
        content = note_file.read_text(encoding="utf-8")
        assert content.startswith("---\n"), note_file
        for key in FRONT_MATTER_KEYS:
            assert key in content, f"{note_file} missing {key}"
        for heading in REQUIRED_HEADINGS:
            assert heading in content, f"{note_file} missing {heading}"


def test_python_code_blocks_compile_and_run() -> None:
    for note_file in iter_note_files():
        content = note_file.read_text(encoding="utf-8")
        blocks = PYTHON_BLOCK_PATTERN.findall(content)
        assert blocks, f"{note_file} has no python code blocks"

        for block in blocks:
            namespace = {"__name__": "__markdown_example__"}
            code = compile(block, str(note_file), "exec")
            exec(code, namespace, namespace)
