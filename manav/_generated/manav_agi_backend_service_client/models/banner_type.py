from enum import StrEnum


class BannerType(StrEnum):
    AD_CARD = "ad_card"
    PROMOTIONAL = "promotional"

    def __str__(self) -> str:
        return str(self.value)
