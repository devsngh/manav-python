from enum import StrEnum


class AgentSocietyStateRowEligibility(StrEnum):
    CONTEMPLATIVE = "contemplative"
    FULL = "full"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
