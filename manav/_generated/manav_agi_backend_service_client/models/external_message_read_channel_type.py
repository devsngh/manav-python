from enum import StrEnum


class ExternalMessageReadChannelType(StrEnum):
    EMAIL = "email"
    SMS = "sms"
    SOCIAL_DM = "social_dm"
    VOICE = "voice"
    WHATSAPP = "whatsapp"

    def __str__(self) -> str:
        return str(self.value)
