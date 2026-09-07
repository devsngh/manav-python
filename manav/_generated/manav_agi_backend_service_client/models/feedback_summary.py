from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.feedback_summary_by_apply_status import FeedbackSummaryByApplyStatus
    from ..models.feedback_summary_by_author_role import FeedbackSummaryByAuthorRole
    from ..models.feedback_summary_by_kind import FeedbackSummaryByKind
    from ..models.feedback_summary_by_target_type import FeedbackSummaryByTargetType


T = TypeVar("T", bound="FeedbackSummary")


@_attrs_define
class FeedbackSummary:
    """
    Attributes:
        window_days (int):
        total (int):
        by_kind (FeedbackSummaryByKind):
        by_target_type (FeedbackSummaryByTargetType):
        by_apply_status (FeedbackSummaryByApplyStatus):
        by_author_role (FeedbackSummaryByAuthorRole):
        apply_success_rate (float):
    """

    window_days: int
    total: int
    by_kind: FeedbackSummaryByKind
    by_target_type: FeedbackSummaryByTargetType
    by_apply_status: FeedbackSummaryByApplyStatus
    by_author_role: FeedbackSummaryByAuthorRole
    apply_success_rate: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        window_days = self.window_days

        total = self.total

        by_kind = self.by_kind.to_dict()

        by_target_type = self.by_target_type.to_dict()

        by_apply_status = self.by_apply_status.to_dict()

        by_author_role = self.by_author_role.to_dict()

        apply_success_rate = self.apply_success_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "window_days": window_days,
                "total": total,
                "by_kind": by_kind,
                "by_target_type": by_target_type,
                "by_apply_status": by_apply_status,
                "by_author_role": by_author_role,
                "apply_success_rate": apply_success_rate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.feedback_summary_by_apply_status import FeedbackSummaryByApplyStatus  # noqa: PLC0415
        from ..models.feedback_summary_by_author_role import FeedbackSummaryByAuthorRole  # noqa: PLC0415
        from ..models.feedback_summary_by_kind import FeedbackSummaryByKind  # noqa: PLC0415
        from ..models.feedback_summary_by_target_type import FeedbackSummaryByTargetType  # noqa: PLC0415

        d = dict(src_dict)
        window_days = d.pop("window_days")

        total = d.pop("total")

        by_kind = FeedbackSummaryByKind.from_dict(d.pop("by_kind"))

        by_target_type = FeedbackSummaryByTargetType.from_dict(d.pop("by_target_type"))

        by_apply_status = FeedbackSummaryByApplyStatus.from_dict(d.pop("by_apply_status"))

        by_author_role = FeedbackSummaryByAuthorRole.from_dict(d.pop("by_author_role"))

        apply_success_rate = d.pop("apply_success_rate")

        feedback_summary = cls(
            window_days=window_days,
            total=total,
            by_kind=by_kind,
            by_target_type=by_target_type,
            by_apply_status=by_apply_status,
            by_author_role=by_author_role,
            apply_success_rate=apply_success_rate,
        )

        feedback_summary.additional_properties = d
        return feedback_summary

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
