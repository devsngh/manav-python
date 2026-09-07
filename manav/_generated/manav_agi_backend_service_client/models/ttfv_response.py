from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ttfv_bucket import TtfvBucket


T = TypeVar("T", bound="TtfvResponse")


@_attrs_define
class TtfvResponse:
    """GET /api/analytics/growth/ttfv

    Attributes:
        buckets (list[TtfvBucket]):
        sample_size (int):
        median_hours (float | None | Unset):
        p90_hours (float | None | Unset):
    """

    buckets: list[TtfvBucket]
    sample_size: int
    median_hours: float | None | Unset = UNSET
    p90_hours: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buckets = []
        for buckets_item_data in self.buckets:
            buckets_item = buckets_item_data.to_dict()
            buckets.append(buckets_item)

        sample_size = self.sample_size

        median_hours: float | None | Unset
        if isinstance(self.median_hours, Unset):
            median_hours = UNSET
        else:
            median_hours = self.median_hours

        p90_hours: float | None | Unset
        if isinstance(self.p90_hours, Unset):
            p90_hours = UNSET
        else:
            p90_hours = self.p90_hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "buckets": buckets,
                "sample_size": sample_size,
            }
        )
        if median_hours is not UNSET:
            field_dict["median_hours"] = median_hours
        if p90_hours is not UNSET:
            field_dict["p90_hours"] = p90_hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ttfv_bucket import TtfvBucket  # noqa: PLC0415

        d = dict(src_dict)
        buckets = []
        _buckets = d.pop("buckets")
        for buckets_item_data in _buckets:
            buckets_item = TtfvBucket.from_dict(buckets_item_data)

            buckets.append(buckets_item)

        sample_size = d.pop("sample_size")

        def _parse_median_hours(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        median_hours = _parse_median_hours(d.pop("median_hours", UNSET))

        def _parse_p90_hours(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        p90_hours = _parse_p90_hours(d.pop("p90_hours", UNSET))

        ttfv_response = cls(
            buckets=buckets,
            sample_size=sample_size,
            median_hours=median_hours,
            p90_hours=p90_hours,
        )

        ttfv_response.additional_properties = d
        return ttfv_response

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
