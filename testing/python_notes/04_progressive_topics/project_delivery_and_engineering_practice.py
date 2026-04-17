from typing import Dict, List, Any

# --- 示例 1: 结构化发布门禁逻辑 ---

def check_release_readiness(metrics: Dict[str, Any]) -> bool:
    """
    检查发布就绪状态：测试通过、覆盖率达标、无高危漏洞。
    """
    gates = {
        "tests": metrics.get("tests_passed", False),
        "coverage": metrics.get("coverage_pct", 0) >= 90,
        "security": metrics.get("vulnerabilities", 1) == 0
    }
    
    can_ship = all(gates.values())
    if not can_ship:
        failed = [k for k, v in gates.items() if not v]
        # 实际项目中应使用 logging
        print(f"Release BLOCKED by gates: {failed}")
    return can_ship

# --- 示例 2: 环境变量加载与验证 ---

def load_env_config(env_vars: Dict[str, str]) -> Dict[str, str]:
    """
    验证必要的环境变量是否存在，这是交付时的核心契约。
    """
    required = ["DB_URL", "API_KEY"]
    config = {}
    for key in required:
        val = env_vars.get(key)
        if not val:
            raise EnvironmentError(f"Missing required environment variable: {key}")
        config[key] = val
    return config

# --- 示例 3: 最小发布决策 (性能预算) ---

def verify_performance_budget(actual: Dict[str, float], budget: Dict[str, float]) -> bool:
    """
    对比性能指标与预算阈值。
    """
    for metric, threshold in budget.items():
        current = actual.get(metric, float('inf'))
        if current > threshold:
            print(f"Performance budget exceeded for {metric}: {current} > {threshold}")
            return False
    return True

if __name__ == "__main__":
    # 验证门禁
    m = {"tests_passed": True, "coverage_pct": 92, "vulnerabilities": 0}
    print(f"Can ship? {check_release_readiness(m)}")
    
    # 验证配置
    try:
        load_env_config({"DB_URL": "sqlite://"})
    except EnvironmentError as e:
        print(f"Config check failed: {e}")
        
    # 验证性能
    perf_actual = {"p95_ms": 250, "error_rate": 0.001}
    perf_budget = {"p95_ms": 300, "error_rate": 0.01}
    print(f"Perf OK: {verify_performance_budget(perf_actual, perf_budget)}")
