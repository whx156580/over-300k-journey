import logging
import json
import datetime
import click
import subprocess
import sys
from typing import Dict, Any, Tuple, Optional

# --- 示例 1: 结构化日志 (JSON Formatter) ---

class JsonFormatter(logging.Formatter):
    """
    自定义格式化器，将日志转换为 JSON。
    """
    def format(self, record: logging.LogRecord) -> str:
        log_entry = {
            "timestamp": datetime.datetime.fromtimestamp(record.created).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
        }
        # 如果有额外的 context 数据 (通过 extra 传入)
        if hasattr(record, "env"):
            log_entry["env"] = getattr(record, "env")
        if record.exc_info:
            log_entry["exc_info"] = self.formatException(record.exc_info)
        return json.dumps(log_entry)

def setup_json_logging(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    # 避免重复添加 handler
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(JsonFormatter())
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger

# --- 示例 2: Subprocess 安全封装 ---

def run_command(args: list, timeout: int = 10) -> Tuple[bool, str]:
    """
    安全执行外部命令。
    """
    try:
        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            check=True,
            timeout=timeout
        )
        return True, result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return False, e.stderr.strip()
    except subprocess.TimeoutExpired:
        return False, "Command timed out"

# --- 示例 3: Click CLI (定义部分，主入口在 __main__) ---

@click.group()
def cli():
    """迈向 30W+ 的测试自动化工具"""
    pass

@cli.command()
@click.option('--env', type=click.Choice(['dev', 'test']), default='test')
def run(env):
    """运行测试"""
    click.echo(f"Running in {env}")

if __name__ == "__main__":
    # 演示日志
    log = setup_json_logging("demo")
    log.info("App started", extra={"env": "dev"})
    
    # 演示命令执行
    ok, out = run_command([sys.executable, "--version"])
    if ok:
        print(f"Python version: {out}")
    
    # 运行 CLI
    # cli() # 交互式运行
