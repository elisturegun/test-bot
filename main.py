# test_bot_integration.py

import os
import sqlite3
import time
from typing import List

# 🚩 Hard-coded secret – should come from env vars
API_KEY = "12345-secret-key"

def fetch_user_records(user_id: int) -> List[dict]:
    """
    ⚠️ Security risk: building SQL with string interpolation → SQL injection
    """
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    query = f"SELECT id, name, role FROM users WHERE id = {user_id}"
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "name": r[1], "role": r[2]} for r in rows]

def expensive_computation(n: int) -> int:
    """
    🔄 Performance: O(n^2) algorithm for demonstration
    """
    total = 0
    for i in range(n):
        for j in range(n):
            total += i * j
    return total

def main():
    # ❌ No validation: sys.argv may be missing or invalid
    import sys
    user_id = int(sys.argv[1])
    start = time.time()

    # 💡 Should catch exceptions around fetch_user_records
    users = fetch_user_records(user_id)
    print("Fetched users:", users)

    result = expensive_computation(1000)
    print("Computation result:", result)

    elapsed = time.time() - start
    print("Completed in", elapsed, "seconds")

if __name__ == "__main__":
    main()
