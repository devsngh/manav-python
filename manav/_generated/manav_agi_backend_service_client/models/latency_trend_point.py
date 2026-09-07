from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LatencyTrendPoint")


@_attrs_define
class LatencyTrendPoint:
    """
    Attributes:
        hour (str):
        p50 (float):
        p95 (float):
        p99 (float):
        count (int):
    """

    hour: str
    p50: float
    p95: float
    p99: float
    count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hour = self.hour

        p50 = self.p50

        p95 = self.p95

        p99 = self.p99

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hour": hour,
                "p50": p50,
                "p95": p95,
                "p99": p99,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hour = d.pop("hour")

        p50 = d.pop("p50")

        p95 = d.pop("p95")

        p99 = d.pop("p99")

        count = d.pop("count")

        latency_trend_point = cls(
            hour=hour,
            p50=p50,
            p95=p95,
            p99=p99,
            count=count,
        )

        latency_trend_point.additional_properties = d
        return latency_trend_point

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
