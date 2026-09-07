from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BotGroupMemberAdd")


@_attrs_define
class BotGroupMemberAdd:
    """Schema for adding a bot to group

    Attributes:
        bot_id (UUID):
        role (str | Unset):  Default: 'member'.
    """

    bot_id: UUID
    role: str | Unset = "member"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bot_id = str(self.bot_id)

        role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bot_id": bot_id,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bot_id = UUID(d.pop("bot_id"))

        role = d.pop("role", UNSET)

        bot_group_member_add = cls(
            bot_id=bot_id,
            role=role,
        )

        bot_group_member_add.additional_properties = d
        return bot_group_member_add

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
