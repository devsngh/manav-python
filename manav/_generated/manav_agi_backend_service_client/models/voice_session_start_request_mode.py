from enum import StrEnum


class VoiceSessionStartRequestMode(StrEnum):
    LIVE_REALTIME = "live_realtime"
    PRERENDERED_DTMF = "prerendered_dtmf"

    def __str__(self) -> str:
        return str(self.value)
