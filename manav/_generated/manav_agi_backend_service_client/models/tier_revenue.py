from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TierRevenue")


@_attrs_define
class TierRevenue:
    """
    Attributes:
        tier (str):
        org_count (int):
        mrr (float):
    """

    tier: str
    org_count: int
    mrr: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tier = self.tier

        org_count = self.org_count

        mrr = self.mrr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tier": tier,
                "org_count": org_count,
                "mrr": mrr,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tier = d.pop("tier")

        org_count = d.pop("org_count")

        mrr = d.pop("mrr")

        tier_revenue = cls(
            tier=tier,
            org_count=org_count,
            mrr=mrr,
        )

        tier_revenue.additional_properties = d
        return tier_revenue

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
