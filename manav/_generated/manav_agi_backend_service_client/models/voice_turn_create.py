from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.voice_turn_create_speaker import VoiceTurnCreateSpeaker
from ..types import UNSET, Unset

T = TypeVar("T", bound="VoiceTurnCreate")


@_attrs_define
class VoiceTurnCreate:
    """Body sent by voice_bridge_service when persisting a new turn.

    Attributes:
        turn_index (int):
        speaker (VoiceTurnCreateSpeaker):
        text (str):
        spoken_at (datetime.datetime | None | Unset):
        duration_ms (int | None | Unset):
        tokens_in (int | None | Unset):
        tokens_out (int | None | Unset):
        response_id (None | str | Unset):
        item_id (None | str | Unset):
    """

    turn_index: int
    speaker: VoiceTurnCreateSpeaker
    text: str
    spoken_at: datetime.datetime | None | Unset = UNSET
    duration_ms: int | None | Unset = UNSET
    tokens_in: int | None | Unset = UNSET
    tokens_out: int | None | Unset = UNSET
    response_id: None | str | Unset = UNSET
    item_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        turn_index = self.turn_index

        speaker = self.speaker.value

        text = self.text

        spoken_at: None | str | Unset
        if isinstance(self.spoken_at, Unset):
            spoken_at = UNSET
        elif isinstance(self.spoken_at, datetime.datetime):
            spoken_at = self.spoken_at.isoformat()
        else:
            spoken_at = self.spoken_at

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
                "turn_index": turn_index,
                "speaker": speaker,
                "text": text,
            }
        )
        if spoken_at is not UNSET:
            field_dict["spoken_at"] = spoken_at
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
        turn_index = d.pop("turn_index")

        speaker = VoiceTurnCreateSpeaker(d.pop("speaker"))

        text = d.pop("text")

        def _parse_spoken_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                spoken_at_type_0 = datetime.datetime.fromisoformat(data)

                return spoken_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        spoken_at = _parse_spoken_at(d.pop("spoken_at", UNSET))

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

        voice_turn_create = cls(
            turn_index=turn_index,
            speaker=speaker,
            text=text,
            spoken_at=spoken_at,
            duration_ms=duration_ms,
            tokens_in=tokens_in,
            tokens_out=tokens_out,
            response_id=response_id,
            item_id=item_id,
        )

        voice_turn_create.additional_properties = d
        return voice_turn_create

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
