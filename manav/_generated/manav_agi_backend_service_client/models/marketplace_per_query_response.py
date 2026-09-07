from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.per_query_day_point import PerQueryDayPoint


T = TypeVar("T", bound="MarketplacePerQueryResponse")


@_attrs_define
class MarketplacePerQueryResponse:
    """GET /api/analytics/marketplace/per-query — daily query usage + credit revenue.

    Attributes:
        points (list[PerQueryDayPoint]):
        current_month_credits (int):
        period_queries (int):
    """

    points: list[PerQueryDayPoint]
    current_month_credits: int
    period_queries: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        points = []
        for points_item_data in self.points:
            points_item = points_item_data.to_dict()
            points.append(points_item)

        current_month_credits = self.current_month_credits

        period_queries = self.period_queries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "points": points,
                "current_month_credits": current_month_credits,
                "period_queries": period_queries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.per_query_day_point import PerQueryDayPoint  # noqa: PLC0415

        d = dict(src_dict)
        points = []
        _points = d.pop("points")
        for points_item_data in _points:
            points_item = PerQueryDayPoint.from_dict(points_item_data)

            points.append(points_item)

        current_month_credits = d.pop("current_month_credits")

        period_queries = d.pop("period_queries")

        marketplace_per_query_response = cls(
            points=points,
            current_month_credits=current_month_credits,
            period_queries=period_queries,
        )

        marketplace_per_query_response.additional_properties = d
        return marketplace_per_query_response

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
