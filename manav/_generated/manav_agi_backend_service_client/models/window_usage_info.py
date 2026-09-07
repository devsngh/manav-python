from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WindowUsageInfo")


@_attrs_define
class WindowUsageInfo:
    """
    Attributes:
        window_index (int):
        window_start_hour (int):
        window_end_hour (int):
        tokens_used (int):
        tokens_limit (int):
        usage_percent (float):
    """

    window_index: int
    window_start_hour: int
    window_end_hour: int
    tokens_used: int
    tokens_limit: int
    usage_percent: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        window_index = self.window_index

        window_start_hour = self.window_start_hour

        window_end_hour = self.window_end_hour

        tokens_used = self.tokens_used

        tokens_limit = self.tokens_limit

        usage_percent = self.usage_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "window_index": window_index,
                "window_start_hour": window_start_hour,
                "window_end_hour": window_end_hour,
                "tokens_used": tokens_used,
                "tokens_limit": tokens_limit,
                "usage_percent": usage_percent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        window_index = d.pop("window_index")

        window_start_hour = d.pop("window_start_hour")

        window_end_hour = d.pop("window_end_hour")

        tokens_used = d.pop("tokens_used")

        tokens_limit = d.pop("tokens_limit")

        usage_percent = d.pop("usage_percent")

        window_usage_info = cls(
            window_index=window_index,
            window_start_hour=window_start_hour,
            window_end_hour=window_end_hour,
            tokens_used=tokens_used,
            tokens_limit=tokens_limit,
            usage_percent=usage_percent,
        )

        window_usage_info.additional_properties = d
        return window_usage_info

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
