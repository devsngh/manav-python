from enum import StrEnum


class InsightStatus(StrEnum):
    ACTIONED = "actioned"
    OPEN = "open"
    RETRACTED = "retracted"
    SUPERSEDED = "superseded"

    def __str__(self) -> str:
        return str(self.value)
