from enum import StrEnum


class HILDecision(StrEnum):
    APPROVE = "approve"
    EDIT = "edit"
    REJECT = "reject"

    def __str__(self) -> str:
        return str(self.value)
