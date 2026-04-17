from typing import List

# --- 示例 1: f-string 高级格式化 ---

def format_test_summary(name: str, passed: int, duration: float) -> str:
    """
    格式化测试摘要，演示对齐和精度控制。
    """
    return f"Case: {name:<15} | Status: {passed:>5} | Time: {duration:.2f}s"

# --- 示例 2: 路径处理与 Raw String ---

def get_filename_from_path(path: str) -> str:
    """
    从路径中提取文件名。演示 raw string 处理 Windows 路径。
    """
    # 统一使用 \ 分割（针对 Windows 风格）
    parts = path.split("\\")
    return parts[-1]

# --- 示例 3: 高效拼接 ---

def join_logs(lines: List[str]) -> str:
    """
    最佳实践：使用 .join() 拼接大量字符串。
    """
    return "\n".join(lines)

if __name__ == "__main__":
    # 验证格式化
    print(format_test_summary("Login", 1, 0.1234))
    
    # 验证路径
    win_p = r"C:\temp\test_file.txt"
    print(f"File: {get_filename_from_path(win_p)}")
    
    # 验证拼接
    print(f"Log:\n{join_logs(['Line1', 'Line2'])}")
