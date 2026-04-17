import pytest
import sys
import importlib.util
from pathlib import Path

# 确保项目根目录在路径中
ROOT = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(ROOT))

# 由于目录名包含数字开头 (03_...)，不能直接用点号导入，需动态导入
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
target_file = current_dir / "metaprogramming_and_descriptors.py"
mod = load_module_from_path("metaprogramming_and_descriptors", target_file)

DatabaseConnection = mod.DatabaseConnection
Product = mod.Product
PluginRegistry = mod.PluginRegistry
HttpPlugin = mod.HttpPlugin
SshPlugin = mod.SshPlugin

def test_singleton_thread_safety():
    """验证元类实现的单例模式是否生效"""
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    assert db1 is db2
    assert db1.connected is True

def test_descriptor_validation():
    """验证描述符的类型和范围校验"""
    p = Product(price=100, stock=50)
    assert p.price == 100
    
    # 验证类型校验
    with pytest.raises(TypeError, match="Expected int"):
        p.price = "100"  # type: ignore
        
    # 验证范围校验
    with pytest.raises(ValueError, match="Value must be >= 1"):
        p.price = 0

def test_descriptor_get_on_class():
    """验证类访问描述符时返回描述符对象本身"""
    # 使用动态加载的模块中的类
    IntegerField = mod.IntegerField
    assert isinstance(Product.price, IntegerField)

def test_plugin_registry():
    """验证元类是否自动注册了子类"""
    assert "httpplugin" in PluginRegistry.registry
    assert "sshplugin" in PluginRegistry.registry
    assert PluginRegistry.registry["httpplugin"] is HttpPlugin
    assert PluginRegistry.registry["sshplugin"] is SshPlugin
    
    # 额外验证 if name != "BasePlugin" 的分支逻辑
    assert "baseplugin" not in PluginRegistry.registry

def test_singleton_double_check_locking():
    """验证单例模式的双重检查锁定分支"""
    # 清理已存在的实例以触发创建逻辑
    SingletonMeta = mod.SingletonMeta
    SingletonMeta._instances.clear()
    
    def create_instance():
        return DatabaseConnection()
        
    import concurrent.futures
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(create_instance) for _ in range(10)]
        results = [f.result() for f in futures]
        
    assert all(r is results[0] for r in results)
    assert len(SingletonMeta._instances) == 1

def test_descriptor_storage_isolation():
    """验证不同实例之间的描述符数据是否隔离"""
    p1 = Product(10, 5)
    p2 = Product(20, 10)
    assert p1.price == 10
    assert p2.price == 20
    p1.price = 15
    assert p1.price == 15
    assert p2.price == 20
