from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RetentionPreviewResponse")


@_attrs_define
class RetentionPreviewResponse:
    """
    Attributes:
        retention_days (int):
        logs_to_purge (int):
        oldest_log_date (datetime.datetime | None | Unset):
    """

    retention_days: int
    logs_to_purge: int
    oldest_log_date: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        retention_days = self.retention_days

        logs_to_purge = self.logs_to_purge

        oldest_log_date: None | str | Unset
        if isinstance(self.oldest_log_date, Unset):
            oldest_log_date = UNSET
        elif isinstance(self.oldest_log_date, datetime.datetime):
            oldest_log_date = self.oldest_log_date.isoformat()
        else:
            oldest_log_date = self.oldest_log_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "retention_days": retention_days,
                "logs_to_purge": logs_to_purge,
            }
        )
        if oldest_log_date is not UNSET:
            field_dict["oldest_log_date"] = oldest_log_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        retention_days = d.pop("retention_days")

        logs_to_purge = d.pop("logs_to_purge")

        def _parse_oldest_log_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                oldest_log_date_type_0 = datetime.datetime.fromisoformat(data)

                return oldest_log_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        oldest_log_date = _parse_oldest_log_date(d.pop("oldest_log_date", UNSET))

        retention_preview_response = cls(
            retention_days=retention_days,
            logs_to_purge=logs_to_purge,
            oldest_log_date=oldest_log_date,
        )

        retention_preview_response.additional_properties = d
        return retention_preview_response

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
