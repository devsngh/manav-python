from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.banner_position import BannerPosition
from ..models.banner_type import BannerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.banner_response_style_config_type_0 import BannerResponseStyleConfigType0
    from ..models.listing_response import ListingResponse


T = TypeVar("T", bound="BannerResponse")


@_attrs_define
class BannerResponse:
    """
    Attributes:
        id (UUID):
        title (str):
        subtitle (None | str):
        image_url (str):
        link_url (None | str):
        link_listing_id (None | UUID):
        position (BannerPosition):
        banner_type (BannerType):
        sort_order (int):
        starts_at (datetime.datetime | None):
        ends_at (datetime.datetime | None):
        is_active (bool):
        style_config (BannerResponseStyleConfigType0 | None):
        impressions (int):
        clicks (int):
        created_by (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime | None):
        listing (ListingResponse | None | Unset):
    """

    id: UUID
    title: str
    subtitle: None | str
    image_url: str
    link_url: None | str
    link_listing_id: None | UUID
    position: BannerPosition
    banner_type: BannerType
    sort_order: int
    starts_at: datetime.datetime | None
    ends_at: datetime.datetime | None
    is_active: bool
    style_config: BannerResponseStyleConfigType0 | None
    impressions: int
    clicks: int
    created_by: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime | None
    listing: ListingResponse | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.banner_response_style_config_type_0 import BannerResponseStyleConfigType0  # noqa: PLC0415
        from ..models.listing_response import ListingResponse  # noqa: PLC0415

        id = str(self.id)

        title = self.title

        subtitle: None | str
        subtitle = self.subtitle

        image_url = self.image_url

        link_url: None | str
        link_url = self.link_url

        link_listing_id: None | str
        if isinstance(self.link_listing_id, UUID):
            link_listing_id = str(self.link_listing_id)
        else:
            link_listing_id = self.link_listing_id

        position = self.position.value

        banner_type = self.banner_type.value

        sort_order = self.sort_order

        starts_at: None | str
        if isinstance(self.starts_at, datetime.datetime):
            starts_at = self.starts_at.isoformat()
        else:
            starts_at = self.starts_at

        ends_at: None | str
        if isinstance(self.ends_at, datetime.datetime):
            ends_at = self.ends_at.isoformat()
        else:
            ends_at = self.ends_at

        is_active = self.is_active

        style_config: dict[str, Any] | None
        if isinstance(self.style_config, BannerResponseStyleConfigType0):
            style_config = self.style_config.to_dict()
        else:
            style_config = self.style_config

        impressions = self.impressions

        clicks = self.clicks

        created_by = str(self.created_by)

        created_at = self.created_at.isoformat()

        updated_at: None | str
        if isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        listing: dict[str, Any] | None | Unset
        if isinstance(self.listing, Unset):
            listing = UNSET
        elif isinstance(self.listing, ListingResponse):
            listing = self.listing.to_dict()
        else:
            listing = self.listing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "subtitle": subtitle,
                "image_url": image_url,
                "link_url": link_url,
                "link_listing_id": link_listing_id,
                "position": position,
                "banner_type": banner_type,
                "sort_order": sort_order,
                "starts_at": starts_at,
                "ends_at": ends_at,
                "is_active": is_active,
                "style_config": style_config,
                "impressions": impressions,
                "clicks": clicks,
                "created_by": created_by,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if listing is not UNSET:
            field_dict["listing"] = listing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.banner_response_style_config_type_0 import BannerResponseStyleConfigType0  # noqa: PLC0415
        from ..models.listing_response import ListingResponse  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        title = d.pop("title")

        def _parse_subtitle(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        subtitle = _parse_subtitle(d.pop("subtitle"))

        image_url = d.pop("image_url")

        def _parse_link_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        link_url = _parse_link_url(d.pop("link_url"))

        def _parse_link_listing_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                link_listing_id_type_0 = UUID(data)

                return link_listing_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        link_listing_id = _parse_link_listing_id(d.pop("link_listing_id"))

        position = BannerPosition(d.pop("position"))

        banner_type = BannerType(d.pop("banner_type"))

        sort_order = d.pop("sort_order")

        def _parse_starts_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                starts_at_type_0 = datetime.datetime.fromisoformat(data)

                return starts_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        starts_at = _parse_starts_at(d.pop("starts_at"))

        def _parse_ends_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ends_at_type_0 = datetime.datetime.fromisoformat(data)

                return ends_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        ends_at = _parse_ends_at(d.pop("ends_at"))

        is_active = d.pop("is_active")

        def _parse_style_config(data: object) -> BannerResponseStyleConfigType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                style_config_type_0 = BannerResponseStyleConfigType0.from_dict(data)

                return style_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BannerResponseStyleConfigType0 | None, data)

        style_config = _parse_style_config(d.pop("style_config"))

        impressions = d.pop("impressions")

        clicks = d.pop("clicks")

        created_by = UUID(d.pop("created_by"))

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

        def _parse_listing(data: object) -> ListingResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                listing_type_0 = ListingResponse.from_dict(data)

                return listing_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListingResponse | None | Unset, data)

        listing = _parse_listing(d.pop("listing", UNSET))

        banner_response = cls(
            id=id,
            title=title,
            subtitle=subtitle,
            image_url=image_url,
            link_url=link_url,
            link_listing_id=link_listing_id,
            position=position,
            banner_type=banner_type,
            sort_order=sort_order,
            starts_at=starts_at,
            ends_at=ends_at,
            is_active=is_active,
            style_config=style_config,
            impressions=impressions,
            clicks=clicks,
            created_by=created_by,
            created_at=created_at,
            updated_at=updated_at,
            listing=listing,
        )

        banner_response.additional_properties = d
        return banner_response

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
