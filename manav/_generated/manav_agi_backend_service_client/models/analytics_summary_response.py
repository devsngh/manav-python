from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnalyticsSummaryResponse")


@_attrs_define
class AnalyticsSummaryResponse:
    """
    Attributes:
        total_tokens_today (int):
        total_tokens_week (int):
        total_tokens_month (int):
        total_credits_month (int):
        avg_tokens_per_request (float):
        total_requests_today (int):
        unique_models_used (int):
    """

    total_tokens_today: int
    total_tokens_week: int
    total_tokens_month: int
    total_credits_month: int
    avg_tokens_per_request: float
    total_requests_today: int
    unique_models_used: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_tokens_today = self.total_tokens_today

        total_tokens_week = self.total_tokens_week

        total_tokens_month = self.total_tokens_month

        total_credits_month = self.total_credits_month

        avg_tokens_per_request = self.avg_tokens_per_request

        total_requests_today = self.total_requests_today

        unique_models_used = self.unique_models_used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_tokens_today": total_tokens_today,
                "total_tokens_week": total_tokens_week,
                "total_tokens_month": total_tokens_month,
                "total_credits_month": total_credits_month,
                "avg_tokens_per_request": avg_tokens_per_request,
                "total_requests_today": total_requests_today,
                "unique_models_used": unique_models_used,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_tokens_today = d.pop("total_tokens_today")

        total_tokens_week = d.pop("total_tokens_week")

        total_tokens_month = d.pop("total_tokens_month")

        total_credits_month = d.pop("total_credits_month")

        avg_tokens_per_request = d.pop("avg_tokens_per_request")

        total_requests_today = d.pop("total_requests_today")

        unique_models_used = d.pop("unique_models_used")

        analytics_summary_response = cls(
            total_tokens_today=total_tokens_today,
            total_tokens_week=total_tokens_week,
            total_tokens_month=total_tokens_month,
            total_credits_month=total_credits_month,
            avg_tokens_per_request=avg_tokens_per_request,
            total_requests_today=total_requests_today,
            unique_models_used=unique_models_used,
        )

        analytics_summary_response.additional_properties = d
        return analytics_summary_response

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
