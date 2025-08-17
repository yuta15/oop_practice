from typing import List

from db_operator.database_operator import DatabaseOperator
from entity.todo import Todo


class TodoRepository:
    """
    Todo Repository class
    """
    def __init__(self, db:DatabaseOperator) -> None:
        self._db = db


    def create_todo(self, todo:Todo) -> str:
        """
        insertする
        """
        sql = """
        INSERT INTO todos (uuid, title, content, status, start_date, limit_date)
        VALUES (:uuid, :title, :content, :status, :start_date, :limit_date);
        """
        res = self._db.execute_write(sql=sql, params=todo.model_dump())
        if res:
            return todo.uuid
        return ""


    def update_todo(self, todo: Todo) -> bool:
        """Updateする"""
        sql = f"""
        UPDATE todos SET title=:title, content=:content, status=:status, start_date=:start_date, limit_date=:limit_date
        WHERE uuid="{todo.uuid}";
        """
        values = {
            "title": todo.title,
            "content": todo.content,
            "status": todo.status,
            "start_date": todo.start_date,
            "limit_date": todo.limit_date
        }
        res = self._db.execute_write(sql=sql, params=values)
        return bool(res)


    def select_todo(self, uuid:str) -> Todo | None:
        """
        該当のデータを取得する。
        """
        sql = f"""
        SELECT * FROM todos WHERE uuid="{uuid}";
        """
        todo_params = self._db.select_one(sql=sql)
        if todo_params:
            return Todo(**todo_params)
        return


    def delete_todo(self, uuid:str) -> bool:
        """
        該当のデータを削除する。
        """
        sql = f"""
        DELETE FROM todos WHERE uuid="{uuid}"
        """
        res = self._db.execute_write(sql=sql)
        return bool(res)
