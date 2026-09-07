from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.training_round_create_question_set_item import TrainingRoundCreateQuestionSetItem
    from ..models.training_round_create_threshold_axes import TrainingRoundCreateThresholdAxes


T = TypeVar("T", bound="TrainingRoundCreate")


@_attrs_define
class TrainingRoundCreate:
    """POST /api/observability/training/rounds — Pariksha starts a round.

    Attributes:
        training_group_id (UUID):
        trainee_bot_id (UUID):
        training_type (str):
        question_set (list[TrainingRoundCreateQuestionSetItem]):
        threshold_axes (TrainingRoundCreateThresholdAxes): axis -> required_score 0.0-1.0
        org_id (UUID):
        trainer_bot_id (None | Unset | UUID):
        evaluator_bot_id (None | Unset | UUID):
        round_number (int | Unset):  Default: 1.
    """

    training_group_id: UUID
    trainee_bot_id: UUID
    training_type: str
    question_set: list[TrainingRoundCreateQuestionSetItem]
    threshold_axes: TrainingRoundCreateThresholdAxes
    org_id: UUID
    trainer_bot_id: None | Unset | UUID = UNSET
    evaluator_bot_id: None | Unset | UUID = UNSET
    round_number: int | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        training_group_id = str(self.training_group_id)

        trainee_bot_id = str(self.trainee_bot_id)

        training_type = self.training_type

        question_set = []
        for question_set_item_data in self.question_set:
            question_set_item = question_set_item_data.to_dict()
            question_set.append(question_set_item)

        threshold_axes = self.threshold_axes.to_dict()

        org_id = str(self.org_id)

        trainer_bot_id: None | str | Unset
        if isinstance(self.trainer_bot_id, Unset):
            trainer_bot_id = UNSET
        elif isinstance(self.trainer_bot_id, UUID):
            trainer_bot_id = str(self.trainer_bot_id)
        else:
            trainer_bot_id = self.trainer_bot_id

        evaluator_bot_id: None | str | Unset
        if isinstance(self.evaluator_bot_id, Unset):
            evaluator_bot_id = UNSET
        elif isinstance(self.evaluator_bot_id, UUID):
            evaluator_bot_id = str(self.evaluator_bot_id)
        else:
            evaluator_bot_id = self.evaluator_bot_id

        round_number = self.round_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "training_group_id": training_group_id,
                "trainee_bot_id": trainee_bot_id,
                "training_type": training_type,
                "question_set": question_set,
                "threshold_axes": threshold_axes,
                "org_id": org_id,
            }
        )
        if trainer_bot_id is not UNSET:
            field_dict["trainer_bot_id"] = trainer_bot_id
        if evaluator_bot_id is not UNSET:
            field_dict["evaluator_bot_id"] = evaluator_bot_id
        if round_number is not UNSET:
            field_dict["round_number"] = round_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.training_round_create_question_set_item import TrainingRoundCreateQuestionSetItem  # noqa: PLC0415
        from ..models.training_round_create_threshold_axes import TrainingRoundCreateThresholdAxes  # noqa: PLC0415

        d = dict(src_dict)
        training_group_id = UUID(d.pop("training_group_id"))

        trainee_bot_id = UUID(d.pop("trainee_bot_id"))

        training_type = d.pop("training_type")

        question_set = []
        _question_set = d.pop("question_set")
        for question_set_item_data in _question_set:
            question_set_item = TrainingRoundCreateQuestionSetItem.from_dict(question_set_item_data)

            question_set.append(question_set_item)

        threshold_axes = TrainingRoundCreateThresholdAxes.from_dict(d.pop("threshold_axes"))

        org_id = UUID(d.pop("org_id"))

        def _parse_trainer_bot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trainer_bot_id_type_0 = UUID(data)

                return trainer_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        trainer_bot_id = _parse_trainer_bot_id(d.pop("trainer_bot_id", UNSET))

        def _parse_evaluator_bot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                evaluator_bot_id_type_0 = UUID(data)

                return evaluator_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        evaluator_bot_id = _parse_evaluator_bot_id(d.pop("evaluator_bot_id", UNSET))

        round_number = d.pop("round_number", UNSET)

        training_round_create = cls(
            training_group_id=training_group_id,
            trainee_bot_id=trainee_bot_id,
            training_type=training_type,
            question_set=question_set,
            threshold_axes=threshold_axes,
            org_id=org_id,
            trainer_bot_id=trainer_bot_id,
            evaluator_bot_id=evaluator_bot_id,
            round_number=round_number,
        )

        training_round_create.additional_properties = d
        return training_round_create

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
