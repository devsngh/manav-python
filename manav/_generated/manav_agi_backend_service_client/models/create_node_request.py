from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_node_request_properties import CreateNodeRequestProperties


T = TypeVar("T", bound="CreateNodeRequest")


@_attrs_define
class CreateNodeRequest:
    """
    Attributes:
        label (str):
        key_property (str): Property name used for MERGE (e.g. 'id', 'iso_code')
        key_value (Any): Value of key_property
        properties (CreateNodeRequestProperties | Unset): Other properties to SET on the node
    """

    label: str
    key_property: str
    key_value: Any
    properties: CreateNodeRequestProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        key_property = self.key_property

        key_value = self.key_value

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "key_property": key_property,
                "key_value": key_value,
            }
        )
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_node_request_properties import CreateNodeRequestProperties  # noqa: PLC0415

        d = dict(src_dict)
        label = d.pop("label")

        key_property = d.pop("key_property")

        key_value = d.pop("key_value")

        _properties = d.pop("properties", UNSET)
        properties: CreateNodeRequestProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = CreateNodeRequestProperties.from_dict(_properties)

        create_node_request = cls(
            label=label,
            key_property=key_property,
            key_value=key_value,
            properties=properties,
        )

        create_node_request.additional_properties = d
        return create_node_request

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
