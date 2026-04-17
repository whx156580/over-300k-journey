import contextlib
from typing import List, Any

# --- 示例 1: 自定义异常体系与 raise from ---

class AppError(Exception):
    """应用级异常基类"""
    pass

class DatabaseError(AppError):
    """数据库操作异常"""
    pass

def query_user(user_id: int) -> str:
    """模拟查询用户，展示异常链"""
    try:
        # 模拟底层连接失败
        if user_id < 0:
            raise ConnectionError("Invalid database port or timeout")
        return f"User_{user_id}"
    except ConnectionError as e:
        # 显式建立异常链，保留原始错误 e
        raise DatabaseError(f"Failed to fetch user {user_id}") from e

# --- 示例 2: 异常上下文管理器 ---

@contextlib.contextmanager
def assert_raises(expected_exc: type):
    """
    一个简单的断言上下文管理器，模拟 pytest.raises。
    """
    try:
        yield
    except expected_exc:
        # 捕获到了预期的异常，正常结束
        pass
    else:
        # 没有抛出异常，触发断言失败
        raise AssertionError(f"Did not raise {expected_exc.__name__}")

# --- 示例 3: 异常组处理 (Python 3.11+ 逻辑模拟) ---

def handle_multiple_errors() -> List[str]:
    """模拟处理多个并发异常的逻辑"""
    errors = []
    # 模拟捕获到的异常列表
    excs = [ValueError("Bad ID"), TypeError("Bad Type")]
    for e in excs:
        errors.append(f"Caught: {type(e).__name__} - {e}")
    return errors

if __name__ == "__main__":
    # 验证异常链
    try:
        query_user(-1)
    except DatabaseError as err:
        print(f"Captured: {err}")
        print(f"Cause: {err.__cause__}")

    # 验证上下文管理器
    with assert_raises(ValueError):
        int("abc")
    print("Context manager test passed.")
