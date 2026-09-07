from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.training_round_answers_update_answers_item import TrainingRoundAnswersUpdateAnswersItem


T = TypeVar("T", bound="TrainingRoundAnswersUpdate")


@_attrs_define
class TrainingRoundAnswersUpdate:
    """PATCH ... /answers — trainee posts answers; status flips to PENDING_GRADE.

    Attributes:
        answers (list[TrainingRoundAnswersUpdateAnswersItem]):
    """

    answers: list[TrainingRoundAnswersUpdateAnswersItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        answers = []
        for answers_item_data in self.answers:
            answers_item = answers_item_data.to_dict()
            answers.append(answers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "answers": answers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.training_round_answers_update_answers_item import (
            TrainingRoundAnswersUpdateAnswersItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        answers = []
        _answers = d.pop("answers")
        for answers_item_data in _answers:
            answers_item = TrainingRoundAnswersUpdateAnswersItem.from_dict(answers_item_data)

            answers.append(answers_item)

        training_round_answers_update = cls(
            answers=answers,
        )

        training_round_answers_update.additional_properties = d
        return training_round_answers_update

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
