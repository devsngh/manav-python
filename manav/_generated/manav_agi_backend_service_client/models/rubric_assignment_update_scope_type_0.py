from enum import StrEnum


class RubricAssignmentUpdateScopeType0(StrEnum):
    ALL = "all"
    MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
