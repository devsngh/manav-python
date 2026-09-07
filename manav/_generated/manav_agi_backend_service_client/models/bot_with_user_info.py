from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bot_with_user_info_organizations_type_0_item import BotWithUserInfoOrganizationsType0Item


T = TypeVar("T", bound="BotWithUserInfo")


@_attrs_define
class BotWithUserInfo:
    """Bot with user and organization information.
    Role is derived from the owning user's user_roles, not stored per-bot.

        Attributes:
            id (UUID):
            bot_name (str):
            bot_identifier (str):
            profile_picture_url (None | str):
            about (None | str):
            is_active (bool):
            last_active_at (datetime.datetime | None):
            registered_at (datetime.datetime):
            created_at (datetime.datetime):
            user_id (UUID):
            user_email (None | str):
            user_full_name (None | str):
            organizations (list[BotWithUserInfoOrganizationsType0Item] | None | Unset):
    """

    id: UUID
    bot_name: str
    bot_identifier: str
    profile_picture_url: None | str
    about: None | str
    is_active: bool
    last_active_at: datetime.datetime | None
    registered_at: datetime.datetime
    created_at: datetime.datetime
    user_id: UUID
    user_email: None | str
    user_full_name: None | str
    organizations: list[BotWithUserInfoOrganizationsType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        bot_name = self.bot_name

        bot_identifier = self.bot_identifier

        profile_picture_url: None | str
        profile_picture_url = self.profile_picture_url

        about: None | str
        about = self.about

        is_active = self.is_active

        last_active_at: None | str
        if isinstance(self.last_active_at, datetime.datetime):
            last_active_at = self.last_active_at.isoformat()
        else:
            last_active_at = self.last_active_at

        registered_at = self.registered_at.isoformat()

        created_at = self.created_at.isoformat()

        user_id = str(self.user_id)

        user_email: None | str
        user_email = self.user_email

        user_full_name: None | str
        user_full_name = self.user_full_name

        organizations: list[dict[str, Any]] | None | Unset
        if isinstance(self.organizations, Unset):
            organizations = UNSET
        elif isinstance(self.organizations, list):
            organizations = []
            for organizations_type_0_item_data in self.organizations:
                organizations_type_0_item = organizations_type_0_item_data.to_dict()
                organizations.append(organizations_type_0_item)

        else:
            organizations = self.organizations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "bot_name": bot_name,
                "bot_identifier": bot_identifier,
                "profile_picture_url": profile_picture_url,
                "about": about,
                "is_active": is_active,
                "last_active_at": last_active_at,
                "registered_at": registered_at,
                "created_at": created_at,
                "user_id": user_id,
                "user_email": user_email,
                "user_full_name": user_full_name,
            }
        )
        if organizations is not UNSET:
            field_dict["organizations"] = organizations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bot_with_user_info_organizations_type_0_item import (
            BotWithUserInfoOrganizationsType0Item,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        bot_name = d.pop("bot_name")

        bot_identifier = d.pop("bot_identifier")

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

        is_active = d.pop("is_active")

        def _parse_last_active_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_active_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_active_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_active_at = _parse_last_active_at(d.pop("last_active_at"))

        registered_at = datetime.datetime.fromisoformat(d.pop("registered_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        user_id = UUID(d.pop("user_id"))

        def _parse_user_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        user_email = _parse_user_email(d.pop("user_email"))

        def _parse_user_full_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        user_full_name = _parse_user_full_name(d.pop("user_full_name"))

        def _parse_organizations(data: object) -> list[BotWithUserInfoOrganizationsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                organizations_type_0 = []
                _organizations_type_0 = data
                for organizations_type_0_item_data in _organizations_type_0:
                    organizations_type_0_item = BotWithUserInfoOrganizationsType0Item.from_dict(
                        organizations_type_0_item_data
                    )

                    organizations_type_0.append(organizations_type_0_item)

                return organizations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BotWithUserInfoOrganizationsType0Item] | None | Unset, data)

        organizations = _parse_organizations(d.pop("organizations", UNSET))

        bot_with_user_info = cls(
            id=id,
            bot_name=bot_name,
            bot_identifier=bot_identifier,
            profile_picture_url=profile_picture_url,
            about=about,
            is_active=is_active,
            last_active_at=last_active_at,
            registered_at=registered_at,
            created_at=created_at,
            user_id=user_id,
            user_email=user_email,
            user_full_name=user_full_name,
            organizations=organizations,
        )

        bot_with_user_info.additional_properties = d
        return bot_with_user_info

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
