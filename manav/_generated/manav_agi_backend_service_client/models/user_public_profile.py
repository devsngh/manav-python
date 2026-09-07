from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserPublicProfile")


@_attrs_define
class UserPublicProfile:
    """Public profile for viewing other users (excludes sensitive data)

    Attributes:
        id (UUID):
        full_name (str):
        email (str):
        profile_picture_url (None | str):
        about (None | str):
        position (None | str):
        phone_number (None | str):
        created_at (datetime.datetime):
        is_online (bool | Unset):  Default: False.
        last_seen_at (datetime.datetime | None | Unset):
    """

    id: UUID
    full_name: str
    email: str
    profile_picture_url: None | str
    about: None | str
    position: None | str
    phone_number: None | str
    created_at: datetime.datetime
    is_online: bool | Unset = False
    last_seen_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        full_name = self.full_name

        email = self.email

        profile_picture_url: None | str
        profile_picture_url = self.profile_picture_url

        about: None | str
        about = self.about

        position: None | str
        position = self.position

        phone_number: None | str
        phone_number = self.phone_number

        created_at = self.created_at.isoformat()

        is_online = self.is_online

        last_seen_at: None | str | Unset
        if isinstance(self.last_seen_at, Unset):
            last_seen_at = UNSET
        elif isinstance(self.last_seen_at, datetime.datetime):
            last_seen_at = self.last_seen_at.isoformat()
        else:
            last_seen_at = self.last_seen_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "full_name": full_name,
                "email": email,
                "profile_picture_url": profile_picture_url,
                "about": about,
                "position": position,
                "phone_number": phone_number,
                "created_at": created_at,
            }
        )
        if is_online is not UNSET:
            field_dict["is_online"] = is_online
        if last_seen_at is not UNSET:
            field_dict["last_seen_at"] = last_seen_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        full_name = d.pop("full_name")

        email = d.pop("email")

        def _parse_profile_picture_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        profile_picture_url = _parse_profile_picture_url(d.pop("profile_picture_url"))

        def _parse_about(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        about = _parse_about(d.pop("about"))

        def _parse_position(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        position = _parse_position(d.pop("position"))

        def _parse_phone_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        phone_number = _parse_phone_number(d.pop("phone_number"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        is_online = d.pop("is_online", UNSET)

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

        user_public_profile = cls(
            id=id,
            full_name=full_name,
            email=email,
            profile_picture_url=profile_picture_url,
            about=about,
            position=position,
            phone_number=phone_number,
            created_at=created_at,
            is_online=is_online,
            last_seen_at=last_seen_at,
        )

        user_public_profile.additional_properties = d
        return user_public_profile

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
