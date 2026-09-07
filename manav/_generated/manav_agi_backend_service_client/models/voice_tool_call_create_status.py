from enum import StrEnum


class VoiceToolCallCreateStatus(StrEnum):
    FAILED = "failed"
    PENDING = "pending"
    SUCCEEDED = "succeeded"
    TIMEOUT = "timeout"

    def __str__(self) -> str:
        return str(self.value)
