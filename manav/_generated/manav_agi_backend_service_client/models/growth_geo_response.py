from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.geo_country_point import GeoCountryPoint
    from ..models.geo_month_point import GeoMonthPoint


T = TypeVar("T", bound="GrowthGeoResponse")


@_attrs_define
class GrowthGeoResponse:
    """GET /api/analytics/growth/geo — orgs by country + monthly history.

    Attributes:
        by_country (list[GeoCountryPoint]):
        monthly (list[GeoMonthPoint]):
    """

    by_country: list[GeoCountryPoint]
    monthly: list[GeoMonthPoint]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        by_country = []
        for by_country_item_data in self.by_country:
            by_country_item = by_country_item_data.to_dict()
            by_country.append(by_country_item)

        monthly = []
        for monthly_item_data in self.monthly:
            monthly_item = monthly_item_data.to_dict()
            monthly.append(monthly_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "by_country": by_country,
                "monthly": monthly,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.geo_country_point import GeoCountryPoint  # noqa: PLC0415
        from ..models.geo_month_point import GeoMonthPoint  # noqa: PLC0415

        d = dict(src_dict)
        by_country = []
        _by_country = d.pop("by_country")
        for by_country_item_data in _by_country:
            by_country_item = GeoCountryPoint.from_dict(by_country_item_data)

            by_country.append(by_country_item)

        monthly = []
        _monthly = d.pop("monthly")
        for monthly_item_data in _monthly:
            monthly_item = GeoMonthPoint.from_dict(monthly_item_data)

            monthly.append(monthly_item)

        growth_geo_response = cls(
            by_country=by_country,
            monthly=monthly,
        )

        growth_geo_response.additional_properties = d
        return growth_geo_response

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
