from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ToolUsageResponse")


@_attrs_define
class ToolUsageResponse:
    """
    Attributes:
        tool_name (str):
        call_count (int):
        error_count (int):
        avg_duration_ms (float):
        total_duration_ms (float):
    """

    tool_name: str
    call_count: int
    error_count: int
    avg_duration_ms: float
    total_duration_ms: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tool_name = self.tool_name

        call_count = self.call_count

        error_count = self.error_count

        avg_duration_ms = self.avg_duration_ms

        total_duration_ms = self.total_duration_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tool_name": tool_name,
                "call_count": call_count,
                "error_count": error_count,
                "avg_duration_ms": avg_duration_ms,
                "total_duration_ms": total_duration_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tool_name = d.pop("tool_name")

        call_count = d.pop("call_count")

        error_count = d.pop("error_count")

        avg_duration_ms = d.pop("avg_duration_ms")

        total_duration_ms = d.pop("total_duration_ms")

        tool_usage_response = cls(
            tool_name=tool_name,
            call_count=call_count,
            error_count=error_count,
            avg_duration_ms=avg_duration_ms,
            total_duration_ms=total_duration_ms,
        )

        tool_usage_response.additional_properties = d
        return tool_usage_response

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
