from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DurationBucket")


@_attrs_define
class DurationBucket:
    """
    Attributes:
        range_ (str):
        count (int):
        min_seconds (int):
        max_seconds (int):
    """

    range_: str
    count: int
    min_seconds: int
    max_seconds: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        range_ = self.range_

        count = self.count

        min_seconds = self.min_seconds

        max_seconds = self.max_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "range": range_,
                "count": count,
                "min_seconds": min_seconds,
                "max_seconds": max_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        range_ = d.pop("range")

        count = d.pop("count")

        min_seconds = d.pop("min_seconds")

        max_seconds = d.pop("max_seconds")

        duration_bucket = cls(
            range_=range_,
            count=count,
            min_seconds=min_seconds,
            max_seconds=max_seconds,
        )

        duration_bucket.additional_properties = d
        return duration_bucket

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
