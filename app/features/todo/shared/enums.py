from enum import Enum


class Order(Enum):
    ASC = "ASC"
    DESC = "DESC"


class SortBy(Enum):
    LIMIT_DATE = "limit_date"
    START_DATE = "start_date"
    TITLE = "title"