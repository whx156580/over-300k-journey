import pytest
import requests
from unittest.mock import Mock

@pytest.fixture
def mock_api_response():
    """
    Given: 准备 Mock 的 API 响应数据
    """
    mock = Mock(spec=requests.Response)
    mock.status_code = 200
    mock.json.return_value = {"status": "success", "data": {"job_title": "SDET", "salary_min": 250000}}
    return mock

@pytest.mark.integration
def test_api_contract_validation(mock_api_response, monkeypatch):
    # Given: 使用 monkeypatch 替换真实的 requests.get
    monkeypatch.setattr(requests, "get", lambda url: mock_api_response)
    
    # When: 模拟调用后端接口
    response = requests.get("https://api.internal/v1/salary-benchmarks")
    data = response.json()
    
    # Then: 验证契约字段
    assert response.status_code == 200
    assert "data" in data
    assert data["data"]["job_title"] == "SDET"
    assert data["data"]["salary_min"] >= 200000
