import pytest
import sys
import importlib.util
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
target_file = current_dir / "context_managers.py"
mod = load_module_from_path("ctx_logic", target_file)

def test_mock_browser_lifecycle():
    """验证类式管理器正常启停"""
    with mod.MockBrowser("Firefox") as b:
        assert b.is_open is True
    assert b.is_open is False

def test_mock_browser_exception_propagation():
    """验证不吞掉异常"""
    with pytest.raises(RuntimeError, match="fail"):
        with mod.MockBrowser("Edge"):
            raise RuntimeError("fail")

def test_temporary_config_restore():
    """验证生成器式管理器还原状态"""
    settings = {"v": 1}
    with mod.temporary_config(settings, "v", 2):
        assert settings["v"] == 2
    assert settings["v"] == 1

def test_temporary_config_restore_on_error():
    """验证即便报错也能还原状态"""
    settings = {"v": 1}
    try:
        with mod.temporary_config(settings, "v", 2):
            raise ValueError()
    except ValueError:
        pass
    assert settings["v"] == 1

def test_suppress_error_logic():
    """验证异常压制逻辑"""
    with mod.SuppressError(TypeError):
        int(None) # type: ignore
    # 若执行到此，说明 TypeError 被吞掉，测试通过
    assert True

def test_suppress_error_propagation():
    """验证非目标异常正常抛出"""
    with pytest.raises(ValueError):
        with mod.SuppressError(TypeError):
            int("abc")
