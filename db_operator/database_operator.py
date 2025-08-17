from abc import ABC, abstractmethod
from typing import Dict, Any, List


class DatabaseOperator(ABC):
    """Abstract base class for database operations."""
    @abstractmethod
    def select_one(self, sql: str, params: Dict[str, Any] | None = None) -> Dict | None: ...
    @abstractmethod
    def select_all(self, sql: str, params: Dict[str, Any] | None = None) -> List[Dict] | None: ...
    @abstractmethod
    def execute_write(self, sql: str, params: Dict[str, Any] | None = None) -> int: ...