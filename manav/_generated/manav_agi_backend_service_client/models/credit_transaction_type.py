from enum import StrEnum


class CreditTransactionType(StrEnum):
    ADMIN_ADJUSTMENT = "admin_adjustment"
    CYCLE_RESET = "cycle_reset"
    MARKETPLACE_QUERY = "marketplace_query"
    PACK_PURCHASE = "pack_purchase"
    PLAN_GRANT = "plan_grant"
    REFUND = "refund"
    USAGE_DEDUCTION = "usage_deduction"

    def __str__(self) -> str:
        return str(self.value)
