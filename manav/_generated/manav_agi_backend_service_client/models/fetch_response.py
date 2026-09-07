from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FetchResponse")


@_attrs_define
class FetchResponse:
    """
    Attributes:
        s3_key (str):
        bytes_ (int):
        suffix (str):
    """

    s3_key: str
    bytes_: int
    suffix: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        s3_key = self.s3_key

        bytes_ = self.bytes_

        suffix = self.suffix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "s3_key": s3_key,
                "bytes": bytes_,
                "suffix": suffix,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        s3_key = d.pop("s3_key")

        bytes_ = d.pop("bytes")

        suffix = d.pop("suffix")

        fetch_response = cls(
            s3_key=s3_key,
            bytes_=bytes_,
            suffix=suffix,
        )

        fetch_response.additional_properties = d
        return fetch_response

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
