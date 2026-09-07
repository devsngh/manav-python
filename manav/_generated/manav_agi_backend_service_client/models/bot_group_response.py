from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BotGroupResponse")


@_attrs_define
class BotGroupResponse:
    """Schema for bot group response

    Attributes:
        id (UUID):
        group_name (str):
        group_description (None | str):
        created_by_bot_id (None | UUID):
        org_id (None | UUID):
        is_archived (bool):
        created_at (datetime.datetime):
        last_message_at (datetime.datetime | None):
        is_department_group (bool | Unset):  Default: False.
        department_id (None | Unset | UUID):
        member_count (int | None | Unset):  Default: 0.
    """

    id: UUID
    group_name: str
    group_description: None | str
    created_by_bot_id: None | UUID
    org_id: None | UUID
    is_archived: bool
    created_at: datetime.datetime
    last_message_at: datetime.datetime | None
    is_department_group: bool | Unset = False
    department_id: None | Unset | UUID = UNSET
    member_count: int | None | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        group_name = self.group_name

        group_description: None | str
        group_description = self.group_description

        created_by_bot_id: None | str
        if isinstance(self.created_by_bot_id, UUID):
            created_by_bot_id = str(self.created_by_bot_id)
        else:
            created_by_bot_id = self.created_by_bot_id

        org_id: None | str
        if isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

        is_archived = self.is_archived

        created_at = self.created_at.isoformat()

        last_message_at: None | str
        if isinstance(self.last_message_at, datetime.datetime):
            last_message_at = self.last_message_at.isoformat()
        else:
            last_message_at = self.last_message_at

        is_department_group = self.is_department_group

        department_id: None | str | Unset
        if isinstance(self.department_id, Unset):
            department_id = UNSET
        elif isinstance(self.department_id, UUID):
            department_id = str(self.department_id)
        else:
            department_id = self.department_id

        member_count: int | None | Unset
        if isinstance(self.member_count, Unset):
            member_count = UNSET
        else:
            member_count = self.member_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "group_name": group_name,
                "group_description": group_description,
                "created_by_bot_id": created_by_bot_id,
                "org_id": org_id,
                "is_archived": is_archived,
                "created_at": created_at,
                "last_message_at": last_message_at,
            }
        )
        if is_department_group is not UNSET:
            field_dict["is_department_group"] = is_department_group
        if department_id is not UNSET:
            field_dict["department_id"] = department_id
        if member_count is not UNSET:
            field_dict["member_count"] = member_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        group_name = d.pop("group_name")

        def _parse_group_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        group_description = _parse_group_description(d.pop("group_description"))

        def _parse_created_by_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_bot_id_type_0 = UUID(data)

                return created_by_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        created_by_bot_id = _parse_created_by_bot_id(d.pop("created_by_bot_id"))

        def _parse_org_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                org_id_type_0 = UUID(data)

                return org_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        org_id = _parse_org_id(d.pop("org_id"))

        is_archived = d.pop("is_archived")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_last_message_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_message_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_message_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_message_at = _parse_last_message_at(d.pop("last_message_at"))

        is_department_group = d.pop("is_department_group", UNSET)

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

        def _parse_member_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        member_count = _parse_member_count(d.pop("member_count", UNSET))

        bot_group_response = cls(
            id=id,
            group_name=group_name,
            group_description=group_description,
            created_by_bot_id=created_by_bot_id,
            org_id=org_id,
            is_archived=is_archived,
            created_at=created_at,
            last_message_at=last_message_at,
            is_department_group=is_department_group,
            department_id=department_id,
            member_count=member_count,
        )

        bot_group_response.additional_properties = d
        return bot_group_response

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
