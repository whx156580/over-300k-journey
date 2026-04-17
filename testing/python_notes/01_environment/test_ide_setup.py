import pytest
import sys
import importlib.util
import json
from pathlib import Path

# 确保项目根目录在路径中
ROOT = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(ROOT))

def load_module_from_path(module_name: str, file_path: Path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module
    raise ImportError(f"Could not load module {module_name} at {file_path}")

# 加载目标模块
current_dir = Path(__file__).resolve().parent
target_file = current_dir / "ide_setup.py"
mod = load_module_from_path("ide_setup_logic", target_file)

def test_generate_settings_creates_file(tmp_path):
    """验证配置生成逻辑是否成功创建文件并包含正确内容"""
    settings_file = tmp_path / "settings.json"
    assert mod.generate_vscode_settings(settings_file) is True
    assert settings_file.exists()
    
    with open(settings_file, "r") as f:
        data = json.load(f)
    assert data["editor.formatOnSave"] is True
    assert "black-formatter" in data["editor.defaultFormatter"]

def test_validate_settings_success(tmp_path):
    """验证有效的配置文件"""
    valid_file = tmp_path / "valid.json"
    valid_file.write_text('{"editor.formatOnSave": true, "editor.defaultFormatter": "test"}')
    assert mod.validate_settings_json(valid_file) is True

def test_validate_settings_missing_keys(tmp_path):
    """验证缺少核心字段的配置文件"""
    invalid_file = tmp_path / "invalid.json"
    invalid_file.write_text('{"other": "value"}')
    assert mod.validate_settings_json(invalid_file) is False

def test_validate_settings_invalid_json(tmp_path):
    """验证无效的 JSON 语法"""
    bad_json = tmp_path / "bad.json"
    bad_json.write_text('{invalid}')
    assert mod.validate_settings_json(bad_json) is False

def test_validate_settings_not_exist():
    """验证不存在的文件"""
    assert mod.validate_settings_json(Path("non_existent_file.json")) is False

def test_generate_settings_error(tmp_path, capsys):
    """验证生成配置时的异常处理"""
    # 传入一个文件路径作为父目录，触发 mkdir 失败或写入失败
    bad_path = tmp_path / "already_a_file"
    bad_path.write_text("not a dir")
    target = bad_path / "settings.json"
    
    assert mod.generate_vscode_settings(target) is False
    captured = capsys.readouterr()
    assert "Error generating settings" in captured.out
