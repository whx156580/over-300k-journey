import pytest
import sys
import importlib.util
from pathlib import Path
from unittest.mock import MagicMock

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
target_file = current_dir / "redis_celery_and_background_jobs.py"
mod = load_module_from_path("job_logic", target_file)

@pytest.fixture
def mock_redis():
    client = MagicMock()
    # 模拟存储字典
    store = {}
    
    def set_mock(name, value, nx=False, ex=None):
        if nx and name in store:
            return False
        store[name] = value
        return True
        
    def delete_mock(name):
        store.pop(name, None)
        
    def exists_mock(name):
        return 1 if name in store else 0
        
    client.set.side_effect = set_mock
    client.delete.side_effect = delete_mock
    client.exists.side_effect = exists_mock
    return client

def test_acquire_lock_success(mock_redis):
    """验证成功获取锁"""
    assert mod.try_acquire_lock(mock_redis, "test_key") is True
    # 再次获取应失败 (nx=True)
    assert mod.try_acquire_lock(mock_redis, "test_key") is False

def test_release_lock_logic(mock_redis):
    """验证释放锁逻辑"""
    mod.try_acquire_lock(mock_redis, "key2")
    mod.release_lock(mock_redis, "key2")
    # 释放后应能再次获取
    assert mod.try_acquire_lock(mock_redis, "key2") is True

def test_task_idempotency_logic(mock_redis):
    """验证幂等性校验逻辑"""
    tid = "task_123"
    assert mod.is_task_processed(mock_redis, tid) is False
    mod.mark_task_as_processed(mock_redis, tid)
    assert mod.is_task_processed(mock_redis, tid) is True

def test_process_background_job_logic():
    """验证后台任务处理逻辑"""
    res = mod.process_background_job({"id": "B-456"})
    assert "B-456" in res
    assert "Success" in res
