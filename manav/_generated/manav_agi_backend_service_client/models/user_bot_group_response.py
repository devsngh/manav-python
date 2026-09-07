from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_bot_group_member_response import UserBotGroupMemberResponse


T = TypeVar("T", bound="UserBotGroupResponse")


@_attrs_define
class UserBotGroupResponse:
    """Schema for a user-bot group response.

    Attributes:
        id (UUID):
        group_name (str):
        group_type (str):
        is_archived (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        group_description (None | str | Unset):
        chair_id (None | Unset | UUID):
        chair_type (None | str | Unset):
        org_id (None | Unset | UUID):
        department_id (None | Unset | UUID):
        last_message_at (datetime.datetime | None | Unset):
        members (list[UserBotGroupMemberResponse] | Unset):
    """

    id: UUID
    group_name: str
    group_type: str
    is_archived: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    group_description: None | str | Unset = UNSET
    chair_id: None | Unset | UUID = UNSET
    chair_type: None | str | Unset = UNSET
    org_id: None | Unset | UUID = UNSET
    department_id: None | Unset | UUID = UNSET
    last_message_at: datetime.datetime | None | Unset = UNSET
    members: list[UserBotGroupMemberResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        group_name = self.group_name

        group_type = self.group_type

        is_archived = self.is_archived

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        group_description: None | str | Unset
        if isinstance(self.group_description, Unset):
            group_description = UNSET
        else:
            group_description = self.group_description

        chair_id: None | str | Unset
        if isinstance(self.chair_id, Unset):
            chair_id = UNSET
        elif isinstance(self.chair_id, UUID):
            chair_id = str(self.chair_id)
        else:
            chair_id = self.chair_id

        chair_type: None | str | Unset
        if isinstance(self.chair_type, Unset):
            chair_type = UNSET
        else:
            chair_type = self.chair_type

        org_id: None | str | Unset
        if isinstance(self.org_id, Unset):
            org_id = UNSET
        elif isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

        department_id: None | str | Unset
        if isinstance(self.department_id, Unset):
            department_id = UNSET
        elif isinstance(self.department_id, UUID):
            department_id = str(self.department_id)
        else:
            department_id = self.department_id

        last_message_at: None | str | Unset
        if isinstance(self.last_message_at, Unset):
            last_message_at = UNSET
        elif isinstance(self.last_message_at, datetime.datetime):
            last_message_at = self.last_message_at.isoformat()
        else:
            last_message_at = self.last_message_at

        members: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "group_name": group_name,
                "group_type": group_type,
                "is_archived": is_archived,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if group_description is not UNSET:
            field_dict["group_description"] = group_description
        if chair_id is not UNSET:
            field_dict["chair_id"] = chair_id
        if chair_type is not UNSET:
            field_dict["chair_type"] = chair_type
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if department_id is not UNSET:
            field_dict["department_id"] = department_id
        if last_message_at is not UNSET:
            field_dict["last_message_at"] = last_message_at
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_bot_group_member_response import UserBotGroupMemberResponse  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        group_name = d.pop("group_name")

        group_type = d.pop("group_type")

        is_archived = d.pop("is_archived")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_group_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_description = _parse_group_description(d.pop("group_description", UNSET))

        def _parse_chair_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                chair_id_type_0 = UUID(data)

                return chair_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        chair_id = _parse_chair_id(d.pop("chair_id", UNSET))

        def _parse_chair_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chair_type = _parse_chair_type(d.pop("chair_type", UNSET))

        def _parse_org_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                org_id_type_0 = UUID(data)

                return org_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        org_id = _parse_org_id(d.pop("org_id", UNSET))

        def _parse_department_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                department_id_type_0 = UUID(data)

                return department_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        department_id = _parse_department_id(d.pop("department_id", UNSET))

        def _parse_last_message_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_message_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_message_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_message_at = _parse_last_message_at(d.pop("last_message_at", UNSET))

        _members = d.pop("members", UNSET)
        members: list[UserBotGroupMemberResponse] | Unset = UNSET
        if _members is not UNSET:
            members = []
            for members_item_data in _members:
                members_item = UserBotGroupMemberResponse.from_dict(members_item_data)

                members.append(members_item)

        user_bot_group_response = cls(
            id=id,
            group_name=group_name,
            group_type=group_type,
            is_archived=is_archived,
            created_at=created_at,
            updated_at=updated_at,
            group_description=group_description,
            chair_id=chair_id,
            chair_type=chair_type,
            org_id=org_id,
            department_id=department_id,
            last_message_at=last_message_at,
            members=members,
        )

        user_bot_group_response.additional_properties = d
        return user_bot_group_response

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
