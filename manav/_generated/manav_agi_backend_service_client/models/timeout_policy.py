from enum import StrEnum


class TimeoutPolicy(StrEnum):
    AUTO_DECLINE = "auto_decline"
    BLOCK_INDEFINITELY = "block_indefinitely"
    DEFAULT_TO_SAFEST = "default_to_safest"
    ESCALATE_TO_DELEGATE = "escalate_to_delegate"

    def __str__(self) -> str:
        return str(self.value)
