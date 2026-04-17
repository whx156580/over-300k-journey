import importlib
import sys
from typing import Any, Optional

# --- 示例 1: 动态插件加载器 ---

def run_plugin_func(module_name: str, func_name: str, *args: Any) -> Any:
    """
    动态加载模块并执行函数。
    """
    try:
        module = importlib.import_module(module_name)
        func = getattr(module, func_name)
        return func(*args)
    except (ImportError, AttributeError) as e:
        return f"Error: {e}"

# --- 示例 2: 模块缓存查询 ---

def is_module_cached(module_name: str) -> bool:
    """
    检查模块是否已存在于 sys.modules 缓存中。
    """
    return module_name in sys.modules

# --- 示例 3: 模拟 API 暴露逻辑 ---

class InternalClient:
    def query(self): return "data"

# 模拟 __init__.py 的行为
__all__ = ["InternalClient"]

if __name__ == "__main__":
    # 验证动态导入
    print(f"JSON Output: {run_plugin_func('json', 'dumps', {'status': 'ok'})}")
    
    # 验证缓存
    import os
    print(f"Is 'os' cached? {is_module_cached('os')}")
