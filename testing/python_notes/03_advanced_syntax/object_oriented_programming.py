from abc import ABC, abstractmethod
from typing import List, Any

# --- 示例 1: 多继承与 MRO ---

class Base:
    def action(self) -> None:
        pass

class Left(Base):
    def action(self) -> None:
        super().action()

class Right(Base):
    def action(self) -> None:
        super().action()

class Child(Left, Right):
    def action(self) -> None:
        super().action()

# --- 示例 2: 抽象基类与 POM ---

class BasePage(ABC):
    def __init__(self, driver: Any) -> None:
        self.driver = driver

    @abstractmethod
    def is_loaded(self) -> bool:
        pass

    def open(self, url: str) -> None:
        if not self.is_loaded():
            raise RuntimeError("Load failed")

class LoginPage(BasePage):
    def is_loaded(self) -> bool:
        return True

# --- 示例 3: __slots__ 内存优化 ---

class Measurement:
    __slots__ = ("timestamp", "value", "unit")
    def __init__(self, ts: int, val: float, unit: str) -> None:
        self.timestamp = ts
        self.value = val
        self.unit = unit

if __name__ == "__main__":
    # 验证 MRO
    print(f"MRO: {[c.__name__ for c in Child.mro()]}")
    
    # 验证 POM
    lp = LoginPage(None)
    lp.open("http://test.com")
    
    # 验证 slots
    m = Measurement(100, 20.0, "m")
    try:
        m.extra = "error" # type: ignore
    except AttributeError:
        print("Slots blocked dynamic attribute.")
