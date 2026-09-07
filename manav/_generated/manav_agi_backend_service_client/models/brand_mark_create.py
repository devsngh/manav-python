from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BrandMarkCreate")


@_attrs_define
class BrandMarkCreate:
    """
    Attributes:
        mark_type (str): primary_logo / secondary_logo / icon / wordmark / monogram / favicon
        asset_id (UUID):
        variant (None | str | Unset): light_bg / dark_bg / mono / reverse / color
        is_primary (bool | Unset):  Default: False.
        usage_rules (None | str | Unset):
    """

    mark_type: str
    asset_id: UUID
    variant: None | str | Unset = UNSET
    is_primary: bool | Unset = False
    usage_rules: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mark_type = self.mark_type

        asset_id = str(self.asset_id)

        variant: None | str | Unset
        if isinstance(self.variant, Unset):
            variant = UNSET
        else:
            variant = self.variant

        is_primary = self.is_primary

        usage_rules: None | str | Unset
        if isinstance(self.usage_rules, Unset):
            usage_rules = UNSET
        else:
            usage_rules = self.usage_rules

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mark_type": mark_type,
                "asset_id": asset_id,
            }
        )
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
        mark_type = d.pop("mark_type")

        asset_id = UUID(d.pop("asset_id"))

        def _parse_variant(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        variant = _parse_variant(d.pop("variant", UNSET))

        is_primary = d.pop("is_primary", UNSET)

        def _parse_usage_rules(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        usage_rules = _parse_usage_rules(d.pop("usage_rules", UNSET))

        brand_mark_create = cls(
            mark_type=mark_type,
            asset_id=asset_id,
            variant=variant,
            is_primary=is_primary,
            usage_rules=usage_rules,
        )

        brand_mark_create.additional_properties = d
        return brand_mark_create

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
