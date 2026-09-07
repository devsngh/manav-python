from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InternalToolParameterResponse")


@_attrs_define
class InternalToolParameterResponse:
    """
    Attributes:
        id (UUID):
        parameter_name (str):
        parameter_description (None | str):
        parameter_type (str):
        required (bool):
        default_value (None | str):
        order (int):
        created_at (datetime.datetime):
    """

    id: UUID
    parameter_name: str
    parameter_description: None | str
    parameter_type: str
    required: bool
    default_value: None | str
    order: int
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        parameter_name = self.parameter_name

        parameter_description: None | str
        parameter_description = self.parameter_description

        parameter_type = self.parameter_type

        required = self.required

        default_value: None | str
        default_value = self.default_value

        order = self.order

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "parameter_name": parameter_name,
                "parameter_description": parameter_description,
                "parameter_type": parameter_type,
                "required": required,
                "default_value": default_value,
                "order": order,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        parameter_name = d.pop("parameter_name")

        def _parse_parameter_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        parameter_description = _parse_parameter_description(d.pop("parameter_description"))

        parameter_type = d.pop("parameter_type")

        required = d.pop("required")

        def _parse_default_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        default_value = _parse_default_value(d.pop("default_value"))

        order = d.pop("order")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        internal_tool_parameter_response = cls(
            id=id,
            parameter_name=parameter_name,
            parameter_description=parameter_description,
            parameter_type=parameter_type,
            required=required,
            default_value=default_value,
            order=order,
            created_at=created_at,
        )

        internal_tool_parameter_response.additional_properties = d
        return internal_tool_parameter_response

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
