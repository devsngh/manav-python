from enum import StrEnum


class ListMessagesApiCommsEmailMessagesGetStatusType0(StrEnum):
    BOUNCED = "bounced"
    CLICKED = "clicked"
    DELIVERED = "delivered"
    FAILED = "failed"
    OPENED = "opened"
    QUEUED = "queued"
    RECEIVED = "received"
    REPLIED = "replied"
    SENT = "sent"
    SPAM = "spam"

    def __str__(self) -> str:
        return str(self.value)
