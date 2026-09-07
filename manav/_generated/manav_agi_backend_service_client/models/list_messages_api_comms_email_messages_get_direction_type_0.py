from enum import StrEnum


class ListMessagesApiCommsEmailMessagesGetDirectionType0(StrEnum):
    INBOUND = "inbound"
    OUTBOUND = "outbound"

    def __str__(self) -> str:
        return str(self.value)
