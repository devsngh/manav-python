from enum import StrEnum


class ProposalStatus(StrEnum):
    CERTIFIED = "certified"
    COMMITTED = "committed"
    DRAFTED = "drafted"
    RATIFIED = "ratified"
    REJECTED = "rejected"
    SURFACED = "surfaced"
    WITHDRAWN = "withdrawn"

    def __str__(self) -> str:
        return str(self.value)
