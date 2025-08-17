from dataclasses import dataclass

from app.features.todo.shared.enums import Order, SortBy


@dataclass
class ListTodosQuery:
    """
    Todoクエリー用データクラス
    """
    limit: int
    offset: int
    order_by: Order
    sort_by: SortBy
    cols: list[str]


