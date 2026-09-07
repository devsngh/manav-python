from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConvertAmountResponse")


@_attrs_define
class ConvertAmountResponse:
    """
    Attributes:
        original_amount (str):
        original_currency (UUID):
        converted_amount (str):
        converted_currency (UUID):
        rate (str):
        rate_effective (datetime.date):
    """

    original_amount: str
    original_currency: UUID
    converted_amount: str
    converted_currency: UUID
    rate: str
    rate_effective: datetime.date
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        original_amount = self.original_amount

        original_currency = str(self.original_currency)

        converted_amount = self.converted_amount

        converted_currency = str(self.converted_currency)

        rate = self.rate

        rate_effective = self.rate_effective.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "original_amount": original_amount,
                "original_currency": original_currency,
                "converted_amount": converted_amount,
                "converted_currency": converted_currency,
                "rate": rate,
                "rate_effective": rate_effective,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        original_amount = d.pop("original_amount")

        original_currency = UUID(d.pop("original_currency"))

        converted_amount = d.pop("converted_amount")

        converted_currency = UUID(d.pop("converted_currency"))

        rate = d.pop("rate")

        rate_effective = datetime.date.fromisoformat(d.pop("rate_effective"))

        convert_amount_response = cls(
            original_amount=original_amount,
            original_currency=original_currency,
            converted_amount=converted_amount,
            converted_currency=converted_currency,
            rate=rate,
            rate_effective=rate_effective,
        )

        convert_amount_response.additional_properties = d
        return convert_amount_response

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
