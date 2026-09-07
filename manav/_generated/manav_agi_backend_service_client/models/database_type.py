from enum import StrEnum


class DatabaseType(StrEnum):
    MYSQL = "mysql"
    POSTGRESQL = "postgresql"

    def __str__(self) -> str:
        return str(self.value)
