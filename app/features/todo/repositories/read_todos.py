from typing import List

from app.features.todo.entities.todo import Todo
from app.features.todo.shared.enums import Order, SortBy
from app.ports.db.database_operator import DatabaseOperator

class TodoReadRepository:
    def __init__(self, db_operator:DatabaseOperator) -> None:
        self._db = db_operator


    def fetch_todo(self, uuid:str, cols:list[str]) -> dict:
        """
        該当のデータを取得する。
        """
        columns = ", ".join(cols)
        sql = f"SELECT {columns} FROM todos WHERE uuid=:uuid;"
        todo_params = self._db.select_one(sql=sql, params={"uuid":uuid})
        return todo_params or {}


    def list_todos(self, limit:int, offset:int, order:str, sort_by: str, cols:list[str]) -> List:
        """
        listを取得する。
        """
        columns = ", ".join(cols)
        sql = f"""
        SELECT {columns} FROM todos
        ORDER BY {sort_by} {order} LIMIT :limit OFFSET :offset
        """
        parmas = {
            "limit": limit,
            "offset": offset
        }
        todos = self._db.select_all(sql=sql, params=parmas)
        return todos or []