import pytest
import sys
import importlib.util
from pathlib import Path
from unittest.mock import patch

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
target_file = current_dir / "decorators.py"
mod = load_module_from_path("decorators", target_file)

def test_retry_success():
    """验证重试装饰器在最终成功时返回结果"""
    call_count = 0
    
    @mod.retry(max_attempts=3, delay=0.01)
    def test_func():
        nonlocal call_count
        call_count += 1
        if call_count < 2:
            raise ValueError("Fail")
        return "OK"
    
    assert test_func() == "OK"
    assert call_count == 2

def test_retry_failure():
    """验证重试装饰器在达到最大次数后抛出异常"""
    call_count = 0
    
    @mod.retry(max_attempts=3, delay=0.01)
    def test_func():
        nonlocal call_count
        call_count += 1
        raise ValueError("Constant Fail")
    
    with pytest.raises(ValueError, match="Constant Fail"):
        test_func()
    assert call_count == 3

def test_call_counter():
    """验证类装饰器计数功能"""
    # 重新定义一个被装饰函数以重置计数
    @mod.CallCounter
    def counted_func():
        return True
        
    assert counted_func.count == 0
    counted_func()
    counted_func()
    assert counted_func.count == 2
    assert counted_func.__name__ == "counted_func"

def test_decorator_chain():
    """验证装饰器链的执行顺序和元信息保留"""
    @mod.bold
    @mod.italic
    def styled_func(text):
        return text
        
    assert styled_func("hello") == "<b><i>hello</i></b>"
    assert styled_func.__name__ == "styled_func"

def test_unstable_api_usage():
    """验证模块中预定义的 unstable_api 示例"""
    # 简单调用，确保不崩溃
    try:
        mod.unstable_api(success_rate=1.0)
    except Exception:
        pytest.fail("unstable_api(1.0) should not fail")

def test_process_data_usage():
    """验证模块中预定义的 process_data 示例"""
    assert mod.process_data("test") == "processed test"

def test_greet_usage():
    """验证模块中预定义的 greet 示例"""
    assert mod.greet("World") == "<b><i>Hello, World</i></b>"

def test_retry_delay_with_jitter():
    """验证重试延迟逻辑（通过 mock time.sleep）"""
    with patch("time.sleep") as mock_sleep:
        @mod.retry(max_attempts=2, delay=1.0)
        def fail_once():
            raise ValueError("Fail")
            
        with pytest.raises(ValueError):
            fail_once()
            
        # 应该调用了一次 sleep
        assert mock_sleep.call_count == 1
        # 检查延迟是否大致符合指数退避 (1.0 * 2^0 = 1.0)
        args, _ = mock_sleep.call_args
        assert 1.0 <= args[0] <= 1.06
