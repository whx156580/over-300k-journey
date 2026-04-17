from typing import Dict, List, Tuple

# --- 示例 1: 技能矩阵建模 ---

def get_skill_matrix() -> Dict[str, List[str]]:
    """返回核心岗位的技能矩阵"""
    return {
        "SDET": ["pytest", "playwright", "fastapi", "docker"],
        "Data_Scientist": ["pandas", "numpy", "pytorch", "matplotlib"],
        "DevOps": ["ansible", "terraform", "kubernetes", "python"]
    }

# --- 示例 2: 学习优先级算法 ---

def get_learning_priority(interest: float, market_demand: float) -> str:
    """
    基于兴趣和市场需求计算优先级。
    """
    score = (interest * 0.3) + (market_demand * 0.7)
    if score >= 0.8: return "P0 (Critical)"
    if score >= 0.5: return "P1 (High)"
    return "P2 (Low)"

# --- 示例 3: 生态分层表达 ---

def get_ecosystem_layers() -> List[Tuple[str, str]]:
    """展示 Python 生态的层次结构"""
    return [
        ("Core", "CPython, Memory Mgmt, GIL"),
        ("Standard Lib", "os, sys, json, collections"),
        ("Third-party", "requests, FastAPI, pandas")
    ]

if __name__ == "__main__":
    matrix = get_skill_matrix()
    print(f"SDET Skills: {matrix['SDET']}")
    
    print(f"Priority for AI study: {get_learning_priority(0.9, 0.95)}")
    
    for layer, content in get_ecosystem_layers():
        print(f"[{layer}]: {content}")
