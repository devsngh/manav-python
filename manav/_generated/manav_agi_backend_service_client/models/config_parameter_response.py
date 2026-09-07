from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConfigParameterResponse")


@_attrs_define
class ConfigParameterResponse:
    """
    Attributes:
        id (UUID):
        datasource_id (UUID):
        parameter_key (str):
        parameter_value (str):
        parameter_type (str):
        is_encrypted (bool):
        is_required (bool):
        description (None | str):
        display_order (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: UUID
    datasource_id: UUID
    parameter_key: str
    parameter_value: str
    parameter_type: str
    is_encrypted: bool
    is_required: bool
    description: None | str
    display_order: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        datasource_id = str(self.datasource_id)

        parameter_key = self.parameter_key

        parameter_value = self.parameter_value

        parameter_type = self.parameter_type

        is_encrypted = self.is_encrypted

        is_required = self.is_required

        description: None | str
        description = self.description

        display_order = self.display_order

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "datasource_id": datasource_id,
                "parameter_key": parameter_key,
                "parameter_value": parameter_value,
                "parameter_type": parameter_type,
                "is_encrypted": is_encrypted,
                "is_required": is_required,
                "description": description,
                "display_order": display_order,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        datasource_id = UUID(d.pop("datasource_id"))

        parameter_key = d.pop("parameter_key")

        parameter_value = d.pop("parameter_value")

        parameter_type = d.pop("parameter_type")

        is_encrypted = d.pop("is_encrypted")

        is_required = d.pop("is_required")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        display_order = d.pop("display_order")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        config_parameter_response = cls(
            id=id,
            datasource_id=datasource_id,
            parameter_key=parameter_key,
            parameter_value=parameter_value,
            parameter_type=parameter_type,
            is_encrypted=is_encrypted,
            is_required=is_required,
            description=description,
            display_order=display_order,
            created_at=created_at,
            updated_at=updated_at,
        )

        config_parameter_response.additional_properties = d
        return config_parameter_response

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
