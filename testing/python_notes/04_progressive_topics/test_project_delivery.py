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
target_file = current_dir / "project_delivery_and_engineering_practice.py"
mod = load_module_from_path("delivery_logic", target_file)

def test_release_readiness_pass():
    """验证质量门禁全通场景"""
    metrics = {"tests_passed": True, "coverage_pct": 90, "vulnerabilities": 0}
    assert mod.check_release_readiness(metrics) is True

def test_release_readiness_fail():
    """验证质量门禁拦截场景"""
    metrics = {"tests_passed": False, "coverage_pct": 85, "vulnerabilities": 1}
    assert mod.check_release_readiness(metrics) is False

def test_load_env_config_success():
    """验证环境变量加载成功"""
    env = {"DB_URL": "mysql://", "API_KEY": "secret"}
    config = mod.load_env_config(env)
    assert config["DB_URL"] == "mysql://"

def test_load_env_config_missing():
    """验证缺失环境变量时抛错"""
    with pytest.raises(EnvironmentError, match="Missing required environment variable"):
        mod.load_env_config({"DB_URL": "only"})

def test_performance_budget_check():
    """验证性能预算对比逻辑"""
    budget = {"p95": 100}
    assert mod.verify_performance_budget({"p95": 50}, budget) is True
    assert mod.verify_performance_budget({"p95": 150}, budget) is False
