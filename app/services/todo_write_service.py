from entity.todo import Todo
from repository.todo_repository import TodoRepository


class AddTodoService:
    """
    AppServiceを定義するクラス
    """
    def __init__(self, todo_repository:TodoRepository, ) -> None:
        self._todo_repo = todo_repository
    
    
    def AddTodo