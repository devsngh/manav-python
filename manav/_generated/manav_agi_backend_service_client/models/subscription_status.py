from enum import StrEnum


class SubscriptionStatus(StrEnum):
    ACTIVE = "active"
    CANCELED = "canceled"
    PAST_DUE = "past_due"
    PAUSED = "paused"
    TRIALING = "trialing"

    def __str__(self) -> str:
        return str(self.value)
