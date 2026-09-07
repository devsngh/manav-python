from enum import StrEnum


class PlanTier(StrEnum):
    ENTERPRISE = "enterprise"
    ENTERPRISE_PLUS = "enterprise_plus"
    FAMILY = "family"
    FREE = "free"
    PRO = "pro"
    TEAM = "team"

    def __str__(self) -> str:
        return str(self.value)
