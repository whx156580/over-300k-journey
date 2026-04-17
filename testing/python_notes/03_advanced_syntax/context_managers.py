from contextlib import contextmanager
from typing import Any, Dict, Optional, Type

# --- 示例 1: 类驱动的资源管理器 ---

class MockBrowser:
    """模拟浏览器资源启停"""
    def __init__(self, name: str):
        self.name = name
        self.is_open = False

    def __enter__(self) -> 'MockBrowser':
        self.is_open = True
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]], 
                 exc_val: Optional[BaseException], 
                 exc_tb: Any) -> bool:
        self.is_open = False
        # 返回 False 表示不吞掉异常
        return False

# --- 示例 2: 生成器驱动的状态管理 ---

@contextmanager
def temporary_config(settings: Dict[str, Any], key: str, value: Any):
    """
    临时覆盖字典配置。
    """
    original_value = settings.get(key)
    settings[key] = value
    try:
        yield settings
    finally:
        # 确保即便报错也能还原
        settings[key] = original_value

# --- 示例 3: 异常压制器 ---

class SuppressError:
    """有选择地忽略特定异常"""
    def __init__(self, error_type: Type[Exception]):
        self.error_type = error_type

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type is not None and issubclass(exc_type, self.error_type)

if __name__ == "__main__":
    # 验证浏览器管理器
    with MockBrowser("Chrome") as b:
        print(f"Browser {b.name} open? {b.is_open}")
    print(f"Browser closed? {not b.is_open}")
    
    # 验证配置切换
    conf = {"env": "prod"}
    with temporary_config(conf, "env", "test"):
        print(f"Inside with: {conf['env']}")
    print(f"Outside with: {conf['env']}")
