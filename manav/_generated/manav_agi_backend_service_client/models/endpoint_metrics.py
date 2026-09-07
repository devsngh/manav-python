from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EndpointMetrics")


@_attrs_define
class EndpointMetrics:
    """
    Attributes:
        path (str):
        request_count (int):
        method (None | str | Unset):
        avg_latency_ms (float | None | Unset):
        p95_latency_ms (float | None | Unset):
        error_rate (float | None | Unset):
    """

    path: str
    request_count: int
    method: None | str | Unset = UNSET
    avg_latency_ms: float | None | Unset = UNSET
    p95_latency_ms: float | None | Unset = UNSET
    error_rate: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        request_count = self.request_count

        method: None | str | Unset
        if isinstance(self.method, Unset):
            method = UNSET
        else:
            method = self.method

        avg_latency_ms: float | None | Unset
        if isinstance(self.avg_latency_ms, Unset):
            avg_latency_ms = UNSET
        else:
            avg_latency_ms = self.avg_latency_ms

        p95_latency_ms: float | None | Unset
        if isinstance(self.p95_latency_ms, Unset):
            p95_latency_ms = UNSET
        else:
            p95_latency_ms = self.p95_latency_ms

        error_rate: float | None | Unset
        if isinstance(self.error_rate, Unset):
            error_rate = UNSET
        else:
            error_rate = self.error_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "request_count": request_count,
            }
        )
        if method is not UNSET:
            field_dict["method"] = method
        if avg_latency_ms is not UNSET:
            field_dict["avg_latency_ms"] = avg_latency_ms
        if p95_latency_ms is not UNSET:
            field_dict["p95_latency_ms"] = p95_latency_ms
        if error_rate is not UNSET:
            field_dict["error_rate"] = error_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        request_count = d.pop("request_count")

        def _parse_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        method = _parse_method(d.pop("method", UNSET))

        def _parse_avg_latency_ms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        avg_latency_ms = _parse_avg_latency_ms(d.pop("avg_latency_ms", UNSET))

        def _parse_p95_latency_ms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        p95_latency_ms = _parse_p95_latency_ms(d.pop("p95_latency_ms", UNSET))

        def _parse_error_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        error_rate = _parse_error_rate(d.pop("error_rate", UNSET))

        endpoint_metrics = cls(
            path=path,
            request_count=request_count,
            method=method,
            avg_latency_ms=avg_latency_ms,
            p95_latency_ms=p95_latency_ms,
            error_rate=error_rate,
        )

        endpoint_metrics.additional_properties = d
        return endpoint_metrics

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
