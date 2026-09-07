from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AssetTagCreate")


@_attrs_define
class AssetTagCreate:
    """
    Attributes:
        tag_key (str):
        tag_value (str):
    """

    tag_key: str
    tag_value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag_key = self.tag_key

        tag_value = self.tag_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tag_key": tag_key,
                "tag_value": tag_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tag_key = d.pop("tag_key")

        tag_value = d.pop("tag_value")

        asset_tag_create = cls(
            tag_key=tag_key,
            tag_value=tag_value,
        )

        asset_tag_create.additional_properties = d
        return asset_tag_create

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
