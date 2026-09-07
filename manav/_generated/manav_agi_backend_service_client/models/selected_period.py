from enum import StrEnum


class SelectedPeriod(StrEnum):
    MONTHLY = "monthly"
    YEARLY = "yearly"

    def __str__(self) -> str:
        return str(self.value)
