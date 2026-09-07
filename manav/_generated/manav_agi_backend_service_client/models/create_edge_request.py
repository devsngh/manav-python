from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_edge_request_properties import CreateEdgeRequestProperties


T = TypeVar("T", bound="CreateEdgeRequest")


@_attrs_define
class CreateEdgeRequest:
    """
    Attributes:
        from_label (str):
        from_key_value (Any):
        to_label (str):
        to_key_value (Any):
        edge_type (str):
        from_key_property (str | Unset):  Default: 'id'.
        to_key_property (str | Unset):  Default: 'id'.
        properties (CreateEdgeRequestProperties | Unset):
    """

    from_label: str
    from_key_value: Any
    to_label: str
    to_key_value: Any
    edge_type: str
    from_key_property: str | Unset = "id"
    to_key_property: str | Unset = "id"
    properties: CreateEdgeRequestProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_label = self.from_label

        from_key_value = self.from_key_value

        to_label = self.to_label

        to_key_value = self.to_key_value

        edge_type = self.edge_type

        from_key_property = self.from_key_property

        to_key_property = self.to_key_property

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from_label": from_label,
                "from_key_value": from_key_value,
                "to_label": to_label,
                "to_key_value": to_key_value,
                "edge_type": edge_type,
            }
        )
        if from_key_property is not UNSET:
            field_dict["from_key_property"] = from_key_property
        if to_key_property is not UNSET:
            field_dict["to_key_property"] = to_key_property
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_edge_request_properties import CreateEdgeRequestProperties  # noqa: PLC0415

        d = dict(src_dict)
        from_label = d.pop("from_label")

        from_key_value = d.pop("from_key_value")

        to_label = d.pop("to_label")

        to_key_value = d.pop("to_key_value")

        edge_type = d.pop("edge_type")

        from_key_property = d.pop("from_key_property", UNSET)

        to_key_property = d.pop("to_key_property", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: CreateEdgeRequestProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = CreateEdgeRequestProperties.from_dict(_properties)

        create_edge_request = cls(
            from_label=from_label,
            from_key_value=from_key_value,
            to_label=to_label,
            to_key_value=to_key_value,
            edge_type=edge_type,
            from_key_property=from_key_property,
            to_key_property=to_key_property,
            properties=properties,
        )

        create_edge_request.additional_properties = d
        return create_edge_request

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
