from enum import StrEnum


class BannerPosition(StrEnum):
    BOTTOM = "bottom"
    FLOATING_RIGHT = "floating_right"
    HERO_TOP = "hero_top"
    INLINE_ROW = "inline_row"

    def __str__(self) -> str:
        return str(self.value)
