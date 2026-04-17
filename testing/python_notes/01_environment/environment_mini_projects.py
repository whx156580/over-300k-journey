import sys
import platform
import json
import importlib.util
from pathlib import Path
from typing import Dict, Any

# --- 项目 1: Python Doctor 核心实现 ---

def get_env_report() -> Dict[str, Any]:
    """
    收集当前环境的关键诊断指标。
    """
    return {
        "python_ver": sys.version.split()[0],
        "is_venv": sys.prefix != getattr(sys, "base_prefix", sys.prefix),
        "os": platform.system(),
        "cwd": str(Path.cwd()),
        "pytest_installed": importlib.util.find_spec("pytest") is not None
    }

# --- 项目 2: 自动化配置初始化 ---

def bootstrap_vscode_settings(project_root: Path) -> Path:
    """
    为指定项目根目录生成 .vscode 配置。
    """
    vscode_dir = project_root / ".vscode"
    vscode_dir.mkdir(parents=True, exist_ok=True)
    
    settings_file = vscode_dir / "settings.json"
    settings = {
        "python.analysis.typeCheckingMode": "basic",
        "editor.formatOnSave": True
    }
    
    with open(settings_file, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4)
    
    return settings_file

if __name__ == "__main__":
    # 打印环境报告
    report = get_env_report()
    print("--- Environment Report ---")
    for k, v in report.items():
        print(f"{k:<18}: {v}")
    
    # 演示初始化
    # bootstrap_vscode_settings(Path.cwd())
