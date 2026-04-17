from typing import List, Dict, Any, Tuple

# --- 项目 1: Expense Tracker (数据汇总器) ---

def analyze_expenses(records: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    聚合消费数据，返回总额、平均值及分类统计。
    """
    if not records:
        return {"total": 0, "avg": 0, "by_category": {}}
    
    total = sum(r["amount"] for r in records)
    categories = {}
    for r in records:
        cat = r["category"]
        categories[cat] = categories.get(cat, 0) + r["amount"]
        
    return {
        "total": total,
        "avg": total / len(records),
        "by_category": categories
    }

# --- 项目 2: Filename Normalizer (文本处理器) ---

def get_rename_preview(filenames: List[str]) -> List[Tuple[str, str]]:
    """
    生成重命名预览：全小写，空格转下划线。
    """
    return [
        (old, old.strip().lower().replace(" ", "_"))
        for old in filenames
    ]

# --- 项目 3: Quiz Scorer (逻辑封装器) ---

def score_quiz(answers: Dict[int, str], student_submission: Dict[int, str]) -> Dict[str, Any]:
    """
    计算得分与错题。
    """
    correct_count = 0
    wrong_ids = []
    
    for q_id, correct_ans in answers.items():
        if student_submission.get(q_id) == correct_ans:
            correct_count += 1
        else:
            wrong_ids.append(q_id)
            
    score_rate = correct_count / len(answers) if answers else 0
    grade = "A" if score_rate >= 0.9 else "B" if score_rate >= 0.7 else "C"
    
    return {
        "score": correct_count,
        "wrong_ids": wrong_ids,
        "grade": grade
    }

if __name__ == "__main__":
    # 演示项目 1
    data = [{"category": "food", "amount": 50}, {"category": "rent", "amount": 1000}]
    print(f"Expense Analysis: {analyze_expenses(data)}")
    
    # 演示项目 2
    files = ["  Daily Report.pdf", "script.PY"]
    print(f"Rename Preview: {get_rename_preview(files)}")
    
    # 演示项目 3
    keys = {1: "A", 2: "B", 3: "C"}
    student = {1: "A", 2: "C", 3: "C"}
    print(f"Quiz Result: {score_quiz(keys, student)}")
