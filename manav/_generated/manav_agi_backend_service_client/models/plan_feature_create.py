from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlanFeatureCreate")


@_attrs_define
class PlanFeatureCreate:
    """
    Attributes:
        feature_key (str):
        feature_name (str):
        description (None | str | Unset):
        is_enabled (bool | Unset):  Default: False.
        sort_order (int | Unset):  Default: 0.
    """

    feature_key: str
    feature_name: str
    description: None | str | Unset = UNSET
    is_enabled: bool | Unset = False
    sort_order: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feature_key = self.feature_key

        feature_name = self.feature_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_enabled = self.is_enabled

        sort_order = self.sort_order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feature_key": feature_key,
                "feature_name": feature_name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if is_enabled is not UNSET:
            field_dict["is_enabled"] = is_enabled
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        feature_key = d.pop("feature_key")

        feature_name = d.pop("feature_name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        is_enabled = d.pop("is_enabled", UNSET)

        sort_order = d.pop("sort_order", UNSET)

        plan_feature_create = cls(
            feature_key=feature_key,
            feature_name=feature_name,
            description=description,
            is_enabled=is_enabled,
            sort_order=sort_order,
        )

        plan_feature_create.additional_properties = d
        return plan_feature_create

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
