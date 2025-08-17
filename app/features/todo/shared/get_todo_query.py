from dataclasses import dataclass


@dataclass
class GetTodoQuery:
    """
    単一のTodoを取得するデータクラス
    """
    uuid: str
    cols: list[str]