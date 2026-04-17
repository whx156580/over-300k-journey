from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
STAGE_DIRECTORIES = {
    "01_environment": {
        "python_landscape_and_career_paths.md",
        "python_version_management.md",
        "dependency_management.md",
        "ide_setup.md",
        "environment_mini_projects.md",
    },
    "02_basic_syntax": {
        "comments_and_input_output.md",
        "variables_and_types.md",
        "operators_and_expressions.md",
        "control_flow.md",
        "strings_and_methods.md",
        "collections.md",
        "comprehensions_and_generator_expressions.md",
        "slicing_unpacking_and_common_builtins.md",
        "mutability_and_copying.md",
        "function_basics.md",
        "basic_syntax_mini_projects.md",
    },
    "03_advanced_syntax": {
        "modules_and_packages.md",
        "iterators_and_generators.md",
        "functional_programming_and_recursion.md",
        "decorators.md",
        "context_managers.md",
        "file_io_and_pathlib.md",
        "structured_data_formats.md",
        "dataclasses_and_enum.md",
        "bytes_encoding_and_text_files.md",
        "object_oriented_programming.md",
        "exceptions.md",
        "breakpoint_and_pdb_basics.md",
        "advanced_syntax_mini_projects.md",
        "metaprogramming_and_descriptors.md",
    },
    "04_progressive_topics": {
        "python_re.md",
        "python_keywords.md",
        "standard_library_toolbox.md",
        "configuration_and_secrets_management.md",
        "python_security_basics.md",
        "python_security_advanced.md",
        "debugging_and_troubleshooting.md",
        "common_python_pitfalls_checklist.md",
        "http_client_and_api_integration.md",
        "logging_and_cli_automation.md",
        "observability_logging_metrics_tracing.md",
        "linux_shell_for_python.md",
        "python_concurrency.md",
        "asyncio_advanced_patterns.md",
        "office_and_document_automation.md",
        "relational_databases_and_sql.md",
        "python_database_programming.md",
        "sqlalchemy_and_alembic.md",
        "web_frontend_and_http_basics.md",
        "web_frameworks_and_api_delivery.md",
        "fastapi_and_asgi_delivery.md",
        "fastapi_advanced_patterns.md",
        "redis_celery_and_background_jobs.md",
        "data_collection_and_browser_automation.md",
        "data_analysis_and_visualization.md",
        "machine_learning_basics.md",
        "python_profiling.md",
        "memory_profiling_tracemalloc_gc.md",
        "memory_management_and_gc.md",
        "type_hints_and_static_checking.md",
        "python_quality_toolchain.md",
        "modern_python_tooling_uv_pdm_hatch_nox.md",
        "testing_pyramid_and_pytest.md",
        "testing_engineering_advanced.md",
        "pytest_asyncio_and_property_based_testing.md",
        "packaging_and_publishing.md",
        "project_delivery_and_engineering_practice.md",
        "progressive_topics_integrated_projects.md",
        "testing_development_capstone_projects.md",
        "data_capstone_projects.md",
        "platform_tools_capstone_projects.md",
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
    for directory in STAGE_DIRECTORIES:
        stage_dir = ROOT / directory
        files.extend(sorted(path for path in stage_dir.rglob("*.md") if "images" not in path.parts))
    return files


def test_expected_files_exist() -> None:
    for directory, expected in STAGE_DIRECTORIES.items():
        actual_names = {path.name for path in (ROOT / directory).glob("*.md")}
        assert actual_names == expected


def test_images_directories_exist() -> None:
    for directory in STAGE_DIRECTORIES:
        image_dir = ROOT / directory / "images"
        assert image_dir.is_dir()
        assert (image_dir / "README.md").exists()


def test_note_front_matter_and_headings() -> None:
    files = iter_note_files()
    expected_count = sum(len(files) for files in STAGE_DIRECTORIES.values())
    assert len(files) == expected_count

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
            code = compile(block, str(note_file), "exec", dont_inherit=True)
            exec(code, namespace, namespace)
