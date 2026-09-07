from enum import StrEnum


class TreasuryAlertType(StrEnum):
    BURN_RATE_SPIKE = "burn_rate_spike"
    CEILING_BREACH = "ceiling_breach"
    COST_OVERRUN_BOT = "cost_overrun_bot"
    COST_OVERRUN_WORKSPACE = "cost_overrun_workspace"
    EBITDA_NEGATIVE = "ebitda_negative"
    REVENUE_DRIFT = "revenue_drift"
    RUNWAY_LOW = "runway_low"

    def __str__(self) -> str:
        return str(self.value)
