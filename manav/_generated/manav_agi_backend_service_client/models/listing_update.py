from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pricing_model import PricingModel
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingUpdate")


@_attrs_define
class ListingUpdate:
    """
    Attributes:
        title (None | str | Unset):
        short_description (None | str | Unset):
        long_description (None | str | Unset):
        logo_url (None | str | Unset):
        banner_url (None | str | Unset):
        screenshots (list[str] | None | Unset):
        tags (list[str] | None | Unset):
        category_id (None | Unset | UUID):
        pricing_model (None | PricingModel | Unset):
        price_cents_monthly (int | None | Unset):
        price_cents_yearly (int | None | Unset):
        credits_per_query (int | None | Unset):
    """

    title: None | str | Unset = UNSET
    short_description: None | str | Unset = UNSET
    long_description: None | str | Unset = UNSET
    logo_url: None | str | Unset = UNSET
    banner_url: None | str | Unset = UNSET
    screenshots: list[str] | None | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    category_id: None | Unset | UUID = UNSET
    pricing_model: None | PricingModel | Unset = UNSET
    price_cents_monthly: int | None | Unset = UNSET
    price_cents_yearly: int | None | Unset = UNSET
    credits_per_query: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
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

        pricing_model: None | str | Unset
        if isinstance(self.pricing_model, Unset):
            pricing_model = UNSET
        elif isinstance(self.pricing_model, PricingModel):
            pricing_model = self.pricing_model.value
        else:
            pricing_model = self.pricing_model

        price_cents_monthly: int | None | Unset
        if isinstance(self.price_cents_monthly, Unset):
            price_cents_monthly = UNSET
        else:
            price_cents_monthly = self.price_cents_monthly

        price_cents_yearly: int | None | Unset
        if isinstance(self.price_cents_yearly, Unset):
            price_cents_yearly = UNSET
        else:
            price_cents_yearly = self.price_cents_yearly

        credits_per_query: int | None | Unset
        if isinstance(self.credits_per_query, Unset):
            credits_per_query = UNSET
        else:
            credits_per_query = self.credits_per_query

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

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

        def _parse_pricing_model(data: object) -> None | PricingModel | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pricing_model_type_0 = PricingModel(data)

                return pricing_model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PricingModel | Unset, data)

        pricing_model = _parse_pricing_model(d.pop("pricing_model", UNSET))

        def _parse_price_cents_monthly(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        price_cents_monthly = _parse_price_cents_monthly(d.pop("price_cents_monthly", UNSET))

        def _parse_price_cents_yearly(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        price_cents_yearly = _parse_price_cents_yearly(d.pop("price_cents_yearly", UNSET))

        def _parse_credits_per_query(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        credits_per_query = _parse_credits_per_query(d.pop("credits_per_query", UNSET))

        listing_update = cls(
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
        )

        listing_update.additional_properties = d
        return listing_update

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
