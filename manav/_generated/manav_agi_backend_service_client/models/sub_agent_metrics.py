from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sub_agent_metrics_by_status import SubAgentMetricsByStatus
    from ..models.sub_agent_metrics_by_type import SubAgentMetricsByType


T = TypeVar("T", bound="SubAgentMetrics")


@_attrs_define
class SubAgentMetrics:
    """
    Attributes:
        total_subagents (int):
        by_status (SubAgentMetricsByStatus):
        by_type (SubAgentMetricsByType):
        active_count (int):
    """

    total_subagents: int
    by_status: SubAgentMetricsByStatus
    by_type: SubAgentMetricsByType
    active_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_subagents = self.total_subagents

        by_status = self.by_status.to_dict()

        by_type = self.by_type.to_dict()

        active_count = self.active_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_subagents": total_subagents,
                "by_status": by_status,
                "by_type": by_type,
                "active_count": active_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sub_agent_metrics_by_status import SubAgentMetricsByStatus  # noqa: PLC0415
        from ..models.sub_agent_metrics_by_type import SubAgentMetricsByType  # noqa: PLC0415

        d = dict(src_dict)
        total_subagents = d.pop("total_subagents")

        by_status = SubAgentMetricsByStatus.from_dict(d.pop("by_status"))

        by_type = SubAgentMetricsByType.from_dict(d.pop("by_type"))

        active_count = d.pop("active_count")

        sub_agent_metrics = cls(
            total_subagents=total_subagents,
            by_status=by_status,
            by_type=by_type,
            active_count=active_count,
        )

        sub_agent_metrics.additional_properties = d
        return sub_agent_metrics

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
