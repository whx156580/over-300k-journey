import re
from typing import Dict, List, Optional, Tuple

# --- 示例 1: 命名分组与日志解析 ---

def parse_structured_log(line: str) -> Optional[Dict[str, str]]:
    """
    使用命名分组解析日志行。
    """
    pattern = re.compile(
        r"\[(?P<level>\w+)\]\s+user=(?P<user>\w+)\s+action=(?P<action>\w+)"
    )
    match = pattern.search(line)
    return match.groupdict() if match else None

# --- 示例 2: 非贪婪匹配 ---

def extract_tags(html: str) -> List[str]:
    """
    使用非贪婪匹配提取 HTML 标签内容。
    """
    return re.findall(r"<div>(.*?)</div>", html)

# --- 示例 3: 零宽断言 ---

def extract_durations(text: str) -> List[str]:
    """
    匹配 'ms' 前的数字，但不包含 'ms'。
    """
    return re.findall(r"\d+(?=ms)", text)

if __name__ == "__main__":
    # 验证日志解析
    log = "[ERROR] user=admin action=login"
    print(f"Log Data: {parse_structured_log(log)}")
    
    # 验证标签提取
    html = "<div>A</div><div>B</div>"
    print(f"Tags: {extract_tags(html)}")
    
    # 验证断言
    metrics = "time: 100ms, cost: 200ms"
    print(f"Durations: {extract_durations(metrics)}")
