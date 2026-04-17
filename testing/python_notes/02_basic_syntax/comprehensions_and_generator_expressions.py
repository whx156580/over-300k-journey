import sys
from typing import List, Dict, Set, Generator

# --- 示例 1: 矩阵转置 ---

def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    使用嵌套推导式实现矩阵转置。
    外层列表推导式遍历列索引，内层遍历行。
    """
    if not matrix:
        return []
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# --- 示例 2: 条件映射推导式 ---

def build_grade_map(scores: Dict[str, int]) -> Dict[str, str]:
    """
    根据分值构建等级字典。
    演示 if-else 在推导式中的前置用法。
    """
    return {name: ("PASS" if score >= 60 else "FAIL") for name, score in scores.items()}

# --- 示例 3: 多级结构拍平 ---

def flatten_suites(suites: List[List[str]]) -> List[str]:
    """
    将二维列表拍平为一维。
    演示多重 for 循环推导式。
    """
    return [test for suite in suites for test in suite]

if __name__ == "__main__":
    # 验证矩阵转置
    m = [[1, 2], [3, 4]]
    print(f"Transposed: {transpose_matrix(m)}")
    
    # 验证等级映射
    s = {"Alice": 80, "Bob": 50}
    print(f"Grades: {build_grade_map(s)}")
    
    # 验证拍平
    ts = [["a", "b"], ["c"]]
    print(f"Flattened: {flatten_suites(ts)}")
