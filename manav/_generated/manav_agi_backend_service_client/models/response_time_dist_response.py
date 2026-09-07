from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.response_time_dist_item import ResponseTimeDistItem


T = TypeVar("T", bound="ResponseTimeDistResponse")


@_attrs_define
class ResponseTimeDistResponse:
    """
    Attributes:
        buckets (list[ResponseTimeDistItem] | Unset):
        total (int | Unset):  Default: 0.
        avg_ms (float | Unset):  Default: 0.0.
        p50_ms (float | Unset):  Default: 0.0.
        p95_ms (float | Unset):  Default: 0.0.
    """

    buckets: list[ResponseTimeDistItem] | Unset = UNSET
    total: int | Unset = 0
    avg_ms: float | Unset = 0.0
    p50_ms: float | Unset = 0.0
    p95_ms: float | Unset = 0.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buckets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.buckets, Unset):
            buckets = []
            for buckets_item_data in self.buckets:
                buckets_item = buckets_item_data.to_dict()
                buckets.append(buckets_item)

        total = self.total

        avg_ms = self.avg_ms

        p50_ms = self.p50_ms

        p95_ms = self.p95_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buckets is not UNSET:
            field_dict["buckets"] = buckets
        if total is not UNSET:
            field_dict["total"] = total
        if avg_ms is not UNSET:
            field_dict["avg_ms"] = avg_ms
        if p50_ms is not UNSET:
            field_dict["p50_ms"] = p50_ms
        if p95_ms is not UNSET:
            field_dict["p95_ms"] = p95_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.response_time_dist_item import ResponseTimeDistItem  # noqa: PLC0415

        d = dict(src_dict)
        _buckets = d.pop("buckets", UNSET)
        buckets: list[ResponseTimeDistItem] | Unset = UNSET
        if _buckets is not UNSET:
            buckets = []
            for buckets_item_data in _buckets:
                buckets_item = ResponseTimeDistItem.from_dict(buckets_item_data)

                buckets.append(buckets_item)

        total = d.pop("total", UNSET)

        avg_ms = d.pop("avg_ms", UNSET)

        p50_ms = d.pop("p50_ms", UNSET)

        p95_ms = d.pop("p95_ms", UNSET)

        response_time_dist_response = cls(
            buckets=buckets,
            total=total,
            avg_ms=avg_ms,
            p50_ms=p50_ms,
            p95_ms=p95_ms,
        )

        response_time_dist_response.additional_properties = d
        return response_time_dist_response

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
