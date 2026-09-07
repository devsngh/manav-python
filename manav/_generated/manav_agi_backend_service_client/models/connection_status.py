from enum import StrEnum


class ConnectionStatus(StrEnum):
    ACTIVE = "active"
    CONNECTING = "connecting"
    ERROR = "error"
    INACTIVE = "inactive"

    def __str__(self) -> str:
        return str(self.value)
