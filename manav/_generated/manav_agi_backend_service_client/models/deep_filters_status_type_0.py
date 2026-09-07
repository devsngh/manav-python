from enum import StrEnum


class DeepFiltersStatusType0(StrEnum):
    ERROR = "ERROR"
    OK = "OK"

    def __str__(self) -> str:
        return str(self.value)
