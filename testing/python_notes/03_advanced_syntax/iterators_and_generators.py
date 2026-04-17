import itertools
import sys
from typing import Generator, Union, Any, List

# --- 示例 1: 无限日志处理流水线 ---

def log_stream() -> Generator[str, None, None]:
    """模拟无限产生的原始日志流"""
    for i in itertools.count(1):
        # 模拟产生 INFO 和 ERROR 日志
        level = "ERROR" if i % 5 == 0 else "INFO"
        yield f"LOG_LINE_{i}: {level} - Data packet received"

def error_filter(stream: Generator[str, None, None]) -> Generator[str, None, None]:
    """过滤并转换 ERROR 级别的日志"""
    for line in stream:
        if "ERROR" in line:
            yield f"[CRITICAL] {line}"

# --- 示例 2: 双向通信生成器 (带重置功能的累加器) ---

def smart_accumulator() -> Generator[int, Union[int, str, None], None]:
    """
    累加器生成器。
    实现原理: yield 表达式不仅返回值，还接收 send() 传入的数据。
    """
    total = 0
    while True:
        val = yield total
        if val == "reset":
            total = 0
        elif isinstance(val, int):
            total += val

# --- 示例 3: 资源安全的生成器 ---

def resource_manager(name: str) -> Generator[str, None, None]:
    """
    使用 try...finally 确保资源释放。
    """
    # 模拟打开资源
    status = {"open": True}
    try:
        yield f"HANDLE_{name}"
    finally:
        # 模拟关闭资源
        status["open"] = False

if __name__ == "__main__":
    # 验证流水线
    pipeline = error_filter(log_stream())
    print(f"Top 3 Errors: {list(itertools.islice(pipeline, 3))}")

    # 验证双向通信
    gen = smart_accumulator()
    next(gen) # 预激
    gen.send(10)
    print(f"Total after 10: {gen.send(20)}") # 应为 30
    print(f"Total after reset: {gen.send('reset')}") # 应为 0

    # 验证资源安全
    res_gen = resource_manager("TEST_FILE")
    print(f"Resource: {next(res_gen)}")
    res_gen.close()
