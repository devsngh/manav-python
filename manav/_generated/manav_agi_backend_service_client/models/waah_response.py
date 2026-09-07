from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.waah_week_point import WaahWeekPoint


T = TypeVar("T", bound="WaahResponse")


@_attrs_define
class WaahResponse:
    """GET /api/analytics/waah — Weekly Active Agent-Hours.

    Attributes:
        current_waah (float):
        trend (list[WaahWeekPoint]):
        target (int):
    """

    current_waah: float
    trend: list[WaahWeekPoint]
    target: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_waah = self.current_waah

        trend = []
        for trend_item_data in self.trend:
            trend_item = trend_item_data.to_dict()
            trend.append(trend_item)

        target = self.target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current_waah": current_waah,
                "trend": trend,
                "target": target,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.waah_week_point import WaahWeekPoint  # noqa: PLC0415

        d = dict(src_dict)
        current_waah = d.pop("current_waah")

        trend = []
        _trend = d.pop("trend")
        for trend_item_data in _trend:
            trend_item = WaahWeekPoint.from_dict(trend_item_data)

            trend.append(trend_item)

        target = d.pop("target")

        waah_response = cls(
            current_waah=current_waah,
            trend=trend,
            target=target,
        )

        waah_response.additional_properties = d
        return waah_response

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
