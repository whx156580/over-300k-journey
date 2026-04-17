import pytest
import sys
import importlib.util
from pathlib import Path

# 确保项目根目录在路径中
ROOT = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(ROOT))

def load_module_from_path(module_name: str, file_path: Path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module
    raise ImportError(f"Could not load module {module_name} at {file_path}")

# 加载目标模块
current_dir = Path(__file__).resolve().parent
target_file = current_dir / "basic_syntax_mini_projects.py"
mod = load_module_from_path("basics_lab_logic", target_file)

def test_analyze_expenses_logic():
    """验证费用汇总逻辑"""
    records = [
        {"category": "food", "amount": 10},
        {"category": "food", "amount": 20},
        {"category": "tech", "amount": 100}
    ]
    res = mod.analyze_expenses(records)
    assert res["total"] == 130
    assert res["avg"] == 130 / 3
    assert res["by_category"]["food"] == 30

def test_analyze_expenses_empty():
    """验证空数据处理"""
    assert mod.analyze_expenses([])["total"] == 0

def test_rename_preview_logic():
    """验证重命名预览转换"""
    names = ["  Data Report.CSV  "]
    preview = mod.get_rename_preview(names)
    assert preview[0][1] == "data_report.csv"

def test_score_quiz_full_marks():
    """验证满分场景"""
    keys = {1: "A", 2: "B"}
    student = {1: "A", 2: "B"}
    res = mod.score_quiz(keys, student)
    assert res["score"] == 2
    assert res["grade"] == "A"
    assert not res["wrong_ids"]

def test_score_quiz_failure():
    """验证低分场景与错题记录"""
    keys = {1: "A", 2: "B", 3: "C"}
    student = {1: "B", 2: "B", 3: "D"}
    res = mod.score_quiz(keys, student)
    assert res["score"] == 1
    assert res["wrong_ids"] == [1, 3]
    assert res["grade"] == "C"
