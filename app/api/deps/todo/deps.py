from typing import Annotated
from fastapi import Depends, Query

from app.adapters.db.sqlite3_database_operator import Sqlite3DatabaseOperator
from app.features.todo.repositories.read_todos import TodoReadRepository
from app.features.todo.schemas.schema_list_todo_query import SchemaListTodosQuery
from app.features.todo.shared.list_todos_query import ListTodosQuery
from app.services.todo_read_service import TodoQueryService


DB_NAME = "todo.db"     # 今後環境変数に移行
DB_KIND = "sqlite3"

def get_db():
    """
    db初期化
    """
    match DB_KIND:
        case "sqlite3":
            return Sqlite3DatabaseOperator(db_name=DB_NAME)


def get_read_repo(db=Depends(get_db)):
    """
    read_repo初期化
    """
    return TodoReadRepository(db)


def get_read_service(repo=Depends(get_read_repo)):
    """
    service初期化
    """
    return TodoQueryService(repo=repo)


def _build_schema_from_query(
    limit: Annotated[int | None, Query()] = None,
    offset: Annotated[int | None, Query()] = None,
    order_by: Annotated[str | None, Query()] = None,
    sort_by: Annotated[str | None, Query()] = None,
    cols: Annotated[list[str] | None, Query()] = None,
) -> SchemaListTodosQuery:
    data = {k: v for k, v in {
        "limit": limit,
        "offset": offset,
        "order_by": order_by,
        "sort_by": sort_by,
        "cols": cols,
    }.items() if v is not None}
    return SchemaListTodosQuery(**data)

def get_query(schema: Annotated[SchemaListTodosQuery, Depends(_build_schema_from_query)]) -> ListTodosQuery:
    return ListTodosQuery(**schema.model_dump())