from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ThreadSummary")


@_attrs_define
class ThreadSummary:
    """Panel-2 hero card metrics for one thread.

    Populated from dialogue_costs (pre-materialized) — no on-the-fly span
    aggregation. If dialogue_costs is empty for the thread (e.g., no
    completed dialogues yet), values fall back to zero and the frontend
    shows "—" placeholders.

        Attributes:
            source_type (str):
            source_id (str):
            title (str | Unset):  Default: ''.
            turn_count (int | Unset):  Default: 0.
            total_llm_calls (int | Unset):  Default: 0.
            total_tool_calls (int | Unset):  Default: 0.
            total_input_tokens (int | Unset):  Default: 0.
            total_output_tokens (int | Unset):  Default: 0.
            total_tokens (int | Unset):  Default: 0.
            total_cost_usd (float | Unset):  Default: 0.0.
            total_duration_ms (int | Unset):  Default: 0.
            error_count (int | Unset):  Default: 0.
            first_activity (datetime.datetime | None | Unset):
            last_activity (datetime.datetime | None | Unset):
            participants (list[str] | Unset):
    """

    source_type: str
    source_id: str
    title: str | Unset = ""
    turn_count: int | Unset = 0
    total_llm_calls: int | Unset = 0
    total_tool_calls: int | Unset = 0
    total_input_tokens: int | Unset = 0
    total_output_tokens: int | Unset = 0
    total_tokens: int | Unset = 0
    total_cost_usd: float | Unset = 0.0
    total_duration_ms: int | Unset = 0
    error_count: int | Unset = 0
    first_activity: datetime.datetime | None | Unset = UNSET
    last_activity: datetime.datetime | None | Unset = UNSET
    participants: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_type = self.source_type

        source_id = self.source_id

        title = self.title

        turn_count = self.turn_count

        total_llm_calls = self.total_llm_calls

        total_tool_calls = self.total_tool_calls

        total_input_tokens = self.total_input_tokens

        total_output_tokens = self.total_output_tokens

        total_tokens = self.total_tokens

        total_cost_usd = self.total_cost_usd

        total_duration_ms = self.total_duration_ms

        error_count = self.error_count

        first_activity: None | str | Unset
        if isinstance(self.first_activity, Unset):
            first_activity = UNSET
        elif isinstance(self.first_activity, datetime.datetime):
            first_activity = self.first_activity.isoformat()
        else:
            first_activity = self.first_activity

        last_activity: None | str | Unset
        if isinstance(self.last_activity, Unset):
            last_activity = UNSET
        elif isinstance(self.last_activity, datetime.datetime):
            last_activity = self.last_activity.isoformat()
        else:
            last_activity = self.last_activity

        participants: list[str] | Unset = UNSET
        if not isinstance(self.participants, Unset):
            participants = self.participants

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_type": source_type,
                "source_id": source_id,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if turn_count is not UNSET:
            field_dict["turn_count"] = turn_count
        if total_llm_calls is not UNSET:
            field_dict["total_llm_calls"] = total_llm_calls
        if total_tool_calls is not UNSET:
            field_dict["total_tool_calls"] = total_tool_calls
        if total_input_tokens is not UNSET:
            field_dict["total_input_tokens"] = total_input_tokens
        if total_output_tokens is not UNSET:
            field_dict["total_output_tokens"] = total_output_tokens
        if total_tokens is not UNSET:
            field_dict["total_tokens"] = total_tokens
        if total_cost_usd is not UNSET:
            field_dict["total_cost_usd"] = total_cost_usd
        if total_duration_ms is not UNSET:
            field_dict["total_duration_ms"] = total_duration_ms
        if error_count is not UNSET:
            field_dict["error_count"] = error_count
        if first_activity is not UNSET:
            field_dict["first_activity"] = first_activity
        if last_activity is not UNSET:
            field_dict["last_activity"] = last_activity
        if participants is not UNSET:
            field_dict["participants"] = participants

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_type = d.pop("source_type")

        source_id = d.pop("source_id")

        title = d.pop("title", UNSET)

        turn_count = d.pop("turn_count", UNSET)

        total_llm_calls = d.pop("total_llm_calls", UNSET)

        total_tool_calls = d.pop("total_tool_calls", UNSET)

        total_input_tokens = d.pop("total_input_tokens", UNSET)

        total_output_tokens = d.pop("total_output_tokens", UNSET)

        total_tokens = d.pop("total_tokens", UNSET)

        total_cost_usd = d.pop("total_cost_usd", UNSET)

        total_duration_ms = d.pop("total_duration_ms", UNSET)

        error_count = d.pop("error_count", UNSET)

        def _parse_first_activity(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_activity_type_0 = datetime.datetime.fromisoformat(data)

                return first_activity_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        first_activity = _parse_first_activity(d.pop("first_activity", UNSET))

        def _parse_last_activity(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_activity_type_0 = datetime.datetime.fromisoformat(data)

                return last_activity_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_activity = _parse_last_activity(d.pop("last_activity", UNSET))

        participants = cast(list[str], d.pop("participants", UNSET))

        thread_summary = cls(
            source_type=source_type,
            source_id=source_id,
            title=title,
            turn_count=turn_count,
            total_llm_calls=total_llm_calls,
            total_tool_calls=total_tool_calls,
            total_input_tokens=total_input_tokens,
            total_output_tokens=total_output_tokens,
            total_tokens=total_tokens,
            total_cost_usd=total_cost_usd,
            total_duration_ms=total_duration_ms,
            error_count=error_count,
            first_activity=first_activity,
            last_activity=last_activity,
            participants=participants,
        )

        thread_summary.additional_properties = d
        return thread_summary

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
