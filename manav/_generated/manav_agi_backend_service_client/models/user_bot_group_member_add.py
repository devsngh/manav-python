from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserBotGroupMemberAdd")


@_attrs_define
class UserBotGroupMemberAdd:
    """Schema for adding a member to an existing user-bot group.

    Attributes:
        member_id (UUID):
        member_type (str):
        role (str | Unset):  Default: 'participant'.
    """

    member_id: UUID
    member_type: str
    role: str | Unset = "participant"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        member_id = str(self.member_id)

        member_type = self.member_type

        role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "member_id": member_id,
                "member_type": member_type,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        member_id = UUID(d.pop("member_id"))

        member_type = d.pop("member_type")

        role = d.pop("role", UNSET)

        user_bot_group_member_add = cls(
            member_id=member_id,
            member_type=member_type,
            role=role,
        )

        user_bot_group_member_add.additional_properties = d
        return user_bot_group_member_add

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
