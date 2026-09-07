from enum import StrEnum


class PricingModel(StrEnum):
    FREE = "free"
    PER_QUERY = "per_query"
    SUBSCRIPTION = "subscription"

    def __str__(self) -> str:
        return str(self.value)
