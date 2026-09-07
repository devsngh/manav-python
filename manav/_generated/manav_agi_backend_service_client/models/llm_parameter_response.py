from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.parameter_type import ParameterType

T = TypeVar("T", bound="LLMParameterResponse")


@_attrs_define
class LLMParameterResponse:
    """LLM parameter response

    Attributes:
        id (UUID):
        llm_id (UUID):
        parameter_name (str):
        parameter_type (ParameterType): Parameter data types
        default_value (Any):
        min_value (float | None):
        max_value (float | None):
        is_required (bool):
        description (None | str):
        order (int):
        created_at (datetime.datetime):
    """

    id: UUID
    llm_id: UUID
    parameter_name: str
    parameter_type: ParameterType
    default_value: Any
    min_value: float | None
    max_value: float | None
    is_required: bool
    description: None | str
    order: int
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        llm_id = str(self.llm_id)

        parameter_name = self.parameter_name

        parameter_type = self.parameter_type.value

        default_value = self.default_value

        min_value: float | None
        min_value = self.min_value

        max_value: float | None
        max_value = self.max_value

        is_required = self.is_required

        description: None | str
        description = self.description

        order = self.order

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "llm_id": llm_id,
                "parameter_name": parameter_name,
                "parameter_type": parameter_type,
                "default_value": default_value,
                "min_value": min_value,
                "max_value": max_value,
                "is_required": is_required,
                "description": description,
                "order": order,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        llm_id = UUID(d.pop("llm_id"))

        parameter_name = d.pop("parameter_name")

        parameter_type = ParameterType(d.pop("parameter_type"))

        default_value = d.pop("default_value")

        def _parse_min_value(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        min_value = _parse_min_value(d.pop("min_value"))

        def _parse_max_value(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        max_value = _parse_max_value(d.pop("max_value"))

        is_required = d.pop("is_required")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        order = d.pop("order")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        llm_parameter_response = cls(
            id=id,
            llm_id=llm_id,
            parameter_name=parameter_name,
            parameter_type=parameter_type,
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
            is_required=is_required,
            description=description,
            order=order,
            created_at=created_at,
        )

        llm_parameter_response.additional_properties = d
        return llm_parameter_response

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
