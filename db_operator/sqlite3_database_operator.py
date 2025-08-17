import sqlite3
from typing import Dict, Any, List, Optional, Tuple

from db_operator.database_operator import DatabaseOperator


class Sqlite3DatabaseOperator(DatabaseOperator):
    """Concrete implementation of DatabaseOperator for SQLite3."""

    def __init__(self, db_name: str):
        self.db_name = db_name


    def select_one(self, sql: str, params: Dict[str, Any] | None = None) -> dict | None:
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute(sql, params or {})
                row = cursor.fetchone()
        except Exception as e:
            print(f"Error executing select_one: {e}")
            return None
        if row:
            return dict(row)
        return row


    def select_all(self, sql: str, params: Dict[str, Any] | None = None) -> List[Dict] | None:
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute(sql, params or {})
                rows = cursor.fetchall()
        except Exception as e:
            print(f"Error executing select_all: {e}")
            return None
        return rows


    def execute_write(self, sql: str, params: Dict[str, Any] | None = None) -> int:
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(sql, params or {})
                conn.commit()
        except Exception as e:
            print(f"Error executing write operation: {e}")
            return 0
        return cursor.rowcount