
from typing import Annotated

from fastapi import APIRouter, Depends

from app.api.deps.todo import deps
from app.features.todo.shared.list_todos_query import ListTodosQuery
from app.services.todo_read_service import TodoQueryService

router = APIRouter(
    prefix="/todos",
    tags=["todos"]
)


@router.get("/list")
def get_todos(
    query:Annotated[ListTodosQuery, Depends(deps.get_query)],
    service:Annotated[TodoQueryService, Depends(deps.get_read_service)]
    ):
    """
    listで取得するAPIエンドポイント
    """
    print(query)
    todos = service.fetch_todos(query)
    return todos