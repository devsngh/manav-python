from enum import StrEnum


class SearchMode(StrEnum):
    DEEP = "deep"
    QUICK = "quick"

    def __str__(self) -> str:
        return str(self.value)
