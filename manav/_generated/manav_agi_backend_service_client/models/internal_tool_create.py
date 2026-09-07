from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.internal_tool_status import InternalToolStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_tool_parameter_create import InternalToolParameterCreate


T = TypeVar("T", bound="InternalToolCreate")


@_attrs_define
class InternalToolCreate:
    """
    Attributes:
        tool_name (str):
        description (str):
        status (InternalToolStatus | Unset): Internal tool status enumeration Default: InternalToolStatus.TESTING.
        parameters (list[InternalToolParameterCreate] | Unset):
    """

    tool_name: str
    description: str
    status: InternalToolStatus | Unset = InternalToolStatus.TESTING
    parameters: list[InternalToolParameterCreate] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tool_name = self.tool_name

        description = self.description

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tool_name": tool_name,
                "description": description,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_tool_parameter_create import InternalToolParameterCreate  # noqa: PLC0415

        d = dict(src_dict)
        tool_name = d.pop("tool_name")

        description = d.pop("description")

        _status = d.pop("status", UNSET)
        status: InternalToolStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = InternalToolStatus(_status)

        _parameters = d.pop("parameters", UNSET)
        parameters: list[InternalToolParameterCreate] | Unset = UNSET
        if _parameters is not UNSET:
            parameters = []
            for parameters_item_data in _parameters:
                parameters_item = InternalToolParameterCreate.from_dict(parameters_item_data)

                parameters.append(parameters_item)

        internal_tool_create = cls(
            tool_name=tool_name,
            description=description,
            status=status,
            parameters=parameters,
        )

        internal_tool_create.additional_properties = d
        return internal_tool_create

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
