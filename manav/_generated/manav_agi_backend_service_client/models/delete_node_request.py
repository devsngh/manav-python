from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteNodeRequest")


@_attrs_define
class DeleteNodeRequest:
    """
    Attributes:
        label (str):
        key_value (Any):
        key_property (str | Unset):  Default: 'id'.
        cascade (bool | Unset): If True, also delete connected edges (DETACH DELETE) Default: False.
    """

    label: str
    key_value: Any
    key_property: str | Unset = "id"
    cascade: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        key_value = self.key_value

        key_property = self.key_property

        cascade = self.cascade

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "key_value": key_value,
            }
        )
        if key_property is not UNSET:
            field_dict["key_property"] = key_property
        if cascade is not UNSET:
            field_dict["cascade"] = cascade

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        key_value = d.pop("key_value")

        key_property = d.pop("key_property", UNSET)

        cascade = d.pop("cascade", UNSET)

        delete_node_request = cls(
            label=label,
            key_value=key_value,
            key_property=key_property,
            cascade=cascade,
        )

        delete_node_request.additional_properties = d
        return delete_node_request

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
