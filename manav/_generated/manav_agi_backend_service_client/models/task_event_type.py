from enum import StrEnum


class TaskEventType(StrEnum):
    ASSIGNED = "assigned"
    CANCELLED = "cancelled"
    COMMENT = "comment"
    COMPLETED = "completed"
    CREATED = "created"
    FAILED = "failed"
    MONITORING_CHECK = "monitoring_check"
    MONITORING_ENTERED = "monitoring_entered"
    MONITORING_RESUMED = "monitoring_resumed"
    PROGRESS = "progress"
    RETRIED = "retried"
    STARTED = "started"
    WAITING_ENTERED = "waiting_entered"
    WAITING_RESUMED = "waiting_resumed"

    def __str__(self) -> str:
        return str(self.value)
