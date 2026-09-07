from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OrgGrowthMonth")


@_attrs_define
class OrgGrowthMonth:
    """
    Attributes:
        month (str):
        free (int):
        pro (int):
        team (int):
        enterprise (int):
        enterprise_plus (int):
        other (int):
        total (int):
    """

    month: str
    free: int
    pro: int
    team: int
    enterprise: int
    enterprise_plus: int
    other: int
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        month = self.month

        free = self.free

        pro = self.pro

        team = self.team

        enterprise = self.enterprise

        enterprise_plus = self.enterprise_plus

        other = self.other

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "month": month,
                "free": free,
                "pro": pro,
                "team": team,
                "enterprise": enterprise,
                "enterprise_plus": enterprise_plus,
                "other": other,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        month = d.pop("month")

        free = d.pop("free")

        pro = d.pop("pro")

        team = d.pop("team")

        enterprise = d.pop("enterprise")

        enterprise_plus = d.pop("enterprise_plus")

        other = d.pop("other")

        total = d.pop("total")

        org_growth_month = cls(
            month=month,
            free=free,
            pro=pro,
            team=team,
            enterprise=enterprise,
            enterprise_plus=enterprise_plus,
            other=other,
            total=total,
        )

        org_growth_month.additional_properties = d
        return org_growth_month

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
