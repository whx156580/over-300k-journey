from dataclasses import dataclass, field, asdict
from enum import Enum, auto
from typing import List, Dict, Any, Optional

# --- 示例 1: 状态枚举 ---

class RunStatus(Enum):
    PENDING = auto()
    RUNNING = auto()
    PASSED = auto()
    FAILED = auto()

# --- 示例 2: 结构化数据模型 ---

@dataclass(frozen=True)
class CaseMeta:
    """不可变元数据"""
    id: int
    author: str

@dataclass
class TestResult:
    """带后置处理的数据类"""
    meta: CaseMeta
    status: RunStatus = RunStatus.PENDING
    tags: List[str] = field(default_factory=list)
    duration: float = 0.0

    def __post_init__(self):
        # 自动校验耗时
        if self.duration < 0:
            raise ValueError("Duration cannot be negative")

# --- 示例 3: 业务模型转换 ---

def result_to_json_ready(res: TestResult) -> Dict[str, Any]:
    """
    将数据类转换为可 JSON 序列化的字典。
    注意：Enum 需要特殊处理。
    """
    data = asdict(res)
    # 将 Enum 对象转换为字符串值
    data["status"] = res.status.name
    return data

if __name__ == "__main__":
    meta = CaseMeta(1, "QA")
    res = TestResult(meta=meta, status=RunStatus.PASSED, duration=1.5)
    
    print(f"Result: {res}")
    print(f"JSON Ready: {result_to_json_ready(res)}")
