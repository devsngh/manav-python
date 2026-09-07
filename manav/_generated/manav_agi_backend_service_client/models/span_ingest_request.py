from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.span_ingest_request_spans_item import SpanIngestRequestSpansItem


T = TypeVar("T", bound="SpanIngestRequest")


@_attrs_define
class SpanIngestRequest:
    """Request to ingest orchestrator spans into trace_spans table.

    Attributes:
        trace_id (str):
        spans (list[SpanIngestRequestSpansItem]):
        user_id (None | str | Unset):
    """

    trace_id: str
    spans: list[SpanIngestRequestSpansItem]
    user_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trace_id = self.trace_id

        spans = []
        for spans_item_data in self.spans:
            spans_item = spans_item_data.to_dict()
            spans.append(spans_item)

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trace_id": trace_id,
                "spans": spans,
            }
        )
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.span_ingest_request_spans_item import SpanIngestRequestSpansItem  # noqa: PLC0415

        d = dict(src_dict)
        trace_id = d.pop("trace_id")

        spans = []
        _spans = d.pop("spans")
        for spans_item_data in _spans:
            spans_item = SpanIngestRequestSpansItem.from_dict(spans_item_data)

            spans.append(spans_item)

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        span_ingest_request = cls(
            trace_id=trace_id,
            spans=spans,
            user_id=user_id,
        )

        span_ingest_request.additional_properties = d
        return span_ingest_request

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
