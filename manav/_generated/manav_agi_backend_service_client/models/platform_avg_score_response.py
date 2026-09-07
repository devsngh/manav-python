from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PlatformAvgScoreResponse")


@_attrs_define
class PlatformAvgScoreResponse:
    """GET /api/analytics/platform-avg-score — platform-wide eval averages.

    Attributes:
        avg_score (float):
        total_evals (int):
        pass_rate (float):
        avg_latency_ms (float):
        avg_tool_error_rate (float):
    """

    avg_score: float
    total_evals: int
    pass_rate: float
    avg_latency_ms: float
    avg_tool_error_rate: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_score = self.avg_score

        total_evals = self.total_evals

        pass_rate = self.pass_rate

        avg_latency_ms = self.avg_latency_ms

        avg_tool_error_rate = self.avg_tool_error_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "avg_score": avg_score,
                "total_evals": total_evals,
                "pass_rate": pass_rate,
                "avg_latency_ms": avg_latency_ms,
                "avg_tool_error_rate": avg_tool_error_rate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avg_score = d.pop("avg_score")

        total_evals = d.pop("total_evals")

        pass_rate = d.pop("pass_rate")

        avg_latency_ms = d.pop("avg_latency_ms")

        avg_tool_error_rate = d.pop("avg_tool_error_rate")

        platform_avg_score_response = cls(
            avg_score=avg_score,
            total_evals=total_evals,
            pass_rate=pass_rate,
            avg_latency_ms=avg_latency_ms,
            avg_tool_error_rate=avg_tool_error_rate,
        )

        platform_avg_score_response.additional_properties = d
        return platform_avg_score_response

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
