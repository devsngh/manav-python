from enum import StrEnum


class ModelCategory(StrEnum):
    CHAT = "chat"
    EMBEDDING = "embedding"
    IMAGE = "image"
    REALTIME_AUDIO = "realtime_audio"
    REASONING = "reasoning"
    RESEARCH = "research"
    SEARCH = "search"
    STT = "stt"
    TTS = "tts"
    VIDEO = "video"

    def __str__(self) -> str:
        return str(self.value)
