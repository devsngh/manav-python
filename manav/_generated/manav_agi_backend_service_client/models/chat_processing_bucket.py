from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ChatProcessingBucket")


@_attrs_define
class ChatProcessingBucket:
    """
    Attributes:
        range_ (str):
        count (int):
        min_ms (int):
        max_ms (int):
    """

    range_: str
    count: int
    min_ms: int
    max_ms: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        range_ = self.range_

        count = self.count

        min_ms = self.min_ms

        max_ms = self.max_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "range": range_,
                "count": count,
                "min_ms": min_ms,
                "max_ms": max_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        range_ = d.pop("range")

        count = d.pop("count")

        min_ms = d.pop("min_ms")

        max_ms = d.pop("max_ms")

        chat_processing_bucket = cls(
            range_=range_,
            count=count,
            min_ms=min_ms,
            max_ms=max_ms,
        )

        chat_processing_bucket.additional_properties = d
        return chat_processing_bucket

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
