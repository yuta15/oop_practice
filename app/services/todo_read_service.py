from app.features.todo.repositories.read_todos import TodoReadRepository

from app.features.todo.shared.list_todos_query import ListTodosQuery
from app.features.todo.shared.get_todo_query import GetTodoQuery


class TodoQueryService:
    """
    Todo Query用のサービス
    """
    def __init__(self, repo:TodoReadRepository) -> None:
        self._repo = repo


    def fetch_todos(self, query:ListTodosQuery) -> list:
        """
        listを取得する関数
        """
        todos = self._repo.list_todos(
            limit=query.limit,
            offset=query.offset,
            order=query.order_by.value,
            sort_by=query.sort_by.value,
            cols=query.cols
            )
        return todos


    def fetch_todo(self, query:GetTodoQuery) -> dict:
        """
        該当のDictを返す関数
        """
        todo = self._repo.fetch_todo(
            uuid=str(query.uuid),
            cols=query.cols
        )
        return todo or {}
