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
target_file = current_dir / "sqlalchemy_and_alembic.py"
mod = load_module_from_path("orm_logic", target_file)

@pytest.fixture
def engine():
    return mod.setup_test_db()

def test_create_user_with_address(engine):
    """验证 ORM 对象的关联创建与持久化"""
    uid = mod.add_user_transactional(engine, "bob", "bob@example.com")
    assert uid is not None
    
    user = mod.get_user_by_name(engine, "bob")
    assert user.fullname == "Bob"
    assert len(user.addresses) == 1
    assert user.addresses[0].email_address == "bob@example.com"

def test_transaction_rollback(engine):
    """验证事务回滚逻辑"""
    # 尝试添加一个不合规的数据触发异常
    from sqlalchemy.exc import IntegrityError
    
    # 模拟异常场景：重复插入主键或违反约束（此处用手动抛出模拟业务异常）
    with pytest.raises(ValueError, match="Mock fail"):
        with mod.Session(engine) as session:
            u = mod.User(name="fail", fullname="Failure")
            session.add(u)
            # 事务中途失败
            raise ValueError("Mock fail")
    
    # 验证数据未写入
    assert mod.get_user_by_name(engine, "fail") is None

def test_user_repr():
    """验证 __repr__ 格式"""
    u = mod.User(id=1, name="test")
    # 显式调用以增加覆盖率
    res = u.__repr__()
    assert "User(id=1, name='test')" in res

def test_cascade_delete(engine):
    """验证级联删除行为"""
    uid = mod.add_user_transactional(engine, "delete_me", "del@test.com")
    
    with mod.Session(engine) as session:
        user = session.get(mod.User, uid)
        session.delete(user)
        session.commit()
        
        # 验证地址也被删除了
        stmt = mod.select(mod.Address).where(mod.Address.user_id == uid)
        assert session.scalar(stmt) is None
