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
target_file = current_dir / "control_flow.py"
mod = load_module_from_path("control_logic", target_file)

def test_poll_task_status():
    """验证 while-else 逻辑结果"""
    res = mod.poll_task_status(max_retries=10)
    assert res in ("SUCCESS", "TIMEOUT")

def test_handle_api_response_logic():
    """验证 API 响应分发逻辑"""
    assert "Success" in mod.handle_api_response_compat({"status": 200, "data": "OK"})
    assert "Auth Error" in mod.handle_api_response_compat({"status": 401})
    assert "Server Error" in mod.handle_api_response_compat({"status": 503})
    assert "Unknown" in mod.handle_api_response_compat({"status": 404})

def test_filter_test_matrix():
    """验证 continue/break 矩阵过滤逻辑"""
    envs = ["dev", "prod"]
    cases = ["smoke", "perf"]
    # dev 不跑 perf, prod 全跳过
    res = mod.filter_test_matrix(envs, cases)
    assert res == ["dev_smoke"]
    assert "prod_smoke" not in res
    assert "dev_perf" not in res

def test_match_case_syntax_compatibility():
    """仅在 Python 3.10+ 环境下验证 match-case 语法"""
    if sys.version_info >= (3, 10):
        code = """
def check(val):
    match val:
        case 1: return "one"
        case _: return "other"
        """
        namespace = {}
        exec(code, namespace)
        assert namespace["check"](1) == "one"
        assert namespace["check"](2) == "other"

def test_truthy_values():
    """验证 Python 中的真值测试逻辑"""
    assert not []
    assert not {}
    assert not 0
    assert not None
    assert [1]
    assert " " # 空格字符串为真
