from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExchangeRateUpsert")


@_attrs_define
class ExchangeRateUpsert:
    """
    Attributes:
        from_currency_id (UUID):
        to_currency_id (UUID):
        rate_type_id (UUID):
        rate (float | str):
        effective_date (datetime.date):
    """

    from_currency_id: UUID
    to_currency_id: UUID
    rate_type_id: UUID
    rate: float | str
    effective_date: datetime.date
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_currency_id = str(self.from_currency_id)

        to_currency_id = str(self.to_currency_id)

        rate_type_id = str(self.rate_type_id)

        rate: float | str
        rate = self.rate

        effective_date = self.effective_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from_currency_id": from_currency_id,
                "to_currency_id": to_currency_id,
                "rate_type_id": rate_type_id,
                "rate": rate,
                "effective_date": effective_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_currency_id = UUID(d.pop("from_currency_id"))

        to_currency_id = UUID(d.pop("to_currency_id"))

        rate_type_id = UUID(d.pop("rate_type_id"))

        def _parse_rate(data: object) -> float | str:
            return cast(float | str, data)

        rate = _parse_rate(d.pop("rate"))

        effective_date = datetime.date.fromisoformat(d.pop("effective_date"))

        exchange_rate_upsert = cls(
            from_currency_id=from_currency_id,
            to_currency_id=to_currency_id,
            rate_type_id=rate_type_id,
            rate=rate,
            effective_date=effective_date,
        )

        exchange_rate_upsert.additional_properties = d
        return exchange_rate_upsert

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
