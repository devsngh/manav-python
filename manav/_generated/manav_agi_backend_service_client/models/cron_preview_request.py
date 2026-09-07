from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CronPreviewRequest")


@_attrs_define
class CronPreviewRequest:
    """
    Attributes:
        cron_expression (str):
        timezone (str | Unset):  Default: 'UTC'.
        count (int | Unset):  Default: 5.
    """

    cron_expression: str
    timezone: str | Unset = "UTC"
    count: int | Unset = 5
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cron_expression = self.cron_expression

        timezone = self.timezone

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cron_expression": cron_expression,
            }
        )
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cron_expression = d.pop("cron_expression")

        timezone = d.pop("timezone", UNSET)

        count = d.pop("count", UNSET)

        cron_preview_request = cls(
            cron_expression=cron_expression,
            timezone=timezone,
            count=count,
        )

        cron_preview_request.additional_properties = d
        return cron_preview_request

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
