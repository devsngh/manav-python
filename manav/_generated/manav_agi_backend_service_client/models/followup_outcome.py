from enum import StrEnum


class FollowupOutcome(StrEnum):
    FAILURE = "failure"
    INCONCLUSIVE = "inconclusive"
    PARTIAL = "partial"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
