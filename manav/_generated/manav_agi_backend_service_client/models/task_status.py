from enum import StrEnum


class TaskStatus(StrEnum):
    ASSIGNED = "assigned"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    FAILED = "failed"
    IN_PROGRESS = "in_progress"
    MONITORING = "monitoring"
    PENDING = "pending"
    SCHEDULED = "scheduled"
    WAITING_HUMAN = "waiting_human"

    def __str__(self) -> str:
        return str(self.value)
