from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditPackUpdate")


@_attrs_define
class CreditPackUpdate:
    """
    Attributes:
        name (None | str | Unset):
        slug (None | str | Unset):
        credits_ (int | None | Unset):
        price_cents (int | None | Unset):
        stripe_price_id (None | str | Unset):
        is_active (bool | None | Unset):
        sort_order (int | None | Unset):
    """

    name: None | str | Unset = UNSET
    slug: None | str | Unset = UNSET
    credits_: int | None | Unset = UNSET
    price_cents: int | None | Unset = UNSET
    stripe_price_id: None | str | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    sort_order: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        credits_: int | None | Unset
        if isinstance(self.credits_, Unset):
            credits_ = UNSET
        else:
            credits_ = self.credits_

        price_cents: int | None | Unset
        if isinstance(self.price_cents, Unset):
            price_cents = UNSET
        else:
            price_cents = self.price_cents

        stripe_price_id: None | str | Unset
        if isinstance(self.stripe_price_id, Unset):
            stripe_price_id = UNSET
        else:
            stripe_price_id = self.stripe_price_id

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        sort_order: int | None | Unset
        if isinstance(self.sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = self.sort_order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if credits_ is not UNSET:
            field_dict["credits"] = credits_
        if price_cents is not UNSET:
            field_dict["price_cents"] = price_cents
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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_credits_(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        credits_ = _parse_credits_(d.pop("credits", UNSET))

        def _parse_price_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        price_cents = _parse_price_cents(d.pop("price_cents", UNSET))

        def _parse_stripe_price_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stripe_price_id = _parse_stripe_price_id(d.pop("stripe_price_id", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        def _parse_sort_order(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sort_order = _parse_sort_order(d.pop("sort_order", UNSET))

        credit_pack_update = cls(
            name=name,
            slug=slug,
            credits_=credits_,
            price_cents=price_cents,
            stripe_price_id=stripe_price_id,
            is_active=is_active,
            sort_order=sort_order,
        )

        credit_pack_update.additional_properties = d
        return credit_pack_update

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
