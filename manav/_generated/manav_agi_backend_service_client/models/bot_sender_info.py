from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BotSenderInfo")


@_attrs_define
class BotSenderInfo:
    """Minimal bot profile for message sender display

    Attributes:
        id (UUID):
        bot_name (str):
        profile_picture_url (None | str | Unset):
        is_online (bool | Unset):  Default: False.
    """

    id: UUID
    bot_name: str
    profile_picture_url: None | str | Unset = UNSET
    is_online: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        bot_name = self.bot_name

        profile_picture_url: None | str | Unset
        if isinstance(self.profile_picture_url, Unset):
            profile_picture_url = UNSET
        else:
            profile_picture_url = self.profile_picture_url

        is_online = self.is_online

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "bot_name": bot_name,
            }
        )
        if profile_picture_url is not UNSET:
            field_dict["profile_picture_url"] = profile_picture_url
        if is_online is not UNSET:
            field_dict["is_online"] = is_online

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        bot_name = d.pop("bot_name")

        def _parse_profile_picture_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_picture_url = _parse_profile_picture_url(d.pop("profile_picture_url", UNSET))

        is_online = d.pop("is_online", UNSET)

        bot_sender_info = cls(
            id=id,
            bot_name=bot_name,
            profile_picture_url=profile_picture_url,
            is_online=is_online,
        )

        bot_sender_info.additional_properties = d
        return bot_sender_info

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
