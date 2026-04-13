import os
import re

def parse_md_to_anki(file_path):
    """
    解析 Markdown 文件中的面试 Q&A，将其转化为 Anki 格式 (CSV)。
    """
    qa_list = []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
        # 匹配模版中的 ## ❓ 面试高频 Q&A 部分
        matches = re.findall(r"### Q: (.*?)\n### A: (.*?)\n", content, re.DOTALL)
        for q, a in matches:
            qa_list.append((q.strip(), a.strip()))
            
    return qa_list

def export_anki_csv():
    print("Starting Anki bank parsing...")
    
    all_qa = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".md"):
                qa = parse_md_to_anki(os.path.join(root, file))
                all_qa.extend(qa)
                
    if not all_qa:
        print("No matching Q&A found, please follow the template!")
        return

    with open("anki_interview_bank.csv", "w", encoding='utf-8') as f:
        for q, a in all_qa:
            # Anki 导入格式通常是 Q;A
            f.write(f"{q};{a}\n")
            
    print(f"Successfully exported {len(all_qa)} questions to anki_interview_bank.csv")

if __name__ == "__main__":
    export_anki_csv()
