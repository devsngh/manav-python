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
    from ..models.banner_create_style_config_type_0 import BannerCreateStyleConfigType0


T = TypeVar("T", bound="BannerCreate")


@_attrs_define
class BannerCreate:
    """
    Attributes:
        title (str):
        subtitle (None | str | Unset):
        link_url (None | str | Unset):
        link_listing_id (None | Unset | UUID):
        position (BannerPosition | Unset):  Default: BannerPosition.HERO_TOP.
        banner_type (BannerType | Unset):  Default: BannerType.PROMOTIONAL.
        sort_order (int | Unset):  Default: 0.
        starts_at (datetime.datetime | None | Unset):
        ends_at (datetime.datetime | None | Unset):
        is_active (bool | Unset):  Default: True.
        style_config (BannerCreateStyleConfigType0 | None | Unset):
    """

    title: str
    subtitle: None | str | Unset = UNSET
    link_url: None | str | Unset = UNSET
    link_listing_id: None | Unset | UUID = UNSET
    position: BannerPosition | Unset = BannerPosition.HERO_TOP
    banner_type: BannerType | Unset = BannerType.PROMOTIONAL
    sort_order: int | Unset = 0
    starts_at: datetime.datetime | None | Unset = UNSET
    ends_at: datetime.datetime | None | Unset = UNSET
    is_active: bool | Unset = True
    style_config: BannerCreateStyleConfigType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.banner_create_style_config_type_0 import BannerCreateStyleConfigType0  # noqa: PLC0415

        title = self.title

        subtitle: None | str | Unset
        if isinstance(self.subtitle, Unset):
            subtitle = UNSET
        else:
            subtitle = self.subtitle

        link_url: None | str | Unset
        if isinstance(self.link_url, Unset):
            link_url = UNSET
        else:
            link_url = self.link_url

        link_listing_id: None | str | Unset
        if isinstance(self.link_listing_id, Unset):
            link_listing_id = UNSET
        elif isinstance(self.link_listing_id, UUID):
            link_listing_id = str(self.link_listing_id)
        else:
            link_listing_id = self.link_listing_id

        position: str | Unset = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.value

        banner_type: str | Unset = UNSET
        if not isinstance(self.banner_type, Unset):
            banner_type = self.banner_type.value

        sort_order = self.sort_order

        starts_at: None | str | Unset
        if isinstance(self.starts_at, Unset):
            starts_at = UNSET
        elif isinstance(self.starts_at, datetime.datetime):
            starts_at = self.starts_at.isoformat()
        else:
            starts_at = self.starts_at

        ends_at: None | str | Unset
        if isinstance(self.ends_at, Unset):
            ends_at = UNSET
        elif isinstance(self.ends_at, datetime.datetime):
            ends_at = self.ends_at.isoformat()
        else:
            ends_at = self.ends_at

        is_active = self.is_active

        style_config: dict[str, Any] | None | Unset
        if isinstance(self.style_config, Unset):
            style_config = UNSET
        elif isinstance(self.style_config, BannerCreateStyleConfigType0):
            style_config = self.style_config.to_dict()
        else:
            style_config = self.style_config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if link_url is not UNSET:
            field_dict["link_url"] = link_url
        if link_listing_id is not UNSET:
            field_dict["link_listing_id"] = link_listing_id
        if position is not UNSET:
            field_dict["position"] = position
        if banner_type is not UNSET:
            field_dict["banner_type"] = banner_type
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order
        if starts_at is not UNSET:
            field_dict["starts_at"] = starts_at
        if ends_at is not UNSET:
            field_dict["ends_at"] = ends_at
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if style_config is not UNSET:
            field_dict["style_config"] = style_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.banner_create_style_config_type_0 import BannerCreateStyleConfigType0  # noqa: PLC0415

        d = dict(src_dict)
        title = d.pop("title")

        def _parse_subtitle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subtitle = _parse_subtitle(d.pop("subtitle", UNSET))

        def _parse_link_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        link_url = _parse_link_url(d.pop("link_url", UNSET))

        def _parse_link_listing_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                link_listing_id_type_0 = UUID(data)

                return link_listing_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        link_listing_id = _parse_link_listing_id(d.pop("link_listing_id", UNSET))

        _position = d.pop("position", UNSET)
        position: BannerPosition | Unset
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = BannerPosition(_position)

        _banner_type = d.pop("banner_type", UNSET)
        banner_type: BannerType | Unset
        if isinstance(_banner_type, Unset):
            banner_type = UNSET
        else:
            banner_type = BannerType(_banner_type)

        sort_order = d.pop("sort_order", UNSET)

        def _parse_starts_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                starts_at_type_0 = datetime.datetime.fromisoformat(data)

                return starts_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        starts_at = _parse_starts_at(d.pop("starts_at", UNSET))

        def _parse_ends_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ends_at_type_0 = datetime.datetime.fromisoformat(data)

                return ends_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        ends_at = _parse_ends_at(d.pop("ends_at", UNSET))

        is_active = d.pop("is_active", UNSET)

        def _parse_style_config(data: object) -> BannerCreateStyleConfigType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                style_config_type_0 = BannerCreateStyleConfigType0.from_dict(data)

                return style_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BannerCreateStyleConfigType0 | None | Unset, data)

        style_config = _parse_style_config(d.pop("style_config", UNSET))

        banner_create = cls(
            title=title,
            subtitle=subtitle,
            link_url=link_url,
            link_listing_id=link_listing_id,
            position=position,
            banner_type=banner_type,
            sort_order=sort_order,
            starts_at=starts_at,
            ends_at=ends_at,
            is_active=is_active,
            style_config=style_config,
        )

        banner_create.additional_properties = d
        return banner_create

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
