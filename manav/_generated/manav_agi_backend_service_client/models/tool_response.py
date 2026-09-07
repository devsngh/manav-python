from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tool_status import ToolStatus
from ..models.tool_type import ToolType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_parameter_response import ToolParameterResponse
    from ..models.tool_response_datasource_mappings_item import ToolResponseDatasourceMappingsItem


T = TypeVar("T", bound="ToolResponse")


@_attrs_define
class ToolResponse:
    """
    Attributes:
        id (UUID):
        tool_name (str):
        tool_function_name (str):
        description (str):
        tool_type (ToolType): Tool type enumeration
        status (ToolStatus): Tool status enumeration
        version (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        parameters (list[ToolParameterResponse] | Unset):
        datasource_count (int | Unset):  Default: 0.
        datasource_mappings (list[ToolResponseDatasourceMappingsItem] | Unset):
        created_by (str | Unset):
        last_modified_by (str | Unset):
    """

    id: UUID
    tool_name: str
    tool_function_name: str
    description: str
    tool_type: ToolType
    status: ToolStatus
    version: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    parameters: list[ToolParameterResponse] | Unset = UNSET
    datasource_count: int | Unset = 0
    datasource_mappings: list[ToolResponseDatasourceMappingsItem] | Unset = UNSET
    created_by: str | Unset = UNSET
    last_modified_by: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        tool_name = self.tool_name

        tool_function_name = self.tool_function_name

        description = self.description

        tool_type = self.tool_type.value

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

        datasource_count = self.datasource_count

        datasource_mappings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.datasource_mappings, Unset):
            datasource_mappings = []
            for datasource_mappings_item_data in self.datasource_mappings:
                datasource_mappings_item = datasource_mappings_item_data.to_dict()
                datasource_mappings.append(datasource_mappings_item)

        created_by = self.created_by

        last_modified_by = self.last_modified_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "tool_name": tool_name,
                "tool_function_name": tool_function_name,
                "description": description,
                "tool_type": tool_type,
                "status": status,
                "version": version,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if datasource_count is not UNSET:
            field_dict["datasource_count"] = datasource_count
        if datasource_mappings is not UNSET:
            field_dict["datasource_mappings"] = datasource_mappings
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if last_modified_by is not UNSET:
            field_dict["last_modified_by"] = last_modified_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_parameter_response import ToolParameterResponse  # noqa: PLC0415
        from ..models.tool_response_datasource_mappings_item import ToolResponseDatasourceMappingsItem  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        tool_name = d.pop("tool_name")

        tool_function_name = d.pop("tool_function_name")

        description = d.pop("description")

        tool_type = ToolType(d.pop("tool_type"))

        status = ToolStatus(d.pop("status"))

        version = d.pop("version")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _parameters = d.pop("parameters", UNSET)
        parameters: list[ToolParameterResponse] | Unset = UNSET
        if _parameters is not UNSET:
            parameters = []
            for parameters_item_data in _parameters:
                parameters_item = ToolParameterResponse.from_dict(parameters_item_data)

                parameters.append(parameters_item)

        datasource_count = d.pop("datasource_count", UNSET)

        _datasource_mappings = d.pop("datasource_mappings", UNSET)
        datasource_mappings: list[ToolResponseDatasourceMappingsItem] | Unset = UNSET
        if _datasource_mappings is not UNSET:
            datasource_mappings = []
            for datasource_mappings_item_data in _datasource_mappings:
                datasource_mappings_item = ToolResponseDatasourceMappingsItem.from_dict(datasource_mappings_item_data)

                datasource_mappings.append(datasource_mappings_item)

        created_by = d.pop("created_by", UNSET)

        last_modified_by = d.pop("last_modified_by", UNSET)

        tool_response = cls(
            id=id,
            tool_name=tool_name,
            tool_function_name=tool_function_name,
            description=description,
            tool_type=tool_type,
            status=status,
            version=version,
            created_at=created_at,
            updated_at=updated_at,
            parameters=parameters,
            datasource_count=datasource_count,
            datasource_mappings=datasource_mappings,
            created_by=created_by,
            last_modified_by=last_modified_by,
        )

        tool_response.additional_properties = d
        return tool_response

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
