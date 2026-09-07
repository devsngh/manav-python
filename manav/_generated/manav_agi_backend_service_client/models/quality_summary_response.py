from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QualitySummaryResponse")


@_attrs_define
class QualitySummaryResponse:
    """
    Attributes:
        total_dialogues (int | Unset):  Default: 0.
        avg_response_time_ms (float | Unset):  Default: 0.0.
        hil_trigger_rate (float | Unset):  Default: 0.0.
        tool_usage_rate (float | Unset):  Default: 0.0.
        like_rate (float | Unset):  Default: 0.0.
        dislike_rate (float | Unset):  Default: 0.0.
        avg_feedback_rating (float | Unset):  Default: 0.0.
        error_rate (float | Unset):  Default: 0.0.
    """

    total_dialogues: int | Unset = 0
    avg_response_time_ms: float | Unset = 0.0
    hil_trigger_rate: float | Unset = 0.0
    tool_usage_rate: float | Unset = 0.0
    like_rate: float | Unset = 0.0
    dislike_rate: float | Unset = 0.0
    avg_feedback_rating: float | Unset = 0.0
    error_rate: float | Unset = 0.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_dialogues = self.total_dialogues

        avg_response_time_ms = self.avg_response_time_ms

        hil_trigger_rate = self.hil_trigger_rate

        tool_usage_rate = self.tool_usage_rate

        like_rate = self.like_rate

        dislike_rate = self.dislike_rate

        avg_feedback_rating = self.avg_feedback_rating

        error_rate = self.error_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_dialogues is not UNSET:
            field_dict["total_dialogues"] = total_dialogues
        if avg_response_time_ms is not UNSET:
            field_dict["avg_response_time_ms"] = avg_response_time_ms
        if hil_trigger_rate is not UNSET:
            field_dict["hil_trigger_rate"] = hil_trigger_rate
        if tool_usage_rate is not UNSET:
            field_dict["tool_usage_rate"] = tool_usage_rate
        if like_rate is not UNSET:
            field_dict["like_rate"] = like_rate
        if dislike_rate is not UNSET:
            field_dict["dislike_rate"] = dislike_rate
        if avg_feedback_rating is not UNSET:
            field_dict["avg_feedback_rating"] = avg_feedback_rating
        if error_rate is not UNSET:
            field_dict["error_rate"] = error_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_dialogues = d.pop("total_dialogues", UNSET)

        avg_response_time_ms = d.pop("avg_response_time_ms", UNSET)

        hil_trigger_rate = d.pop("hil_trigger_rate", UNSET)

        tool_usage_rate = d.pop("tool_usage_rate", UNSET)

        like_rate = d.pop("like_rate", UNSET)

        dislike_rate = d.pop("dislike_rate", UNSET)

        avg_feedback_rating = d.pop("avg_feedback_rating", UNSET)

        error_rate = d.pop("error_rate", UNSET)

        quality_summary_response = cls(
            total_dialogues=total_dialogues,
            avg_response_time_ms=avg_response_time_ms,
            hil_trigger_rate=hil_trigger_rate,
            tool_usage_rate=tool_usage_rate,
            like_rate=like_rate,
            dislike_rate=dislike_rate,
            avg_feedback_rating=avg_feedback_rating,
            error_rate=error_rate,
        )

        quality_summary_response.additional_properties = d
        return quality_summary_response

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
