from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DialogueItem")


@_attrs_define
class DialogueItem:
    """One turn within a thread.

    Attributes:
        dialogue_id (UUID):
        turn_index (int | Unset):  Default: 0.
        who_id (None | Unset | UUID):
        who_name (str | Unset):  Default: ''.
        input_snippet (str | Unset):  Default: ''.
        output_snippet (str | Unset):  Default: ''.
        started_at (datetime.datetime | None | Unset):
        duration_ms (float | None | Unset):
        cost_usd (float | Unset):  Default: 0.0.
        tokens_in (int | Unset):  Default: 0.
        tokens_out (int | Unset):  Default: 0.
        span_count (int | Unset):  Default: 0.
        error_count (int | Unset):  Default: 0.
        status (str | Unset):  Default: 'ok'.
    """

    dialogue_id: UUID
    turn_index: int | Unset = 0
    who_id: None | Unset | UUID = UNSET
    who_name: str | Unset = ""
    input_snippet: str | Unset = ""
    output_snippet: str | Unset = ""
    started_at: datetime.datetime | None | Unset = UNSET
    duration_ms: float | None | Unset = UNSET
    cost_usd: float | Unset = 0.0
    tokens_in: int | Unset = 0
    tokens_out: int | Unset = 0
    span_count: int | Unset = 0
    error_count: int | Unset = 0
    status: str | Unset = "ok"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dialogue_id = str(self.dialogue_id)

        turn_index = self.turn_index

        who_id: None | str | Unset
        if isinstance(self.who_id, Unset):
            who_id = UNSET
        elif isinstance(self.who_id, UUID):
            who_id = str(self.who_id)
        else:
            who_id = self.who_id

        who_name = self.who_name

        input_snippet = self.input_snippet

        output_snippet = self.output_snippet

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        duration_ms: float | None | Unset
        if isinstance(self.duration_ms, Unset):
            duration_ms = UNSET
        else:
            duration_ms = self.duration_ms

        cost_usd = self.cost_usd

        tokens_in = self.tokens_in

        tokens_out = self.tokens_out

        span_count = self.span_count

        error_count = self.error_count

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dialogue_id": dialogue_id,
            }
        )
        if turn_index is not UNSET:
            field_dict["turn_index"] = turn_index
        if who_id is not UNSET:
            field_dict["who_id"] = who_id
        if who_name is not UNSET:
            field_dict["who_name"] = who_name
        if input_snippet is not UNSET:
            field_dict["input_snippet"] = input_snippet
        if output_snippet is not UNSET:
            field_dict["output_snippet"] = output_snippet
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if cost_usd is not UNSET:
            field_dict["cost_usd"] = cost_usd
        if tokens_in is not UNSET:
            field_dict["tokens_in"] = tokens_in
        if tokens_out is not UNSET:
            field_dict["tokens_out"] = tokens_out
        if span_count is not UNSET:
            field_dict["span_count"] = span_count
        if error_count is not UNSET:
            field_dict["error_count"] = error_count
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dialogue_id = UUID(d.pop("dialogue_id"))

        turn_index = d.pop("turn_index", UNSET)

        def _parse_who_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                who_id_type_0 = UUID(data)

                return who_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        who_id = _parse_who_id(d.pop("who_id", UNSET))

        who_name = d.pop("who_name", UNSET)

        input_snippet = d.pop("input_snippet", UNSET)

        output_snippet = d.pop("output_snippet", UNSET)

        def _parse_started_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = datetime.datetime.fromisoformat(data)

                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_duration_ms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration_ms = _parse_duration_ms(d.pop("duration_ms", UNSET))

        cost_usd = d.pop("cost_usd", UNSET)

        tokens_in = d.pop("tokens_in", UNSET)

        tokens_out = d.pop("tokens_out", UNSET)

        span_count = d.pop("span_count", UNSET)

        error_count = d.pop("error_count", UNSET)

        status = d.pop("status", UNSET)

        dialogue_item = cls(
            dialogue_id=dialogue_id,
            turn_index=turn_index,
            who_id=who_id,
            who_name=who_name,
            input_snippet=input_snippet,
            output_snippet=output_snippet,
            started_at=started_at,
            duration_ms=duration_ms,
            cost_usd=cost_usd,
            tokens_in=tokens_in,
            tokens_out=tokens_out,
            span_count=span_count,
            error_count=error_count,
            status=status,
        )

        dialogue_item.additional_properties = d
        return dialogue_item

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
