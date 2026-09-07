from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.factory_response_data import FactoryResponseData


T = TypeVar("T", bound="FactoryResponse")


@_attrs_define
class FactoryResponse:
    """
    Attributes:
        success (bool):
        operation (str):
        message (str):
        data (FactoryResponseData | Unset):
    """

    success: bool
    operation: str
    message: str
    data: FactoryResponseData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        operation = self.operation

        message = self.message

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "operation": operation,
                "message": message,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.factory_response_data import FactoryResponseData  # noqa: PLC0415

        d = dict(src_dict)
        success = d.pop("success")

        operation = d.pop("operation")

        message = d.pop("message")

        _data = d.pop("data", UNSET)
        data: FactoryResponseData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = FactoryResponseData.from_dict(_data)

        factory_response = cls(
            success=success,
            operation=operation,
            message=message,
            data=data,
        )

        factory_response.additional_properties = d
        return factory_response

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
