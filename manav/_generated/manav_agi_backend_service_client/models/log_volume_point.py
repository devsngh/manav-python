from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LogVolumePoint")


@_attrs_define
class LogVolumePoint:
    """
    Attributes:
        hour (str):
        error (int):
        warning (int):
        info (int):
        debug (int):
    """

    hour: str
    error: int
    warning: int
    info: int
    debug: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hour = self.hour

        error = self.error

        warning = self.warning

        info = self.info

        debug = self.debug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hour": hour,
                "error": error,
                "warning": warning,
                "info": info,
                "debug": debug,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hour = d.pop("hour")

        error = d.pop("error")

        warning = d.pop("warning")

        info = d.pop("info")

        debug = d.pop("debug")

        log_volume_point = cls(
            hour=hour,
            error=error,
            warning=warning,
            info=info,
            debug=debug,
        )

        log_volume_point.additional_properties = d
        return log_volume_point

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
