from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.internal_tool_metrics_by_status import InternalToolMetricsByStatus


T = TypeVar("T", bound="InternalToolMetrics")


@_attrs_define
class InternalToolMetrics:
    """
    Attributes:
        total_tools (int):
        by_status (InternalToolMetricsByStatus):
    """

    total_tools: int
    by_status: InternalToolMetricsByStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_tools = self.total_tools

        by_status = self.by_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_tools": total_tools,
                "by_status": by_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_tool_metrics_by_status import InternalToolMetricsByStatus  # noqa: PLC0415

        d = dict(src_dict)
        total_tools = d.pop("total_tools")

        by_status = InternalToolMetricsByStatus.from_dict(d.pop("by_status"))

        internal_tool_metrics = cls(
            total_tools=total_tools,
            by_status=by_status,
        )

        internal_tool_metrics.additional_properties = d
        return internal_tool_metrics

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
