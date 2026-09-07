from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BotInfo")


@_attrs_define
class BotInfo:
    """Basic bot information for conversation response

    Attributes:
        id (UUID):
        bot_name (str):
        bot_identifier (str):
        created_at (datetime.datetime):
        bot_type (None | str | Unset):
        description (None | str | Unset):
        profile_picture_url (None | str | Unset):
        is_active (bool | Unset):  Default: True.
        is_online (bool | Unset):  Default: False.
        last_active_at (datetime.datetime | None | Unset):
    """

    id: UUID
    bot_name: str
    bot_identifier: str
    created_at: datetime.datetime
    bot_type: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    profile_picture_url: None | str | Unset = UNSET
    is_active: bool | Unset = True
    is_online: bool | Unset = False
    last_active_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        bot_name = self.bot_name

        bot_identifier = self.bot_identifier

        created_at = self.created_at.isoformat()

        bot_type: None | str | Unset
        if isinstance(self.bot_type, Unset):
            bot_type = UNSET
        else:
            bot_type = self.bot_type

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        profile_picture_url: None | str | Unset
        if isinstance(self.profile_picture_url, Unset):
            profile_picture_url = UNSET
        else:
            profile_picture_url = self.profile_picture_url

        is_active = self.is_active

        is_online = self.is_online

        last_active_at: None | str | Unset
        if isinstance(self.last_active_at, Unset):
            last_active_at = UNSET
        elif isinstance(self.last_active_at, datetime.datetime):
            last_active_at = self.last_active_at.isoformat()
        else:
            last_active_at = self.last_active_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "bot_name": bot_name,
                "bot_identifier": bot_identifier,
                "created_at": created_at,
            }
        )
        if bot_type is not UNSET:
            field_dict["bot_type"] = bot_type
        if description is not UNSET:
            field_dict["description"] = description
        if profile_picture_url is not UNSET:
            field_dict["profile_picture_url"] = profile_picture_url
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_online is not UNSET:
            field_dict["is_online"] = is_online
        if last_active_at is not UNSET:
            field_dict["last_active_at"] = last_active_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        bot_name = d.pop("bot_name")

        bot_identifier = d.pop("bot_identifier")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_bot_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bot_type = _parse_bot_type(d.pop("bot_type", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_profile_picture_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_picture_url = _parse_profile_picture_url(d.pop("profile_picture_url", UNSET))

        is_active = d.pop("is_active", UNSET)

        is_online = d.pop("is_online", UNSET)

        def _parse_last_active_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_active_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_active_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_active_at = _parse_last_active_at(d.pop("last_active_at", UNSET))

        bot_info = cls(
            id=id,
            bot_name=bot_name,
            bot_identifier=bot_identifier,
            created_at=created_at,
            bot_type=bot_type,
            description=description,
            profile_picture_url=profile_picture_url,
            is_active=is_active,
            is_online=is_online,
            last_active_at=last_active_at,
        )

        bot_info.additional_properties = d
        return bot_info

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
