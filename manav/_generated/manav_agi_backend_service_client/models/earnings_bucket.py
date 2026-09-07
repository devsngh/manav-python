from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EarningsBucket")


@_attrs_define
class EarningsBucket:
    """
    Attributes:
        range_ (str):
        publisher_count (int):
        min_usd (float):
        max_usd (float):
    """

    range_: str
    publisher_count: int
    min_usd: float
    max_usd: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        range_ = self.range_

        publisher_count = self.publisher_count

        min_usd = self.min_usd

        max_usd = self.max_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "range": range_,
                "publisher_count": publisher_count,
                "min_usd": min_usd,
                "max_usd": max_usd,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        range_ = d.pop("range")

        publisher_count = d.pop("publisher_count")

        min_usd = d.pop("min_usd")

        max_usd = d.pop("max_usd")

        earnings_bucket = cls(
            range_=range_,
            publisher_count=publisher_count,
            min_usd=min_usd,
            max_usd=max_usd,
        )

        earnings_bucket.additional_properties = d
        return earnings_bucket

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
