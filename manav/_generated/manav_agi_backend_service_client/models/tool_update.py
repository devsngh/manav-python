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


T = TypeVar("T", bound="ToolUpdate")


@_attrs_define
class ToolUpdate:
    """
    Attributes:
        tool_function_name (None | str | Unset):
        description (None | str | Unset):
        tool_type (None | ToolType | Unset):
        status (None | ToolStatus | Unset):
        parameters (list[ToolParameterCreate] | None | Unset):
        datasource_ids (list[str] | None | Unset):
    """

    tool_function_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    tool_type: None | ToolType | Unset = UNSET
    status: None | ToolStatus | Unset = UNSET
    parameters: list[ToolParameterCreate] | None | Unset = UNSET
    datasource_ids: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tool_function_name: None | str | Unset
        if isinstance(self.tool_function_name, Unset):
            tool_function_name = UNSET
        else:
            tool_function_name = self.tool_function_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        tool_type: None | str | Unset
        if isinstance(self.tool_type, Unset):
            tool_type = UNSET
        elif isinstance(self.tool_type, ToolType):
            tool_type = self.tool_type.value
        else:
            tool_type = self.tool_type

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, ToolStatus):
            status = self.status.value
        else:
            status = self.status

        parameters: list[dict[str, Any]] | None | Unset
        if isinstance(self.parameters, Unset):
            parameters = UNSET
        elif isinstance(self.parameters, list):
            parameters = []
            for parameters_type_0_item_data in self.parameters:
                parameters_type_0_item = parameters_type_0_item_data.to_dict()
                parameters.append(parameters_type_0_item)

        else:
            parameters = self.parameters

        datasource_ids: list[str] | None | Unset
        if isinstance(self.datasource_ids, Unset):
            datasource_ids = UNSET
        elif isinstance(self.datasource_ids, list):
            datasource_ids = self.datasource_ids

        else:
            datasource_ids = self.datasource_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tool_function_name is not UNSET:
            field_dict["tool_function_name"] = tool_function_name
        if description is not UNSET:
            field_dict["description"] = description
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

        def _parse_tool_function_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_function_name = _parse_tool_function_name(d.pop("tool_function_name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_tool_type(data: object) -> None | ToolType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tool_type_type_0 = ToolType(data)

                return tool_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ToolType | Unset, data)

        tool_type = _parse_tool_type(d.pop("tool_type", UNSET))

        def _parse_status(data: object) -> None | ToolStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = ToolStatus(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ToolStatus | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_parameters(data: object) -> list[ToolParameterCreate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                parameters_type_0 = []
                _parameters_type_0 = data
                for parameters_type_0_item_data in _parameters_type_0:
                    parameters_type_0_item = ToolParameterCreate.from_dict(parameters_type_0_item_data)

                    parameters_type_0.append(parameters_type_0_item)

                return parameters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ToolParameterCreate] | None | Unset, data)

        parameters = _parse_parameters(d.pop("parameters", UNSET))

        def _parse_datasource_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                datasource_ids_type_0 = cast(list[str], data)

                return datasource_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        datasource_ids = _parse_datasource_ids(d.pop("datasource_ids", UNSET))

        tool_update = cls(
            tool_function_name=tool_function_name,
            description=description,
            tool_type=tool_type,
            status=status,
            parameters=parameters,
            datasource_ids=datasource_ids,
        )

        tool_update.additional_properties = d
        return tool_update

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
