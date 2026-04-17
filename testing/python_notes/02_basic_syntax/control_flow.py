import time
import random
import sys
from typing import List, Dict, Any, Tuple

# --- 示例 1: 智能轮询与 while-else ---

def poll_task_status(max_retries: int = 3) -> str:
    """
    演示 while-else：如果循环因条件变为假而结束（未触发 break），则执行 else。
    """
    retries = 0
    while retries < max_retries:
        # 模拟成功率 30%
        if random.random() < 0.3:
            return "SUCCESS"
        retries += 1
    else:
        # 仅在循环自然结束（即达到最大重试次数）时运行
        return "TIMEOUT"

# --- 示例 2: 结构化模式匹配 (Logic 模拟，兼容 3.8+) ---

def handle_api_response_compat(response: Dict[str, Any]) -> str:
    """
    模拟 match-case 逻辑，确保 3.8+ 兼容性。
    """
    status = response.get("status")
    
    if status == 200 and "data" in response:
        return f"Success with: {response['data']}"
    elif status in (401, 403):
        return "Auth Error: Access Denied"
    elif isinstance(status, int) and status >= 500:
        return f"Server Error: {status}"
    else:
        return "Unknown Response Format"

# --- 示例 3: 矩阵过滤与循环控制 ---

def filter_test_matrix(envs: List[str], cases: List[str]) -> List[str]:
    """
    演示 continue 与 break 的组合。
    """
    results = []
    for env in envs:
        if env == "prod":
            continue # 生产环境跳过
            
        for case in cases:
            if env == "dev" and case == "perf":
                break # 开发环境不跑性能测试
            results.append(f"{env}_{case}")
            
    return results

if __name__ == "__main__":
    # 验证轮询
    print(f"Poll result: {poll_task_status()}")
    
    # 验证响应处理
    print(handle_api_response_compat({"status": 200, "data": "OK"}))
    
    # 验证矩阵
    print(f"Matrix: {filter_test_matrix(['dev', 'prod'], ['smoke', 'perf'])}")
