from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditPackCreate")


@_attrs_define
class CreditPackCreate:
    """
    Attributes:
        name (str):
        slug (str):
        credits_ (int):
        price_cents (int):
        stripe_price_id (None | str | Unset):
        is_active (bool | Unset):  Default: True.
        sort_order (int | Unset):  Default: 0.
    """

    name: str
    slug: str
    credits_: int
    price_cents: int
    stripe_price_id: None | str | Unset = UNSET
    is_active: bool | Unset = True
    sort_order: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug = self.slug

        credits_ = self.credits_

        price_cents = self.price_cents

        stripe_price_id: None | str | Unset
        if isinstance(self.stripe_price_id, Unset):
            stripe_price_id = UNSET
        else:
            stripe_price_id = self.stripe_price_id

        is_active = self.is_active

        sort_order = self.sort_order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "slug": slug,
                "credits": credits_,
                "price_cents": price_cents,
            }
        )
        if stripe_price_id is not UNSET:
            field_dict["stripe_price_id"] = stripe_price_id
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        slug = d.pop("slug")

        credits_ = d.pop("credits")

        price_cents = d.pop("price_cents")

        def _parse_stripe_price_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stripe_price_id = _parse_stripe_price_id(d.pop("stripe_price_id", UNSET))

        is_active = d.pop("is_active", UNSET)

        sort_order = d.pop("sort_order", UNSET)

        credit_pack_create = cls(
            name=name,
            slug=slug,
            credits_=credits_,
            price_cents=price_cents,
            stripe_price_id=stripe_price_id,
            is_active=is_active,
            sort_order=sort_order,
        )

        credit_pack_create.additional_properties = d
        return credit_pack_create

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
