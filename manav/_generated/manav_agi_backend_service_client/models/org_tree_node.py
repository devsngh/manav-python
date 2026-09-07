from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.org_tree_member import OrgTreeMember


T = TypeVar("T", bound="OrgTreeNode")


@_attrs_define
class OrgTreeNode:
    """A position node in the org tree with children and members

    Attributes:
        id (str):
        title (str):
        seniority_level (None | str | Unset):
        department (None | str | Unset):
        reports_to_position_id (None | str | Unset):
        subordinate_count (int | Unset):  Default: 0.
        members (list[OrgTreeMember] | Unset):
        children (list[OrgTreeNode] | Unset):
    """

    id: str
    title: str
    seniority_level: None | str | Unset = UNSET
    department: None | str | Unset = UNSET
    reports_to_position_id: None | str | Unset = UNSET
    subordinate_count: int | Unset = 0
    members: list[OrgTreeMember] | Unset = UNSET
    children: list[OrgTreeNode] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        seniority_level: None | str | Unset
        if isinstance(self.seniority_level, Unset):
            seniority_level = UNSET
        else:
            seniority_level = self.seniority_level

        department: None | str | Unset
        if isinstance(self.department, Unset):
            department = UNSET
        else:
            department = self.department

        reports_to_position_id: None | str | Unset
        if isinstance(self.reports_to_position_id, Unset):
            reports_to_position_id = UNSET
        else:
            reports_to_position_id = self.reports_to_position_id

        subordinate_count = self.subordinate_count

        members: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
            }
        )
        if seniority_level is not UNSET:
            field_dict["seniority_level"] = seniority_level
        if department is not UNSET:
            field_dict["department"] = department
        if reports_to_position_id is not UNSET:
            field_dict["reports_to_position_id"] = reports_to_position_id
        if subordinate_count is not UNSET:
            field_dict["subordinate_count"] = subordinate_count
        if members is not UNSET:
            field_dict["members"] = members
        if children is not UNSET:
            field_dict["children"] = children

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.org_tree_member import OrgTreeMember  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        def _parse_seniority_level(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        seniority_level = _parse_seniority_level(d.pop("seniority_level", UNSET))

        def _parse_department(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        department = _parse_department(d.pop("department", UNSET))

        def _parse_reports_to_position_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reports_to_position_id = _parse_reports_to_position_id(d.pop("reports_to_position_id", UNSET))

        subordinate_count = d.pop("subordinate_count", UNSET)

        _members = d.pop("members", UNSET)
        members: list[OrgTreeMember] | Unset = UNSET
        if _members is not UNSET:
            members = []
            for members_item_data in _members:
                members_item = OrgTreeMember.from_dict(members_item_data)

                members.append(members_item)

        _children = d.pop("children", UNSET)
        children: list[OrgTreeNode] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = OrgTreeNode.from_dict(children_item_data)

                children.append(children_item)

        org_tree_node = cls(
            id=id,
            title=title,
            seniority_level=seniority_level,
            department=department,
            reports_to_position_id=reports_to_position_id,
            subordinate_count=subordinate_count,
            members=members,
            children=children,
        )

        org_tree_node.additional_properties = d
        return org_tree_node

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
