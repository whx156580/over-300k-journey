from typing import List, Optional
from sqlalchemy import String, ForeignKey, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session, selectinload

# --- 示例 1: 声明式模型定义 (SQLAlchemy 2.0) ---

class Base(DeclarativeBase):
    """基类，用于统一管理所有模型"""
    pass

class User(Base):
    __tablename__ = "user_account"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    
    # 建立双向关联
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r})"

class Address(Base):
    __tablename__ = "address"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    
    user: Mapped["User"] = relationship(back_populates="addresses")

# --- 示例 2: 事务与 CRUD 操作 ---

def setup_test_db(url: str = "sqlite:///:memory:"):
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    return engine

def add_user_transactional(engine, name: str, email: str):
    """
    演示 Session 事务管理。
    """
    with Session(engine) as session:
        try:
            user = User(name=name, fullname=name.capitalize())
            user.addresses.append(Address(email_address=email))
            session.add(user)
            session.commit() # 显式提交
            return user.id
        except Exception:
            session.rollback() # 出错回滚
            raise

# --- 示例 3: 查询逻辑 ---

def get_user_by_name(engine, name: str) -> Optional[User]:
    with Session(engine) as session:
        # 使用 selectinload 预加载关联，防止脱离 Session 后报错 (DetachedInstanceError)
        stmt = select(User).where(User.name == name).options(selectinload(User.addresses))
        return session.scalar(stmt)

if __name__ == "__main__":
    eng = setup_test_db()
    uid = add_user_transactional(eng, "alice", "alice@test.com")
    print(f"Created user with ID: {uid}")
    
    user = get_user_by_name(eng, "alice")
    if user:
        print(f"Found: {user.fullname} with {len(user.addresses)} address(es)")
