from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_response_metadata_type_0 import ProductResponseMetadataType0


T = TypeVar("T", bound="ProductResponse")


@_attrs_define
class ProductResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        name (str):
        slug (str):
        description (None | str):
        category (None | str):
        status (str):
        launched_at (datetime.datetime | None):
        sunsetted_at (datetime.datetime | None):
        owner_bot_id (None | UUID):
        parent_product_id (None | UUID):
        logo_asset_id (None | UUID):
        hero_asset_id (None | UUID):
        demo_asset_id (None | UUID):
        website_url (None | str):
        documentation_url (None | str):
        created_by_bot_id (None | UUID):
        approved_by_user_id (None | UUID):
        last_modified_by_bot_id (None | UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        deleted_at (datetime.datetime | None):
        metadata (None | ProductResponseMetadataType0 | Unset):
    """

    id: UUID
    org_id: UUID
    name: str
    slug: str
    description: None | str
    category: None | str
    status: str
    launched_at: datetime.datetime | None
    sunsetted_at: datetime.datetime | None
    owner_bot_id: None | UUID
    parent_product_id: None | UUID
    logo_asset_id: None | UUID
    hero_asset_id: None | UUID
    demo_asset_id: None | UUID
    website_url: None | str
    documentation_url: None | str
    created_by_bot_id: None | UUID
    approved_by_user_id: None | UUID
    last_modified_by_bot_id: None | UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    metadata: None | ProductResponseMetadataType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.product_response_metadata_type_0 import ProductResponseMetadataType0  # noqa: PLC0415

        id = str(self.id)

        org_id = str(self.org_id)

        name = self.name

        slug = self.slug

        description: None | str
        description = self.description

        category: None | str
        category = self.category

        status = self.status

        launched_at: None | str
        if isinstance(self.launched_at, datetime.datetime):
            launched_at = self.launched_at.isoformat()
        else:
            launched_at = self.launched_at

        sunsetted_at: None | str
        if isinstance(self.sunsetted_at, datetime.datetime):
            sunsetted_at = self.sunsetted_at.isoformat()
        else:
            sunsetted_at = self.sunsetted_at

        owner_bot_id: None | str
        if isinstance(self.owner_bot_id, UUID):
            owner_bot_id = str(self.owner_bot_id)
        else:
            owner_bot_id = self.owner_bot_id

        parent_product_id: None | str
        if isinstance(self.parent_product_id, UUID):
            parent_product_id = str(self.parent_product_id)
        else:
            parent_product_id = self.parent_product_id

        logo_asset_id: None | str
        if isinstance(self.logo_asset_id, UUID):
            logo_asset_id = str(self.logo_asset_id)
        else:
            logo_asset_id = self.logo_asset_id

        hero_asset_id: None | str
        if isinstance(self.hero_asset_id, UUID):
            hero_asset_id = str(self.hero_asset_id)
        else:
            hero_asset_id = self.hero_asset_id

        demo_asset_id: None | str
        if isinstance(self.demo_asset_id, UUID):
            demo_asset_id = str(self.demo_asset_id)
        else:
            demo_asset_id = self.demo_asset_id

        website_url: None | str
        website_url = self.website_url

        documentation_url: None | str
        documentation_url = self.documentation_url

        created_by_bot_id: None | str
        if isinstance(self.created_by_bot_id, UUID):
            created_by_bot_id = str(self.created_by_bot_id)
        else:
            created_by_bot_id = self.created_by_bot_id

        approved_by_user_id: None | str
        if isinstance(self.approved_by_user_id, UUID):
            approved_by_user_id = str(self.approved_by_user_id)
        else:
            approved_by_user_id = self.approved_by_user_id

        last_modified_by_bot_id: None | str
        if isinstance(self.last_modified_by_bot_id, UUID):
            last_modified_by_bot_id = str(self.last_modified_by_bot_id)
        else:
            last_modified_by_bot_id = self.last_modified_by_bot_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        deleted_at: None | str
        if isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, ProductResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "name": name,
                "slug": slug,
                "description": description,
                "category": category,
                "status": status,
                "launched_at": launched_at,
                "sunsetted_at": sunsetted_at,
                "owner_bot_id": owner_bot_id,
                "parent_product_id": parent_product_id,
                "logo_asset_id": logo_asset_id,
                "hero_asset_id": hero_asset_id,
                "demo_asset_id": demo_asset_id,
                "website_url": website_url,
                "documentation_url": documentation_url,
                "created_by_bot_id": created_by_bot_id,
                "approved_by_user_id": approved_by_user_id,
                "last_modified_by_bot_id": last_modified_by_bot_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "deleted_at": deleted_at,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_response_metadata_type_0 import ProductResponseMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        name = d.pop("name")

        slug = d.pop("slug")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_category(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        category = _parse_category(d.pop("category"))

        status = d.pop("status")

        def _parse_launched_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                launched_at_type_0 = datetime.datetime.fromisoformat(data)

                return launched_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        launched_at = _parse_launched_at(d.pop("launched_at"))

        def _parse_sunsetted_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sunsetted_at_type_0 = datetime.datetime.fromisoformat(data)

                return sunsetted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        sunsetted_at = _parse_sunsetted_at(d.pop("sunsetted_at"))

        def _parse_owner_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_bot_id_type_0 = UUID(data)

                return owner_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        owner_bot_id = _parse_owner_bot_id(d.pop("owner_bot_id"))

        def _parse_parent_product_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_product_id_type_0 = UUID(data)

                return parent_product_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        parent_product_id = _parse_parent_product_id(d.pop("parent_product_id"))

        def _parse_logo_asset_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                logo_asset_id_type_0 = UUID(data)

                return logo_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        logo_asset_id = _parse_logo_asset_id(d.pop("logo_asset_id"))

        def _parse_hero_asset_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                hero_asset_id_type_0 = UUID(data)

                return hero_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        hero_asset_id = _parse_hero_asset_id(d.pop("hero_asset_id"))

        def _parse_demo_asset_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                demo_asset_id_type_0 = UUID(data)

                return demo_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        demo_asset_id = _parse_demo_asset_id(d.pop("demo_asset_id"))

        def _parse_website_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        website_url = _parse_website_url(d.pop("website_url"))

        def _parse_documentation_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        documentation_url = _parse_documentation_url(d.pop("documentation_url"))

        def _parse_created_by_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_bot_id_type_0 = UUID(data)

                return created_by_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        created_by_bot_id = _parse_created_by_bot_id(d.pop("created_by_bot_id"))

        def _parse_approved_by_user_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_by_user_id_type_0 = UUID(data)

                return approved_by_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        approved_by_user_id = _parse_approved_by_user_id(d.pop("approved_by_user_id"))

        def _parse_last_modified_by_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_modified_by_bot_id_type_0 = UUID(data)

                return last_modified_by_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        last_modified_by_bot_id = _parse_last_modified_by_bot_id(d.pop("last_modified_by_bot_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_deleted_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = datetime.datetime.fromisoformat(data)

                return deleted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at"))

        def _parse_metadata(data: object) -> None | ProductResponseMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = ProductResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProductResponseMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        product_response = cls(
            id=id,
            org_id=org_id,
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
            created_by_bot_id=created_by_bot_id,
            approved_by_user_id=approved_by_user_id,
            last_modified_by_bot_id=last_modified_by_bot_id,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            metadata=metadata,
        )

        product_response.additional_properties = d
        return product_response

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
