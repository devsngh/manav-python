from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.debate_event_detail import DebateEventDetail


T = TypeVar("T", bound="DebateEvent")


@_attrs_define
class DebateEvent:
    """One row in a debate's merged event timeline.

    Kinds surfaced today (extend as more sources land):
      speaker_post      — a message posted in the debate group by a
                          participant who is NOT the moderator
      moderator_message — a message from the moderator (framing, cue,
                          ruling, phase transition marker)
      procedural_violation — a score_event with event_type in the
                          procedural bucket (bare_assertion,
                          out_of_turn_in_debate, personal_attack)
      state_change      — reserved; requires audit trail (Wave 4B v2)

        Attributes:
            ts (datetime.datetime):
            kind (str):
            summary (str):
            sender_id (None | Unset | UUID):
            sender_type (None | str | Unset):
            message_id (None | Unset | UUID):
            score_event_id (None | Unset | UUID):
            content_length (int | None | Unset):
            detail (DebateEventDetail | Unset):
            anomalies (list[str] | Unset):
    """

    ts: datetime.datetime
    kind: str
    summary: str
    sender_id: None | Unset | UUID = UNSET
    sender_type: None | str | Unset = UNSET
    message_id: None | Unset | UUID = UNSET
    score_event_id: None | Unset | UUID = UNSET
    content_length: int | None | Unset = UNSET
    detail: DebateEventDetail | Unset = UNSET
    anomalies: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ts = self.ts.isoformat()

        kind = self.kind

        summary = self.summary

        sender_id: None | str | Unset
        if isinstance(self.sender_id, Unset):
            sender_id = UNSET
        elif isinstance(self.sender_id, UUID):
            sender_id = str(self.sender_id)
        else:
            sender_id = self.sender_id

        sender_type: None | str | Unset
        if isinstance(self.sender_type, Unset):
            sender_type = UNSET
        else:
            sender_type = self.sender_type

        message_id: None | str | Unset
        if isinstance(self.message_id, Unset):
            message_id = UNSET
        elif isinstance(self.message_id, UUID):
            message_id = str(self.message_id)
        else:
            message_id = self.message_id

        score_event_id: None | str | Unset
        if isinstance(self.score_event_id, Unset):
            score_event_id = UNSET
        elif isinstance(self.score_event_id, UUID):
            score_event_id = str(self.score_event_id)
        else:
            score_event_id = self.score_event_id

        content_length: int | None | Unset
        if isinstance(self.content_length, Unset):
            content_length = UNSET
        else:
            content_length = self.content_length

        detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.detail, Unset):
            detail = self.detail.to_dict()

        anomalies: list[str] | Unset = UNSET
        if not isinstance(self.anomalies, Unset):
            anomalies = self.anomalies

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ts": ts,
                "kind": kind,
                "summary": summary,
            }
        )
        if sender_id is not UNSET:
            field_dict["sender_id"] = sender_id
        if sender_type is not UNSET:
            field_dict["sender_type"] = sender_type
        if message_id is not UNSET:
            field_dict["message_id"] = message_id
        if score_event_id is not UNSET:
            field_dict["score_event_id"] = score_event_id
        if content_length is not UNSET:
            field_dict["content_length"] = content_length
        if detail is not UNSET:
            field_dict["detail"] = detail
        if anomalies is not UNSET:
            field_dict["anomalies"] = anomalies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.debate_event_detail import DebateEventDetail  # noqa: PLC0415

        d = dict(src_dict)
        ts = datetime.datetime.fromisoformat(d.pop("ts"))

        kind = d.pop("kind")

        summary = d.pop("summary")

        def _parse_sender_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sender_id_type_0 = UUID(data)

                return sender_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        sender_id = _parse_sender_id(d.pop("sender_id", UNSET))

        def _parse_sender_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender_type = _parse_sender_type(d.pop("sender_type", UNSET))

        def _parse_message_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                message_id_type_0 = UUID(data)

                return message_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        message_id = _parse_message_id(d.pop("message_id", UNSET))

        def _parse_score_event_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                score_event_id_type_0 = UUID(data)

                return score_event_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        score_event_id = _parse_score_event_id(d.pop("score_event_id", UNSET))

        def _parse_content_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        content_length = _parse_content_length(d.pop("content_length", UNSET))

        _detail = d.pop("detail", UNSET)
        detail: DebateEventDetail | Unset
        if isinstance(_detail, Unset):
            detail = UNSET
        else:
            detail = DebateEventDetail.from_dict(_detail)

        anomalies = cast(list[str], d.pop("anomalies", UNSET))

        debate_event = cls(
            ts=ts,
            kind=kind,
            summary=summary,
            sender_id=sender_id,
            sender_type=sender_type,
            message_id=message_id,
            score_event_id=score_event_id,
            content_length=content_length,
            detail=detail,
            anomalies=anomalies,
        )

        debate_event.additional_properties = d
        return debate_event

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
