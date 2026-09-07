from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.internal_tool_status import InternalToolStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_tool_parameter_response import InternalToolParameterResponse


T = TypeVar("T", bound="InternalToolResponse")


@_attrs_define
class InternalToolResponse:
    """
    Attributes:
        id (UUID):
        tool_name (str):
        description (str):
        status (InternalToolStatus): Internal tool status enumeration
        version (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        parameters (list[InternalToolParameterResponse] | Unset):
        created_by (None | Unset | UUID):
        last_modified_by (None | Unset | UUID):
    """

    id: UUID
    tool_name: str
    description: str
    status: InternalToolStatus
    version: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    parameters: list[InternalToolParameterResponse] | Unset = UNSET
    created_by: None | Unset | UUID = UNSET
    last_modified_by: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        tool_name = self.tool_name

        description = self.description

        status = self.status.value

        version = self.version

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        elif isinstance(self.created_by, UUID):
            created_by = str(self.created_by)
        else:
            created_by = self.created_by

        last_modified_by: None | str | Unset
        if isinstance(self.last_modified_by, Unset):
            last_modified_by = UNSET
        elif isinstance(self.last_modified_by, UUID):
            last_modified_by = str(self.last_modified_by)
        else:
            last_modified_by = self.last_modified_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "tool_name": tool_name,
                "description": description,
                "status": status,
                "version": version,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if last_modified_by is not UNSET:
            field_dict["last_modified_by"] = last_modified_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_tool_parameter_response import InternalToolParameterResponse  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        tool_name = d.pop("tool_name")

        description = d.pop("description")

        status = InternalToolStatus(d.pop("status"))

        version = d.pop("version")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _parameters = d.pop("parameters", UNSET)
        parameters: list[InternalToolParameterResponse] | Unset = UNSET
        if _parameters is not UNSET:
            parameters = []
            for parameters_item_data in _parameters:
                parameters_item = InternalToolParameterResponse.from_dict(parameters_item_data)

                parameters.append(parameters_item)

        def _parse_created_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_type_0 = UUID(data)

                return created_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_last_modified_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_modified_by_type_0 = UUID(data)

                return last_modified_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        last_modified_by = _parse_last_modified_by(d.pop("last_modified_by", UNSET))

        internal_tool_response = cls(
            id=id,
            tool_name=tool_name,
            description=description,
            status=status,
            version=version,
            created_at=created_at,
            updated_at=updated_at,
            parameters=parameters,
            created_by=created_by,
            last_modified_by=last_modified_by,
        )

        internal_tool_response.additional_properties = d
        return internal_tool_response

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
