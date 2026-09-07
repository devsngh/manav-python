from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_update_metadata_type_0 import ProductUpdateMetadataType0


T = TypeVar("T", bound="ProductUpdate")


@_attrs_define
class ProductUpdate:
    """
    Attributes:
        name (None | str | Unset):
        slug (None | str | Unset):
        description (None | str | Unset):
        category (None | str | Unset):
        status (None | str | Unset):
        launched_at (datetime.datetime | None | Unset):
        sunsetted_at (datetime.datetime | None | Unset):
        owner_bot_id (None | Unset | UUID):
        parent_product_id (None | Unset | UUID):
        logo_asset_id (None | Unset | UUID):
        hero_asset_id (None | Unset | UUID):
        demo_asset_id (None | Unset | UUID):
        website_url (None | str | Unset):
        documentation_url (None | str | Unset):
        metadata (None | ProductUpdateMetadataType0 | Unset):
    """

    name: None | str | Unset = UNSET
    slug: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    launched_at: datetime.datetime | None | Unset = UNSET
    sunsetted_at: datetime.datetime | None | Unset = UNSET
    owner_bot_id: None | Unset | UUID = UNSET
    parent_product_id: None | Unset | UUID = UNSET
    logo_asset_id: None | Unset | UUID = UNSET
    hero_asset_id: None | Unset | UUID = UNSET
    demo_asset_id: None | Unset | UUID = UNSET
    website_url: None | str | Unset = UNSET
    documentation_url: None | str | Unset = UNSET
    metadata: None | ProductUpdateMetadataType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.product_update_metadata_type_0 import ProductUpdateMetadataType0  # noqa: PLC0415

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

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        launched_at: None | str | Unset
        if isinstance(self.launched_at, Unset):
            launched_at = UNSET
        elif isinstance(self.launched_at, datetime.datetime):
            launched_at = self.launched_at.isoformat()
        else:
            launched_at = self.launched_at

        sunsetted_at: None | str | Unset
        if isinstance(self.sunsetted_at, Unset):
            sunsetted_at = UNSET
        elif isinstance(self.sunsetted_at, datetime.datetime):
            sunsetted_at = self.sunsetted_at.isoformat()
        else:
            sunsetted_at = self.sunsetted_at

        owner_bot_id: None | str | Unset
        if isinstance(self.owner_bot_id, Unset):
            owner_bot_id = UNSET
        elif isinstance(self.owner_bot_id, UUID):
            owner_bot_id = str(self.owner_bot_id)
        else:
            owner_bot_id = self.owner_bot_id

        parent_product_id: None | str | Unset
        if isinstance(self.parent_product_id, Unset):
            parent_product_id = UNSET
        elif isinstance(self.parent_product_id, UUID):
            parent_product_id = str(self.parent_product_id)
        else:
            parent_product_id = self.parent_product_id

        logo_asset_id: None | str | Unset
        if isinstance(self.logo_asset_id, Unset):
            logo_asset_id = UNSET
        elif isinstance(self.logo_asset_id, UUID):
            logo_asset_id = str(self.logo_asset_id)
        else:
            logo_asset_id = self.logo_asset_id

        hero_asset_id: None | str | Unset
        if isinstance(self.hero_asset_id, Unset):
            hero_asset_id = UNSET
        elif isinstance(self.hero_asset_id, UUID):
            hero_asset_id = str(self.hero_asset_id)
        else:
            hero_asset_id = self.hero_asset_id

        demo_asset_id: None | str | Unset
        if isinstance(self.demo_asset_id, Unset):
            demo_asset_id = UNSET
        elif isinstance(self.demo_asset_id, UUID):
            demo_asset_id = str(self.demo_asset_id)
        else:
            demo_asset_id = self.demo_asset_id

        website_url: None | str | Unset
        if isinstance(self.website_url, Unset):
            website_url = UNSET
        else:
            website_url = self.website_url

        documentation_url: None | str | Unset
        if isinstance(self.documentation_url, Unset):
            documentation_url = UNSET
        else:
            documentation_url = self.documentation_url

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, ProductUpdateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if description is not UNSET:
            field_dict["description"] = description
        if category is not UNSET:
            field_dict["category"] = category
        if status is not UNSET:
            field_dict["status"] = status
        if launched_at is not UNSET:
            field_dict["launched_at"] = launched_at
        if sunsetted_at is not UNSET:
            field_dict["sunsetted_at"] = sunsetted_at
        if owner_bot_id is not UNSET:
            field_dict["owner_bot_id"] = owner_bot_id
        if parent_product_id is not UNSET:
            field_dict["parent_product_id"] = parent_product_id
        if logo_asset_id is not UNSET:
            field_dict["logo_asset_id"] = logo_asset_id
        if hero_asset_id is not UNSET:
            field_dict["hero_asset_id"] = hero_asset_id
        if demo_asset_id is not UNSET:
            field_dict["demo_asset_id"] = demo_asset_id
        if website_url is not UNSET:
            field_dict["website_url"] = website_url
        if documentation_url is not UNSET:
            field_dict["documentation_url"] = documentation_url
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_update_metadata_type_0 import ProductUpdateMetadataType0  # noqa: PLC0415

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

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_launched_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                launched_at_type_0 = datetime.datetime.fromisoformat(data)

                return launched_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        launched_at = _parse_launched_at(d.pop("launched_at", UNSET))

        def _parse_sunsetted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sunsetted_at_type_0 = datetime.datetime.fromisoformat(data)

                return sunsetted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        sunsetted_at = _parse_sunsetted_at(d.pop("sunsetted_at", UNSET))

        def _parse_owner_bot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_bot_id_type_0 = UUID(data)

                return owner_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        owner_bot_id = _parse_owner_bot_id(d.pop("owner_bot_id", UNSET))

        def _parse_parent_product_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_product_id_type_0 = UUID(data)

                return parent_product_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_product_id = _parse_parent_product_id(d.pop("parent_product_id", UNSET))

        def _parse_logo_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                logo_asset_id_type_0 = UUID(data)

                return logo_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        logo_asset_id = _parse_logo_asset_id(d.pop("logo_asset_id", UNSET))

        def _parse_hero_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                hero_asset_id_type_0 = UUID(data)

                return hero_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        hero_asset_id = _parse_hero_asset_id(d.pop("hero_asset_id", UNSET))

        def _parse_demo_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                demo_asset_id_type_0 = UUID(data)

                return demo_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        demo_asset_id = _parse_demo_asset_id(d.pop("demo_asset_id", UNSET))

        def _parse_website_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_url = _parse_website_url(d.pop("website_url", UNSET))

        def _parse_documentation_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        documentation_url = _parse_documentation_url(d.pop("documentation_url", UNSET))

        def _parse_metadata(data: object) -> None | ProductUpdateMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = ProductUpdateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProductUpdateMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        product_update = cls(
            name=name,
            slug=slug,
            description=description,
            category=category,
            status=status,
            launched_at=launched_at,
            sunsetted_at=sunsetted_at,
            owner_bot_id=owner_bot_id,
            parent_product_id=parent_product_id,
            logo_asset_id=logo_asset_id,
            hero_asset_id=hero_asset_id,
            demo_asset_id=demo_asset_id,
            website_url=website_url,
            documentation_url=documentation_url,
            metadata=metadata,
        )

        product_update.additional_properties = d
        return product_update

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
