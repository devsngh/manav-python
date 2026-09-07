from enum import StrEnum


class VoiceTurnCreateSpeaker(StrEnum):
    AGENT = "agent"
    CALLER = "caller"
    SYSTEM = "system"

    def __str__(self) -> str:
        return str(self.value)
