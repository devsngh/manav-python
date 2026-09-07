from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.prompt_metrics_by_category import PromptMetricsByCategory
    from ..models.prompt_metrics_by_role import PromptMetricsByRole
    from ..models.prompt_metrics_by_status import PromptMetricsByStatus


T = TypeVar("T", bound="PromptMetrics")


@_attrs_define
class PromptMetrics:
    """
    Attributes:
        total_prompts (int):
        by_status (PromptMetricsByStatus):
        by_category (PromptMetricsByCategory):
        by_role (PromptMetricsByRole):
    """

    total_prompts: int
    by_status: PromptMetricsByStatus
    by_category: PromptMetricsByCategory
    by_role: PromptMetricsByRole
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_prompts = self.total_prompts

        by_status = self.by_status.to_dict()

        by_category = self.by_category.to_dict()

        by_role = self.by_role.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_prompts": total_prompts,
                "by_status": by_status,
                "by_category": by_category,
                "by_role": by_role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_metrics_by_category import PromptMetricsByCategory  # noqa: PLC0415
        from ..models.prompt_metrics_by_role import PromptMetricsByRole  # noqa: PLC0415
        from ..models.prompt_metrics_by_status import PromptMetricsByStatus  # noqa: PLC0415

        d = dict(src_dict)
        total_prompts = d.pop("total_prompts")

        by_status = PromptMetricsByStatus.from_dict(d.pop("by_status"))

        by_category = PromptMetricsByCategory.from_dict(d.pop("by_category"))

        by_role = PromptMetricsByRole.from_dict(d.pop("by_role"))

        prompt_metrics = cls(
            total_prompts=total_prompts,
            by_status=by_status,
            by_category=by_category,
            by_role=by_role,
        )

        prompt_metrics.additional_properties = d
        return prompt_metrics

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
