import re
from typing import Optional, Any, Tuple

# --- 示例 1: 海象运算符与链式比较 ---

def extract_and_validate_score(text: str) -> Optional[int]:
    """
    演示海象运算符在条件语句中的应用。
    """
    if (match := re.search(r"score:(\d+)", text)):
        score = int(match.group(1))
        # 链式比较：优雅且高效
        if 0 <= score <= 100:
            return score
    return None

# --- 示例 2: 逻辑短路保护 ---

class MockUser:
    def __init__(self, name: str):
        self.name = name

def get_username(user: Optional[MockUser]) -> str:
    """
    演示利用 and 短路保护 None 访问，利用 or 设置默认值。
    """
    # 逻辑：如果 user 为 None，则 (user and user.name) 为 None
    # 随后 None or "Guest" 得到 "Guest"
    return (user and user.name) or "Guest"

# --- 示例 3: 位运算权限 ---

def toggle_permission(current: int, mask: int) -> int:
    """
    利用异或 (XOR) 翻转特定权限位。
    """
    return current ^ mask

if __name__ == "__main__":
    print(f"Score extracted: {extract_and_validate_score('test score:95')}")
    print(f"User Name: {get_username(MockUser('Alice'))}")
    print(f"Guest Name: {get_username(None)}")
    
    READ, WRITE = 0b01, 0b10
    perm = READ
    perm = toggle_permission(perm, WRITE)
    print(f"New Perm: {bin(perm)}") # 0b11
