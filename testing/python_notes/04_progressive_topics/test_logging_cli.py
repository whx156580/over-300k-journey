import pytest
import sys
import importlib.util
import json
import io
from pathlib import Path
from click.testing import CliRunner

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
target_file = current_dir / "logging_and_cli_automation.py"
mod = load_module_from_path("logging_automation", target_file)

def test_json_formatter():
    """验证日志输出为有效的 JSON"""
    logger = mod.setup_json_logging("test_json")
    
    # 捕获 stdout
    log_capture = io.StringIO()
    # 替换现有 handler 以指向我们的 StringIO
    for h in logger.handlers[:]:
        logger.removeHandler(h)
    
    handler = mod.logging.StreamHandler(log_capture)
    handler.setFormatter(mod.JsonFormatter())
    logger.addHandler(handler)
    
    logger.info("Hello JSON", extra={"env": "test"})
    
    output = log_capture.getvalue().strip()
    data = json.loads(output)
    
    assert data["message"] == "Hello JSON"
    assert data["level"] == "INFO"
    assert data["env"] == "test"
    assert "timestamp" in data

def test_run_command_success():
    """验证外部命令执行成功"""
    ok, out = mod.run_command([sys.executable, "-c", "print('ok')"])
    assert ok is True
    assert out == "ok"

def test_run_command_failure():
    """验证外部命令执行失败"""
    # 执行一个不存在的文件
    ok, out = mod.run_command([sys.executable, "-c", "import sys; sys.exit(1)"])
    assert ok is False

def test_run_command_timeout():
    """验证外部命令执行超时"""
    ok, out = mod.run_command([sys.executable, "-c", "import time; time.sleep(2)"], timeout=1)
    assert ok is False
    assert "timed out" in out

def test_click_cli_run():
    """验证 Click CLI 命令"""
    runner = CliRunner()
    result = runner.invoke(mod.cli, ["run", "--env", "dev"])
    assert result.exit_code == 0
    assert "Running in dev" in result.output
