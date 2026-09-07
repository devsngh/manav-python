from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BotResponse")


@_attrs_define
class BotResponse:
    """Complete bot profile information.
    Role is derived from the owning user's user_roles, not stored per-bot.

        Attributes:
            id (UUID):
            user_id (UUID):
            bot_name (str):
            bot_identifier (str):
            profile_picture_url (None | str):
            position (None | str):
            about (None | str):
            age_in_days (int):
            registered_at (datetime.datetime):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
    """

    id: UUID
    user_id: UUID
    bot_name: str
    bot_identifier: str
    profile_picture_url: None | str
    position: None | str
    about: None | str
    age_in_days: int
    registered_at: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        user_id = str(self.user_id)

        bot_name = self.bot_name

        bot_identifier = self.bot_identifier

        profile_picture_url: None | str
        profile_picture_url = self.profile_picture_url

        position: None | str
        position = self.position

        about: None | str
        about = self.about

        age_in_days = self.age_in_days

        registered_at = self.registered_at.isoformat()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "bot_name": bot_name,
                "bot_identifier": bot_identifier,
                "profile_picture_url": profile_picture_url,
                "position": position,
                "about": about,
                "age_in_days": age_in_days,
                "registered_at": registered_at,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        user_id = UUID(d.pop("user_id"))

        bot_name = d.pop("bot_name")

        bot_identifier = d.pop("bot_identifier")

        def _parse_profile_picture_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        profile_picture_url = _parse_profile_picture_url(d.pop("profile_picture_url"))

        def _parse_position(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        position = _parse_position(d.pop("position"))

        def _parse_about(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        about = _parse_about(d.pop("about"))

        age_in_days = d.pop("age_in_days")

        registered_at = datetime.datetime.fromisoformat(d.pop("registered_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        bot_response = cls(
            id=id,
            user_id=user_id,
            bot_name=bot_name,
            bot_identifier=bot_identifier,
            profile_picture_url=profile_picture_url,
            position=position,
            about=about,
            age_in_days=age_in_days,
            registered_at=registered_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        bot_response.additional_properties = d
        return bot_response

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
