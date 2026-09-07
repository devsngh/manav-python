from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.marketplace_item_type import MarketplaceItemType
from ..models.pricing_model import PricingModel
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingCreate")


@_attrs_define
class ListingCreate:
    """
    Attributes:
        item_type (MarketplaceItemType):
        item_id (UUID):
        slug (str):
        title (str):
        short_description (None | str | Unset):
        long_description (None | str | Unset):
        logo_url (None | str | Unset):
        banner_url (None | str | Unset):
        screenshots (list[str] | None | Unset):
        tags (list[str] | None | Unset):
        category_id (None | Unset | UUID):
        pricing_model (PricingModel | Unset):  Default: PricingModel.FREE.
        price_cents_monthly (int | Unset):  Default: 0.
        price_cents_yearly (int | Unset):  Default: 0.
        credits_per_query (int | Unset):  Default: 0.
        offer_price_cents_monthly (int | Unset):  Default: 0.
        offer_price_cents_yearly (int | Unset):  Default: 0.
        offer_ends_at (datetime.datetime | None | Unset):
        platform_commission_cents (int | Unset):  Default: 200.
        is_platform_item (bool | Unset):  Default: False.
        revenue_share_pct (int | Unset):  Default: 70.
    """

    item_type: MarketplaceItemType
    item_id: UUID
    slug: str
    title: str
    short_description: None | str | Unset = UNSET
    long_description: None | str | Unset = UNSET
    logo_url: None | str | Unset = UNSET
    banner_url: None | str | Unset = UNSET
    screenshots: list[str] | None | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    category_id: None | Unset | UUID = UNSET
    pricing_model: PricingModel | Unset = PricingModel.FREE
    price_cents_monthly: int | Unset = 0
    price_cents_yearly: int | Unset = 0
    credits_per_query: int | Unset = 0
    offer_price_cents_monthly: int | Unset = 0
    offer_price_cents_yearly: int | Unset = 0
    offer_ends_at: datetime.datetime | None | Unset = UNSET
    platform_commission_cents: int | Unset = 200
    is_platform_item: bool | Unset = False
    revenue_share_pct: int | Unset = 70
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_type = self.item_type.value

        item_id = str(self.item_id)

        slug = self.slug

        title = self.title

        short_description: None | str | Unset
        if isinstance(self.short_description, Unset):
            short_description = UNSET
        else:
            short_description = self.short_description

        long_description: None | str | Unset
        if isinstance(self.long_description, Unset):
            long_description = UNSET
        else:
            long_description = self.long_description

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        banner_url: None | str | Unset
        if isinstance(self.banner_url, Unset):
            banner_url = UNSET
        else:
            banner_url = self.banner_url

        screenshots: list[str] | None | Unset
        if isinstance(self.screenshots, Unset):
            screenshots = UNSET
        elif isinstance(self.screenshots, list):
            screenshots = self.screenshots

        else:
            screenshots = self.screenshots

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        category_id: None | str | Unset
        if isinstance(self.category_id, Unset):
            category_id = UNSET
        elif isinstance(self.category_id, UUID):
            category_id = str(self.category_id)
        else:
            category_id = self.category_id

        pricing_model: str | Unset = UNSET
        if not isinstance(self.pricing_model, Unset):
            pricing_model = self.pricing_model.value

        price_cents_monthly = self.price_cents_monthly

        price_cents_yearly = self.price_cents_yearly

        credits_per_query = self.credits_per_query

        offer_price_cents_monthly = self.offer_price_cents_monthly

        offer_price_cents_yearly = self.offer_price_cents_yearly

        offer_ends_at: None | str | Unset
        if isinstance(self.offer_ends_at, Unset):
            offer_ends_at = UNSET
        elif isinstance(self.offer_ends_at, datetime.datetime):
            offer_ends_at = self.offer_ends_at.isoformat()
        else:
            offer_ends_at = self.offer_ends_at

        platform_commission_cents = self.platform_commission_cents

        is_platform_item = self.is_platform_item

        revenue_share_pct = self.revenue_share_pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item_type": item_type,
                "item_id": item_id,
                "slug": slug,
                "title": title,
            }
        )
        if short_description is not UNSET:
            field_dict["short_description"] = short_description
        if long_description is not UNSET:
            field_dict["long_description"] = long_description
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if banner_url is not UNSET:
            field_dict["banner_url"] = banner_url
        if screenshots is not UNSET:
            field_dict["screenshots"] = screenshots
        if tags is not UNSET:
            field_dict["tags"] = tags
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if pricing_model is not UNSET:
            field_dict["pricing_model"] = pricing_model
        if price_cents_monthly is not UNSET:
            field_dict["price_cents_monthly"] = price_cents_monthly
        if price_cents_yearly is not UNSET:
            field_dict["price_cents_yearly"] = price_cents_yearly
        if credits_per_query is not UNSET:
            field_dict["credits_per_query"] = credits_per_query
        if offer_price_cents_monthly is not UNSET:
            field_dict["offer_price_cents_monthly"] = offer_price_cents_monthly
        if offer_price_cents_yearly is not UNSET:
            field_dict["offer_price_cents_yearly"] = offer_price_cents_yearly
        if offer_ends_at is not UNSET:
            field_dict["offer_ends_at"] = offer_ends_at
        if platform_commission_cents is not UNSET:
            field_dict["platform_commission_cents"] = platform_commission_cents
        if is_platform_item is not UNSET:
            field_dict["is_platform_item"] = is_platform_item
        if revenue_share_pct is not UNSET:
            field_dict["revenue_share_pct"] = revenue_share_pct

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_type = MarketplaceItemType(d.pop("item_type"))

        item_id = UUID(d.pop("item_id"))

        slug = d.pop("slug")

        title = d.pop("title")

        def _parse_short_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        short_description = _parse_short_description(d.pop("short_description", UNSET))

        def _parse_long_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        long_description = _parse_long_description(d.pop("long_description", UNSET))

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))

        def _parse_banner_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        banner_url = _parse_banner_url(d.pop("banner_url", UNSET))

        def _parse_screenshots(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                screenshots_type_0 = cast(list[str], data)

                return screenshots_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        screenshots = _parse_screenshots(d.pop("screenshots", UNSET))

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_category_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                category_id_type_0 = UUID(data)

                return category_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        category_id = _parse_category_id(d.pop("category_id", UNSET))

        _pricing_model = d.pop("pricing_model", UNSET)
        pricing_model: PricingModel | Unset
        if isinstance(_pricing_model, Unset):
            pricing_model = UNSET
        else:
            pricing_model = PricingModel(_pricing_model)

        price_cents_monthly = d.pop("price_cents_monthly", UNSET)

        price_cents_yearly = d.pop("price_cents_yearly", UNSET)

        credits_per_query = d.pop("credits_per_query", UNSET)

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

        platform_commission_cents = d.pop("platform_commission_cents", UNSET)

        is_platform_item = d.pop("is_platform_item", UNSET)

        revenue_share_pct = d.pop("revenue_share_pct", UNSET)

        listing_create = cls(
            item_type=item_type,
            item_id=item_id,
            slug=slug,
            title=title,
            short_description=short_description,
            long_description=long_description,
            logo_url=logo_url,
            banner_url=banner_url,
            screenshots=screenshots,
            tags=tags,
            category_id=category_id,
            pricing_model=pricing_model,
            price_cents_monthly=price_cents_monthly,
            price_cents_yearly=price_cents_yearly,
            credits_per_query=credits_per_query,
            offer_price_cents_monthly=offer_price_cents_monthly,
            offer_price_cents_yearly=offer_price_cents_yearly,
            offer_ends_at=offer_ends_at,
            platform_commission_cents=platform_commission_cents,
            is_platform_item=is_platform_item,
            revenue_share_pct=revenue_share_pct,
        )

        listing_create.additional_properties = d
        return listing_create

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
