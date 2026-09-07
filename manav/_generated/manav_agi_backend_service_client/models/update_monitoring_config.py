from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateMonitoringConfig")


@_attrs_define
class UpdateMonitoringConfig:
    """Update monitoring config on a task already in MONITORING state.

    Attributes:
        check_interval_seconds (int | None | Unset):
        max_duration_seconds (int | None | Unset):
    """

    check_interval_seconds: int | None | Unset = UNSET
    max_duration_seconds: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        check_interval_seconds: int | None | Unset
        if isinstance(self.check_interval_seconds, Unset):
            check_interval_seconds = UNSET
        else:
            check_interval_seconds = self.check_interval_seconds

        max_duration_seconds: int | None | Unset
        if isinstance(self.max_duration_seconds, Unset):
            max_duration_seconds = UNSET
        else:
            max_duration_seconds = self.max_duration_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if check_interval_seconds is not UNSET:
            field_dict["check_interval_seconds"] = check_interval_seconds
        if max_duration_seconds is not UNSET:
            field_dict["max_duration_seconds"] = max_duration_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_check_interval_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        check_interval_seconds = _parse_check_interval_seconds(d.pop("check_interval_seconds", UNSET))

        def _parse_max_duration_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_duration_seconds = _parse_max_duration_seconds(d.pop("max_duration_seconds", UNSET))

        update_monitoring_config = cls(
            check_interval_seconds=check_interval_seconds,
            max_duration_seconds=max_duration_seconds,
        )

        update_monitoring_config.additional_properties = d
        return update_monitoring_config

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
