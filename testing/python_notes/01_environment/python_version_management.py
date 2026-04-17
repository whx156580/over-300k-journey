import sys
from pathlib import Path
from typing import Dict, Any

# --- 示例 1: 跨平台环境自检 ---

def get_env_details() -> Dict[str, Any]:
    """
    自检并返回当前 Python 解释器详情。
    """
    is_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
    return {
        "version": sys.version.split()[0],
        "executable": sys.executable,
        "is_venv": is_venv,
        "prefix": sys.prefix,
        "base_prefix": getattr(sys, "base_prefix", sys.prefix),
        "platform": sys.platform
    }

# --- 示例 2: 虚拟环境安全检查 ---

def is_safe_to_run() -> bool:
    """
    检查是否运行在虚拟环境中，返回布尔值。
    """
    # 逻辑：prefix 必须不同于 base_prefix (PEP 405)
    return sys.prefix != getattr(sys, "base_prefix", sys.prefix)

# --- 示例 3: 模拟路径清理逻辑 ---

def get_venv_path(name: str = ".venv") -> Path:
    """
    根据名称返回虚拟环境路径。
    """
    return Path.cwd() / name

if __name__ == "__main__":
    details = get_env_details()
    print("Python Environment Details:")
    for k, v in details.items():
        print(f"  {k:<12}: {v}")
    
    print(f"\nSafe to run (in venv)? {is_safe_to_run()}")
