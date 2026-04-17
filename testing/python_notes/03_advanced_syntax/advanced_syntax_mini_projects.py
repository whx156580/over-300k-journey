import re
from dataclasses import dataclass
from pathlib import Path
from typing import Generator, Dict, List, Any

# --- 项目 1: Log Inspector ---

@dataclass
class LogEntry:
    level: str
    message: str

def parse_logs(lines: List[str]) -> Generator[LogEntry, None, None]:
    """
    解析原始日志行。
    """
    pattern = re.compile(r"\[(?P<level>\w+)\]\s+(?P<message>.*)")
    for line in lines:
        if (match := pattern.search(line)):
            yield LogEntry(**match.groupdict())

# --- 项目 2: Disk Auditor ---

def get_file_stats(root_path: Path) -> Dict[str, int]:
    """
    统计文件扩展名分布。
    """
    stats = {}
    for item in root_path.rglob("*"):
        if item.is_file():
            ext = item.suffix.lower() or ".none"
            stats[ext] = stats.get(ext, 0) + 1
    return stats

# --- 项目 3: Config Merger ---

def merge_project_config(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    """
    合并配置字典。
    """
    result = base.copy()
    for k, v in override.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = merge_project_config(result[k], v)
        else:
            result[k] = v
    return result

if __name__ == "__main__":
    # 演示 1
    logs = ["[INFO] Boot", "[ERROR] Fail"]
    print(f"Parsed Logs: {list(parse_logs(logs))}")
    
    # 演示 2
    print(f"Current Stats: {get_file_stats(Path.cwd())}")
    
    # 演示 3
    c1 = {"a": 1, "nested": {"x": 10}}
    c2 = {"nested": {"y": 20}}
    print(f"Merged Config: {merge_project_config(c1, c2)}")
