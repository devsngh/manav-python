from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.parameter_type import ParameterType

T = TypeVar("T", bound="UserParameterValueResponse")


@_attrs_define
class UserParameterValueResponse:
    """User parameter value response

    Attributes:
        id (UUID):
        user_config_id (UUID):
        parameter_id (UUID):
        parameter_name (str):
        parameter_type (ParameterType): Parameter data types
        parameter_value (Any):
        is_enabled (bool):
        created_at (datetime.datetime):
    """

    id: UUID
    user_config_id: UUID
    parameter_id: UUID
    parameter_name: str
    parameter_type: ParameterType
    parameter_value: Any
    is_enabled: bool
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        user_config_id = str(self.user_config_id)

        parameter_id = str(self.parameter_id)

        parameter_name = self.parameter_name

        parameter_type = self.parameter_type.value

        parameter_value = self.parameter_value

        is_enabled = self.is_enabled

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_config_id": user_config_id,
                "parameter_id": parameter_id,
                "parameter_name": parameter_name,
                "parameter_type": parameter_type,
                "parameter_value": parameter_value,
                "is_enabled": is_enabled,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        user_config_id = UUID(d.pop("user_config_id"))

        parameter_id = UUID(d.pop("parameter_id"))

        parameter_name = d.pop("parameter_name")

        parameter_type = ParameterType(d.pop("parameter_type"))

        parameter_value = d.pop("parameter_value")

        is_enabled = d.pop("is_enabled")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        user_parameter_value_response = cls(
            id=id,
            user_config_id=user_config_id,
            parameter_id=parameter_id,
            parameter_name=parameter_name,
            parameter_type=parameter_type,
            parameter_value=parameter_value,
            is_enabled=is_enabled,
            created_at=created_at,
        )

        user_parameter_value_response.additional_properties = d
        return user_parameter_value_response

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
