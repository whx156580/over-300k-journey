import os

def init_project_structure():
    """
    初始化项目目录结构，确保所有核心模块及技术栈子目录存在，并添加 .gitkeep 文件防止空目录被忽略。
    """
    structure = {
        "testing": ["ui/playwright", "ui/selenium", "api/pytest", "api/rest-assured", "performance/k6", "performance/jmeter", "mobile/appium", "ai-eval/ragas", "ai-eval/deepeval", "strategy"],
        "frontend": ["engineering", "performance", "frameworks"],
        "backend": ["distributed", "database", "system-design"],
        "ai": ["llm-agent", "mlops", "dataset"],
        "common": ["checklists", "snippets", "tools", "docs"],
        "scripts": []
    }

    print("Starting project structure initialization...")

    for root, subs in structure.items():
        # 创建根模块目录
        if not os.path.exists(root):
            os.makedirs(root)
            print(f"  [Created] {root}")
        
        # 创建子目录
        for sub in subs:
            path = os.path.join(root, sub)
            if not os.path.exists(path):
                os.makedirs(path)
                print(f"  [Created] {path}")
            
            # 为每个叶子目录添加 .gitkeep
            gitkeep_path = os.path.join(path, ".gitkeep")
            if not os.path.exists(gitkeep_path):
                with open(gitkeep_path, 'w') as f:
                    pass
                print(f"    [Added] {gitkeep_path}")

    print("Project structure initialization completed!")

if __name__ == "__main__":
    init_project_structure()
