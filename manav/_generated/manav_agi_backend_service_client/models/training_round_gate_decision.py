from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrainingRoundGateDecision")


@_attrs_define
class TrainingRoundGateDecision:
    """PATCH ... /gate — write the post-round decision.

    Attributes:
        gate_decision (str):
        gate_decision_by (UUID):
        gate_decision_by_role (str):
        gate_reasoning (None | str | Unset):
    """

    gate_decision: str
    gate_decision_by: UUID
    gate_decision_by_role: str
    gate_reasoning: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gate_decision = self.gate_decision

        gate_decision_by = str(self.gate_decision_by)

        gate_decision_by_role = self.gate_decision_by_role

        gate_reasoning: None | str | Unset
        if isinstance(self.gate_reasoning, Unset):
            gate_reasoning = UNSET
        else:
            gate_reasoning = self.gate_reasoning

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gate_decision": gate_decision,
                "gate_decision_by": gate_decision_by,
                "gate_decision_by_role": gate_decision_by_role,
            }
        )
        if gate_reasoning is not UNSET:
            field_dict["gate_reasoning"] = gate_reasoning

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gate_decision = d.pop("gate_decision")

        gate_decision_by = UUID(d.pop("gate_decision_by"))

        gate_decision_by_role = d.pop("gate_decision_by_role")

        def _parse_gate_reasoning(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gate_reasoning = _parse_gate_reasoning(d.pop("gate_reasoning", UNSET))

        training_round_gate_decision = cls(
            gate_decision=gate_decision,
            gate_decision_by=gate_decision_by,
            gate_decision_by_role=gate_decision_by_role,
            gate_reasoning=gate_reasoning,
        )

        training_round_gate_decision.additional_properties = d
        return training_round_gate_decision

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
