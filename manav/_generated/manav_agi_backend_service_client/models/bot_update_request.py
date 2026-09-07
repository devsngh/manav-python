from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BotUpdateRequest")


@_attrs_define
class BotUpdateRequest:
    """User can update their bot's name and about

    Attributes:
        bot_name (None | str | Unset): Bot name
        about (None | str | Unset): Bot description
    """

    bot_name: None | str | Unset = UNSET
    about: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bot_name: None | str | Unset
        if isinstance(self.bot_name, Unset):
            bot_name = UNSET
        else:
            bot_name = self.bot_name

        about: None | str | Unset
        if isinstance(self.about, Unset):
            about = UNSET
        else:
            about = self.about

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bot_name is not UNSET:
            field_dict["bot_name"] = bot_name
        if about is not UNSET:
            field_dict["about"] = about

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_bot_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bot_name = _parse_bot_name(d.pop("bot_name", UNSET))

        def _parse_about(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        about = _parse_about(d.pop("about", UNSET))

        bot_update_request = cls(
            bot_name=bot_name,
            about=about,
        )

        bot_update_request.additional_properties = d
        return bot_update_request

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
