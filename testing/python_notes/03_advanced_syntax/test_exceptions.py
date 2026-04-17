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
target_file = current_dir / "exceptions.py"
mod = load_module_from_path("exceptions", target_file)

def test_exception_chaining():
    """验证 raise from 保留原始异常链"""
    with pytest.raises(mod.DatabaseError) as exc_info:
        mod.query_user(-1)
    
    assert "Failed to fetch user -1" in str(exc_info.value)
    # 验证 __cause__ 是否为原始 ConnectionError
    assert isinstance(exc_info.value.__cause__, ConnectionError)

def test_query_user_success():
    """验证正常路径"""
    assert mod.query_user(10) == "User_10"

def test_assert_raises_success():
    """验证自定义上下文管理器捕获异常成功"""
    with mod.assert_raises(ValueError):
        int("not_a_number")

def test_assert_raises_failure():
    """验证自定义上下文管理器在未抛出异常时报错"""
    with pytest.raises(AssertionError, match="Did not raise ValueError"):
        with mod.assert_raises(ValueError):
            int("123")

def test_multiple_errors_logic():
    """验证多错误处理逻辑"""
    results = mod.handle_multiple_errors()
    assert len(results) == 2
    assert "ValueError" in results[0]
    assert "TypeError" in results[1]
