from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfileResponse")


@_attrs_define
class ProfileResponse:
    """Unified user-or-bot profile, used by the ProfileWindow.

    Most fields are optional so we can return whatever's available; UI
    decides how to render based on `kind`.

        Attributes:
            kind (str):
            id (UUID):
            name (str):
            avatar_url (None | str | Unset):
            role (None | str | Unset):
            email (None | str | Unset):
            bot_identifier (None | str | Unset):
            org_id (None | Unset | UUID):
            department (None | str | Unset):
            is_active (bool | Unset):  Default: True.
            joined_at (datetime.datetime | None | Unset):
            last_seen_at (datetime.datetime | None | Unset):
            recent_threads (list[str] | Unset):
    """

    kind: str
    id: UUID
    name: str
    avatar_url: None | str | Unset = UNSET
    role: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    bot_identifier: None | str | Unset = UNSET
    org_id: None | Unset | UUID = UNSET
    department: None | str | Unset = UNSET
    is_active: bool | Unset = True
    joined_at: datetime.datetime | None | Unset = UNSET
    last_seen_at: datetime.datetime | None | Unset = UNSET
    recent_threads: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        id = str(self.id)

        name = self.name

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        bot_identifier: None | str | Unset
        if isinstance(self.bot_identifier, Unset):
            bot_identifier = UNSET
        else:
            bot_identifier = self.bot_identifier

        org_id: None | str | Unset
        if isinstance(self.org_id, Unset):
            org_id = UNSET
        elif isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

        department: None | str | Unset
        if isinstance(self.department, Unset):
            department = UNSET
        else:
            department = self.department

        is_active = self.is_active

        joined_at: None | str | Unset
        if isinstance(self.joined_at, Unset):
            joined_at = UNSET
        elif isinstance(self.joined_at, datetime.datetime):
            joined_at = self.joined_at.isoformat()
        else:
            joined_at = self.joined_at

        last_seen_at: None | str | Unset
        if isinstance(self.last_seen_at, Unset):
            last_seen_at = UNSET
        elif isinstance(self.last_seen_at, datetime.datetime):
            last_seen_at = self.last_seen_at.isoformat()
        else:
            last_seen_at = self.last_seen_at

        recent_threads: list[str] | Unset = UNSET
        if not isinstance(self.recent_threads, Unset):
            recent_threads = self.recent_threads

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "id": id,
                "name": name,
            }
        )
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if role is not UNSET:
            field_dict["role"] = role
        if email is not UNSET:
            field_dict["email"] = email
        if bot_identifier is not UNSET:
            field_dict["bot_identifier"] = bot_identifier
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if department is not UNSET:
            field_dict["department"] = department
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if joined_at is not UNSET:
            field_dict["joined_at"] = joined_at
        if last_seen_at is not UNSET:
            field_dict["last_seen_at"] = last_seen_at
        if recent_threads is not UNSET:
            field_dict["recent_threads"] = recent_threads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = d.pop("kind")

        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatar_url", UNSET))

        def _parse_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role = _parse_role(d.pop("role", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_bot_identifier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bot_identifier = _parse_bot_identifier(d.pop("bot_identifier", UNSET))

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

        def _parse_department(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        department = _parse_department(d.pop("department", UNSET))

        is_active = d.pop("is_active", UNSET)

        def _parse_joined_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                joined_at_type_0 = datetime.datetime.fromisoformat(data)

                return joined_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        joined_at = _parse_joined_at(d.pop("joined_at", UNSET))

        def _parse_last_seen_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_seen_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_seen_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_seen_at = _parse_last_seen_at(d.pop("last_seen_at", UNSET))

        recent_threads = cast(list[str], d.pop("recent_threads", UNSET))

        profile_response = cls(
            kind=kind,
            id=id,
            name=name,
            avatar_url=avatar_url,
            role=role,
            email=email,
            bot_identifier=bot_identifier,
            org_id=org_id,
            department=department,
            is_active=is_active,
            joined_at=joined_at,
            last_seen_at=last_seen_at,
            recent_threads=recent_threads,
        )

        profile_response.additional_properties = d
        return profile_response

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
