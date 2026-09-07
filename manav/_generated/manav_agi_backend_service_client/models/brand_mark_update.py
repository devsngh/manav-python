from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BrandMarkUpdate")


@_attrs_define
class BrandMarkUpdate:
    """
    Attributes:
        variant (None | str | Unset):
        is_primary (bool | None | Unset):
        usage_rules (None | str | Unset):
    """

    variant: None | str | Unset = UNSET
    is_primary: bool | None | Unset = UNSET
    usage_rules: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        variant: None | str | Unset
        if isinstance(self.variant, Unset):
            variant = UNSET
        else:
            variant = self.variant

        is_primary: bool | None | Unset
        if isinstance(self.is_primary, Unset):
            is_primary = UNSET
        else:
            is_primary = self.is_primary

        usage_rules: None | str | Unset
        if isinstance(self.usage_rules, Unset):
            usage_rules = UNSET
        else:
            usage_rules = self.usage_rules

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if variant is not UNSET:
            field_dict["variant"] = variant
        if is_primary is not UNSET:
            field_dict["is_primary"] = is_primary
        if usage_rules is not UNSET:
            field_dict["usage_rules"] = usage_rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_variant(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        variant = _parse_variant(d.pop("variant", UNSET))

        def _parse_is_primary(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_primary = _parse_is_primary(d.pop("is_primary", UNSET))

        def _parse_usage_rules(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        usage_rules = _parse_usage_rules(d.pop("usage_rules", UNSET))

        brand_mark_update = cls(
            variant=variant,
            is_primary=is_primary,
            usage_rules=usage_rules,
        )

        brand_mark_update.additional_properties = d
        return brand_mark_update

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
