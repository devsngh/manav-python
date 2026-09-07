from enum import StrEnum


class HILEventStatus(StrEnum):
    ESCALATED = "escalated"
    EXPIRED = "expired"
    PENDING = "pending"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
