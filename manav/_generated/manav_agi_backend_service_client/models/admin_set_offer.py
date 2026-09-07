from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminSetOffer")


@_attrs_define
class AdminSetOffer:
    """
    Attributes:
        offer_price_cents (int | Unset):  Default: 0.
        offer_price_cents_monthly (int | Unset):  Default: 0.
        offer_price_cents_yearly (int | Unset):  Default: 0.
        offer_ends_at (datetime.datetime | None | Unset):
        platform_commission_cents (int | None | Unset):
    """

    offer_price_cents: int | Unset = 0
    offer_price_cents_monthly: int | Unset = 0
    offer_price_cents_yearly: int | Unset = 0
    offer_ends_at: datetime.datetime | None | Unset = UNSET
    platform_commission_cents: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offer_price_cents = self.offer_price_cents

        offer_price_cents_monthly = self.offer_price_cents_monthly

        offer_price_cents_yearly = self.offer_price_cents_yearly

        offer_ends_at: None | str | Unset
        if isinstance(self.offer_ends_at, Unset):
            offer_ends_at = UNSET
        elif isinstance(self.offer_ends_at, datetime.datetime):
            offer_ends_at = self.offer_ends_at.isoformat()
        else:
            offer_ends_at = self.offer_ends_at

        platform_commission_cents: int | None | Unset
        if isinstance(self.platform_commission_cents, Unset):
            platform_commission_cents = UNSET
        else:
            platform_commission_cents = self.platform_commission_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if offer_price_cents is not UNSET:
            field_dict["offer_price_cents"] = offer_price_cents
        if offer_price_cents_monthly is not UNSET:
            field_dict["offer_price_cents_monthly"] = offer_price_cents_monthly
        if offer_price_cents_yearly is not UNSET:
            field_dict["offer_price_cents_yearly"] = offer_price_cents_yearly
        if offer_ends_at is not UNSET:
            field_dict["offer_ends_at"] = offer_ends_at
        if platform_commission_cents is not UNSET:
            field_dict["platform_commission_cents"] = platform_commission_cents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offer_price_cents = d.pop("offer_price_cents", UNSET)

        offer_price_cents_monthly = d.pop("offer_price_cents_monthly", UNSET)

        offer_price_cents_yearly = d.pop("offer_price_cents_yearly", UNSET)

        def _parse_offer_ends_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                offer_ends_at_type_0 = datetime.datetime.fromisoformat(data)

                return offer_ends_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        offer_ends_at = _parse_offer_ends_at(d.pop("offer_ends_at", UNSET))

        def _parse_platform_commission_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        platform_commission_cents = _parse_platform_commission_cents(d.pop("platform_commission_cents", UNSET))

        admin_set_offer = cls(
            offer_price_cents=offer_price_cents,
            offer_price_cents_monthly=offer_price_cents_monthly,
            offer_price_cents_yearly=offer_price_cents_yearly,
            offer_ends_at=offer_ends_at,
            platform_commission_cents=platform_commission_cents,
        )

        admin_set_offer.additional_properties = d
        return admin_set_offer

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
