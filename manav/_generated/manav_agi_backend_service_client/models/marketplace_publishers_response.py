from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.earnings_bucket import EarningsBucket
    from ..models.publisher_item import PublisherItem


T = TypeVar("T", bound="MarketplacePublishersResponse")


@_attrs_define
class MarketplacePublishersResponse:
    """GET /api/analytics/marketplace/publishers — leaderboard + earnings histogram.

    Attributes:
        leaderboard (list[PublisherItem]):
        histogram (list[EarningsBucket]):
    """

    leaderboard: list[PublisherItem]
    histogram: list[EarningsBucket]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        leaderboard = []
        for leaderboard_item_data in self.leaderboard:
            leaderboard_item = leaderboard_item_data.to_dict()
            leaderboard.append(leaderboard_item)

        histogram = []
        for histogram_item_data in self.histogram:
            histogram_item = histogram_item_data.to_dict()
            histogram.append(histogram_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "leaderboard": leaderboard,
                "histogram": histogram,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.earnings_bucket import EarningsBucket  # noqa: PLC0415
        from ..models.publisher_item import PublisherItem  # noqa: PLC0415

        d = dict(src_dict)
        leaderboard = []
        _leaderboard = d.pop("leaderboard")
        for leaderboard_item_data in _leaderboard:
            leaderboard_item = PublisherItem.from_dict(leaderboard_item_data)

            leaderboard.append(leaderboard_item)

        histogram = []
        _histogram = d.pop("histogram")
        for histogram_item_data in _histogram:
            histogram_item = EarningsBucket.from_dict(histogram_item_data)

            histogram.append(histogram_item)

        marketplace_publishers_response = cls(
            leaderboard=leaderboard,
            histogram=histogram,
        )

        marketplace_publishers_response.additional_properties = d
        return marketplace_publishers_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
