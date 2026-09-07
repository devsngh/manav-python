from enum import StrEnum


class VoiceInboundRouteUpdateVoiceProviderType0(StrEnum):
    ELEVENLABS_STREAMING = "elevenlabs_streaming"
    OPENAI_REALTIME = "openai_realtime"

    def __str__(self) -> str:
        return str(self.value)
