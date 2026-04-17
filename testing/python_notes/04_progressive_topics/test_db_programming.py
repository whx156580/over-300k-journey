import pytest
import sys
import importlib.util
import sqlite3
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
target_file = current_dir / "python_database_programming.py"
mod = load_module_from_path("db_logic", target_file)

DB_PATH = ":memory:"

def test_get_user_by_id():
    """验证参数化查询与字典化结果"""
    user = mod.get_user_by_id(DB_PATH, 1)
    assert user is not None
    assert user["name"] == "QA_User"
    assert mod.get_user_by_id(DB_PATH, 999) is None

def test_batch_insert_data():
    """验证 executemany 批量插入逻辑"""
    data = [(10,), (20,), (30,)]
    count = mod.batch_insert_data(DB_PATH, "metrics", data)
    assert count == 3

def test_transfer_funds_success():
    """验证事务提交逻辑"""
    # 由于是 :memory:，每次都是新库
    assert mod.transfer_funds(DB_PATH, 1, 2, 30) is True

def test_transfer_funds_rollback():
    """验证异常回滚逻辑"""
    # 模拟失败
    assert mod.transfer_funds(DB_PATH, 1, 2, 5000) is False
    
def test_sql_injection_defense_logic():
    """验证参数化查询的防御逻辑"""
    # 即使传入 SQL 注入片段，由于参数化，它会被当作纯字符串处理，不会报错
    user = mod.get_user_by_id(DB_PATH, "1 OR 1=1") # type: ignore
    assert user is None
