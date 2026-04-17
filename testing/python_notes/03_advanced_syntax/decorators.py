import time
import random
from functools import wraps
from typing import Callable, Any, Dict

# --- 示例 1: 带参数的智能重试装饰器 ---

def retry(max_attempts: int = 3, delay: float = 0.1):
    """
    带参数的重试装饰器。
    实现原理: 指数退避 + 抖动。
    """
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise e
                    sleep_time = delay * (2 ** (attempts - 1)) + random.uniform(0, 0.05)
                    time.sleep(sleep_time)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.01)
def unstable_api(success_rate: float = 0.5):
    if random.random() > success_rate:
        raise ConnectionError("Network flaked")
    return "Success"

# --- 示例 2: 带状态的类装饰器 ---

class CallCounter:
    """
    类装饰器：记录函数被调用的总次数。
    """
    def __init__(self, func: Callable):
        wraps(func)(self)
        self.func = func
        self.count = 0

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.count += 1
        return self.func(*args, **kwargs)

@CallCounter
def process_data(data: str) -> str:
    return f"processed {data}"

# --- 示例 3: 装饰器链 ---

def bold(func: Callable):
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> str:
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func: Callable):
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> str:
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold
@italic
def greet(name: str) -> str:
    return f"Hello, {name}"

if __name__ == "__main__":
    # 验证重试
    try:
        print(f"API result: {unstable_api(success_rate=0.1)}")
    except ConnectionError:
        print("API failed after retries")

    # 验证计数
    process_data("A")
    process_data("B")
    print(f"Call count: {process_data.count}")

    # 验证装饰器链
    print(f"Styled greet: {greet('Alice')}")
    assert greet("Alice") == "<b><i>Hello, Alice</i></b>"
