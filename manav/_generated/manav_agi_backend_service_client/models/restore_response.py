from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RestoreResponse")


@_attrs_define
class RestoreResponse:
    """
    Attributes:
        success (bool):
        domain (str):
        table_count (int):
        size_mb (float):
        message (str):
    """

    success: bool
    domain: str
    table_count: int
    size_mb: float
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        domain = self.domain

        table_count = self.table_count

        size_mb = self.size_mb

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "domain": domain,
                "table_count": table_count,
                "size_mb": size_mb,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        domain = d.pop("domain")

        table_count = d.pop("table_count")

        size_mb = d.pop("size_mb")

        message = d.pop("message")

        restore_response = cls(
            success=success,
            domain=domain,
            table_count=table_count,
            size_mb=size_mb,
            message=message,
        )

        restore_response.additional_properties = d
        return restore_response

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
