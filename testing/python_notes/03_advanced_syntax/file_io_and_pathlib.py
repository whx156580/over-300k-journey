import shutil
from pathlib import Path
from typing import List, Optional

# --- 示例 1: 健壮的跨平台路径定位 ---

def get_data_file_path(filename: str) -> Path:
    """
    基于当前文件位置定位数据文件。
    """
    return Path(__file__).resolve().parent / "data" / filename

# --- 示例 2: 大文件流式处理 ---

def find_keywords_in_file(file_path: Path, keyword: str) -> List[int]:
    """
    流式读取文件，返回包含关键字的行号列表。
    """
    matches = []
    if not file_path.exists() or not file_path.is_file():
        return []
        
    with file_path.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            if keyword in line:
                matches.append(i)
    return matches

# --- 示例 3: 自动化目录管理 ---

def ensure_clean_dir(dir_path: Path) -> None:
    """
    确保目录存在且为空。
    """
    if dir_path.exists():
        shutil.rmtree(dir_path)
    dir_path.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    # 路径验证
    print(f"Target path: {get_data_file_path('test.txt')}")
    
    # 模拟文件处理
    temp_file = Path("temp_io_test.log")
    temp_file.write_text("line1\nERROR: something wrong\nline3", encoding="utf-8")
    print(f"Error lines: {find_keywords_in_file(temp_file, 'ERROR')}")
    temp_file.unlink() # 清理
