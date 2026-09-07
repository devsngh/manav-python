from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tool_metrics_by_status import ToolMetricsByStatus
    from ..models.tool_metrics_by_type import ToolMetricsByType


T = TypeVar("T", bound="ToolMetrics")


@_attrs_define
class ToolMetrics:
    """
    Attributes:
        total_tools (int):
        by_status (ToolMetricsByStatus):
        by_type (ToolMetricsByType):
        datasource_tagged (int):
        custom_tools (int):
    """

    total_tools: int
    by_status: ToolMetricsByStatus
    by_type: ToolMetricsByType
    datasource_tagged: int
    custom_tools: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_tools = self.total_tools

        by_status = self.by_status.to_dict()

        by_type = self.by_type.to_dict()

        datasource_tagged = self.datasource_tagged

        custom_tools = self.custom_tools

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_tools": total_tools,
                "by_status": by_status,
                "by_type": by_type,
                "datasource_tagged": datasource_tagged,
                "custom_tools": custom_tools,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_metrics_by_status import ToolMetricsByStatus  # noqa: PLC0415
        from ..models.tool_metrics_by_type import ToolMetricsByType  # noqa: PLC0415

        d = dict(src_dict)
        total_tools = d.pop("total_tools")

        by_status = ToolMetricsByStatus.from_dict(d.pop("by_status"))

        by_type = ToolMetricsByType.from_dict(d.pop("by_type"))

        datasource_tagged = d.pop("datasource_tagged")

        custom_tools = d.pop("custom_tools")

        tool_metrics = cls(
            total_tools=total_tools,
            by_status=by_status,
            by_type=by_type,
            datasource_tagged=datasource_tagged,
            custom_tools=custom_tools,
        )

        tool_metrics.additional_properties = d
        return tool_metrics

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
