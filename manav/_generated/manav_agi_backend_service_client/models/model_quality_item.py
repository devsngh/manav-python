from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelQualityItem")


@_attrs_define
class ModelQualityItem:
    """
    Attributes:
        model_id (str):
        total_dialogues (int | Unset):  Default: 0.
        avg_response_time_ms (float | Unset):  Default: 0.0.
        avg_tokens_per_request (float | Unset):  Default: 0.0.
        like_rate (float | Unset):  Default: 0.0.
        dislike_rate (float | Unset):  Default: 0.0.
        error_rate (float | Unset):  Default: 0.0.
    """

    model_id: str
    total_dialogues: int | Unset = 0
    avg_response_time_ms: float | Unset = 0.0
    avg_tokens_per_request: float | Unset = 0.0
    like_rate: float | Unset = 0.0
    dislike_rate: float | Unset = 0.0
    error_rate: float | Unset = 0.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_id = self.model_id

        total_dialogues = self.total_dialogues

        avg_response_time_ms = self.avg_response_time_ms

        avg_tokens_per_request = self.avg_tokens_per_request

        like_rate = self.like_rate

        dislike_rate = self.dislike_rate

        error_rate = self.error_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model_id": model_id,
            }
        )
        if total_dialogues is not UNSET:
            field_dict["total_dialogues"] = total_dialogues
        if avg_response_time_ms is not UNSET:
            field_dict["avg_response_time_ms"] = avg_response_time_ms
        if avg_tokens_per_request is not UNSET:
            field_dict["avg_tokens_per_request"] = avg_tokens_per_request
        if like_rate is not UNSET:
            field_dict["like_rate"] = like_rate
        if dislike_rate is not UNSET:
            field_dict["dislike_rate"] = dislike_rate
        if error_rate is not UNSET:
            field_dict["error_rate"] = error_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model_id = d.pop("model_id")

        total_dialogues = d.pop("total_dialogues", UNSET)

        avg_response_time_ms = d.pop("avg_response_time_ms", UNSET)

        avg_tokens_per_request = d.pop("avg_tokens_per_request", UNSET)

        like_rate = d.pop("like_rate", UNSET)

        dislike_rate = d.pop("dislike_rate", UNSET)

        error_rate = d.pop("error_rate", UNSET)

        model_quality_item = cls(
            model_id=model_id,
            total_dialogues=total_dialogues,
            avg_response_time_ms=avg_response_time_ms,
            avg_tokens_per_request=avg_tokens_per_request,
            like_rate=like_rate,
            dislike_rate=dislike_rate,
            error_rate=error_rate,
        )

        model_quality_item.additional_properties = d
        return model_quality_item

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
