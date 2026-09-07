from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MonthlyRevenuePoint")


@_attrs_define
class MonthlyRevenuePoint:
    """
    Attributes:
        month (str):
        gmv (float):
        platform (float):
        publisher (float):
    """

    month: str
    gmv: float
    platform: float
    publisher: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        month = self.month

        gmv = self.gmv

        platform = self.platform

        publisher = self.publisher

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "month": month,
                "gmv": gmv,
                "platform": platform,
                "publisher": publisher,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        month = d.pop("month")

        gmv = d.pop("gmv")

        platform = d.pop("platform")

        publisher = d.pop("publisher")

        monthly_revenue_point = cls(
            month=month,
            gmv=gmv,
            platform=platform,
            publisher=publisher,
        )

        monthly_revenue_point.additional_properties = d
        return monthly_revenue_point

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
