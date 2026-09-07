from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DebateMetrics")


@_attrs_define
class DebateMetrics:
    """Pre-aggregated tile data for the Control Tower hero. Cheap:
    counts + phase durations. Anything expensive (per-bot token spend,
    procedural-density trend) lives in separate endpoints.

        Attributes:
            debate_id (UUID):
            total_events (int):
            speaker_turns (int):
            moderator_messages (int):
            procedural_violations (int):
            duplicate_filings (int):
            short_messages (int):
            wall_clock_seconds (int):
            started_at (datetime.datetime):
            current_phase (str):
            is_active (bool):
            concluded_at (datetime.datetime | None | Unset):
    """

    debate_id: UUID
    total_events: int
    speaker_turns: int
    moderator_messages: int
    procedural_violations: int
    duplicate_filings: int
    short_messages: int
    wall_clock_seconds: int
    started_at: datetime.datetime
    current_phase: str
    is_active: bool
    concluded_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        debate_id = str(self.debate_id)

        total_events = self.total_events

        speaker_turns = self.speaker_turns

        moderator_messages = self.moderator_messages

        procedural_violations = self.procedural_violations

        duplicate_filings = self.duplicate_filings

        short_messages = self.short_messages

        wall_clock_seconds = self.wall_clock_seconds

        started_at = self.started_at.isoformat()

        current_phase = self.current_phase

        is_active = self.is_active

        concluded_at: None | str | Unset
        if isinstance(self.concluded_at, Unset):
            concluded_at = UNSET
        elif isinstance(self.concluded_at, datetime.datetime):
            concluded_at = self.concluded_at.isoformat()
        else:
            concluded_at = self.concluded_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "debate_id": debate_id,
                "total_events": total_events,
                "speaker_turns": speaker_turns,
                "moderator_messages": moderator_messages,
                "procedural_violations": procedural_violations,
                "duplicate_filings": duplicate_filings,
                "short_messages": short_messages,
                "wall_clock_seconds": wall_clock_seconds,
                "started_at": started_at,
                "current_phase": current_phase,
                "is_active": is_active,
            }
        )
        if concluded_at is not UNSET:
            field_dict["concluded_at"] = concluded_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        debate_id = UUID(d.pop("debate_id"))

        total_events = d.pop("total_events")

        speaker_turns = d.pop("speaker_turns")

        moderator_messages = d.pop("moderator_messages")

        procedural_violations = d.pop("procedural_violations")

        duplicate_filings = d.pop("duplicate_filings")

        short_messages = d.pop("short_messages")

        wall_clock_seconds = d.pop("wall_clock_seconds")

        started_at = datetime.datetime.fromisoformat(d.pop("started_at"))

        current_phase = d.pop("current_phase")

        is_active = d.pop("is_active")

        def _parse_concluded_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                concluded_at_type_0 = datetime.datetime.fromisoformat(data)

                return concluded_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        concluded_at = _parse_concluded_at(d.pop("concluded_at", UNSET))

        debate_metrics = cls(
            debate_id=debate_id,
            total_events=total_events,
            speaker_turns=speaker_turns,
            moderator_messages=moderator_messages,
            procedural_violations=procedural_violations,
            duplicate_filings=duplicate_filings,
            short_messages=short_messages,
            wall_clock_seconds=wall_clock_seconds,
            started_at=started_at,
            current_phase=current_phase,
            is_active=is_active,
            concluded_at=concluded_at,
        )

        debate_metrics.additional_properties = d
        return debate_metrics

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
