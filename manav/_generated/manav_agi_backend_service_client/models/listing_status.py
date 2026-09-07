from enum import StrEnum


class ListingStatus(StrEnum):
    APPROVED = "approved"
    DELISTED = "delisted"
    DRAFT = "draft"
    LISTED = "listed"
    PENDING_REVIEW = "pending_review"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
