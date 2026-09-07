from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BulkRegisterItem")


@_attrs_define
class BulkRegisterItem:
    """
    Attributes:
        element_key (str):
        label (str):
        category (str):
    """

    element_key: str
    label: str
    category: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        element_key = self.element_key

        label = self.label

        category = self.category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "element_key": element_key,
                "label": label,
                "category": category,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        element_key = d.pop("element_key")

        label = d.pop("label")

        category = d.pop("category")

        bulk_register_item = cls(
            element_key=element_key,
            label=label,
            category=category,
        )

        bulk_register_item.additional_properties = d
        return bulk_register_item

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
