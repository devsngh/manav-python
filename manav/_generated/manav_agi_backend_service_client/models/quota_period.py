from enum import StrEnum


class QuotaPeriod(StrEnum):
    DAILY = "daily"
    LIFETIME = "lifetime"
    MONTHLY = "monthly"
    YEARLY = "yearly"

    def __str__(self) -> str:
        return str(self.value)
