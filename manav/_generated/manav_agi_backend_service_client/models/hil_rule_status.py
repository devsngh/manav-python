from enum import StrEnum


class HILRuleStatus(StrEnum):
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    DRAFT = "draft"
    TESTING = "testing"

    def __str__(self) -> str:
        return str(self.value)
