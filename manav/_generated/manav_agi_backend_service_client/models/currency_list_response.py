from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.currency_response import CurrencyResponse


T = TypeVar("T", bound="CurrencyListResponse")


@_attrs_define
class CurrencyListResponse:
    """
    Attributes:
        currencies (list[CurrencyResponse]):
        total (int):
    """

    currencies: list[CurrencyResponse]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currencies = []
        for currencies_item_data in self.currencies:
            currencies_item = currencies_item_data.to_dict()
            currencies.append(currencies_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currencies": currencies,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.currency_response import CurrencyResponse  # noqa: PLC0415

        d = dict(src_dict)
        currencies = []
        _currencies = d.pop("currencies")
        for currencies_item_data in _currencies:
            currencies_item = CurrencyResponse.from_dict(currencies_item_data)

            currencies.append(currencies_item)

        total = d.pop("total")

        currency_list_response = cls(
            currencies=currencies,
            total=total,
        )

        currency_list_response.additional_properties = d
        return currency_list_response

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
