import datetime
import uuid

from db_operator.sqlite3_database_operator import Sqlite3DatabaseOperator


class User:
    """
    User Class
    """
    def __init__(
        self,
        user_name: str,
        age: int,
        mail_address: str,
        user_uuid: str | None = None,
        created_at: datetime.date | None = None
        ) -> None:
        self.uuid:str | None = user_uuid
        self.user_name:str = user_name
        self.age:int = age
        self.mail_address:str = mail_address
        self.created_at:datetime.date | None = created_at
        self._table_name:str = 'users'
        self._db_operator:Sqlite3DatabaseOperator = Sqlite3DatabaseOperator('todo.db')

    def __repr__(self) -> str:
        return f"User(uuid={self.uuid}, user_name={self.user_name})"

    def insert(self):
        """Create a new user in the database."""
        self.uuid = str(uuid.uuid4())
        self.created_at = datetime.date.today()
        if self.created_at is None:
            self.created_at = datetime.date.today()
        command = """
        INSERT INTO users (uuid, user_name, age, mail_address, created_at)
        VALUES (:uuid, :user_name, :age, :mail_address, :created_at);
        """
        params = {
            'uuid': self.uuid,
            'user_name': self.user_name,
            'age': self.age,
            'mail_address': self.mail_address,
            'created_at': str(self.created_at)
        }
        # Assuming _db_operator is defined and connected to the database
        return self._db_operator.execute_write(command, params)