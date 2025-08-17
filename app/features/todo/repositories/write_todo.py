from app.features.todo.entities.todo import Todo
from app.ports.db.database_operator import DatabaseOperator


class TodoRepository:
    """
    Todo Repository class
    """
    def __init__(self, db:DatabaseOperator) -> None:
        self._db = db


    def create_todo(self, todo:Todo) -> str | None:
        """
        insertする
        """
        sql = """
        INSERT INTO todos (uuid, title, content, status, start_date, limit_date, version)
        VALUES (:uuid, :title, :content, :status, :start_date, :limit_date, :version);
        """
        res = self._db.execute_write(sql=sql, params={
            "uuid": str(todo.uuid),
            "title": todo.title,
            "content": todo.content,
            "status": todo.status,
            "start_date": todo.start_date,
            "limit_date": todo.limit_date,
            "version":todo.version
        })
        if res:
            return str(todo.uuid)
        return None


    def update_todo(self, todo: Todo) -> bool:
        """Updateする"""
        sql = """
        UPDATE todos SET title=:title, content=:content, status=:status, start_date=:start_date, limit_date=:limit_date, version=:update_version
        WHERE uuid=:uuid AND version=:current_version;
        """
        values = {
            "uuid": todo.uuid,
            "title": todo.title,
            "content": todo.content,
            "status": todo.status,
            "start_date": todo.start_date,
            "limit_date": todo.limit_date,
            "current_version": todo.version,
            "update_version": todo.version + 1
        }
        res = self._db.execute_write(sql=sql, params=values)
        if res:
            todo.version += 1
        return bool(res)


    def select_todo(self, uuid:str) -> Todo | None:
        """
        該当のデータを取得する。
        """
        SAFE_COLS = ["uuid", "title", "content", "start_date", "limit_date", "status", "version"]
        columns = ", ".join(SAFE_COLS)
        sql = f"SELECT {columns} FROM todos WHERE uuid=:uuid;"
        todo_params = self._db.select_one(sql=sql, params={"uuid":uuid})
        if todo_params:
            return Todo(**todo_params)
        return None


    def delete_todo(self, uuid:str) -> bool:
        """
        該当のデータを削除する。
        """
        sql = """
        DELETE FROM todos WHERE uuid=:uuid;
        """
        res = self._db.execute_write(sql=sql, params={"uuid":uuid})
        return bool(res)
