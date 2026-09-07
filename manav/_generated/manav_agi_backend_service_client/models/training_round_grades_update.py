from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.training_round_grades_update_grades import TrainingRoundGradesUpdateGrades


T = TypeVar("T", bound="TrainingRoundGradesUpdate")


@_attrs_define
class TrainingRoundGradesUpdate:
    """PATCH ... /grades — Pariksha grades; server computes overall_score.

    Attributes:
        grades (TrainingRoundGradesUpdateGrades): q_idx -> {score, reasoning, axes:{axis:score}}
        threshold_status (None | str | Unset):
    """

    grades: TrainingRoundGradesUpdateGrades
    threshold_status: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grades = self.grades.to_dict()

        threshold_status: None | str | Unset
        if isinstance(self.threshold_status, Unset):
            threshold_status = UNSET
        else:
            threshold_status = self.threshold_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grades": grades,
            }
        )
        if threshold_status is not UNSET:
            field_dict["threshold_status"] = threshold_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.training_round_grades_update_grades import TrainingRoundGradesUpdateGrades  # noqa: PLC0415

        d = dict(src_dict)
        grades = TrainingRoundGradesUpdateGrades.from_dict(d.pop("grades"))

        def _parse_threshold_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        threshold_status = _parse_threshold_status(d.pop("threshold_status", UNSET))

        training_round_grades_update = cls(
            grades=grades,
            threshold_status=threshold_status,
        )

        training_round_grades_update.additional_properties = d
        return training_round_grades_update

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
