from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_step_response_step_input_type_0 import ExecutionStepResponseStepInputType0


T = TypeVar("T", bound="ExecutionStepResponse")


@_attrs_define
class ExecutionStepResponse:
    """
    Attributes:
        id (UUID):
        dialogue_id (UUID):
        step_type (str):
        step_name (str):
        status (str):
        sequence (int):
        trace_id (None | str | Unset):
        step_input (ExecutionStepResponseStepInputType0 | None | Unset):
        step_output (None | str | Unset):
        duration_ms (float | None | Unset):
        error_message (None | str | Unset):
        created_at (datetime.datetime | None | Unset):
    """

    id: UUID
    dialogue_id: UUID
    step_type: str
    step_name: str
    status: str
    sequence: int
    trace_id: None | str | Unset = UNSET
    step_input: ExecutionStepResponseStepInputType0 | None | Unset = UNSET
    step_output: None | str | Unset = UNSET
    duration_ms: float | None | Unset = UNSET
    error_message: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.execution_step_response_step_input_type_0 import (
            ExecutionStepResponseStepInputType0,  # noqa: PLC0415
        )

        id = str(self.id)

        dialogue_id = str(self.dialogue_id)

        step_type = self.step_type

        step_name = self.step_name

        status = self.status

        sequence = self.sequence

        trace_id: None | str | Unset
        if isinstance(self.trace_id, Unset):
            trace_id = UNSET
        else:
            trace_id = self.trace_id

        step_input: dict[str, Any] | None | Unset
        if isinstance(self.step_input, Unset):
            step_input = UNSET
        elif isinstance(self.step_input, ExecutionStepResponseStepInputType0):
            step_input = self.step_input.to_dict()
        else:
            step_input = self.step_input

        step_output: None | str | Unset
        if isinstance(self.step_output, Unset):
            step_output = UNSET
        else:
            step_output = self.step_output

        duration_ms: float | None | Unset
        if isinstance(self.duration_ms, Unset):
            duration_ms = UNSET
        else:
            duration_ms = self.duration_ms

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "dialogue_id": dialogue_id,
                "step_type": step_type,
                "step_name": step_name,
                "status": status,
                "sequence": sequence,
            }
        )
        if trace_id is not UNSET:
            field_dict["trace_id"] = trace_id
        if step_input is not UNSET:
            field_dict["step_input"] = step_input
        if step_output is not UNSET:
            field_dict["step_output"] = step_output
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_step_response_step_input_type_0 import (
            ExecutionStepResponseStepInputType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        dialogue_id = UUID(d.pop("dialogue_id"))

        step_type = d.pop("step_type")

        step_name = d.pop("step_name")

        status = d.pop("status")

        sequence = d.pop("sequence")

        def _parse_trace_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trace_id = _parse_trace_id(d.pop("trace_id", UNSET))

        def _parse_step_input(data: object) -> ExecutionStepResponseStepInputType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                step_input_type_0 = ExecutionStepResponseStepInputType0.from_dict(data)

                return step_input_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExecutionStepResponseStepInputType0 | None | Unset, data)

        step_input = _parse_step_input(d.pop("step_input", UNSET))

        def _parse_step_output(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        step_output = _parse_step_output(d.pop("step_output", UNSET))

        def _parse_duration_ms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration_ms = _parse_duration_ms(d.pop("duration_ms", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        execution_step_response = cls(
            id=id,
            dialogue_id=dialogue_id,
            step_type=step_type,
            step_name=step_name,
            status=status,
            sequence=sequence,
            trace_id=trace_id,
            step_input=step_input,
            step_output=step_output,
            duration_ms=duration_ms,
            error_message=error_message,
            created_at=created_at,
        )

        execution_step_response.additional_properties = d
        return execution_step_response

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
