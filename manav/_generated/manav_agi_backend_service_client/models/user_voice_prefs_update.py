from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserVoicePrefsUpdate")


@_attrs_define
class UserVoicePrefsUpdate:
    """User's personal voice preferences.

    Attributes:
        wake_word_enabled (bool | None | Unset):
    """

    wake_word_enabled: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wake_word_enabled: bool | None | Unset
        if isinstance(self.wake_word_enabled, Unset):
            wake_word_enabled = UNSET
        else:
            wake_word_enabled = self.wake_word_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wake_word_enabled is not UNSET:
            field_dict["wake_word_enabled"] = wake_word_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_wake_word_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        wake_word_enabled = _parse_wake_word_enabled(d.pop("wake_word_enabled", UNSET))

        user_voice_prefs_update = cls(
            wake_word_enabled=wake_word_enabled,
        )

        user_voice_prefs_update.additional_properties = d
        return user_voice_prefs_update

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
