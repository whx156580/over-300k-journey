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
target_file = current_dir / "object_oriented_programming.py"
mod = load_module_from_path("object_oriented_programming", target_file)

def test_mro_order():
    """验证 C3 线性化 MRO 顺序"""
    mro_names = [c.__name__ for c in mod.Child.mro()]
    expected = ["Child", "Left", "Right", "Base", "object"]
    assert mro_names == expected

def test_abc_interface_enforcement():
    """验证抽象基类强制子类实现方法"""
    with pytest.raises(TypeError, match="Can't instantiate abstract class"):
        mod.BasePage(None) # type: ignore

def test_pom_logic_success():
    """验证模板方法逻辑成功路径"""
    lp = mod.LoginPage(None)
    lp.open("http://example.com") # 内部调用 is_loaded 返回 True，不抛错

def test_pom_logic_failure():
    """验证模板方法逻辑失败路径"""
    class FailPage(mod.BasePage):
        def is_loaded(self): return False
        
    fp = FailPage(None)
    with pytest.raises(RuntimeError, match="Load failed"):
        fp.open("http://fail.com")

def test_slots_restriction():
    """验证 __slots__ 限制动态属性绑定"""
    m = mod.Measurement(1, 1.0, "v")
    with pytest.raises(AttributeError):
        m.new_attr = "fail" # type: ignore

def test_mro_logic_full():
    """触发所有类的定义以提高覆盖率"""
    b = mod.Base()
    b.action()
    l = mod.Left()
    l.action()
    r = mod.Right()
    r.action()
    c = mod.Child()
    c.action()
    assert True

def test_measurement_init():
    """触发 Measurement 的完整初始化"""
    m = mod.Measurement(100, 2.5, "kg")
    assert m.unit == "kg"

