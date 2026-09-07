from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.execution_stats_response_by_type_item import ExecutionStatsResponseByTypeItem


T = TypeVar("T", bound="ExecutionStatsResponse")


@_attrs_define
class ExecutionStatsResponse:
    """
    Attributes:
        total_steps (int):
        total_dialogues (int):
        avg_steps_per_dialogue (float):
        total_errors (int):
        error_rate (float):
        avg_duration_ms (float):
        by_type (list[ExecutionStatsResponseByTypeItem]):
    """

    total_steps: int
    total_dialogues: int
    avg_steps_per_dialogue: float
    total_errors: int
    error_rate: float
    avg_duration_ms: float
    by_type: list[ExecutionStatsResponseByTypeItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_steps = self.total_steps

        total_dialogues = self.total_dialogues

        avg_steps_per_dialogue = self.avg_steps_per_dialogue

        total_errors = self.total_errors

        error_rate = self.error_rate

        avg_duration_ms = self.avg_duration_ms

        by_type = []
        for by_type_item_data in self.by_type:
            by_type_item = by_type_item_data.to_dict()
            by_type.append(by_type_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_steps": total_steps,
                "total_dialogues": total_dialogues,
                "avg_steps_per_dialogue": avg_steps_per_dialogue,
                "total_errors": total_errors,
                "error_rate": error_rate,
                "avg_duration_ms": avg_duration_ms,
                "by_type": by_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_stats_response_by_type_item import ExecutionStatsResponseByTypeItem  # noqa: PLC0415

        d = dict(src_dict)
        total_steps = d.pop("total_steps")

        total_dialogues = d.pop("total_dialogues")

        avg_steps_per_dialogue = d.pop("avg_steps_per_dialogue")

        total_errors = d.pop("total_errors")

        error_rate = d.pop("error_rate")

        avg_duration_ms = d.pop("avg_duration_ms")

        by_type = []
        _by_type = d.pop("by_type")
        for by_type_item_data in _by_type:
            by_type_item = ExecutionStatsResponseByTypeItem.from_dict(by_type_item_data)

            by_type.append(by_type_item)

        execution_stats_response = cls(
            total_steps=total_steps,
            total_dialogues=total_dialogues,
            avg_steps_per_dialogue=avg_steps_per_dialogue,
            total_errors=total_errors,
            error_rate=error_rate,
            avg_duration_ms=avg_duration_ms,
            by_type=by_type,
        )

        execution_stats_response.additional_properties = d
        return execution_stats_response

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
