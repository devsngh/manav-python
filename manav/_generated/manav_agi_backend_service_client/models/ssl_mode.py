from enum import StrEnum


class SSLMode(StrEnum):
    DISABLE = "disable"
    PREFER = "prefer"
    REQUIRE = "require"

    def __str__(self) -> str:
        return str(self.value)
