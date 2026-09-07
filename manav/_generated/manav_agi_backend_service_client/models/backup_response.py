from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BackupResponse")


@_attrs_define
class BackupResponse:
    """
    Attributes:
        success (bool):
        timestamp (datetime.datetime):
        domains_backed_up (list[str]):
        total_tables (int):
        total_size_mb (float):
        message (str):
    """

    success: bool
    timestamp: datetime.datetime
    domains_backed_up: list[str]
    total_tables: int
    total_size_mb: float
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        timestamp = self.timestamp.isoformat()

        domains_backed_up = self.domains_backed_up

        total_tables = self.total_tables

        total_size_mb = self.total_size_mb

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "timestamp": timestamp,
                "domains_backed_up": domains_backed_up,
                "total_tables": total_tables,
                "total_size_mb": total_size_mb,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        domains_backed_up = cast(list[str], d.pop("domains_backed_up"))

        total_tables = d.pop("total_tables")

        total_size_mb = d.pop("total_size_mb")

        message = d.pop("message")

        backup_response = cls(
            success=success,
            timestamp=timestamp,
            domains_backed_up=domains_backed_up,
            total_tables=total_tables,
            total_size_mb=total_size_mb,
            message=message,
        )

        backup_response.additional_properties = d
        return backup_response

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
