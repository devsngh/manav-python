from enum import StrEnum


class RubricAssignmentCreateScope(StrEnum):
    ALL = "all"
    MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
