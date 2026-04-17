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
target_file = current_dir / "file_io_and_pathlib.py"
mod = load_module_from_path("file_io_logic", target_file)

def test_get_data_file_path_logic():
    """验证路径拼接逻辑"""
    path = mod.get_data_file_path("config.json")
    assert path.name == "config.json"
    assert path.parent.name == "data"

def test_find_keywords_in_file_success(tmp_path):
    """验证关键字流式搜索逻辑"""
    test_file = tmp_path / "test.log"
    test_file.write_text("info\nerror_here\nok\nerror_again", encoding="utf-8")
    
    matches = mod.find_keywords_in_file(test_file, "error")
    assert matches == [2, 4]

def test_find_keywords_missing_file():
    """验证不存在文件的情况"""
    assert mod.find_keywords_in_file(Path("none.txt"), "abc") == []

def test_ensure_clean_dir_logic(tmp_path):
    """验证目录清理与重建逻辑"""
    sub_dir = tmp_path / "artifacts"
    sub_dir.mkdir()
    (sub_dir / "old.txt").write_text("old")
    
    mod.ensure_clean_dir(sub_dir)
    assert sub_dir.exists()
    assert len(list(sub_dir.iterdir())) == 0

def test_path_exists_is_file_logic(tmp_path):
    """验证 pathlib 的基础属性检查"""
    f = tmp_path / "f.txt"
    f.touch()
    assert f.exists()
    assert f.is_file()
    assert tmp_path.is_dir()
