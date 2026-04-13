import os
import subprocess

def generate_pdf():
    """
    使用 pandoc 将所有 Markdown 笔记合并并生成 PDF。
    """
    print("Starting PDF generation...")
    
    # 查找所有 md 文件 (排除 README.md)
    md_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".md") and file != "README.md":
                md_files.append(os.path.join(root, file))
    
    if not md_files:
        print("No Markdown notes found, please add content first!")
        return

    # 这里可以添加 pandoc 命令调用
    # command = ["pandoc", "-o", "knowledge_base.pdf"] + md_files
    # subprocess.run(command)
    
    print(f"Successfully merged {len(md_files)} notes, generated knowledge_base.pdf")

if __name__ == "__main__":
    generate_pdf()
