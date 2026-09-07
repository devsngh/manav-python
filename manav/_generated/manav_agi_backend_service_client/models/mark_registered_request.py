from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MarkRegisteredRequest")


@_attrs_define
class MarkRegisteredRequest:
    """
    Attributes:
        registration_number (str):
        registration_date (datetime.date | None | Unset):
        expiry_date (datetime.date | None | Unset):
    """

    registration_number: str
    registration_date: datetime.date | None | Unset = UNSET
    expiry_date: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        registration_number = self.registration_number

        registration_date: None | str | Unset
        if isinstance(self.registration_date, Unset):
            registration_date = UNSET
        elif isinstance(self.registration_date, datetime.date):
            registration_date = self.registration_date.isoformat()
        else:
            registration_date = self.registration_date

        expiry_date: None | str | Unset
        if isinstance(self.expiry_date, Unset):
            expiry_date = UNSET
        elif isinstance(self.expiry_date, datetime.date):
            expiry_date = self.expiry_date.isoformat()
        else:
            expiry_date = self.expiry_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "registration_number": registration_number,
            }
        )
        if registration_date is not UNSET:
            field_dict["registration_date"] = registration_date
        if expiry_date is not UNSET:
            field_dict["expiry_date"] = expiry_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        registration_number = d.pop("registration_number")

        def _parse_registration_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                registration_date_type_0 = datetime.date.fromisoformat(data)

                return registration_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        registration_date = _parse_registration_date(d.pop("registration_date", UNSET))

        def _parse_expiry_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiry_date_type_0 = datetime.date.fromisoformat(data)

                return expiry_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        expiry_date = _parse_expiry_date(d.pop("expiry_date", UNSET))

        mark_registered_request = cls(
            registration_number=registration_number,
            registration_date=registration_date,
            expiry_date=expiry_date,
        )

        mark_registered_request.additional_properties = d
        return mark_registered_request

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
