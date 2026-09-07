from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.geo_month_point_countries import GeoMonthPointCountries


T = TypeVar("T", bound="GeoMonthPoint")


@_attrs_define
class GeoMonthPoint:
    """
    Attributes:
        month (str):
        countries (GeoMonthPointCountries):
    """

    month: str
    countries: GeoMonthPointCountries
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        month = self.month

        countries = self.countries.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "month": month,
                "countries": countries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.geo_month_point_countries import GeoMonthPointCountries  # noqa: PLC0415

        d = dict(src_dict)
        month = d.pop("month")

        countries = GeoMonthPointCountries.from_dict(d.pop("countries"))

        geo_month_point = cls(
            month=month,
            countries=countries,
        )

        geo_month_point.additional_properties = d
        return geo_month_point

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
