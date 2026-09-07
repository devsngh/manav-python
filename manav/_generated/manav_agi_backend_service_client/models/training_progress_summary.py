from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.training_progress_summary_per_axis_average import TrainingProgressSummaryPerAxisAverage


T = TypeVar("T", bound="TrainingProgressSummary")


@_attrs_define
class TrainingProgressSummary:
    """GET .../training/progress/{trainee_bot_id} — Manav reads this.

    Attributes:
        trainee_bot_id (UUID):
        total_rounds (int):
        rounds_passed (int):
        rounds_failed (int):
        rounds_in_progress (int):
        latest_round_number (int):
        latest_threshold_status (None | str | Unset):
        latest_overall_score (float | None | Unset):
        average_score (float | None | Unset):
        per_axis_average (TrainingProgressSummaryPerAxisAverage | Unset):
        has_pending_gate (bool | Unset):  Default: False.
    """

    trainee_bot_id: UUID
    total_rounds: int
    rounds_passed: int
    rounds_failed: int
    rounds_in_progress: int
    latest_round_number: int
    latest_threshold_status: None | str | Unset = UNSET
    latest_overall_score: float | None | Unset = UNSET
    average_score: float | None | Unset = UNSET
    per_axis_average: TrainingProgressSummaryPerAxisAverage | Unset = UNSET
    has_pending_gate: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trainee_bot_id = str(self.trainee_bot_id)

        total_rounds = self.total_rounds

        rounds_passed = self.rounds_passed

        rounds_failed = self.rounds_failed

        rounds_in_progress = self.rounds_in_progress

        latest_round_number = self.latest_round_number

        latest_threshold_status: None | str | Unset
        if isinstance(self.latest_threshold_status, Unset):
            latest_threshold_status = UNSET
        else:
            latest_threshold_status = self.latest_threshold_status

        latest_overall_score: float | None | Unset
        if isinstance(self.latest_overall_score, Unset):
            latest_overall_score = UNSET
        else:
            latest_overall_score = self.latest_overall_score

        average_score: float | None | Unset
        if isinstance(self.average_score, Unset):
            average_score = UNSET
        else:
            average_score = self.average_score

        per_axis_average: dict[str, Any] | Unset = UNSET
        if not isinstance(self.per_axis_average, Unset):
            per_axis_average = self.per_axis_average.to_dict()

        has_pending_gate = self.has_pending_gate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trainee_bot_id": trainee_bot_id,
                "total_rounds": total_rounds,
                "rounds_passed": rounds_passed,
                "rounds_failed": rounds_failed,
                "rounds_in_progress": rounds_in_progress,
                "latest_round_number": latest_round_number,
            }
        )
        if latest_threshold_status is not UNSET:
            field_dict["latest_threshold_status"] = latest_threshold_status
        if latest_overall_score is not UNSET:
            field_dict["latest_overall_score"] = latest_overall_score
        if average_score is not UNSET:
            field_dict["average_score"] = average_score
        if per_axis_average is not UNSET:
            field_dict["per_axis_average"] = per_axis_average
        if has_pending_gate is not UNSET:
            field_dict["has_pending_gate"] = has_pending_gate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.training_progress_summary_per_axis_average import (
            TrainingProgressSummaryPerAxisAverage,  # noqa: PLC0415
        )

        d = dict(src_dict)
        trainee_bot_id = UUID(d.pop("trainee_bot_id"))

        total_rounds = d.pop("total_rounds")

        rounds_passed = d.pop("rounds_passed")

        rounds_failed = d.pop("rounds_failed")

        rounds_in_progress = d.pop("rounds_in_progress")

        latest_round_number = d.pop("latest_round_number")

        def _parse_latest_threshold_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_threshold_status = _parse_latest_threshold_status(d.pop("latest_threshold_status", UNSET))

        def _parse_latest_overall_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latest_overall_score = _parse_latest_overall_score(d.pop("latest_overall_score", UNSET))

        def _parse_average_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        average_score = _parse_average_score(d.pop("average_score", UNSET))

        _per_axis_average = d.pop("per_axis_average", UNSET)
        per_axis_average: TrainingProgressSummaryPerAxisAverage | Unset
        if isinstance(_per_axis_average, Unset):
            per_axis_average = UNSET
        else:
            per_axis_average = TrainingProgressSummaryPerAxisAverage.from_dict(_per_axis_average)

        has_pending_gate = d.pop("has_pending_gate", UNSET)

        training_progress_summary = cls(
            trainee_bot_id=trainee_bot_id,
            total_rounds=total_rounds,
            rounds_passed=rounds_passed,
            rounds_failed=rounds_failed,
            rounds_in_progress=rounds_in_progress,
            latest_round_number=latest_round_number,
            latest_threshold_status=latest_threshold_status,
            latest_overall_score=latest_overall_score,
            average_score=average_score,
            per_axis_average=per_axis_average,
            has_pending_gate=has_pending_gate,
        )

        training_progress_summary.additional_properties = d
        return training_progress_summary

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
