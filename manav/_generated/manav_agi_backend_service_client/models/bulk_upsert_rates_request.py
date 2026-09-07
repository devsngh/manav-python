from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.exchange_rate_upsert import ExchangeRateUpsert


T = TypeVar("T", bound="BulkUpsertRatesRequest")


@_attrs_define
class BulkUpsertRatesRequest:
    """
    Attributes:
        rates (list[ExchangeRateUpsert]):
    """

    rates: list[ExchangeRateUpsert]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rates = []
        for rates_item_data in self.rates:
            rates_item = rates_item_data.to_dict()
            rates.append(rates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rates": rates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exchange_rate_upsert import ExchangeRateUpsert  # noqa: PLC0415

        d = dict(src_dict)
        rates = []
        _rates = d.pop("rates")
        for rates_item_data in _rates:
            rates_item = ExchangeRateUpsert.from_dict(rates_item_data)

            rates.append(rates_item)

        bulk_upsert_rates_request = cls(
            rates=rates,
        )

        bulk_upsert_rates_request.additional_properties = d
        return bulk_upsert_rates_request

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
