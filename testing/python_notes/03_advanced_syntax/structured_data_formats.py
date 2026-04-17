import json
import csv
import io
from datetime import datetime
from decimal import Decimal
from typing import List, Dict, Any, Optional

# --- 示例 1: 扩展 JSON 编码器 ---

class CustomEncoder(json.JSONEncoder):
    def default(self, obj: Any) -> Any:
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return str(obj)
        return super().default(obj)

def serialize_complex_data(data: Dict[str, Any]) -> str:
    """使用自定义编码器进行序列化"""
    return json.dumps(data, cls=CustomEncoder, ensure_ascii=False)

# --- 示例 2: CSV 转换逻辑 ---

def parse_csv_to_dicts(csv_text: str) -> List[Dict[str, str]]:
    """将 CSV 文本解析为字典列表"""
    f = io.StringIO(csv_text.strip())
    reader = csv.DictReader(f)
    return list(reader)

# --- 示例 3: 结构化转换 (CSV -> JSON) ---

def convert_flat_to_nested(flat_data: List[Dict[str, Any]], group_key: str) -> Dict[str, List[Dict[str, Any]]]:
    """将扁平数据按指定键组织为嵌套结构"""
    nested: Dict[str, List[Any]] = {}
    for item in flat_data:
        val = item.pop(group_key, "Other")
        if val not in nested:
            nested[val] = []
        nested[val].append(item)
    return nested

if __name__ == "__main__":
    # 验证 JSON
    print(serialize_complex_data({"t": datetime.now(), "d": Decimal("1.1")}))
    
    # 验证 CSV
    raw_csv = "id,status\n1,PASS\n2,FAIL"
    print(f"CSV Parsed: {parse_csv_to_dicts(raw_csv)}")
