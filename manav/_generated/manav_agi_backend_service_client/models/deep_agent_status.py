from enum import StrEnum


class DeepAgentStatus(StrEnum):
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    DRAFT = "draft"

    def __str__(self) -> str:
        return str(self.value)
