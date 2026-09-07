from enum import StrEnum


class TreasuryAlertStatus(StrEnum):
    ACKNOWLEDGED = "acknowledged"
    OPEN = "open"
    RESOLVED = "resolved"
    RETRACTED = "retracted"

    def __str__(self) -> str:
        return str(self.value)
