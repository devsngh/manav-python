from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpanNode")


@_attrs_define
class SpanNode:
    """One node in the execution tree.

    Attributes:
        id (UUID):
        operation (str):
        parent_id (None | Unset | UUID):
        category (None | str | Unset):
        kind (str | Unset):  Default: 'INTERNAL'.
        service (str | Unset):  Default: 'orchestrator'.
        start_time (datetime.datetime | None | Unset):
        end_time (datetime.datetime | None | Unset):
        duration_ms (float | None | Unset):
        status (str | Unset):  Default: 'OK'.
        error_type (None | str | Unset):
        error_message (None | str | Unset):
        tokens_in (int | Unset):  Default: 0.
        tokens_out (int | Unset):  Default: 0.
        cost_usd (float | Unset):  Default: 0.0.
        inline_preview (None | str | Unset):
        depth (int | Unset):  Default: 0.
    """

    id: UUID
    operation: str
    parent_id: None | Unset | UUID = UNSET
    category: None | str | Unset = UNSET
    kind: str | Unset = "INTERNAL"
    service: str | Unset = "orchestrator"
    start_time: datetime.datetime | None | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    duration_ms: float | None | Unset = UNSET
    status: str | Unset = "OK"
    error_type: None | str | Unset = UNSET
    error_message: None | str | Unset = UNSET
    tokens_in: int | Unset = 0
    tokens_out: int | Unset = 0
    cost_usd: float | Unset = 0.0
    inline_preview: None | str | Unset = UNSET
    depth: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        operation = self.operation

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        elif isinstance(self.parent_id, UUID):
            parent_id = str(self.parent_id)
        else:
            parent_id = self.parent_id

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        kind = self.kind

        service = self.service

        start_time: None | str | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        elif isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        duration_ms: float | None | Unset
        if isinstance(self.duration_ms, Unset):
            duration_ms = UNSET
        else:
            duration_ms = self.duration_ms

        status = self.status

        error_type: None | str | Unset
        if isinstance(self.error_type, Unset):
            error_type = UNSET
        else:
            error_type = self.error_type

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        tokens_in = self.tokens_in

        tokens_out = self.tokens_out

        cost_usd = self.cost_usd

        inline_preview: None | str | Unset
        if isinstance(self.inline_preview, Unset):
            inline_preview = UNSET
        else:
            inline_preview = self.inline_preview

        depth = self.depth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "operation": operation,
            }
        )
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if category is not UNSET:
            field_dict["category"] = category
        if kind is not UNSET:
            field_dict["kind"] = kind
        if service is not UNSET:
            field_dict["service"] = service
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if status is not UNSET:
            field_dict["status"] = status
        if error_type is not UNSET:
            field_dict["error_type"] = error_type
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if tokens_in is not UNSET:
            field_dict["tokens_in"] = tokens_in
        if tokens_out is not UNSET:
            field_dict["tokens_out"] = tokens_out
        if cost_usd is not UNSET:
            field_dict["cost_usd"] = cost_usd
        if inline_preview is not UNSET:
            field_dict["inline_preview"] = inline_preview
        if depth is not UNSET:
            field_dict["depth"] = depth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        operation = d.pop("operation")

        def _parse_parent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_id_type_0 = UUID(data)

                return parent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        kind = d.pop("kind", UNSET)

        service = d.pop("service", UNSET)

        def _parse_start_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_0 = datetime.datetime.fromisoformat(data)

                return start_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_time = _parse_start_time(d.pop("start_time", UNSET))

        def _parse_end_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = datetime.datetime.fromisoformat(data)

                return end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_time = _parse_end_time(d.pop("end_time", UNSET))

        def _parse_duration_ms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration_ms = _parse_duration_ms(d.pop("duration_ms", UNSET))

        status = d.pop("status", UNSET)

        def _parse_error_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_type = _parse_error_type(d.pop("error_type", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        tokens_in = d.pop("tokens_in", UNSET)

        tokens_out = d.pop("tokens_out", UNSET)

        cost_usd = d.pop("cost_usd", UNSET)

        def _parse_inline_preview(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        inline_preview = _parse_inline_preview(d.pop("inline_preview", UNSET))

        depth = d.pop("depth", UNSET)

        span_node = cls(
            id=id,
            operation=operation,
            parent_id=parent_id,
            category=category,
            kind=kind,
            service=service,
            start_time=start_time,
            end_time=end_time,
            duration_ms=duration_ms,
            status=status,
            error_type=error_type,
            error_message=error_message,
            tokens_in=tokens_in,
            tokens_out=tokens_out,
            cost_usd=cost_usd,
            inline_preview=inline_preview,
            depth=depth,
        )

        span_node.additional_properties = d
        return span_node

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
