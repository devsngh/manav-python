from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExchangeRateResponse")


@_attrs_define
class ExchangeRateResponse:
    """
    Attributes:
        id (UUID):
        from_currency_id (UUID):
        to_currency_id (UUID):
        rate_type_id (UUID):
        rate (str):
        effective_date (datetime.date):
        created_at (datetime.datetime):
    """

    id: UUID
    from_currency_id: UUID
    to_currency_id: UUID
    rate_type_id: UUID
    rate: str
    effective_date: datetime.date
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        from_currency_id = str(self.from_currency_id)

        to_currency_id = str(self.to_currency_id)

        rate_type_id = str(self.rate_type_id)

        rate = self.rate

        effective_date = self.effective_date.isoformat()

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "from_currency_id": from_currency_id,
                "to_currency_id": to_currency_id,
                "rate_type_id": rate_type_id,
                "rate": rate,
                "effective_date": effective_date,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        from_currency_id = UUID(d.pop("from_currency_id"))

        to_currency_id = UUID(d.pop("to_currency_id"))

        rate_type_id = UUID(d.pop("rate_type_id"))

        rate = d.pop("rate")

        effective_date = datetime.date.fromisoformat(d.pop("effective_date"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        exchange_rate_response = cls(
            id=id,
            from_currency_id=from_currency_id,
            to_currency_id=to_currency_id,
            rate_type_id=rate_type_id,
            rate=rate,
            effective_date=effective_date,
            created_at=created_at,
        )

        exchange_rate_response.additional_properties = d
        return exchange_rate_response

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
