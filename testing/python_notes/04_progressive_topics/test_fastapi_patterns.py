import pytest
import sys
import importlib.util
from pathlib import Path
from fastapi.testclient import TestClient

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
target_file = current_dir / "fastapi_advanced_patterns.py"
mod = load_module_from_path("fastapi_patterns", target_file)

client = TestClient(mod.app)

def test_health_check():
    """验证健康检查接口"""
    # 由于 TestClient 不会自动触发 lifespan，需使用 with 块
    with TestClient(mod.app) as ac:
        response = ac.get("/health")
        assert response.status_code == 200
        assert response.json()["db"] is True

def test_secure_data_no_token():
    """验证缺失 Token 时的 422 (FastAPI 默认行为)"""
    response = client.get("/secure-data")
    assert response.status_code == 422

def test_secure_data_invalid_token():
    """验证错误 Token 时的 401"""
    response = client.get("/secure-data", headers={"x-token": "wrong"})
    assert response.status_code == 401

def test_secure_data_success():
    """验证正确 Token 时的成功响应"""
    response = client.get("/secure-data", headers={"x-token": "valid-token"})
    assert response.status_code == 200
    assert response.json()["user"]["username"] == "qa_admin"

def test_dependency_override():
    """验证依赖覆盖测试模式"""
    def mock_db_status():
        return "MOCKED_STATUS"
    
    # 应用覆盖
    mod.app.dependency_overrides[mod.get_db_status] = mock_db_status
    response = client.get("/db-status")
    assert response.status_code == 200
    assert response.json()["connected"] == "MOCKED_STATUS"
    
    # 清理覆盖
    mod.app.dependency_overrides.clear()
