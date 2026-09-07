from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserBotGroupMemberResponse")


@_attrs_define
class UserBotGroupMemberResponse:
    """Single member in a user-bot group.

    Attributes:
        id (UUID):
        group_id (UUID):
        member_id (UUID):
        member_type (str):
        role (str):
        is_active (bool):
        joined_at (datetime.datetime):
        left_at (datetime.datetime | None | Unset):
    """

    id: UUID
    group_id: UUID
    member_id: UUID
    member_type: str
    role: str
    is_active: bool
    joined_at: datetime.datetime
    left_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        group_id = str(self.group_id)

        member_id = str(self.member_id)

        member_type = self.member_type

        role = self.role

        is_active = self.is_active

        joined_at = self.joined_at.isoformat()

        left_at: None | str | Unset
        if isinstance(self.left_at, Unset):
            left_at = UNSET
        elif isinstance(self.left_at, datetime.datetime):
            left_at = self.left_at.isoformat()
        else:
            left_at = self.left_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "group_id": group_id,
                "member_id": member_id,
                "member_type": member_type,
                "role": role,
                "is_active": is_active,
                "joined_at": joined_at,
            }
        )
        if left_at is not UNSET:
            field_dict["left_at"] = left_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        group_id = UUID(d.pop("group_id"))

        member_id = UUID(d.pop("member_id"))

        member_type = d.pop("member_type")

        role = d.pop("role")

        is_active = d.pop("is_active")

        joined_at = datetime.datetime.fromisoformat(d.pop("joined_at"))

        def _parse_left_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                left_at_type_0 = datetime.datetime.fromisoformat(data)

                return left_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        left_at = _parse_left_at(d.pop("left_at", UNSET))

        user_bot_group_member_response = cls(
            id=id,
            group_id=group_id,
            member_id=member_id,
            member_type=member_type,
            role=role,
            is_active=is_active,
            joined_at=joined_at,
            left_at=left_at,
        )

        user_bot_group_member_response.additional_properties = d
        return user_bot_group_member_response

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
