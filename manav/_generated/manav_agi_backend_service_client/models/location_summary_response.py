from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.country_count import CountryCount
    from ..models.country_with_cities import CountryWithCities


T = TypeVar("T", bound="LocationSummaryResponse")


@_attrs_define
class LocationSummaryResponse:
    """
    Attributes:
        total_logins (int):
        total_users (int):
        unique_countries (int):
        unique_cities (int):
        unique_ips (int):
        by_country (list[CountryCount]):
        by_country_with_cities (list[CountryWithCities]):
    """

    total_logins: int
    total_users: int
    unique_countries: int
    unique_cities: int
    unique_ips: int
    by_country: list[CountryCount]
    by_country_with_cities: list[CountryWithCities]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_logins = self.total_logins

        total_users = self.total_users

        unique_countries = self.unique_countries

        unique_cities = self.unique_cities

        unique_ips = self.unique_ips

        by_country = []
        for by_country_item_data in self.by_country:
            by_country_item = by_country_item_data.to_dict()
            by_country.append(by_country_item)

        by_country_with_cities = []
        for by_country_with_cities_item_data in self.by_country_with_cities:
            by_country_with_cities_item = by_country_with_cities_item_data.to_dict()
            by_country_with_cities.append(by_country_with_cities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_logins": total_logins,
                "total_users": total_users,
                "unique_countries": unique_countries,
                "unique_cities": unique_cities,
                "unique_ips": unique_ips,
                "by_country": by_country,
                "by_country_with_cities": by_country_with_cities,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.country_count import CountryCount  # noqa: PLC0415
        from ..models.country_with_cities import CountryWithCities  # noqa: PLC0415

        d = dict(src_dict)
        total_logins = d.pop("total_logins")

        total_users = d.pop("total_users")

        unique_countries = d.pop("unique_countries")

        unique_cities = d.pop("unique_cities")

        unique_ips = d.pop("unique_ips")

        by_country = []
        _by_country = d.pop("by_country")
        for by_country_item_data in _by_country:
            by_country_item = CountryCount.from_dict(by_country_item_data)

            by_country.append(by_country_item)

        by_country_with_cities = []
        _by_country_with_cities = d.pop("by_country_with_cities")
        for by_country_with_cities_item_data in _by_country_with_cities:
            by_country_with_cities_item = CountryWithCities.from_dict(by_country_with_cities_item_data)

            by_country_with_cities.append(by_country_with_cities_item)

        location_summary_response = cls(
            total_logins=total_logins,
            total_users=total_users,
            unique_countries=unique_countries,
            unique_cities=unique_cities,
            unique_ips=unique_ips,
            by_country=by_country,
            by_country_with_cities=by_country_with_cities,
        )

        location_summary_response.additional_properties = d
        return location_summary_response

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
