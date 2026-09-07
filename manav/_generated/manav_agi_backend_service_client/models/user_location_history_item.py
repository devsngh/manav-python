from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserLocationHistoryItem")


@_attrs_define
class UserLocationHistoryItem:
    """
    Attributes:
        id (str):
        ip_address (str):
        latitude (float):
        longitude (float):
        country (str):
        country_code (str):
        logged_in_at (str):
        city (None | str | Unset):
        region (None | str | Unset):
        user_agent (None | str | Unset):
    """

    id: str
    ip_address: str
    latitude: float
    longitude: float
    country: str
    country_code: str
    logged_in_at: str
    city: None | str | Unset = UNSET
    region: None | str | Unset = UNSET
    user_agent: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ip_address = self.ip_address

        latitude = self.latitude

        longitude = self.longitude

        country = self.country

        country_code = self.country_code

        logged_in_at = self.logged_in_at

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        user_agent: None | str | Unset
        if isinstance(self.user_agent, Unset):
            user_agent = UNSET
        else:
            user_agent = self.user_agent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "ip_address": ip_address,
                "latitude": latitude,
                "longitude": longitude,
                "country": country,
                "country_code": country_code,
                "logged_in_at": logged_in_at,
            }
        )
        if city is not UNSET:
            field_dict["city"] = city
        if region is not UNSET:
            field_dict["region"] = region
        if user_agent is not UNSET:
            field_dict["user_agent"] = user_agent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        ip_address = d.pop("ip_address")

        latitude = d.pop("latitude")

        longitude = d.pop("longitude")

        country = d.pop("country")

        country_code = d.pop("country_code")

        logged_in_at = d.pop("logged_in_at")

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_user_agent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_agent = _parse_user_agent(d.pop("user_agent", UNSET))

        user_location_history_item = cls(
            id=id,
            ip_address=ip_address,
            latitude=latitude,
            longitude=longitude,
            country=country,
            country_code=country_code,
            logged_in_at=logged_in_at,
            city=city,
            region=region,
            user_agent=user_agent,
        )

        user_location_history_item.additional_properties = d
        return user_location_history_item

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
