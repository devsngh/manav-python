from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.span_response import SpanResponse


T = TypeVar("T", bound="TraceDetailResponse")


@_attrs_define
class TraceDetailResponse:
    """
    Attributes:
        trace_id (str):
        root_operation (str):
        span_count (int):
        error_count (int):
        start_time (datetime.datetime):
        spans (list[SpanResponse]):
        total_duration_ms (float | None | Unset):
    """

    trace_id: str
    root_operation: str
    span_count: int
    error_count: int
    start_time: datetime.datetime
    spans: list[SpanResponse]
    total_duration_ms: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trace_id = self.trace_id

        root_operation = self.root_operation

        span_count = self.span_count

        error_count = self.error_count

        start_time = self.start_time.isoformat()

        spans = []
        for spans_item_data in self.spans:
            spans_item = spans_item_data.to_dict()
            spans.append(spans_item)

        total_duration_ms: float | None | Unset
        if isinstance(self.total_duration_ms, Unset):
            total_duration_ms = UNSET
        else:
            total_duration_ms = self.total_duration_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trace_id": trace_id,
                "root_operation": root_operation,
                "span_count": span_count,
                "error_count": error_count,
                "start_time": start_time,
                "spans": spans,
            }
        )
        if total_duration_ms is not UNSET:
            field_dict["total_duration_ms"] = total_duration_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.span_response import SpanResponse  # noqa: PLC0415

        d = dict(src_dict)
        trace_id = d.pop("trace_id")

        root_operation = d.pop("root_operation")

        span_count = d.pop("span_count")

        error_count = d.pop("error_count")

        start_time = datetime.datetime.fromisoformat(d.pop("start_time"))

        spans = []
        _spans = d.pop("spans")
        for spans_item_data in _spans:
            spans_item = SpanResponse.from_dict(spans_item_data)

            spans.append(spans_item)

        def _parse_total_duration_ms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_duration_ms = _parse_total_duration_ms(d.pop("total_duration_ms", UNSET))

        trace_detail_response = cls(
            trace_id=trace_id,
            root_operation=root_operation,
            span_count=span_count,
            error_count=error_count,
            start_time=start_time,
            spans=spans,
            total_duration_ms=total_duration_ms,
        )

        trace_detail_response.additional_properties = d
        return trace_detail_response

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
