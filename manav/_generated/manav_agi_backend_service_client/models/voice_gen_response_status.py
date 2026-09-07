from enum import StrEnum


class VoiceGenResponseStatus(StrEnum):
    FAILED = "failed"
    GENERATED = "generated"
    QUEUED_HUMAN = "queued_human"

    def __str__(self) -> str:
        return str(self.value)
