from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ChatSummaryResponse")


@_attrs_define
class ChatSummaryResponse:
    """GET /api/analytics/chat/summary — KPIs from chat_dialogues for a period.

    Attributes:
        total_dialogues (int):
        total_tokens_period (int):
        avg_processing_time_ms (float):
        likes (int):
        dislikes (int):
        rated_count (int):
        satisfaction_rate (float):
        interrupted_count (int):
    """

    total_dialogues: int
    total_tokens_period: int
    avg_processing_time_ms: float
    likes: int
    dislikes: int
    rated_count: int
    satisfaction_rate: float
    interrupted_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_dialogues = self.total_dialogues

        total_tokens_period = self.total_tokens_period

        avg_processing_time_ms = self.avg_processing_time_ms

        likes = self.likes

        dislikes = self.dislikes

        rated_count = self.rated_count

        satisfaction_rate = self.satisfaction_rate

        interrupted_count = self.interrupted_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_dialogues": total_dialogues,
                "total_tokens_period": total_tokens_period,
                "avg_processing_time_ms": avg_processing_time_ms,
                "likes": likes,
                "dislikes": dislikes,
                "rated_count": rated_count,
                "satisfaction_rate": satisfaction_rate,
                "interrupted_count": interrupted_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_dialogues = d.pop("total_dialogues")

        total_tokens_period = d.pop("total_tokens_period")

        avg_processing_time_ms = d.pop("avg_processing_time_ms")

        likes = d.pop("likes")

        dislikes = d.pop("dislikes")

        rated_count = d.pop("rated_count")

        satisfaction_rate = d.pop("satisfaction_rate")

        interrupted_count = d.pop("interrupted_count")

        chat_summary_response = cls(
            total_dialogues=total_dialogues,
            total_tokens_period=total_tokens_period,
            avg_processing_time_ms=avg_processing_time_ms,
            likes=likes,
            dislikes=dislikes,
            rated_count=rated_count,
            satisfaction_rate=satisfaction_rate,
            interrupted_count=interrupted_count,
        )

        chat_summary_response.additional_properties = d
        return chat_summary_response

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
