from enum import StrEnum


class WebhookRegistryReadCategory(StrEnum):
    AD_CONVERSION = "ad_conversion"
    CALENDAR = "calendar"
    CHAT_PLATFORM = "chat_platform"
    CUSTOM = "custom"
    EMAIL_INBOUND = "email_inbound"
    INGESTION = "ingestion"
    PAYMENT = "payment"
    SMS_INBOUND = "sms_inbound"
    SOCIAL_ENGAGEMENT = "social_engagement"
    VOICE_INBOUND = "voice_inbound"
    WEBHOOK_CALLBACK = "webhook_callback"

    def __str__(self) -> str:
        return str(self.value)
