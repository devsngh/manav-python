from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FieldValidation")


@_attrs_define
class FieldValidation:
    """
    Attributes:
        pattern (None | str | Unset):
        min_length (int | None | Unset):
        max_length (int | None | Unset):
        min_ (int | None | Unset):
        max_ (int | None | Unset):
        custom_error (None | str | Unset):
    """

    pattern: None | str | Unset = UNSET
    min_length: int | None | Unset = UNSET
    max_length: int | None | Unset = UNSET
    min_: int | None | Unset = UNSET
    max_: int | None | Unset = UNSET
    custom_error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pattern: None | str | Unset
        if isinstance(self.pattern, Unset):
            pattern = UNSET
        else:
            pattern = self.pattern

        min_length: int | None | Unset
        if isinstance(self.min_length, Unset):
            min_length = UNSET
        else:
            min_length = self.min_length

        max_length: int | None | Unset
        if isinstance(self.max_length, Unset):
            max_length = UNSET
        else:
            max_length = self.max_length

        min_: int | None | Unset
        if isinstance(self.min_, Unset):
            min_ = UNSET
        else:
            min_ = self.min_

        max_: int | None | Unset
        if isinstance(self.max_, Unset):
            max_ = UNSET
        else:
            max_ = self.max_

        custom_error: None | str | Unset
        if isinstance(self.custom_error, Unset):
            custom_error = UNSET
        else:
            custom_error = self.custom_error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if min_length is not UNSET:
            field_dict["min_length"] = min_length
        if max_length is not UNSET:
            field_dict["max_length"] = max_length
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_
        if custom_error is not UNSET:
            field_dict["custom_error"] = custom_error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_pattern(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pattern = _parse_pattern(d.pop("pattern", UNSET))

        def _parse_min_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_length = _parse_min_length(d.pop("min_length", UNSET))

        def _parse_max_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_length = _parse_max_length(d.pop("max_length", UNSET))

        def _parse_min_(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_ = _parse_min_(d.pop("min", UNSET))

        def _parse_max_(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_ = _parse_max_(d.pop("max", UNSET))

        def _parse_custom_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_error = _parse_custom_error(d.pop("custom_error", UNSET))

        field_validation = cls(
            pattern=pattern,
            min_length=min_length,
            max_length=max_length,
            min_=min_,
            max_=max_,
            custom_error=custom_error,
        )

        field_validation.additional_properties = d
        return field_validation

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
