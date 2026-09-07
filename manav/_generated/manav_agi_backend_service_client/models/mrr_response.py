from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.mrr_breakdown import MrrBreakdown
    from ..models.mrr_month_point import MrrMonthPoint


T = TypeVar("T", bound="MrrResponse")


@_attrs_define
class MrrResponse:
    """GET /api/analytics/mrr — Monthly Recurring Revenue across streams.

    Attributes:
        current_mrr (float):
        breakdown (MrrBreakdown):
        trend (list[MrrMonthPoint]):
    """

    current_mrr: float
    breakdown: MrrBreakdown
    trend: list[MrrMonthPoint]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_mrr = self.current_mrr

        breakdown = self.breakdown.to_dict()

        trend = []
        for trend_item_data in self.trend:
            trend_item = trend_item_data.to_dict()
            trend.append(trend_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current_mrr": current_mrr,
                "breakdown": breakdown,
                "trend": trend,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mrr_breakdown import MrrBreakdown  # noqa: PLC0415
        from ..models.mrr_month_point import MrrMonthPoint  # noqa: PLC0415

        d = dict(src_dict)
        current_mrr = d.pop("current_mrr")

        breakdown = MrrBreakdown.from_dict(d.pop("breakdown"))

        trend = []
        _trend = d.pop("trend")
        for trend_item_data in _trend:
            trend_item = MrrMonthPoint.from_dict(trend_item_data)

            trend.append(trend_item)

        mrr_response = cls(
            current_mrr=current_mrr,
            breakdown=breakdown,
            trend=trend,
        )

        mrr_response.additional_properties = d
        return mrr_response

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
