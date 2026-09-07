from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CurrencyCreate")


@_attrs_define
class CurrencyCreate:
    """
    Attributes:
        code (str): ISO 4217 code (USD, INR, EUR)
        name (str):
        symbol (None | str | Unset):
        decimal_places (int | Unset):  Default: 2.
        is_active (bool | Unset):  Default: True.
    """

    code: str
    name: str
    symbol: None | str | Unset = UNSET
    decimal_places: int | Unset = 2
    is_active: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        name = self.name

        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        decimal_places = self.decimal_places

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "name": name,
            }
        )
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if decimal_places is not UNSET:
            field_dict["decimal_places"] = decimal_places
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        name = d.pop("name")

        def _parse_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol = _parse_symbol(d.pop("symbol", UNSET))

        decimal_places = d.pop("decimal_places", UNSET)

        is_active = d.pop("is_active", UNSET)

        currency_create = cls(
            code=code,
            name=name,
            symbol=symbol,
            decimal_places=decimal_places,
            is_active=is_active,
        )

        currency_create.additional_properties = d
        return currency_create

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
