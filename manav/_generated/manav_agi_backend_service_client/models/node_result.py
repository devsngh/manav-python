from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.node_result_properties import NodeResultProperties


T = TypeVar("T", bound="NodeResult")


@_attrs_define
class NodeResult:
    """
    Attributes:
        labels (list[str]):
        properties (NodeResultProperties):
    """

    labels: list[str]
    properties: NodeResultProperties
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        labels = self.labels

        properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "labels": labels,
                "properties": properties,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.node_result_properties import NodeResultProperties  # noqa: PLC0415

        d = dict(src_dict)
        labels = cast(list[str], d.pop("labels"))

        properties = NodeResultProperties.from_dict(d.pop("properties"))

        node_result = cls(
            labels=labels,
            properties=properties,
        )

        node_result.additional_properties = d
        return node_result

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
