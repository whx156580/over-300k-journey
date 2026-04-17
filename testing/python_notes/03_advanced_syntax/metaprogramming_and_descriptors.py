import threading
from typing import Any, Dict, Type

# --- 示例 1: 线程安全单例元类 ---

class SingletonMeta(type):
    """
    线程安全的单例元类。
    实现原理: 使用双重检查锁定 (Double-Checked Locking) 确保多线程安全。
    """
    _instances: Dict[Type[Any], Any] = {}
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    # super().__call__ 会调用 cls.__new__ 和 cls.__init__
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.connected = True

# --- 示例 2: 描述符协议实现属性校验 ---

class IntegerField:
    """
    数据描述符：强制要求属性为整数且满足最小值约束。
    """
    def __init__(self, min_val: int = 0) -> None:
        self.min_val = min_val
        self.storage_name = ""

    def __set_name__(self, owner: Any, name: str) -> None:
        # 自动绑定实例属性名，如 price -> _price
        self.storage_name = f"_{name}"

    def __get__(self, instance: Any, owner: Any) -> Any:
        if instance is None:
            return self
        return getattr(instance, self.storage_name, None)

    def __set__(self, instance: Any, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"Expected int, got {type(value).__name__}")
        if value < self.min_val:
            raise ValueError(f"Value must be >= {self.min_val}")
        setattr(instance, self.storage_name, value)

class Product:
    price = IntegerField(min_val=1)
    stock = IntegerField(min_val=0)

    def __init__(self, price: int, stock: int) -> None:
        self.price = price
        self.stock = stock

# --- 示例 3: 插件注册元类 ---

class PluginRegistry(type):
    """
    自动注册子类的元类。
    """
    registry: Dict[str, Type['BasePlugin']] = {}

    def __new__(mcs, name: str, bases: tuple, attrs: Dict[str, Any]) -> Any:
        cls = super().__new__(mcs, name, bases, attrs)
        if name != "BasePlugin":
            mcs.registry[name.lower()] = cls
        return cls

class BasePlugin(metaclass=PluginRegistry):
    pass

class HttpPlugin(BasePlugin):
    pass

class SshPlugin(BasePlugin):
    pass

if __name__ == "__main__":
    # 验证单例
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    assert db1 is db2
    print("Singleton verification passed.")

    # 验证描述符
    p = Product(100, 50)
    assert p.price == 100
    try:
        p.price = -1
    except ValueError as e:
        print(f"Descriptor validation caught error: {e}")

    # 验证注册器
    print(f"Registered plugins: {list(PluginRegistry.registry.keys())}")
    assert "httpplugin" in PluginRegistry.registry
