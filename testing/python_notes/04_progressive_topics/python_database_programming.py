import sqlite3
from typing import Dict, List, Optional, Any, Tuple

# --- 示例 1: 参数化查询与 Row Factory ---

def get_user_by_id(db_path: str, user_id: int) -> Optional[Dict[str, Any]]:
    """
    使用参数化查询获取用户信息，并返回字典格式。
    """
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT, name TEXT)")
        cursor.execute("INSERT INTO users VALUES (1, 'QA_User')")
        
        # 参数化查询，防御 SQL 注入
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        return dict(row) if row else None

# --- 示例 2: 批量写入 (Executemany) ---

def batch_insert_data(db_path: str, table_name: str, data: List[Tuple[Any, ...]]) -> int:
    """
    使用 executemany 进行高性能批量插入。
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (val INT)")
        cursor.executemany(f"INSERT INTO {table_name} VALUES (?)", data)
        conn.commit()
        
        cursor.execute(f"SELECT count(*) FROM {table_name}")
        return cursor.fetchone()[0]

# --- 示例 3: 事务与回滚 ---

def transfer_funds(db_path: str, from_id: int, to_id: int, amount: int) -> bool:
    """
    演示显式事务控制与异常回滚。
    """
    conn = sqlite3.connect(db_path)
    try:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS accounts (id INT, balance INT)")
        cursor.execute("INSERT OR IGNORE INTO accounts VALUES (1, 100), (2, 100)")
        
        # 扣除
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?", (amount, from_id))
        
        # 模拟中间失败
        if amount > 1000:
            raise ValueError("Insufficient funds or limit exceeded")
            
        # 增加
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?", (amount, to_id))
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        print(f"Transaction failed: {e}")
        return False
    finally:
        conn.close()

if __name__ == "__main__":
    db = ":memory:"
    print(f"User 1: {get_user_by_id(db, 1)}")
    
    count = batch_insert_data(db, "test_table", [(i,) for i in range(10)])
    print(f"Total rows: {count}")
    
    success = transfer_funds(db, 1, 2, 50)
    print(f"Transfer success: {success}")
