from fastapi import FastAPI, Depends, Header, HTTPException, status
from contextlib import asynccontextmanager
from typing import Dict, Any, Optional

# --- 示例 1: 依赖注入 (DI) 链 ---

async def get_token(x_token: str = Header(...)) -> str:
    """第一层依赖：提取并验证 Token"""
    if x_token != "valid-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing Token"
        )
    return x_token

async def get_current_user(token: str = Depends(get_token)) -> Dict[str, str]:
    """第二层依赖：根据 Token 获取用户信息"""
    # 模拟数据库查询
    return {"username": "qa_admin", "scope": "full_access"}

# --- 示例 2: Lifespan 资源管理 ---

class MockDatabase:
    def __init__(self):
        self.connected = False
    async def connect(self): 
        self.connected = True
        print("DB Connected")
    async def disconnect(self): 
        self.connected = False
        print("DB Disconnected")

db = MockDatabase()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时连接数据库
    await db.connect()
    yield
    # 关闭时断开连接
    await db.disconnect()

# --- 应用创建 ---

app = FastAPI(lifespan=lifespan)

@app.get("/health")
async def health_check():
    return {"status": "ok", "db": db.connected}

@app.get("/secure-data")
async def get_secure_data(user: dict = Depends(get_current_user)):
    return {"data": "secret_content", "user": user}

def get_db_status():
    """用于测试覆盖的依赖项"""
    return db.connected

@app.get("/db-status")
async def db_status_route(status: bool = Depends(get_db_status)):
    return {"connected": status}

if __name__ == "__main__":
    import uvicorn
    # uvicorn.run(app, host="0.0.0.0", port=8000)
