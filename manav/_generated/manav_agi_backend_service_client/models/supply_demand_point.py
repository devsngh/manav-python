from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SupplyDemandPoint")


@_attrs_define
class SupplyDemandPoint:
    """
    Attributes:
        month (str):
        new_listings (int):
        new_purchases (int):
    """

    month: str
    new_listings: int
    new_purchases: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        month = self.month

        new_listings = self.new_listings

        new_purchases = self.new_purchases

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "month": month,
                "new_listings": new_listings,
                "new_purchases": new_purchases,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        month = d.pop("month")

        new_listings = d.pop("new_listings")

        new_purchases = d.pop("new_purchases")

        supply_demand_point = cls(
            month=month,
            new_listings=new_listings,
            new_purchases=new_purchases,
        )

        supply_demand_point.additional_properties = d
        return supply_demand_point

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
