from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="BodyVoiceStreamApiVoiceStreamPost")


@_attrs_define
class BodyVoiceStreamApiVoiceStreamPost:
    """
    Attributes:
        audio (File): Audio file from microphone
        thread_id (str): Chat thread ID
        prefer_bot_id (None | str | Unset): Preferred bot ID
    """

    audio: File
    thread_id: str
    prefer_bot_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audio = self.audio.to_tuple()

        thread_id = self.thread_id

        prefer_bot_id: None | str | Unset
        if isinstance(self.prefer_bot_id, Unset):
            prefer_bot_id = UNSET
        else:
            prefer_bot_id = self.prefer_bot_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "audio": audio,
                "thread_id": thread_id,
            }
        )
        if prefer_bot_id is not UNSET:
            field_dict["prefer_bot_id"] = prefer_bot_id

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("audio", self.audio.to_tuple()))

        files.append(("thread_id", (None, str(self.thread_id).encode(), "text/plain")))

        if not isinstance(self.prefer_bot_id, Unset):
            if isinstance(self.prefer_bot_id, str):
                files.append(("prefer_bot_id", (None, str(self.prefer_bot_id).encode(), "text/plain")))
            else:
                files.append(("prefer_bot_id", (None, str(self.prefer_bot_id).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        audio = File(payload=BytesIO(d.pop("audio")))

        thread_id = d.pop("thread_id")

        def _parse_prefer_bot_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prefer_bot_id = _parse_prefer_bot_id(d.pop("prefer_bot_id", UNSET))

        body_voice_stream_api_voice_stream_post = cls(
            audio=audio,
            thread_id=thread_id,
            prefer_bot_id=prefer_bot_id,
        )

        body_voice_stream_api_voice_stream_post.additional_properties = d
        return body_voice_stream_api_voice_stream_post

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
