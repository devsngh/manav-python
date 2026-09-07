from enum import StrEnum


class ExternalMessageReadClassificationType0(StrEnum):
    AUTORESPONDER = "autoresponder"
    BOUNCE = "bounce"
    OTHER = "other"
    PARTNERSHIP_INQUIRY = "partnership_inquiry"
    PERSONAL_REPLY = "personal_reply"
    SALES_LEAD = "sales_lead"
    SPAM = "spam"
    SUPPORT_QUESTION = "support_question"
    UNSUBSCRIBE_REQUEST = "unsubscribe_request"

    def __str__(self) -> str:
        return str(self.value)
