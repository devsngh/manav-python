from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tool_status import ToolStatus
from ..models.tool_type import ToolType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_parameter_create import ToolParameterCreate


T = TypeVar("T", bound="ToolCreate")


@_attrs_define
class ToolCreate:
    """
    Attributes:
        tool_name (str):
        description (str):
        tool_function_name (None | str | Unset):
        tool_type (ToolType | Unset): Tool type enumeration Default: ToolType.GENERAL.
        status (ToolStatus | Unset): Tool status enumeration Default: ToolStatus.TESTING.
        parameters (list[ToolParameterCreate] | Unset):
        datasource_ids (list[str] | Unset):
    """

    tool_name: str
    description: str
    tool_function_name: None | str | Unset = UNSET
    tool_type: ToolType | Unset = ToolType.GENERAL
    status: ToolStatus | Unset = ToolStatus.TESTING
    parameters: list[ToolParameterCreate] | Unset = UNSET
    datasource_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tool_name = self.tool_name

        description = self.description

        tool_function_name: None | str | Unset
        if isinstance(self.tool_function_name, Unset):
            tool_function_name = UNSET
        else:
            tool_function_name = self.tool_function_name

        tool_type: str | Unset = UNSET
        if not isinstance(self.tool_type, Unset):
            tool_type = self.tool_type.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        datasource_ids: list[str] | Unset = UNSET
        if not isinstance(self.datasource_ids, Unset):
            datasource_ids = self.datasource_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tool_name": tool_name,
                "description": description,
            }
        )
        if tool_function_name is not UNSET:
            field_dict["tool_function_name"] = tool_function_name
        if tool_type is not UNSET:
            field_dict["tool_type"] = tool_type
        if status is not UNSET:
            field_dict["status"] = status
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if datasource_ids is not UNSET:
            field_dict["datasource_ids"] = datasource_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_parameter_create import ToolParameterCreate  # noqa: PLC0415

        d = dict(src_dict)
        tool_name = d.pop("tool_name")

        description = d.pop("description")

        def _parse_tool_function_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_function_name = _parse_tool_function_name(d.pop("tool_function_name", UNSET))

        _tool_type = d.pop("tool_type", UNSET)
        tool_type: ToolType | Unset
        if isinstance(_tool_type, Unset):
            tool_type = UNSET
        else:
            tool_type = ToolType(_tool_type)

        _status = d.pop("status", UNSET)
        status: ToolStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ToolStatus(_status)

        _parameters = d.pop("parameters", UNSET)
        parameters: list[ToolParameterCreate] | Unset = UNSET
        if _parameters is not UNSET:
            parameters = []
            for parameters_item_data in _parameters:
                parameters_item = ToolParameterCreate.from_dict(parameters_item_data)

                parameters.append(parameters_item)

        datasource_ids = cast(list[str], d.pop("datasource_ids", UNSET))

        tool_create = cls(
            tool_name=tool_name,
            description=description,
            tool_function_name=tool_function_name,
            tool_type=tool_type,
            status=status,
            parameters=parameters,
            datasource_ids=datasource_ids,
        )

        tool_create.additional_properties = d
        return tool_create

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
