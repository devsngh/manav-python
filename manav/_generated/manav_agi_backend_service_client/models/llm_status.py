from enum import StrEnum


class LLMStatus(StrEnum):
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    INACTIVE = "inactive"
    TESTING = "testing"

    def __str__(self) -> str:
        return str(self.value)
