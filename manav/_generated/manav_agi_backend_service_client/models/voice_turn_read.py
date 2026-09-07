from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.voice_turn_read_speaker import VoiceTurnReadSpeaker
from ..types import UNSET, Unset

T = TypeVar("T", bound="VoiceTurnRead")


@_attrs_define
class VoiceTurnRead:
    """
    Attributes:
        id (UUID):
        turn_index (int):
        speaker (VoiceTurnReadSpeaker):
        text (str):
        spoken_at (datetime.datetime):
        audio_asset_id (None | Unset | UUID):
        duration_ms (int | None | Unset):
        tokens_in (int | None | Unset):
        tokens_out (int | None | Unset):
        response_id (None | str | Unset):
        item_id (None | str | Unset):
    """

    id: UUID
    turn_index: int
    speaker: VoiceTurnReadSpeaker
    text: str
    spoken_at: datetime.datetime
    audio_asset_id: None | Unset | UUID = UNSET
    duration_ms: int | None | Unset = UNSET
    tokens_in: int | None | Unset = UNSET
    tokens_out: int | None | Unset = UNSET
    response_id: None | str | Unset = UNSET
    item_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        turn_index = self.turn_index

        speaker = self.speaker.value

        text = self.text

        spoken_at = self.spoken_at.isoformat()

        audio_asset_id: None | str | Unset
        if isinstance(self.audio_asset_id, Unset):
            audio_asset_id = UNSET
        elif isinstance(self.audio_asset_id, UUID):
            audio_asset_id = str(self.audio_asset_id)
        else:
            audio_asset_id = self.audio_asset_id

        duration_ms: int | None | Unset
        if isinstance(self.duration_ms, Unset):
            duration_ms = UNSET
        else:
            duration_ms = self.duration_ms

        tokens_in: int | None | Unset
        if isinstance(self.tokens_in, Unset):
            tokens_in = UNSET
        else:
            tokens_in = self.tokens_in

        tokens_out: int | None | Unset
        if isinstance(self.tokens_out, Unset):
            tokens_out = UNSET
        else:
            tokens_out = self.tokens_out

        response_id: None | str | Unset
        if isinstance(self.response_id, Unset):
            response_id = UNSET
        else:
            response_id = self.response_id

        item_id: None | str | Unset
        if isinstance(self.item_id, Unset):
            item_id = UNSET
        else:
            item_id = self.item_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "turn_index": turn_index,
                "speaker": speaker,
                "text": text,
                "spoken_at": spoken_at,
            }
        )
        if audio_asset_id is not UNSET:
            field_dict["audio_asset_id"] = audio_asset_id
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if tokens_in is not UNSET:
            field_dict["tokens_in"] = tokens_in
        if tokens_out is not UNSET:
            field_dict["tokens_out"] = tokens_out
        if response_id is not UNSET:
            field_dict["response_id"] = response_id
        if item_id is not UNSET:
            field_dict["item_id"] = item_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        turn_index = d.pop("turn_index")

        speaker = VoiceTurnReadSpeaker(d.pop("speaker"))

        text = d.pop("text")

        spoken_at = datetime.datetime.fromisoformat(d.pop("spoken_at"))

        def _parse_audio_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                audio_asset_id_type_0 = UUID(data)

                return audio_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        audio_asset_id = _parse_audio_asset_id(d.pop("audio_asset_id", UNSET))

        def _parse_duration_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_ms = _parse_duration_ms(d.pop("duration_ms", UNSET))

        def _parse_tokens_in(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tokens_in = _parse_tokens_in(d.pop("tokens_in", UNSET))

        def _parse_tokens_out(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tokens_out = _parse_tokens_out(d.pop("tokens_out", UNSET))

        def _parse_response_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        response_id = _parse_response_id(d.pop("response_id", UNSET))

        def _parse_item_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        item_id = _parse_item_id(d.pop("item_id", UNSET))

        voice_turn_read = cls(
            id=id,
            turn_index=turn_index,
            speaker=speaker,
            text=text,
            spoken_at=spoken_at,
            audio_asset_id=audio_asset_id,
            duration_ms=duration_ms,
            tokens_in=tokens_in,
            tokens_out=tokens_out,
            response_id=response_id,
            item_id=item_id,
        )

        voice_turn_read.additional_properties = d
        return voice_turn_read

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
