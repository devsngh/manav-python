from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RawColumn")


@_attrs_define
class RawColumn:
    """
    Attributes:
        raw_name (str):
        data_type (str):
        is_nullable (bool):
        is_primary_key (bool):
        is_foreign_key (bool):
        is_unique (bool):
        is_enum (bool):
        enum_values (list[Any] | None | Unset):
        sample_values (list[Any] | None | Unset):
        min_value (Any | None | Unset):
        max_value (Any | None | Unset):
        avg_value (Any | None | Unset):
        null_percentage (float | None | Unset):
    """

    raw_name: str
    data_type: str
    is_nullable: bool
    is_primary_key: bool
    is_foreign_key: bool
    is_unique: bool
    is_enum: bool
    enum_values: list[Any] | None | Unset = UNSET
    sample_values: list[Any] | None | Unset = UNSET
    min_value: Any | None | Unset = UNSET
    max_value: Any | None | Unset = UNSET
    avg_value: Any | None | Unset = UNSET
    null_percentage: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        raw_name = self.raw_name

        data_type = self.data_type

        is_nullable = self.is_nullable

        is_primary_key = self.is_primary_key

        is_foreign_key = self.is_foreign_key

        is_unique = self.is_unique

        is_enum = self.is_enum

        enum_values: list[Any] | None | Unset
        if isinstance(self.enum_values, Unset):
            enum_values = UNSET
        elif isinstance(self.enum_values, list):
            enum_values = self.enum_values

        else:
            enum_values = self.enum_values

        sample_values: list[Any] | None | Unset
        if isinstance(self.sample_values, Unset):
            sample_values = UNSET
        elif isinstance(self.sample_values, list):
            sample_values = self.sample_values

        else:
            sample_values = self.sample_values

        min_value: Any | None | Unset
        if isinstance(self.min_value, Unset):
            min_value = UNSET
        else:
            min_value = self.min_value

        max_value: Any | None | Unset
        if isinstance(self.max_value, Unset):
            max_value = UNSET
        else:
            max_value = self.max_value

        avg_value: Any | None | Unset
        if isinstance(self.avg_value, Unset):
            avg_value = UNSET
        else:
            avg_value = self.avg_value

        null_percentage: float | None | Unset
        if isinstance(self.null_percentage, Unset):
            null_percentage = UNSET
        else:
            null_percentage = self.null_percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "raw_name": raw_name,
                "data_type": data_type,
                "is_nullable": is_nullable,
                "is_primary_key": is_primary_key,
                "is_foreign_key": is_foreign_key,
                "is_unique": is_unique,
                "is_enum": is_enum,
            }
        )
        if enum_values is not UNSET:
            field_dict["enum_values"] = enum_values
        if sample_values is not UNSET:
            field_dict["sample_values"] = sample_values
        if min_value is not UNSET:
            field_dict["min_value"] = min_value
        if max_value is not UNSET:
            field_dict["max_value"] = max_value
        if avg_value is not UNSET:
            field_dict["avg_value"] = avg_value
        if null_percentage is not UNSET:
            field_dict["null_percentage"] = null_percentage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        raw_name = d.pop("raw_name")

        data_type = d.pop("data_type")

        is_nullable = d.pop("is_nullable")

        is_primary_key = d.pop("is_primary_key")

        is_foreign_key = d.pop("is_foreign_key")

        is_unique = d.pop("is_unique")

        is_enum = d.pop("is_enum")

        def _parse_enum_values(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                enum_values_type_0 = cast(list[Any], data)

                return enum_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        enum_values = _parse_enum_values(d.pop("enum_values", UNSET))

        def _parse_sample_values(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sample_values_type_0 = cast(list[Any], data)

                return sample_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        sample_values = _parse_sample_values(d.pop("sample_values", UNSET))

        def _parse_min_value(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        min_value = _parse_min_value(d.pop("min_value", UNSET))

        def _parse_max_value(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        max_value = _parse_max_value(d.pop("max_value", UNSET))

        def _parse_avg_value(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        avg_value = _parse_avg_value(d.pop("avg_value", UNSET))

        def _parse_null_percentage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        null_percentage = _parse_null_percentage(d.pop("null_percentage", UNSET))

        raw_column = cls(
            raw_name=raw_name,
            data_type=data_type,
            is_nullable=is_nullable,
            is_primary_key=is_primary_key,
            is_foreign_key=is_foreign_key,
            is_unique=is_unique,
            is_enum=is_enum,
            enum_values=enum_values,
            sample_values=sample_values,
            min_value=min_value,
            max_value=max_value,
            avg_value=avg_value,
            null_percentage=null_percentage,
        )

        raw_column.additional_properties = d
        return raw_column

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
