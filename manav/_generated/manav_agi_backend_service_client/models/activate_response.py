from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ActivateResponse")


@_attrs_define
class ActivateResponse:
    """
    Attributes:
        name (str):
        is_active (bool):
        cascade_fired (bool):
        cabinet_files (int):
        schedules_flipped (int):
        message (str):
    """

    name: str
    is_active: bool
    cascade_fired: bool
    cabinet_files: int
    schedules_flipped: int
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        is_active = self.is_active

        cascade_fired = self.cascade_fired

        cabinet_files = self.cabinet_files

        schedules_flipped = self.schedules_flipped

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "is_active": is_active,
                "cascade_fired": cascade_fired,
                "cabinet_files": cabinet_files,
                "schedules_flipped": schedules_flipped,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        is_active = d.pop("is_active")

        cascade_fired = d.pop("cascade_fired")

        cabinet_files = d.pop("cabinet_files")

        schedules_flipped = d.pop("schedules_flipped")

        message = d.pop("message")

        activate_response = cls(
            name=name,
            is_active=is_active,
            cascade_fired=cascade_fired,
            cabinet_files=cabinet_files,
            schedules_flipped=schedules_flipped,
            message=message,
        )

        activate_response.additional_properties = d
        return activate_response

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
