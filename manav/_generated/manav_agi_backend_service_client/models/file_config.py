from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileConfig")


@_attrs_define
class FileConfig:
    """
    Attributes:
        accepted_formats (list[str] | Unset):
        max_size_mb (int | Unset):  Default: 5.
    """

    accepted_formats: list[str] | Unset = UNSET
    max_size_mb: int | Unset = 5
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accepted_formats: list[str] | Unset = UNSET
        if not isinstance(self.accepted_formats, Unset):
            accepted_formats = self.accepted_formats

        max_size_mb = self.max_size_mb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accepted_formats is not UNSET:
            field_dict["accepted_formats"] = accepted_formats
        if max_size_mb is not UNSET:
            field_dict["max_size_mb"] = max_size_mb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accepted_formats = cast(list[str], d.pop("accepted_formats", UNSET))

        max_size_mb = d.pop("max_size_mb", UNSET)

        file_config = cls(
            accepted_formats=accepted_formats,
            max_size_mb=max_size_mb,
        )

        file_config.additional_properties = d
        return file_config

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
