from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.internal_tool_status import InternalToolStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_tool_parameter_create import InternalToolParameterCreate


T = TypeVar("T", bound="InternalToolUpdate")


@_attrs_define
class InternalToolUpdate:
    """
    Attributes:
        description (None | str | Unset):
        status (InternalToolStatus | None | Unset):
        parameters (list[InternalToolParameterCreate] | None | Unset):
    """

    description: None | str | Unset = UNSET
    status: InternalToolStatus | None | Unset = UNSET
    parameters: list[InternalToolParameterCreate] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, InternalToolStatus):
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_tool_parameter_create import InternalToolParameterCreate  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_status(data: object) -> InternalToolStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = InternalToolStatus(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InternalToolStatus | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_parameters(data: object) -> list[InternalToolParameterCreate] | None | Unset:
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
                    parameters_type_0_item = InternalToolParameterCreate.from_dict(parameters_type_0_item_data)

                    parameters_type_0.append(parameters_type_0_item)

                return parameters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[InternalToolParameterCreate] | None | Unset, data)

        parameters = _parse_parameters(d.pop("parameters", UNSET))

        internal_tool_update = cls(
            description=description,
            status=status,
            parameters=parameters,
        )

        internal_tool_update.additional_properties = d
        return internal_tool_update

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
