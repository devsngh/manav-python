from enum import StrEnum


class AgentLifeModeResponseEligibility(StrEnum):
    CONTEMPLATIVE = "contemplative"
    FULL = "full"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
