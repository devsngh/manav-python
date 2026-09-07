from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ColumnInfo")


@_attrs_define
class ColumnInfo:
    """
    Attributes:
        name (str):
        data_type (str):
        is_nullable (bool):
        default_value (None | str | Unset):
        is_primary_key (bool | Unset):  Default: False.
        is_unique (bool | Unset):  Default: False.
        is_foreign_key (bool | Unset):  Default: False.
    """

    name: str
    data_type: str
    is_nullable: bool
    default_value: None | str | Unset = UNSET
    is_primary_key: bool | Unset = False
    is_unique: bool | Unset = False
    is_foreign_key: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        data_type = self.data_type

        is_nullable = self.is_nullable

        default_value: None | str | Unset
        if isinstance(self.default_value, Unset):
            default_value = UNSET
        else:
            default_value = self.default_value

        is_primary_key = self.is_primary_key

        is_unique = self.is_unique

        is_foreign_key = self.is_foreign_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "data_type": data_type,
                "is_nullable": is_nullable,
            }
        )
        if default_value is not UNSET:
            field_dict["default_value"] = default_value
        if is_primary_key is not UNSET:
            field_dict["is_primary_key"] = is_primary_key
        if is_unique is not UNSET:
            field_dict["is_unique"] = is_unique
        if is_foreign_key is not UNSET:
            field_dict["is_foreign_key"] = is_foreign_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        data_type = d.pop("data_type")

        is_nullable = d.pop("is_nullable")

        def _parse_default_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_value = _parse_default_value(d.pop("default_value", UNSET))

        is_primary_key = d.pop("is_primary_key", UNSET)

        is_unique = d.pop("is_unique", UNSET)

        is_foreign_key = d.pop("is_foreign_key", UNSET)

        column_info = cls(
            name=name,
            data_type=data_type,
            is_nullable=is_nullable,
            default_value=default_value,
            is_primary_key=is_primary_key,
            is_unique=is_unique,
            is_foreign_key=is_foreign_key,
        )

        column_info.additional_properties = d
        return column_info

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
