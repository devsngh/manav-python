from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.org_tree_node import OrgTreeNode


T = TypeVar("T", bound="OrgTreeResponse")


@_attrs_define
class OrgTreeResponse:
    """Full org tree response with org info and position tree

    Attributes:
        org_name (str):
        org_type (None | str | Unset):
        roots (list[OrgTreeNode] | Unset):
    """

    org_name: str
    org_type: None | str | Unset = UNSET
    roots: list[OrgTreeNode] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_name = self.org_name

        org_type: None | str | Unset
        if isinstance(self.org_type, Unset):
            org_type = UNSET
        else:
            org_type = self.org_type

        roots: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.roots, Unset):
            roots = []
            for roots_item_data in self.roots:
                roots_item = roots_item_data.to_dict()
                roots.append(roots_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "org_name": org_name,
            }
        )
        if org_type is not UNSET:
            field_dict["org_type"] = org_type
        if roots is not UNSET:
            field_dict["roots"] = roots

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.org_tree_node import OrgTreeNode  # noqa: PLC0415

        d = dict(src_dict)
        org_name = d.pop("org_name")

        def _parse_org_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        org_type = _parse_org_type(d.pop("org_type", UNSET))

        _roots = d.pop("roots", UNSET)
        roots: list[OrgTreeNode] | Unset = UNSET
        if _roots is not UNSET:
            roots = []
            for roots_item_data in _roots:
                roots_item = OrgTreeNode.from_dict(roots_item_data)

                roots.append(roots_item)

        org_tree_response = cls(
            org_name=org_name,
            org_type=org_type,
            roots=roots,
        )

        org_tree_response.additional_properties = d
        return org_tree_response

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
