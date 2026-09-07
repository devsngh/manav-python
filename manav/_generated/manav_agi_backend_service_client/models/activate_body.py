from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivateBody")


@_attrs_define
class ActivateBody:
    """
    Attributes:
        name (str):
        activate (bool):
        briefing (None | str | Unset):
    """

    name: str
    activate: bool
    briefing: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        activate = self.activate

        briefing: None | str | Unset
        if isinstance(self.briefing, Unset):
            briefing = UNSET
        else:
            briefing = self.briefing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "activate": activate,
            }
        )
        if briefing is not UNSET:
            field_dict["briefing"] = briefing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        activate = d.pop("activate")

        def _parse_briefing(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        briefing = _parse_briefing(d.pop("briefing", UNSET))

        activate_body = cls(
            name=name,
            activate=activate,
            briefing=briefing,
        )

        activate_body.additional_properties = d
        return activate_body

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
