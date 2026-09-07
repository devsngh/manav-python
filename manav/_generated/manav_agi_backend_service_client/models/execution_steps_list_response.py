from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_step_response import ExecutionStepResponse


T = TypeVar("T", bound="ExecutionStepsListResponse")


@_attrs_define
class ExecutionStepsListResponse:
    """
    Attributes:
        steps (list[ExecutionStepResponse]):
        total (int):
        dialogue_id (None | str | Unset):
    """

    steps: list[ExecutionStepResponse]
    total: int
    dialogue_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        total = self.total

        dialogue_id: None | str | Unset
        if isinstance(self.dialogue_id, Unset):
            dialogue_id = UNSET
        else:
            dialogue_id = self.dialogue_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "steps": steps,
                "total": total,
            }
        )
        if dialogue_id is not UNSET:
            field_dict["dialogue_id"] = dialogue_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_step_response import ExecutionStepResponse  # noqa: PLC0415

        d = dict(src_dict)
        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = ExecutionStepResponse.from_dict(steps_item_data)

            steps.append(steps_item)

        total = d.pop("total")

        def _parse_dialogue_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dialogue_id = _parse_dialogue_id(d.pop("dialogue_id", UNSET))

        execution_steps_list_response = cls(
            steps=steps,
            total=total,
            dialogue_id=dialogue_id,
        )

        execution_steps_list_response.additional_properties = d
        return execution_steps_list_response

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
