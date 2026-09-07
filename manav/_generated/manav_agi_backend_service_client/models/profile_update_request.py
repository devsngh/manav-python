from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfileUpdateRequest")


@_attrs_define
class ProfileUpdateRequest:
    """User can update their own profile fields

    Attributes:
        full_name (None | str | Unset):
        agi_name (None | str | Unset): Bot name - deprecated
        bot_id (None | str | Unset): Bot ID - deprecated
        age (int | None | Unset):
        date_of_birth (None | str | Unset): Date of birth (YYYY-MM-DD)
        phone_number (None | str | Unset):
        about (None | str | Unset): User description
        timezone (None | str | Unset): IANA timezone name
    """

    full_name: None | str | Unset = UNSET
    agi_name: None | str | Unset = UNSET
    bot_id: None | str | Unset = UNSET
    age: int | None | Unset = UNSET
    date_of_birth: None | str | Unset = UNSET
    phone_number: None | str | Unset = UNSET
    about: None | str | Unset = UNSET
    timezone: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        full_name: None | str | Unset
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        agi_name: None | str | Unset
        if isinstance(self.agi_name, Unset):
            agi_name = UNSET
        else:
            agi_name = self.agi_name

        bot_id: None | str | Unset
        if isinstance(self.bot_id, Unset):
            bot_id = UNSET
        else:
            bot_id = self.bot_id

        age: int | None | Unset
        if isinstance(self.age, Unset):
            age = UNSET
        else:
            age = self.age

        date_of_birth: None | str | Unset
        if isinstance(self.date_of_birth, Unset):
            date_of_birth = UNSET
        else:
            date_of_birth = self.date_of_birth

        phone_number: None | str | Unset
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        else:
            phone_number = self.phone_number

        about: None | str | Unset
        if isinstance(self.about, Unset):
            about = UNSET
        else:
            about = self.about

        timezone: None | str | Unset
        if isinstance(self.timezone, Unset):
            timezone = UNSET
        else:
            timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if agi_name is not UNSET:
            field_dict["agi_name"] = agi_name
        if bot_id is not UNSET:
            field_dict["bot_id"] = bot_id
        if age is not UNSET:
            field_dict["age"] = age
        if date_of_birth is not UNSET:
            field_dict["date_of_birth"] = date_of_birth
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if about is not UNSET:
            field_dict["about"] = about
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_full_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_name = _parse_full_name(d.pop("full_name", UNSET))

        def _parse_agi_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agi_name = _parse_agi_name(d.pop("agi_name", UNSET))

        def _parse_bot_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bot_id = _parse_bot_id(d.pop("bot_id", UNSET))

        def _parse_age(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        age = _parse_age(d.pop("age", UNSET))

        def _parse_date_of_birth(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_of_birth = _parse_date_of_birth(d.pop("date_of_birth", UNSET))

        def _parse_phone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone_number = _parse_phone_number(d.pop("phone_number", UNSET))

        def _parse_about(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        about = _parse_about(d.pop("about", UNSET))

        def _parse_timezone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timezone = _parse_timezone(d.pop("timezone", UNSET))

        profile_update_request = cls(
            full_name=full_name,
            agi_name=agi_name,
            bot_id=bot_id,
            age=age,
            date_of_birth=date_of_birth,
            phone_number=phone_number,
            about=about,
            timezone=timezone,
        )

        profile_update_request.additional_properties = d
        return profile_update_request

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
