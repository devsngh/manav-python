from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deep_agent_metrics_by_status import DeepAgentMetricsByStatus


T = TypeVar("T", bound="DeepAgentMetrics")


@_attrs_define
class DeepAgentMetrics:
    """
    Attributes:
        total_deepagents (int):
        by_status (DeepAgentMetricsByStatus):
        active_count (int):
        total_assignments (int):
        user_assignments (int | Unset):  Default: 0.
        bot_assignments (int | Unset):  Default: 0.
        role_assignments (int | Unset):  Default: 0.
        default_assignments (int | Unset):  Default: 0.
    """

    total_deepagents: int
    by_status: DeepAgentMetricsByStatus
    active_count: int
    total_assignments: int
    user_assignments: int | Unset = 0
    bot_assignments: int | Unset = 0
    role_assignments: int | Unset = 0
    default_assignments: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_deepagents = self.total_deepagents

        by_status = self.by_status.to_dict()

        active_count = self.active_count

        total_assignments = self.total_assignments

        user_assignments = self.user_assignments

        bot_assignments = self.bot_assignments

        role_assignments = self.role_assignments

        default_assignments = self.default_assignments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_deepagents": total_deepagents,
                "by_status": by_status,
                "active_count": active_count,
                "total_assignments": total_assignments,
            }
        )
        if user_assignments is not UNSET:
            field_dict["user_assignments"] = user_assignments
        if bot_assignments is not UNSET:
            field_dict["bot_assignments"] = bot_assignments
        if role_assignments is not UNSET:
            field_dict["role_assignments"] = role_assignments
        if default_assignments is not UNSET:
            field_dict["default_assignments"] = default_assignments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deep_agent_metrics_by_status import DeepAgentMetricsByStatus  # noqa: PLC0415

        d = dict(src_dict)
        total_deepagents = d.pop("total_deepagents")

        by_status = DeepAgentMetricsByStatus.from_dict(d.pop("by_status"))

        active_count = d.pop("active_count")

        total_assignments = d.pop("total_assignments")

        user_assignments = d.pop("user_assignments", UNSET)

        bot_assignments = d.pop("bot_assignments", UNSET)

        role_assignments = d.pop("role_assignments", UNSET)

        default_assignments = d.pop("default_assignments", UNSET)

        deep_agent_metrics = cls(
            total_deepagents=total_deepagents,
            by_status=by_status,
            active_count=active_count,
            total_assignments=total_assignments,
            user_assignments=user_assignments,
            bot_assignments=bot_assignments,
            role_assignments=role_assignments,
            default_assignments=default_assignments,
        )

        deep_agent_metrics.additional_properties = d
        return deep_agent_metrics

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
