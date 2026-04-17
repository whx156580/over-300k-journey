import time
import json
from typing import Any, Dict, Optional

# --- 示例 1: Redis 分布式锁逻辑 (Atomic Lock) ---

def try_acquire_lock(redis_client: Any, key: str, timeout: int = 5) -> bool:
    """
    尝试获取分布式锁。
    """
    lock_key = f"lock:{key}"
    # nx=True: 仅在键不存在时设置
    # ex=timeout: 设置过期时间，防止死锁
    return bool(redis_client.set(lock_key, "1", nx=True, ex=timeout))

def release_lock(redis_client: Any, key: str) -> None:
    """释放锁"""
    redis_client.delete(f"lock:{key}")

# --- 示例 2: 任务幂等性校验 ---

def is_task_processed(redis_client: Any, task_id: str) -> bool:
    """
    检查任务是否已处理过。
    """
    key = f"processed_task:{task_id}"
    return redis_client.exists(key) > 0

def mark_task_as_processed(redis_client: Any, task_id: str, expire: int = 3600) -> None:
    """标记任务已完成"""
    key = f"processed_task:{task_id}"
    redis_client.set(key, "done", ex=expire)

# --- 示例 3: 模拟 Celery 任务行为 ---

def process_background_job(job_data: Dict[str, Any]) -> str:
    """
    模拟一个后台任务的内部处理逻辑。
    """
    job_id = job_data.get("id", "unknown")
    print(f"[*] Processing background job: {job_id}")
    # 模拟工作
    time.sleep(0.01)
    return f"Job {job_id} Success"

if __name__ == "__main__":
    # 仅演示，实际运行需 redis-server
    print("Background jobs logic defined.")
