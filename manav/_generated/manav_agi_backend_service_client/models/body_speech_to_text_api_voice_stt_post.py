from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="BodySpeechToTextApiVoiceSttPost")


@_attrs_define
class BodySpeechToTextApiVoiceSttPost:
    """
    Attributes:
        audio (File): Audio file (webm, mp3, wav, etc.)
        provider (None | str | Unset): STT provider: openai or google
    """

    audio: File
    provider: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audio = self.audio.to_tuple()

        provider: None | str | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "audio": audio,
            }
        )
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("audio", self.audio.to_tuple()))

        if not isinstance(self.provider, Unset):
            if isinstance(self.provider, str):
                files.append(("provider", (None, str(self.provider).encode(), "text/plain")))
            else:
                files.append(("provider", (None, str(self.provider).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        audio = File(payload=BytesIO(d.pop("audio")))

        def _parse_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider = _parse_provider(d.pop("provider", UNSET))

        body_speech_to_text_api_voice_stt_post = cls(
            audio=audio,
            provider=provider,
        )

        body_speech_to_text_api_voice_stt_post.additional_properties = d
        return body_speech_to_text_api_voice_stt_post

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
