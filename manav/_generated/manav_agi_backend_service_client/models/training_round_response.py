from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.training_round_response_answers_type_0_item import TrainingRoundResponseAnswersType0Item
    from ..models.training_round_response_grades_type_0 import TrainingRoundResponseGradesType0
    from ..models.training_round_response_question_set_item import TrainingRoundResponseQuestionSetItem
    from ..models.training_round_response_threshold_axes import TrainingRoundResponseThresholdAxes


T = TypeVar("T", bound="TrainingRoundResponse")


@_attrs_define
class TrainingRoundResponse:
    """
    Attributes:
        id (UUID):
        training_group_id (UUID):
        trainee_bot_id (UUID):
        round_number (int):
        training_type (str):
        question_set (list[TrainingRoundResponseQuestionSetItem]):
        threshold_axes (TrainingRoundResponseThresholdAxes):
        threshold_status (str):
        started_at (datetime.datetime):
        org_id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        trainer_bot_id (None | Unset | UUID):
        evaluator_bot_id (None | Unset | UUID):
        answers (list[TrainingRoundResponseAnswersType0Item] | None | Unset):
        grades (None | TrainingRoundResponseGradesType0 | Unset):
        overall_score (float | None | Unset):
        gate_decision (None | str | Unset):
        gate_decision_by (None | Unset | UUID):
        gate_decision_by_role (None | str | Unset):
        gate_decision_at (datetime.datetime | None | Unset):
        gate_reasoning (None | str | Unset):
        completed_at (datetime.datetime | None | Unset):
    """

    id: UUID
    training_group_id: UUID
    trainee_bot_id: UUID
    round_number: int
    training_type: str
    question_set: list[TrainingRoundResponseQuestionSetItem]
    threshold_axes: TrainingRoundResponseThresholdAxes
    threshold_status: str
    started_at: datetime.datetime
    org_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    trainer_bot_id: None | Unset | UUID = UNSET
    evaluator_bot_id: None | Unset | UUID = UNSET
    answers: list[TrainingRoundResponseAnswersType0Item] | None | Unset = UNSET
    grades: None | TrainingRoundResponseGradesType0 | Unset = UNSET
    overall_score: float | None | Unset = UNSET
    gate_decision: None | str | Unset = UNSET
    gate_decision_by: None | Unset | UUID = UNSET
    gate_decision_by_role: None | str | Unset = UNSET
    gate_decision_at: datetime.datetime | None | Unset = UNSET
    gate_reasoning: None | str | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.training_round_response_grades_type_0 import TrainingRoundResponseGradesType0  # noqa: PLC0415

        id = str(self.id)

        training_group_id = str(self.training_group_id)

        trainee_bot_id = str(self.trainee_bot_id)

        round_number = self.round_number

        training_type = self.training_type

        question_set = []
        for question_set_item_data in self.question_set:
            question_set_item = question_set_item_data.to_dict()
            question_set.append(question_set_item)

        threshold_axes = self.threshold_axes.to_dict()

        threshold_status = self.threshold_status

        started_at = self.started_at.isoformat()

        org_id = str(self.org_id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

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

        answers: list[dict[str, Any]] | None | Unset
        if isinstance(self.answers, Unset):
            answers = UNSET
        elif isinstance(self.answers, list):
            answers = []
            for answers_type_0_item_data in self.answers:
                answers_type_0_item = answers_type_0_item_data.to_dict()
                answers.append(answers_type_0_item)

        else:
            answers = self.answers

        grades: dict[str, Any] | None | Unset
        if isinstance(self.grades, Unset):
            grades = UNSET
        elif isinstance(self.grades, TrainingRoundResponseGradesType0):
            grades = self.grades.to_dict()
        else:
            grades = self.grades

        overall_score: float | None | Unset
        if isinstance(self.overall_score, Unset):
            overall_score = UNSET
        else:
            overall_score = self.overall_score

        gate_decision: None | str | Unset
        if isinstance(self.gate_decision, Unset):
            gate_decision = UNSET
        else:
            gate_decision = self.gate_decision

        gate_decision_by: None | str | Unset
        if isinstance(self.gate_decision_by, Unset):
            gate_decision_by = UNSET
        elif isinstance(self.gate_decision_by, UUID):
            gate_decision_by = str(self.gate_decision_by)
        else:
            gate_decision_by = self.gate_decision_by

        gate_decision_by_role: None | str | Unset
        if isinstance(self.gate_decision_by_role, Unset):
            gate_decision_by_role = UNSET
        else:
            gate_decision_by_role = self.gate_decision_by_role

        gate_decision_at: None | str | Unset
        if isinstance(self.gate_decision_at, Unset):
            gate_decision_at = UNSET
        elif isinstance(self.gate_decision_at, datetime.datetime):
            gate_decision_at = self.gate_decision_at.isoformat()
        else:
            gate_decision_at = self.gate_decision_at

        gate_reasoning: None | str | Unset
        if isinstance(self.gate_reasoning, Unset):
            gate_reasoning = UNSET
        else:
            gate_reasoning = self.gate_reasoning

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "training_group_id": training_group_id,
                "trainee_bot_id": trainee_bot_id,
                "round_number": round_number,
                "training_type": training_type,
                "question_set": question_set,
                "threshold_axes": threshold_axes,
                "threshold_status": threshold_status,
                "started_at": started_at,
                "org_id": org_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if trainer_bot_id is not UNSET:
            field_dict["trainer_bot_id"] = trainer_bot_id
        if evaluator_bot_id is not UNSET:
            field_dict["evaluator_bot_id"] = evaluator_bot_id
        if answers is not UNSET:
            field_dict["answers"] = answers
        if grades is not UNSET:
            field_dict["grades"] = grades
        if overall_score is not UNSET:
            field_dict["overall_score"] = overall_score
        if gate_decision is not UNSET:
            field_dict["gate_decision"] = gate_decision
        if gate_decision_by is not UNSET:
            field_dict["gate_decision_by"] = gate_decision_by
        if gate_decision_by_role is not UNSET:
            field_dict["gate_decision_by_role"] = gate_decision_by_role
        if gate_decision_at is not UNSET:
            field_dict["gate_decision_at"] = gate_decision_at
        if gate_reasoning is not UNSET:
            field_dict["gate_reasoning"] = gate_reasoning
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.training_round_response_answers_type_0_item import (
            TrainingRoundResponseAnswersType0Item,  # noqa: PLC0415
        )
        from ..models.training_round_response_grades_type_0 import TrainingRoundResponseGradesType0  # noqa: PLC0415
        from ..models.training_round_response_question_set_item import (
            TrainingRoundResponseQuestionSetItem,  # noqa: PLC0415
        )
        from ..models.training_round_response_threshold_axes import TrainingRoundResponseThresholdAxes  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        training_group_id = UUID(d.pop("training_group_id"))

        trainee_bot_id = UUID(d.pop("trainee_bot_id"))

        round_number = d.pop("round_number")

        training_type = d.pop("training_type")

        question_set = []
        _question_set = d.pop("question_set")
        for question_set_item_data in _question_set:
            question_set_item = TrainingRoundResponseQuestionSetItem.from_dict(question_set_item_data)

            question_set.append(question_set_item)

        threshold_axes = TrainingRoundResponseThresholdAxes.from_dict(d.pop("threshold_axes"))

        threshold_status = d.pop("threshold_status")

        started_at = datetime.datetime.fromisoformat(d.pop("started_at"))

        org_id = UUID(d.pop("org_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

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

        def _parse_answers(data: object) -> list[TrainingRoundResponseAnswersType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                answers_type_0 = []
                _answers_type_0 = data
                for answers_type_0_item_data in _answers_type_0:
                    answers_type_0_item = TrainingRoundResponseAnswersType0Item.from_dict(answers_type_0_item_data)

                    answers_type_0.append(answers_type_0_item)

                return answers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TrainingRoundResponseAnswersType0Item] | None | Unset, data)

        answers = _parse_answers(d.pop("answers", UNSET))

        def _parse_grades(data: object) -> None | TrainingRoundResponseGradesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                grades_type_0 = TrainingRoundResponseGradesType0.from_dict(data)

                return grades_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TrainingRoundResponseGradesType0 | Unset, data)

        grades = _parse_grades(d.pop("grades", UNSET))

        def _parse_overall_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        overall_score = _parse_overall_score(d.pop("overall_score", UNSET))

        def _parse_gate_decision(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gate_decision = _parse_gate_decision(d.pop("gate_decision", UNSET))

        def _parse_gate_decision_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gate_decision_by_type_0 = UUID(data)

                return gate_decision_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        gate_decision_by = _parse_gate_decision_by(d.pop("gate_decision_by", UNSET))

        def _parse_gate_decision_by_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gate_decision_by_role = _parse_gate_decision_by_role(d.pop("gate_decision_by_role", UNSET))

        def _parse_gate_decision_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gate_decision_at_type_0 = datetime.datetime.fromisoformat(data)

                return gate_decision_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        gate_decision_at = _parse_gate_decision_at(d.pop("gate_decision_at", UNSET))

        def _parse_gate_reasoning(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gate_reasoning = _parse_gate_reasoning(d.pop("gate_reasoning", UNSET))

        def _parse_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = datetime.datetime.fromisoformat(data)

                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completed_at", UNSET))

        training_round_response = cls(
            id=id,
            training_group_id=training_group_id,
            trainee_bot_id=trainee_bot_id,
            round_number=round_number,
            training_type=training_type,
            question_set=question_set,
            threshold_axes=threshold_axes,
            threshold_status=threshold_status,
            started_at=started_at,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            trainer_bot_id=trainer_bot_id,
            evaluator_bot_id=evaluator_bot_id,
            answers=answers,
            grades=grades,
            overall_score=overall_score,
            gate_decision=gate_decision,
            gate_decision_by=gate_decision_by,
            gate_decision_by_role=gate_decision_by_role,
            gate_decision_at=gate_decision_at,
            gate_reasoning=gate_reasoning,
            completed_at=completed_at,
        )

        training_round_response.additional_properties = d
        return training_round_response

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
