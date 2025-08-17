from pydantic import BaseModel, Field, field_validator
from pydantic_core import PydanticUndefined

from app.features.todo.shared.enums import Order, SortBy
from app.features.todo.entities.todo import Todo


ALLOWED_COLS = list(Todo.model_fields.keys())

class SchemaListTodosQuery(BaseModel):
    """
    Todoのリード用クエリースキーマ
    """
    limit: int = Field(default=10, ge=1, le=200)
    offset: int = Field(default=0, ge=0)
    order_by: Order = Field(default=Order.ASC)
    sort_by: SortBy = Field(default=SortBy.LIMIT_DATE)
    cols: list[str] | None= None


    @field_validator('order_by', mode='before')
    @classmethod
    def order_validate(cls, value) -> Order:
        """
        orderの内容をvalidateする。
        """
        try:
            if isinstance(value,str) and value.upper() in Order:
                value = Order(value.upper())
        except:
            raise ValueError(f"Invalid value. Please set only {Order._member_names_}")
        else:
            return value


    @field_validator('sort_by', mode='before')
    @classmethod
    def sort_by_validate(cls, value) -> SortBy:
        """
        SortByの内容をvalidateする。
        """
        if isinstance(value,str) and value.upper() in SortBy:
            value = SortBy(value.upper())
        return value


    @field_validator("cols", mode="before")
    @classmethod
    def cols_validate(cls, value):
        if isinstance(value, list):
            if set(value) <= set(ALLOWED_COLS):
                return value
        else:
            return ALLOWED_COLS