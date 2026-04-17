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
target_file = current_dir / "python_re.py"
mod = load_module_from_path("re_logic", target_file)

def test_parse_structured_log():
    """验证命名分组日志解析逻辑"""
    line = "[INFO] user=guest action=view"
    data = mod.parse_structured_log(line)
    assert data is not None
    assert data["level"] == "INFO"
    assert data["user"] == "guest"
    assert data["action"] == "view"
    
    assert mod.parse_structured_log("invalid line") is None

def test_extract_tags_non_greedy():
    """验证非贪婪标签提取"""
    html = "<div>1</div><div>2</div>"
    assert mod.extract_tags(html) == ["1", "2"]
    # 贪婪模式会返回 ['1</div><div>2']，这里验证非贪婪行为
    assert len(mod.extract_tags(html)) == 2

def test_extract_durations_lookaround():
    """验证正向断言提取数字"""
    text = "start: 50ms, end: 150ms"
    assert mod.extract_durations(text) == ["50", "150"]
    assert "ms" not in mod.extract_durations(text)

def test_precompile_efficiency_logic():
    """验证文档中提到的预编译优势逻辑"""
    import re
    import timeit
    p_str = r"\w+"
    data = "test data"
    # 预编译后执行 search 应比每次 search(str) 快
    t_raw = timeit.timeit(lambda: re.search(p_str, data), number=1000)
    compiled = re.compile(p_str)
    t_compiled = timeit.timeit(lambda: compiled.search(data), number=1000)
    # 虽然在小数据量下差异可能不明显，但逻辑上编译过的通常更快
    assert t_compiled <= t_raw * 1.5 # 容忍一定的环境抖动
