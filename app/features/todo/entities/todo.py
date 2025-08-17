import uuid as lib_uuid
import datetime

from pydantic import BaseModel, Field, field_validator


class Todo(BaseModel):
    """
    Todo Class
    """
    uuid: lib_uuid.UUID = Field(default_factory=lib_uuid.uuid4)
    title: str
    content: str | None = None
    start_date: datetime.date = Field(default_factory=datetime.date.today)
    limit_date: datetime.date = Field(default_factory=datetime.date.today)
    status: bool = False
    version: int = 0

    model_config = {
        "validate_assignment": True,
    }


    def __repr__(self) -> str:
        return f"Todo(uuid={self.uuid}, title={self.title})"


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Todo):
            return NotImplemented
        return self.uuid == other.uuid


    def mark_done(self) -> None:
        """Mark the todo item as done."""
        self.status = True


    def mark_undone(self) -> None:
        """Mark the todo item as done."""
        self.status = False


    def set_start_date(self, start_date: datetime.date) -> None:
        """Set the start date for the todo item."""
        if not self.limit_date:
            self.start_date = start_date
        elif start_date <= self.limit_date:
            self.start_date = start_date
        else:
            raise ValueError("Start date cannot be after the limit date.")


    def set_limit_date(self, limit_date: datetime.date) -> None:
        """Set the limit date for the todo item."""
        if self.start_date <= limit_date:
            self.limit_date = limit_date