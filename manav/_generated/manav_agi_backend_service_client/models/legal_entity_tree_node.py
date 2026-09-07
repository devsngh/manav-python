from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LegalEntityTreeNode")


@_attrs_define
class LegalEntityTreeNode:
    """
    Attributes:
        id (UUID):
        code (str):
        name (str):
        country_code (str):
        children (list[LegalEntityTreeNode]):
    """

    id: UUID
    code: str
    name: str
    country_code: str
    children: list[LegalEntityTreeNode]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        code = self.code

        name = self.name

        country_code = self.country_code

        children = []
        for children_item_data in self.children:
            children_item = children_item_data.to_dict()
            children.append(children_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "code": code,
                "name": name,
                "country_code": country_code,
                "children": children,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        code = d.pop("code")

        name = d.pop("name")

        country_code = d.pop("country_code")

        children = []
        _children = d.pop("children")
        for children_item_data in _children:
            children_item = LegalEntityTreeNode.from_dict(children_item_data)

            children.append(children_item)

        legal_entity_tree_node = cls(
            id=id,
            code=code,
            name=name,
            country_code=country_code,
            children=children,
        )

        legal_entity_tree_node.additional_properties = d
        return legal_entity_tree_node

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
