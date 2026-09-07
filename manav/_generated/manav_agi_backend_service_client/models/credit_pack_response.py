from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditPackResponse")


@_attrs_define
class CreditPackResponse:
    """
    Attributes:
        id (UUID):
        name (str):
        slug (str):
        credits_ (int):
        price_cents (int):
        is_active (bool):
        sort_order (int):
        stripe_price_id (None | str | Unset):
        created_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    id: UUID
    name: str
    slug: str
    credits_: int
    price_cents: int
    is_active: bool
    sort_order: int
    stripe_price_id: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        slug = self.slug

        credits_ = self.credits_

        price_cents = self.price_cents

        is_active = self.is_active

        sort_order = self.sort_order

        stripe_price_id: None | str | Unset
        if isinstance(self.stripe_price_id, Unset):
            stripe_price_id = UNSET
        else:
            stripe_price_id = self.stripe_price_id

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "credits": credits_,
                "price_cents": price_cents,
                "is_active": is_active,
                "sort_order": sort_order,
            }
        )
        if stripe_price_id is not UNSET:
            field_dict["stripe_price_id"] = stripe_price_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        slug = d.pop("slug")

        credits_ = d.pop("credits")

        price_cents = d.pop("price_cents")

        is_active = d.pop("is_active")

        sort_order = d.pop("sort_order")

        def _parse_stripe_price_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stripe_price_id = _parse_stripe_price_id(d.pop("stripe_price_id", UNSET))

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        credit_pack_response = cls(
            id=id,
            name=name,
            slug=slug,
            credits_=credits_,
            price_cents=price_cents,
            is_active=is_active,
            sort_order=sort_order,
            stripe_price_id=stripe_price_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        credit_pack_response.additional_properties = d
        return credit_pack_response

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
