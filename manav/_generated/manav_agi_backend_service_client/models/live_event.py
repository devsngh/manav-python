from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.live_event_extras import LiveEventExtras


T = TypeVar("T", bound="LiveEvent")


@_attrs_define
class LiveEvent:
    """One event row in the boot log.

    `kind` drives the icon + colour in the UI. `subject_kind` (extra
    tag) distinguishes special "milestone" events (`phase_sentinel`,
    `activation_done`) from raw call events.

        Attributes:
            id (str):
            ts (datetime.datetime):
            kind (str):
            label (str):
            subject_kind (None | str | Unset):
            thread_id (None | str | Unset):
            dialogue_id (None | str | Unset):
            span_id (None | str | Unset):
            parent_id (None | str | Unset):
            checkpoint_id (None | str | Unset):
            duration_ms (int | None | Unset):
            tokens (int | None | Unset):
            cost_usd (float | None | Unset):
            status (None | str | Unset):
            error (None | str | Unset):
            extras (LiveEventExtras | Unset):
    """

    id: str
    ts: datetime.datetime
    kind: str
    label: str
    subject_kind: None | str | Unset = UNSET
    thread_id: None | str | Unset = UNSET
    dialogue_id: None | str | Unset = UNSET
    span_id: None | str | Unset = UNSET
    parent_id: None | str | Unset = UNSET
    checkpoint_id: None | str | Unset = UNSET
    duration_ms: int | None | Unset = UNSET
    tokens: int | None | Unset = UNSET
    cost_usd: float | None | Unset = UNSET
    status: None | str | Unset = UNSET
    error: None | str | Unset = UNSET
    extras: LiveEventExtras | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ts = self.ts.isoformat()

        kind = self.kind

        label = self.label

        subject_kind: None | str | Unset
        if isinstance(self.subject_kind, Unset):
            subject_kind = UNSET
        else:
            subject_kind = self.subject_kind

        thread_id: None | str | Unset
        if isinstance(self.thread_id, Unset):
            thread_id = UNSET
        else:
            thread_id = self.thread_id

        dialogue_id: None | str | Unset
        if isinstance(self.dialogue_id, Unset):
            dialogue_id = UNSET
        else:
            dialogue_id = self.dialogue_id

        span_id: None | str | Unset
        if isinstance(self.span_id, Unset):
            span_id = UNSET
        else:
            span_id = self.span_id

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        checkpoint_id: None | str | Unset
        if isinstance(self.checkpoint_id, Unset):
            checkpoint_id = UNSET
        else:
            checkpoint_id = self.checkpoint_id

        duration_ms: int | None | Unset
        if isinstance(self.duration_ms, Unset):
            duration_ms = UNSET
        else:
            duration_ms = self.duration_ms

        tokens: int | None | Unset
        if isinstance(self.tokens, Unset):
            tokens = UNSET
        else:
            tokens = self.tokens

        cost_usd: float | None | Unset
        if isinstance(self.cost_usd, Unset):
            cost_usd = UNSET
        else:
            cost_usd = self.cost_usd

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "ts": ts,
                "kind": kind,
                "label": label,
            }
        )
        if subject_kind is not UNSET:
            field_dict["subject_kind"] = subject_kind
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id
        if dialogue_id is not UNSET:
            field_dict["dialogue_id"] = dialogue_id
        if span_id is not UNSET:
            field_dict["span_id"] = span_id
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if checkpoint_id is not UNSET:
            field_dict["checkpoint_id"] = checkpoint_id
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if tokens is not UNSET:
            field_dict["tokens"] = tokens
        if cost_usd is not UNSET:
            field_dict["cost_usd"] = cost_usd
        if status is not UNSET:
            field_dict["status"] = status
        if error is not UNSET:
            field_dict["error"] = error
        if extras is not UNSET:
            field_dict["extras"] = extras

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.live_event_extras import LiveEventExtras  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        ts = datetime.datetime.fromisoformat(d.pop("ts"))

        kind = d.pop("kind")

        label = d.pop("label")

        def _parse_subject_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject_kind = _parse_subject_kind(d.pop("subject_kind", UNSET))

        def _parse_thread_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thread_id = _parse_thread_id(d.pop("thread_id", UNSET))

        def _parse_dialogue_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dialogue_id = _parse_dialogue_id(d.pop("dialogue_id", UNSET))

        def _parse_span_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        span_id = _parse_span_id(d.pop("span_id", UNSET))

        def _parse_parent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        def _parse_checkpoint_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        checkpoint_id = _parse_checkpoint_id(d.pop("checkpoint_id", UNSET))

        def _parse_duration_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_ms = _parse_duration_ms(d.pop("duration_ms", UNSET))

        def _parse_tokens(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tokens = _parse_tokens(d.pop("tokens", UNSET))

        def _parse_cost_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cost_usd = _parse_cost_usd(d.pop("cost_usd", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        _extras = d.pop("extras", UNSET)
        extras: LiveEventExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = LiveEventExtras.from_dict(_extras)

        live_event = cls(
            id=id,
            ts=ts,
            kind=kind,
            label=label,
            subject_kind=subject_kind,
            thread_id=thread_id,
            dialogue_id=dialogue_id,
            span_id=span_id,
            parent_id=parent_id,
            checkpoint_id=checkpoint_id,
            duration_ms=duration_ms,
            tokens=tokens,
            cost_usd=cost_usd,
            status=status,
            error=error,
            extras=extras,
        )

        live_event.additional_properties = d
        return live_event

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
