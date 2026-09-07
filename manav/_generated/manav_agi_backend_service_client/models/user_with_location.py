from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_location_history_item import UserLocationHistoryItem


T = TypeVar("T", bound="UserWithLocation")


@_attrs_define
class UserWithLocation:
    """
    Attributes:
        user_id (str):
        current_ip (str):
        current_latitude (float):
        current_longitude (float):
        current_country (str):
        current_country_code (str):
        current_logged_in_at (str):
        total_logins (int):
        history (list[UserLocationHistoryItem]):
        user_email (None | str | Unset):
        user_name (None | str | Unset):
        current_city (None | str | Unset):
        current_region (None | str | Unset):
        current_user_agent (None | str | Unset):
    """

    user_id: str
    current_ip: str
    current_latitude: float
    current_longitude: float
    current_country: str
    current_country_code: str
    current_logged_in_at: str
    total_logins: int
    history: list[UserLocationHistoryItem]
    user_email: None | str | Unset = UNSET
    user_name: None | str | Unset = UNSET
    current_city: None | str | Unset = UNSET
    current_region: None | str | Unset = UNSET
    current_user_agent: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        current_ip = self.current_ip

        current_latitude = self.current_latitude

        current_longitude = self.current_longitude

        current_country = self.current_country

        current_country_code = self.current_country_code

        current_logged_in_at = self.current_logged_in_at

        total_logins = self.total_logins

        history = []
        for history_item_data in self.history:
            history_item = history_item_data.to_dict()
            history.append(history_item)

        user_email: None | str | Unset
        if isinstance(self.user_email, Unset):
            user_email = UNSET
        else:
            user_email = self.user_email

        user_name: None | str | Unset
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        current_city: None | str | Unset
        if isinstance(self.current_city, Unset):
            current_city = UNSET
        else:
            current_city = self.current_city

        current_region: None | str | Unset
        if isinstance(self.current_region, Unset):
            current_region = UNSET
        else:
            current_region = self.current_region

        current_user_agent: None | str | Unset
        if isinstance(self.current_user_agent, Unset):
            current_user_agent = UNSET
        else:
            current_user_agent = self.current_user_agent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "current_ip": current_ip,
                "current_latitude": current_latitude,
                "current_longitude": current_longitude,
                "current_country": current_country,
                "current_country_code": current_country_code,
                "current_logged_in_at": current_logged_in_at,
                "total_logins": total_logins,
                "history": history,
            }
        )
        if user_email is not UNSET:
            field_dict["user_email"] = user_email
        if user_name is not UNSET:
            field_dict["user_name"] = user_name
        if current_city is not UNSET:
            field_dict["current_city"] = current_city
        if current_region is not UNSET:
            field_dict["current_region"] = current_region
        if current_user_agent is not UNSET:
            field_dict["current_user_agent"] = current_user_agent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_location_history_item import UserLocationHistoryItem  # noqa: PLC0415

        d = dict(src_dict)
        user_id = d.pop("user_id")

        current_ip = d.pop("current_ip")

        current_latitude = d.pop("current_latitude")

        current_longitude = d.pop("current_longitude")

        current_country = d.pop("current_country")

        current_country_code = d.pop("current_country_code")

        current_logged_in_at = d.pop("current_logged_in_at")

        total_logins = d.pop("total_logins")

        history = []
        _history = d.pop("history")
        for history_item_data in _history:
            history_item = UserLocationHistoryItem.from_dict(history_item_data)

            history.append(history_item)

        def _parse_user_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_email = _parse_user_email(d.pop("user_email", UNSET))

        def _parse_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_name = _parse_user_name(d.pop("user_name", UNSET))

        def _parse_current_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_city = _parse_current_city(d.pop("current_city", UNSET))

        def _parse_current_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_region = _parse_current_region(d.pop("current_region", UNSET))

        def _parse_current_user_agent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_user_agent = _parse_current_user_agent(d.pop("current_user_agent", UNSET))

        user_with_location = cls(
            user_id=user_id,
            current_ip=current_ip,
            current_latitude=current_latitude,
            current_longitude=current_longitude,
            current_country=current_country,
            current_country_code=current_country_code,
            current_logged_in_at=current_logged_in_at,
            total_logins=total_logins,
            history=history,
            user_email=user_email,
            user_name=user_name,
            current_city=current_city,
            current_region=current_region,
            current_user_agent=current_user_agent,
        )

        user_with_location.additional_properties = d
        return user_with_location

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
