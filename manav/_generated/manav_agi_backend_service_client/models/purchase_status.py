from enum import StrEnum


class PurchaseStatus(StrEnum):
    ACTIVE = "active"
    CANCELLED = "cancelled"
    EXPIRED = "expired"
    REFUNDED = "refunded"

    def __str__(self) -> str:
        return str(self.value)
