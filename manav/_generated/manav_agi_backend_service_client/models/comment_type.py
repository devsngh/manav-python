from enum import StrEnum


class CommentType(StrEnum):
    ACKNOWLEDGEMENT = "acknowledgement"
    COMMENT = "comment"
    REVISION_REQUEST = "revision_request"

    def __str__(self) -> str:
        return str(self.value)
