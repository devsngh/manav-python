from enum import StrEnum


class RubricAssignmentResponseScope(StrEnum):
    ALL = "all"
    MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
