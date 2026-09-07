from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceSummary")


@_attrs_define
class TraceSummary:
    """
    Attributes:
        trace_id (str):
        root_operation (str):
        status (str):
        span_count (int):
        error_count (int):
        start_time (datetime.datetime):
        method (None | str | Unset):
        path (None | str | Unset):
        status_code (int | None | Unset):
        duration_ms (float | None | Unset):
        user_id (None | Unset | UUID):
        service (None | str | Unset):
    """

    trace_id: str
    root_operation: str
    status: str
    span_count: int
    error_count: int
    start_time: datetime.datetime
    method: None | str | Unset = UNSET
    path: None | str | Unset = UNSET
    status_code: int | None | Unset = UNSET
    duration_ms: float | None | Unset = UNSET
    user_id: None | Unset | UUID = UNSET
    service: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trace_id = self.trace_id

        root_operation = self.root_operation

        status = self.status

        span_count = self.span_count

        error_count = self.error_count

        start_time = self.start_time.isoformat()

        method: None | str | Unset
        if isinstance(self.method, Unset):
            method = UNSET
        else:
            method = self.method

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        status_code: int | None | Unset
        if isinstance(self.status_code, Unset):
            status_code = UNSET
        else:
            status_code = self.status_code

        duration_ms: float | None | Unset
        if isinstance(self.duration_ms, Unset):
            duration_ms = UNSET
        else:
            duration_ms = self.duration_ms

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        service: None | str | Unset
        if isinstance(self.service, Unset):
            service = UNSET
        else:
            service = self.service

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trace_id": trace_id,
                "root_operation": root_operation,
                "status": status,
                "span_count": span_count,
                "error_count": error_count,
                "start_time": start_time,
            }
        )
        if method is not UNSET:
            field_dict["method"] = method
        if path is not UNSET:
            field_dict["path"] = path
        if status_code is not UNSET:
            field_dict["status_code"] = status_code
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if service is not UNSET:
            field_dict["service"] = service

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        trace_id = d.pop("trace_id")

        root_operation = d.pop("root_operation")

        status = d.pop("status")

        span_count = d.pop("span_count")

        error_count = d.pop("error_count")

        start_time = datetime.datetime.fromisoformat(d.pop("start_time"))

        def _parse_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        method = _parse_method(d.pop("method", UNSET))

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_status_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        status_code = _parse_status_code(d.pop("status_code", UNSET))

        def _parse_duration_ms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration_ms = _parse_duration_ms(d.pop("duration_ms", UNSET))

        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_service(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service = _parse_service(d.pop("service", UNSET))

        trace_summary = cls(
            trace_id=trace_id,
            root_operation=root_operation,
            status=status,
            span_count=span_count,
            error_count=error_count,
            start_time=start_time,
            method=method,
            path=path,
            status_code=status_code,
            duration_ms=duration_ms,
            user_id=user_id,
            service=service,
        )

        trace_summary.additional_properties = d
        return trace_summary

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
