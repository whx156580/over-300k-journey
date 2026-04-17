import io
from typing import List, Optional

# --- 示例 1: 健壮的文本与字节转换 ---

def safe_decode(payload: bytes, encodings: Optional[List[str]] = None) -> str:
    """
    尝试多种编码进行解码。
    """
    if encodings is None:
        encodings = ["utf-8", "gbk", "latin-1"]
        
    for enc in encodings:
        try:
            return payload.decode(enc)
        except UnicodeDecodeError:
            continue
    return payload.decode("utf-8", errors="replace")

# --- 示例 2: 二进制流操作 ---

def process_binary_header(data: bytes) -> str:
    """
    解析二进制头部并返回十六进制表示。
    """
    buffer = io.BytesIO(data)
    # 读取前 4 字节
    header = buffer.read(4)
    return header.hex().upper()

# --- 示例 3: 编码转换 ---

def convert_encoding(payload: bytes, from_enc: str, to_enc: str) -> bytes:
    """
    将字节流从一种编码转换为另一种编码。
    """
    text = payload.decode(from_enc)
    return text.encode(to_enc)

if __name__ == "__main__":
    # 验证安全解码
    utf8_bytes = "你好".encode("utf-8")
    gbk_bytes = "你好".encode("gbk")
    print(f"UTF-8: {safe_decode(utf8_bytes)}")
    print(f"GBK:   {safe_decode(gbk_bytes)}")
    
    # 验证二进制处理
    # 修复：f-string 表达式中不能含反斜杠，先提取为变量
    png_header = b'\x89PNG\r\n'
    print(f"Header: {process_binary_header(png_header)}")
