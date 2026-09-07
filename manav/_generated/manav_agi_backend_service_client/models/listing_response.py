from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.listing_status import ListingStatus
from ..models.marketplace_item_type import MarketplaceItemType
from ..models.pricing_model import PricingModel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category_response import CategoryResponse


T = TypeVar("T", bound="ListingResponse")


@_attrs_define
class ListingResponse:
    """
    Attributes:
        id (UUID):
        item_type (MarketplaceItemType):
        item_id (UUID):
        slug (str):
        title (str):
        short_description (None | str):
        long_description (None | str):
        logo_url (None | str):
        banner_url (None | str):
        screenshots (list[str] | None):
        tags (list[str] | None):
        category_id (None | UUID):
        pricing_model (PricingModel):
        price_cents_monthly (int):
        price_cents_yearly (int):
        publisher_org_id (None | UUID):
        publisher_user_id (UUID):
        status (ListingStatus):
        install_count (int):
        rating_avg (float):
        rating_count (int):
        is_platform_item (bool):
        version (str):
        listed_at (datetime.datetime | None):
        created_at (datetime.datetime):
        updated_at (datetime.datetime | None):
        category (CategoryResponse | None | Unset):
        credits_per_query (int | Unset):  Default: 0.
        offer_price_cents_monthly (int | Unset):  Default: 0.
        offer_price_cents_yearly (int | Unset):  Default: 0.
        offer_ends_at (datetime.datetime | None | Unset):
        platform_commission_cents (int | Unset):  Default: 200.
        has_active_offer (bool | Unset):  Default: False.
        is_featured (bool | Unset):  Default: False.
    """

    id: UUID
    item_type: MarketplaceItemType
    item_id: UUID
    slug: str
    title: str
    short_description: None | str
    long_description: None | str
    logo_url: None | str
    banner_url: None | str
    screenshots: list[str] | None
    tags: list[str] | None
    category_id: None | UUID
    pricing_model: PricingModel
    price_cents_monthly: int
    price_cents_yearly: int
    publisher_org_id: None | UUID
    publisher_user_id: UUID
    status: ListingStatus
    install_count: int
    rating_avg: float
    rating_count: int
    is_platform_item: bool
    version: str
    listed_at: datetime.datetime | None
    created_at: datetime.datetime
    updated_at: datetime.datetime | None
    category: CategoryResponse | None | Unset = UNSET
    credits_per_query: int | Unset = 0
    offer_price_cents_monthly: int | Unset = 0
    offer_price_cents_yearly: int | Unset = 0
    offer_ends_at: datetime.datetime | None | Unset = UNSET
    platform_commission_cents: int | Unset = 200
    has_active_offer: bool | Unset = False
    is_featured: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.category_response import CategoryResponse  # noqa: PLC0415

        id = str(self.id)

        item_type = self.item_type.value

        item_id = str(self.item_id)

        slug = self.slug

        title = self.title

        short_description: None | str
        short_description = self.short_description

        long_description: None | str
        long_description = self.long_description

        logo_url: None | str
        logo_url = self.logo_url

        banner_url: None | str
        banner_url = self.banner_url

        screenshots: list[str] | None
        if isinstance(self.screenshots, list):
            screenshots = self.screenshots

        else:
            screenshots = self.screenshots

        tags: list[str] | None
        if isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        category_id: None | str
        if isinstance(self.category_id, UUID):
            category_id = str(self.category_id)
        else:
            category_id = self.category_id

        pricing_model = self.pricing_model.value

        price_cents_monthly = self.price_cents_monthly

        price_cents_yearly = self.price_cents_yearly

        publisher_org_id: None | str
        if isinstance(self.publisher_org_id, UUID):
            publisher_org_id = str(self.publisher_org_id)
        else:
            publisher_org_id = self.publisher_org_id

        publisher_user_id = str(self.publisher_user_id)

        status = self.status.value

        install_count = self.install_count

        rating_avg = self.rating_avg

        rating_count = self.rating_count

        is_platform_item = self.is_platform_item

        version = self.version

        listed_at: None | str
        if isinstance(self.listed_at, datetime.datetime):
            listed_at = self.listed_at.isoformat()
        else:
            listed_at = self.listed_at

        created_at = self.created_at.isoformat()

        updated_at: None | str
        if isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        category: dict[str, Any] | None | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        elif isinstance(self.category, CategoryResponse):
            category = self.category.to_dict()
        else:
            category = self.category

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

        has_active_offer = self.has_active_offer

        is_featured = self.is_featured

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "item_type": item_type,
                "item_id": item_id,
                "slug": slug,
                "title": title,
                "short_description": short_description,
                "long_description": long_description,
                "logo_url": logo_url,
                "banner_url": banner_url,
                "screenshots": screenshots,
                "tags": tags,
                "category_id": category_id,
                "pricing_model": pricing_model,
                "price_cents_monthly": price_cents_monthly,
                "price_cents_yearly": price_cents_yearly,
                "publisher_org_id": publisher_org_id,
                "publisher_user_id": publisher_user_id,
                "status": status,
                "install_count": install_count,
                "rating_avg": rating_avg,
                "rating_count": rating_count,
                "is_platform_item": is_platform_item,
                "version": version,
                "listed_at": listed_at,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
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
        if has_active_offer is not UNSET:
            field_dict["has_active_offer"] = has_active_offer
        if is_featured is not UNSET:
            field_dict["is_featured"] = is_featured

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category_response import CategoryResponse  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        item_type = MarketplaceItemType(d.pop("item_type"))

        item_id = UUID(d.pop("item_id"))

        slug = d.pop("slug")

        title = d.pop("title")

        def _parse_short_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        short_description = _parse_short_description(d.pop("short_description"))

        def _parse_long_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        long_description = _parse_long_description(d.pop("long_description"))

        def _parse_logo_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        logo_url = _parse_logo_url(d.pop("logo_url"))

        def _parse_banner_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        banner_url = _parse_banner_url(d.pop("banner_url"))

        def _parse_screenshots(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                screenshots_type_0 = cast(list[str], data)

                return screenshots_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        screenshots = _parse_screenshots(d.pop("screenshots"))

        def _parse_tags(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        tags = _parse_tags(d.pop("tags"))

        def _parse_category_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                category_id_type_0 = UUID(data)

                return category_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        category_id = _parse_category_id(d.pop("category_id"))

        pricing_model = PricingModel(d.pop("pricing_model"))

        price_cents_monthly = d.pop("price_cents_monthly")

        price_cents_yearly = d.pop("price_cents_yearly")

        def _parse_publisher_org_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                publisher_org_id_type_0 = UUID(data)

                return publisher_org_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        publisher_org_id = _parse_publisher_org_id(d.pop("publisher_org_id"))

        publisher_user_id = UUID(d.pop("publisher_user_id"))

        status = ListingStatus(d.pop("status"))

        install_count = d.pop("install_count")

        rating_avg = d.pop("rating_avg")

        rating_count = d.pop("rating_count")

        is_platform_item = d.pop("is_platform_item")

        version = d.pop("version")

        def _parse_listed_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                listed_at_type_0 = datetime.datetime.fromisoformat(data)

                return listed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        listed_at = _parse_listed_at(d.pop("listed_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_updated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))

        def _parse_category(data: object) -> CategoryResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                category_type_0 = CategoryResponse.from_dict(data)

                return category_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CategoryResponse | None | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

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

        has_active_offer = d.pop("has_active_offer", UNSET)

        is_featured = d.pop("is_featured", UNSET)

        listing_response = cls(
            id=id,
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
            publisher_org_id=publisher_org_id,
            publisher_user_id=publisher_user_id,
            status=status,
            install_count=install_count,
            rating_avg=rating_avg,
            rating_count=rating_count,
            is_platform_item=is_platform_item,
            version=version,
            listed_at=listed_at,
            created_at=created_at,
            updated_at=updated_at,
            category=category,
            credits_per_query=credits_per_query,
            offer_price_cents_monthly=offer_price_cents_monthly,
            offer_price_cents_yearly=offer_price_cents_yearly,
            offer_ends_at=offer_ends_at,
            platform_commission_cents=platform_commission_cents,
            has_active_offer=has_active_offer,
            is_featured=is_featured,
        )

        listing_response.additional_properties = d
        return listing_response

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
