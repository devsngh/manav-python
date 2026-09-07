from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupHistoryEntry")


@_attrs_define
class BackupHistoryEntry:
    """
    Attributes:
        id (int):
        domain (str):
        schema_name (str):
        status (str):
        table_count (int):
        size_mb (float):
        created_at (str):
        triggered_by (None | str | Unset):
        trigger_reason (None | str | Unset):
        duration_seconds (float | None | Unset):
        error_message (None | str | Unset):
    """

    id: int
    domain: str
    schema_name: str
    status: str
    table_count: int
    size_mb: float
    created_at: str
    triggered_by: None | str | Unset = UNSET
    trigger_reason: None | str | Unset = UNSET
    duration_seconds: float | None | Unset = UNSET
    error_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        domain = self.domain

        schema_name = self.schema_name

        status = self.status

        table_count = self.table_count

        size_mb = self.size_mb

        created_at = self.created_at

        triggered_by: None | str | Unset
        if isinstance(self.triggered_by, Unset):
            triggered_by = UNSET
        else:
            triggered_by = self.triggered_by

        trigger_reason: None | str | Unset
        if isinstance(self.trigger_reason, Unset):
            trigger_reason = UNSET
        else:
            trigger_reason = self.trigger_reason

        duration_seconds: float | None | Unset
        if isinstance(self.duration_seconds, Unset):
            duration_seconds = UNSET
        else:
            duration_seconds = self.duration_seconds

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "domain": domain,
                "schema_name": schema_name,
                "status": status,
                "table_count": table_count,
                "size_mb": size_mb,
                "created_at": created_at,
            }
        )
        if triggered_by is not UNSET:
            field_dict["triggered_by"] = triggered_by
        if trigger_reason is not UNSET:
            field_dict["trigger_reason"] = trigger_reason
        if duration_seconds is not UNSET:
            field_dict["duration_seconds"] = duration_seconds
        if error_message is not UNSET:
            field_dict["error_message"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        domain = d.pop("domain")

        schema_name = d.pop("schema_name")

        status = d.pop("status")

        table_count = d.pop("table_count")

        size_mb = d.pop("size_mb")

        created_at = d.pop("created_at")

        def _parse_triggered_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        triggered_by = _parse_triggered_by(d.pop("triggered_by", UNSET))

        def _parse_trigger_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trigger_reason = _parse_trigger_reason(d.pop("trigger_reason", UNSET))

        def _parse_duration_seconds(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration_seconds = _parse_duration_seconds(d.pop("duration_seconds", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        backup_history_entry = cls(
            id=id,
            domain=domain,
            schema_name=schema_name,
            status=status,
            table_count=table_count,
            size_mb=size_mb,
            created_at=created_at,
            triggered_by=triggered_by,
            trigger_reason=trigger_reason,
            duration_seconds=duration_seconds,
            error_message=error_message,
        )

        backup_history_entry.additional_properties = d
        return backup_history_entry

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
