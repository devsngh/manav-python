from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MasterSwitchResponse")


@_attrs_define
class MasterSwitchResponse:
    """
    Attributes:
        master_switch_enabled (bool):
        updated_at (datetime.datetime):
        note (None | str | Unset):
    """

    master_switch_enabled: bool
    updated_at: datetime.datetime
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        master_switch_enabled = self.master_switch_enabled

        updated_at = self.updated_at.isoformat()

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "master_switch_enabled": master_switch_enabled,
                "updated_at": updated_at,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        master_switch_enabled = d.pop("master_switch_enabled")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        master_switch_response = cls(
            master_switch_enabled=master_switch_enabled,
            updated_at=updated_at,
            note=note,
        )

        master_switch_response.additional_properties = d
        return master_switch_response

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
