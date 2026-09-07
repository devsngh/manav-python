from enum import StrEnum


class VoiceToolCallReadStatus(StrEnum):
    FAILED = "failed"
    PENDING = "pending"
    SUCCEEDED = "succeeded"
    TIMEOUT = "timeout"

    def __str__(self) -> str:
        return str(self.value)
