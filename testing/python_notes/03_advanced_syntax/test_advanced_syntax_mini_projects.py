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
target_file = current_dir / "advanced_syntax_mini_projects.py"
mod = load_module_from_path("advanced_lab_logic", target_file)

def test_parse_logs_logic():
    """验证日志解析与数据类生成"""
    lines = ["[DEBUG] trace 1", "[INFO] ok", "invalid line"]
    results = list(mod.parse_logs(lines))
    assert len(results) == 2
    assert results[0].level == "DEBUG"
    assert results[1].message == "ok"

def test_get_file_stats_logic(tmp_path):
    """验证文件分布统计"""
    (tmp_path / "a.txt").touch()
    (tmp_path / "b.TXT").touch()
    (tmp_path / "c.log").touch()
    
    stats = mod.get_file_stats(tmp_path)
    assert stats[".txt"] == 2
    assert stats[".log"] == 1

def test_merge_project_config_deep():
    """验证深层字典合并"""
    base = {"db": {"host": "localhost", "port": 3306}, "debug": False}
    over = {"db": {"host": "prod_db"}, "debug": True}
    res = mod.merge_project_config(base, over)
    
    assert res["db"]["host"] == "prod_db"
    assert res["db"]["port"] == 3306
    assert res["debug"] is True

def test_log_entry_dataclass():
    """验证数据类属性访问"""
    entry = mod.LogEntry(level="INFO", message="msg")
    assert entry.level == "INFO"
    assert entry.message == "msg"
