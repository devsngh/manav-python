from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.member_status import MemberStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationMemberResponse")


@_attrs_define
class OrganizationMemberResponse:
    """Schema for organization member response

    Attributes:
        id (UUID):
        org_id (UUID):
        user_id (UUID):
        joined_at (datetime.datetime):
        is_primary (bool):
        status (MemberStatus): Organization member status enum
        bot_id (None | Unset | UUID):
        added_by_user_id (None | Unset | UUID):
        user_email (None | str | Unset):
        user_full_name (None | str | Unset):
        bot_name (None | str | Unset):
    """

    id: UUID
    org_id: UUID
    user_id: UUID
    joined_at: datetime.datetime
    is_primary: bool
    status: MemberStatus
    bot_id: None | Unset | UUID = UNSET
    added_by_user_id: None | Unset | UUID = UNSET
    user_email: None | str | Unset = UNSET
    user_full_name: None | str | Unset = UNSET
    bot_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        org_id = str(self.org_id)

        user_id = str(self.user_id)

        joined_at = self.joined_at.isoformat()

        is_primary = self.is_primary

        status = self.status.value

        bot_id: None | str | Unset
        if isinstance(self.bot_id, Unset):
            bot_id = UNSET
        elif isinstance(self.bot_id, UUID):
            bot_id = str(self.bot_id)
        else:
            bot_id = self.bot_id

        added_by_user_id: None | str | Unset
        if isinstance(self.added_by_user_id, Unset):
            added_by_user_id = UNSET
        elif isinstance(self.added_by_user_id, UUID):
            added_by_user_id = str(self.added_by_user_id)
        else:
            added_by_user_id = self.added_by_user_id

        user_email: None | str | Unset
        if isinstance(self.user_email, Unset):
            user_email = UNSET
        else:
            user_email = self.user_email

        user_full_name: None | str | Unset
        if isinstance(self.user_full_name, Unset):
            user_full_name = UNSET
        else:
            user_full_name = self.user_full_name

        bot_name: None | str | Unset
        if isinstance(self.bot_name, Unset):
            bot_name = UNSET
        else:
            bot_name = self.bot_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "user_id": user_id,
                "joined_at": joined_at,
                "is_primary": is_primary,
                "status": status,
            }
        )
        if bot_id is not UNSET:
            field_dict["bot_id"] = bot_id
        if added_by_user_id is not UNSET:
            field_dict["added_by_user_id"] = added_by_user_id
        if user_email is not UNSET:
            field_dict["user_email"] = user_email
        if user_full_name is not UNSET:
            field_dict["user_full_name"] = user_full_name
        if bot_name is not UNSET:
            field_dict["bot_name"] = bot_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        user_id = UUID(d.pop("user_id"))

        joined_at = datetime.datetime.fromisoformat(d.pop("joined_at"))

        is_primary = d.pop("is_primary")

        status = MemberStatus(d.pop("status"))

        def _parse_bot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                bot_id_type_0 = UUID(data)

                return bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        bot_id = _parse_bot_id(d.pop("bot_id", UNSET))

        def _parse_added_by_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                added_by_user_id_type_0 = UUID(data)

                return added_by_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        added_by_user_id = _parse_added_by_user_id(d.pop("added_by_user_id", UNSET))

        def _parse_user_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_email = _parse_user_email(d.pop("user_email", UNSET))

        def _parse_user_full_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_full_name = _parse_user_full_name(d.pop("user_full_name", UNSET))

        def _parse_bot_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bot_name = _parse_bot_name(d.pop("bot_name", UNSET))

        organization_member_response = cls(
            id=id,
            org_id=org_id,
            user_id=user_id,
            joined_at=joined_at,
            is_primary=is_primary,
            status=status,
            bot_id=bot_id,
            added_by_user_id=added_by_user_id,
            user_email=user_email,
            user_full_name=user_full_name,
            bot_name=bot_name,
        )

        organization_member_response.additional_properties = d
        return organization_member_response

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
