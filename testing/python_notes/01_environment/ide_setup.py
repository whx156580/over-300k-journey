import json
import os
from pathlib import Path
from typing import Dict, Any

# --- 示例 1: 自动化配置生成逻辑 ---

def generate_vscode_settings(target_path: Path) -> bool:
    """
    生成推荐的 VS Code 设置文件。
    """
    settings: Dict[str, Any] = {
        "python.defaultInterpreterPath": ".venv/bin/python",
        "editor.formatOnSave": True,
        "editor.defaultFormatter": "ms-python.black-formatter",
        "python.analysis.typeCheckingMode": "basic",
        "isort.args": ["--profile", "black"],
    }
    
    try:
        target_path.parent.mkdir(parents=True, exist_ok=True)
        with open(target_path, "w", encoding="utf-8") as f:
            json.dump(settings, f, indent=4)
        return True
    except Exception as e:
        print(f"Error generating settings: {e}")
        return False

# --- 示例 2: 验证配置文件的有效性 ---

def validate_settings_json(file_path: Path) -> bool:
    """
    简单验证 settings.json 是否包含核心字段。
    """
    if not file_path.exists():
        return False
        
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        required_keys = ["editor.formatOnSave", "editor.defaultFormatter"]
        return all(key in data for key in required_keys)
    except (json.JSONDecodeError, IOError):
        return False

if __name__ == "__main__":
    temp_settings = Path("temp_vscode_settings.json")
    if generate_vscode_settings(temp_settings):
        print(f"Settings generated. Valid? {validate_settings_json(temp_settings)}")
        # 清理临时文件
        if temp_settings.exists():
            temp_settings.unlink()
