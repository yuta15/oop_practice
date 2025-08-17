import uuid as lib_uuid

from pydantic import BaseModel, field_validator

from app.features.todo.entities.todo import Todo


class SchemaGetTodoQuery(BaseModel):
    """
    UUIDから該当のTodoを取得するクエリ
    """
    uuid:lib_uuid.UUID
    cols: list[str]


    @field_validator("uuid", mode="before")
    @classmethod
    def uuid_validate(cls, value:str) -> lib_uuid.UUID:
        """
        strをUUIDに変換
        """
        try:
            valid_uuid = lib_uuid.UUID(value)
        except:
            raise ValueError("Invalid value. Please Input only UUID strings")
        else:
            return valid_uuid


    @field_validator('cols', mode='before')
    @classmethod
    def cols_validate(cls, value:list) -> list[str]:
        """
        colsの内容を確認し適切な形に変更する。
        """
        if value and set(value) <= set(Todo.model_fields.keys()):
            return value
        else:
            return list(Todo.model_fields.keys())