from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VoiceConfigUpdate")


@_attrs_define
class VoiceConfigUpdate:
    """Update voice configuration. Only include fields you want to change.

    Attributes:
        stt_provider (None | str | Unset):
        tts_provider (None | str | Unset):
        tts_voice (None | str | Unset):
        voice_chat_enabled (None | str | Unset):
        wake_word_enabled (None | str | Unset):
        wake_word_keyword (None | str | Unset):
    """

    stt_provider: None | str | Unset = UNSET
    tts_provider: None | str | Unset = UNSET
    tts_voice: None | str | Unset = UNSET
    voice_chat_enabled: None | str | Unset = UNSET
    wake_word_enabled: None | str | Unset = UNSET
    wake_word_keyword: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stt_provider: None | str | Unset
        if isinstance(self.stt_provider, Unset):
            stt_provider = UNSET
        else:
            stt_provider = self.stt_provider

        tts_provider: None | str | Unset
        if isinstance(self.tts_provider, Unset):
            tts_provider = UNSET
        else:
            tts_provider = self.tts_provider

        tts_voice: None | str | Unset
        if isinstance(self.tts_voice, Unset):
            tts_voice = UNSET
        else:
            tts_voice = self.tts_voice

        voice_chat_enabled: None | str | Unset
        if isinstance(self.voice_chat_enabled, Unset):
            voice_chat_enabled = UNSET
        else:
            voice_chat_enabled = self.voice_chat_enabled

        wake_word_enabled: None | str | Unset
        if isinstance(self.wake_word_enabled, Unset):
            wake_word_enabled = UNSET
        else:
            wake_word_enabled = self.wake_word_enabled

        wake_word_keyword: None | str | Unset
        if isinstance(self.wake_word_keyword, Unset):
            wake_word_keyword = UNSET
        else:
            wake_word_keyword = self.wake_word_keyword

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stt_provider is not UNSET:
            field_dict["stt_provider"] = stt_provider
        if tts_provider is not UNSET:
            field_dict["tts_provider"] = tts_provider
        if tts_voice is not UNSET:
            field_dict["tts_voice"] = tts_voice
        if voice_chat_enabled is not UNSET:
            field_dict["voice_chat_enabled"] = voice_chat_enabled
        if wake_word_enabled is not UNSET:
            field_dict["wake_word_enabled"] = wake_word_enabled
        if wake_word_keyword is not UNSET:
            field_dict["wake_word_keyword"] = wake_word_keyword

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_stt_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stt_provider = _parse_stt_provider(d.pop("stt_provider", UNSET))

        def _parse_tts_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tts_provider = _parse_tts_provider(d.pop("tts_provider", UNSET))

        def _parse_tts_voice(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tts_voice = _parse_tts_voice(d.pop("tts_voice", UNSET))

        def _parse_voice_chat_enabled(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        voice_chat_enabled = _parse_voice_chat_enabled(d.pop("voice_chat_enabled", UNSET))

        def _parse_wake_word_enabled(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wake_word_enabled = _parse_wake_word_enabled(d.pop("wake_word_enabled", UNSET))

        def _parse_wake_word_keyword(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wake_word_keyword = _parse_wake_word_keyword(d.pop("wake_word_keyword", UNSET))

        voice_config_update = cls(
            stt_provider=stt_provider,
            tts_provider=tts_provider,
            tts_voice=tts_voice,
            voice_chat_enabled=voice_chat_enabled,
            wake_word_enabled=wake_word_enabled,
            wake_word_keyword=wake_word_keyword,
        )

        voice_config_update.additional_properties = d
        return voice_config_update

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
