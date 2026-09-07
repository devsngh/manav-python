from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivationSummary")


@_attrs_define
class ActivationSummary:
    """Populated when `_first_boot_DONE.md` (or `first_boot_complete.md`) exists.

    The tower replaces the live stream with this card the moment boot
    is verified. Historical events are still reachable via link-to
    Agent Traces / Session Playback.

        Attributes:
            name (str):
            is_booted (bool):
            activated_at (datetime.datetime | None | Unset):
            completed_at (datetime.datetime | None | Unset):
            duration_min (float | None | Unset):
            total_events (int | Unset):  Default: 0.
            llm_calls (int | Unset):  Default: 0.
            mcp_calls (int | Unset):  Default: 0.
            file_writes (int | Unset):  Default: 0.
            total_cost_usd (float | Unset):  Default: 0.0.
            total_tokens (int | Unset):  Default: 0.
            error_count (int | Unset):  Default: 0.
            thread_ids (list[str] | Unset):
            phase_sentinels (list[str] | Unset):
            ratifier (None | str | Unset):
            completion_file (None | str | Unset):
    """

    name: str
    is_booted: bool
    activated_at: datetime.datetime | None | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    duration_min: float | None | Unset = UNSET
    total_events: int | Unset = 0
    llm_calls: int | Unset = 0
    mcp_calls: int | Unset = 0
    file_writes: int | Unset = 0
    total_cost_usd: float | Unset = 0.0
    total_tokens: int | Unset = 0
    error_count: int | Unset = 0
    thread_ids: list[str] | Unset = UNSET
    phase_sentinels: list[str] | Unset = UNSET
    ratifier: None | str | Unset = UNSET
    completion_file: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        is_booted = self.is_booted

        activated_at: None | str | Unset
        if isinstance(self.activated_at, Unset):
            activated_at = UNSET
        elif isinstance(self.activated_at, datetime.datetime):
            activated_at = self.activated_at.isoformat()
        else:
            activated_at = self.activated_at

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        duration_min: float | None | Unset
        if isinstance(self.duration_min, Unset):
            duration_min = UNSET
        else:
            duration_min = self.duration_min

        total_events = self.total_events

        llm_calls = self.llm_calls

        mcp_calls = self.mcp_calls

        file_writes = self.file_writes

        total_cost_usd = self.total_cost_usd

        total_tokens = self.total_tokens

        error_count = self.error_count

        thread_ids: list[str] | Unset = UNSET
        if not isinstance(self.thread_ids, Unset):
            thread_ids = self.thread_ids

        phase_sentinels: list[str] | Unset = UNSET
        if not isinstance(self.phase_sentinels, Unset):
            phase_sentinels = self.phase_sentinels

        ratifier: None | str | Unset
        if isinstance(self.ratifier, Unset):
            ratifier = UNSET
        else:
            ratifier = self.ratifier

        completion_file: None | str | Unset
        if isinstance(self.completion_file, Unset):
            completion_file = UNSET
        else:
            completion_file = self.completion_file

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "is_booted": is_booted,
            }
        )
        if activated_at is not UNSET:
            field_dict["activated_at"] = activated_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if duration_min is not UNSET:
            field_dict["duration_min"] = duration_min
        if total_events is not UNSET:
            field_dict["total_events"] = total_events
        if llm_calls is not UNSET:
            field_dict["llm_calls"] = llm_calls
        if mcp_calls is not UNSET:
            field_dict["mcp_calls"] = mcp_calls
        if file_writes is not UNSET:
            field_dict["file_writes"] = file_writes
        if total_cost_usd is not UNSET:
            field_dict["total_cost_usd"] = total_cost_usd
        if total_tokens is not UNSET:
            field_dict["total_tokens"] = total_tokens
        if error_count is not UNSET:
            field_dict["error_count"] = error_count
        if thread_ids is not UNSET:
            field_dict["thread_ids"] = thread_ids
        if phase_sentinels is not UNSET:
            field_dict["phase_sentinels"] = phase_sentinels
        if ratifier is not UNSET:
            field_dict["ratifier"] = ratifier
        if completion_file is not UNSET:
            field_dict["completion_file"] = completion_file

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        is_booted = d.pop("is_booted")

        def _parse_activated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                activated_at_type_0 = datetime.datetime.fromisoformat(data)

                return activated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        activated_at = _parse_activated_at(d.pop("activated_at", UNSET))

        def _parse_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = datetime.datetime.fromisoformat(data)

                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completed_at", UNSET))

        def _parse_duration_min(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration_min = _parse_duration_min(d.pop("duration_min", UNSET))

        total_events = d.pop("total_events", UNSET)

        llm_calls = d.pop("llm_calls", UNSET)

        mcp_calls = d.pop("mcp_calls", UNSET)

        file_writes = d.pop("file_writes", UNSET)

        total_cost_usd = d.pop("total_cost_usd", UNSET)

        total_tokens = d.pop("total_tokens", UNSET)

        error_count = d.pop("error_count", UNSET)

        thread_ids = cast(list[str], d.pop("thread_ids", UNSET))

        phase_sentinels = cast(list[str], d.pop("phase_sentinels", UNSET))

        def _parse_ratifier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ratifier = _parse_ratifier(d.pop("ratifier", UNSET))

        def _parse_completion_file(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completion_file = _parse_completion_file(d.pop("completion_file", UNSET))

        activation_summary = cls(
            name=name,
            is_booted=is_booted,
            activated_at=activated_at,
            completed_at=completed_at,
            duration_min=duration_min,
            total_events=total_events,
            llm_calls=llm_calls,
            mcp_calls=mcp_calls,
            file_writes=file_writes,
            total_cost_usd=total_cost_usd,
            total_tokens=total_tokens,
            error_count=error_count,
            thread_ids=thread_ids,
            phase_sentinels=phase_sentinels,
            ratifier=ratifier,
            completion_file=completion_file,
        )

        activation_summary.additional_properties = d
        return activation_summary

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
