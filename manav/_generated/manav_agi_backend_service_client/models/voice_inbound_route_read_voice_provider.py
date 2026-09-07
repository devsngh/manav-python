from enum import StrEnum


class VoiceInboundRouteReadVoiceProvider(StrEnum):
    ELEVENLABS_STREAMING = "elevenlabs_streaming"
    OPENAI_REALTIME = "openai_realtime"

    def __str__(self) -> str:
        return str(self.value)
