from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatsResponse")


@_attrs_define
class StatsResponse:
    """Aggregate pills for the top-of-page filter bar.

    Attributes:
        total_threads (int | Unset):  Default: 0.
        total_dialogues (int | Unset):  Default: 0.
        total_spans (int | Unset):  Default: 0.
        total_errors (int | Unset):  Default: 0.
        total_cost_usd (float | Unset):  Default: 0.0.
        total_tokens (int | Unset):  Default: 0.
        avg_duration_ms (float | Unset):  Default: 0.0.
    """

    total_threads: int | Unset = 0
    total_dialogues: int | Unset = 0
    total_spans: int | Unset = 0
    total_errors: int | Unset = 0
    total_cost_usd: float | Unset = 0.0
    total_tokens: int | Unset = 0
    avg_duration_ms: float | Unset = 0.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_threads = self.total_threads

        total_dialogues = self.total_dialogues

        total_spans = self.total_spans

        total_errors = self.total_errors

        total_cost_usd = self.total_cost_usd

        total_tokens = self.total_tokens

        avg_duration_ms = self.avg_duration_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_threads is not UNSET:
            field_dict["total_threads"] = total_threads
        if total_dialogues is not UNSET:
            field_dict["total_dialogues"] = total_dialogues
        if total_spans is not UNSET:
            field_dict["total_spans"] = total_spans
        if total_errors is not UNSET:
            field_dict["total_errors"] = total_errors
        if total_cost_usd is not UNSET:
            field_dict["total_cost_usd"] = total_cost_usd
        if total_tokens is not UNSET:
            field_dict["total_tokens"] = total_tokens
        if avg_duration_ms is not UNSET:
            field_dict["avg_duration_ms"] = avg_duration_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_threads = d.pop("total_threads", UNSET)

        total_dialogues = d.pop("total_dialogues", UNSET)

        total_spans = d.pop("total_spans", UNSET)

        total_errors = d.pop("total_errors", UNSET)

        total_cost_usd = d.pop("total_cost_usd", UNSET)

        total_tokens = d.pop("total_tokens", UNSET)

        avg_duration_ms = d.pop("avg_duration_ms", UNSET)

        stats_response = cls(
            total_threads=total_threads,
            total_dialogues=total_dialogues,
            total_spans=total_spans,
            total_errors=total_errors,
            total_cost_usd=total_cost_usd,
            total_tokens=total_tokens,
            avg_duration_ms=avg_duration_ms,
        )

        stats_response.additional_properties = d
        return stats_response

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
