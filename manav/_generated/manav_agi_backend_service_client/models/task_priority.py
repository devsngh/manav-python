from enum import StrEnum


class TaskPriority(StrEnum):
    CRITICAL = "critical"
    HIGH = "high"
    LOW = "low"
    NORMAL = "normal"

    def __str__(self) -> str:
        return str(self.value)
