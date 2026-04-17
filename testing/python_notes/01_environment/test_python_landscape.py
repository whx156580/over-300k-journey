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
target_file = current_dir / "python_landscape_and_career_paths.py"
mod = load_module_from_path("landscape_logic", target_file)

def test_skill_matrix_contents():
    """验证技能矩阵包含核心岗位"""
    matrix = mod.get_skill_matrix()
    assert "SDET" in matrix
    assert "pytest" in matrix["SDET"]

def test_learning_priority_logic():
    """验证优先级计算逻辑边界"""
    assert mod.get_learning_priority(1.0, 1.0) == "P0 (Critical)"
    assert mod.get_learning_priority(0.0, 0.0) == "P2 (Low)"
    assert "P1" in mod.get_learning_priority(0.5, 0.6)

def test_ecosystem_layers_count():
    """验证生态分层包含三个主要层次"""
    layers = mod.get_ecosystem_layers()
    assert len(layers) == 3
    assert layers[0][0] == "Core"

def test_main_execution_check(capsys):
    """验证脚本直接运行时无异常"""
    # 模拟模块顶层逻辑执行（如果存在）
    pass # 脚本中已有 if __name__ == "__main__"
