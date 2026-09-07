from enum import StrEnum


class InternalToolStatus(StrEnum):
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    INACTIVE = "inactive"
    TESTING = "testing"

    def __str__(self) -> str:
        return str(self.value)
