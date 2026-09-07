from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_platform_response_features_type_0 import SocialPlatformResponseFeaturesType0
    from ..models.social_platform_response_metadata_type_0 import SocialPlatformResponseMetadataType0


T = TypeVar("T", bound="SocialPlatformResponse")


@_attrs_define
class SocialPlatformResponse:
    """
    Attributes:
        id (UUID):
        name (str):
        slug (str):
        category (str):
        base_url (None | str):
        icon_url (None | str):
        description (None | str):
        supports_dm (bool):
        supports_comments (bool):
        supports_connection (bool):
        supports_posts (bool):
        character_limit_post (int | None):
        character_limit_dm (int | None):
        api_available (bool):
        features (None | SocialPlatformResponseFeaturesType0):
        is_active (bool):
        sort_order (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        metadata (None | SocialPlatformResponseMetadataType0 | Unset):
    """

    id: UUID
    name: str
    slug: str
    category: str
    base_url: None | str
    icon_url: None | str
    description: None | str
    supports_dm: bool
    supports_comments: bool
    supports_connection: bool
    supports_posts: bool
    character_limit_post: int | None
    character_limit_dm: int | None
    api_available: bool
    features: None | SocialPlatformResponseFeaturesType0
    is_active: bool
    sort_order: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata: None | SocialPlatformResponseMetadataType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.social_platform_response_features_type_0 import (
            SocialPlatformResponseFeaturesType0,  # noqa: PLC0415
        )
        from ..models.social_platform_response_metadata_type_0 import (
            SocialPlatformResponseMetadataType0,  # noqa: PLC0415
        )

        id = str(self.id)

        name = self.name

        slug = self.slug

        category = self.category

        base_url: None | str
        base_url = self.base_url

        icon_url: None | str
        icon_url = self.icon_url

        description: None | str
        description = self.description

        supports_dm = self.supports_dm

        supports_comments = self.supports_comments

        supports_connection = self.supports_connection

        supports_posts = self.supports_posts

        character_limit_post: int | None
        character_limit_post = self.character_limit_post

        character_limit_dm: int | None
        character_limit_dm = self.character_limit_dm

        api_available = self.api_available

        features: dict[str, Any] | None
        if isinstance(self.features, SocialPlatformResponseFeaturesType0):
            features = self.features.to_dict()
        else:
            features = self.features

        is_active = self.is_active

        sort_order = self.sort_order

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, SocialPlatformResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "category": category,
                "base_url": base_url,
                "icon_url": icon_url,
                "description": description,
                "supports_dm": supports_dm,
                "supports_comments": supports_comments,
                "supports_connection": supports_connection,
                "supports_posts": supports_posts,
                "character_limit_post": character_limit_post,
                "character_limit_dm": character_limit_dm,
                "api_available": api_available,
                "features": features,
                "is_active": is_active,
                "sort_order": sort_order,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_platform_response_features_type_0 import (
            SocialPlatformResponseFeaturesType0,  # noqa: PLC0415
        )
        from ..models.social_platform_response_metadata_type_0 import (
            SocialPlatformResponseMetadataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        slug = d.pop("slug")

        category = d.pop("category")

        def _parse_base_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        base_url = _parse_base_url(d.pop("base_url"))

        def _parse_icon_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        icon_url = _parse_icon_url(d.pop("icon_url"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        supports_dm = d.pop("supports_dm")

        supports_comments = d.pop("supports_comments")

        supports_connection = d.pop("supports_connection")

        supports_posts = d.pop("supports_posts")

        def _parse_character_limit_post(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        character_limit_post = _parse_character_limit_post(d.pop("character_limit_post"))

        def _parse_character_limit_dm(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        character_limit_dm = _parse_character_limit_dm(d.pop("character_limit_dm"))

        api_available = d.pop("api_available")

        def _parse_features(data: object) -> None | SocialPlatformResponseFeaturesType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                features_type_0 = SocialPlatformResponseFeaturesType0.from_dict(data)

                return features_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SocialPlatformResponseFeaturesType0, data)

        features = _parse_features(d.pop("features"))

        is_active = d.pop("is_active")

        sort_order = d.pop("sort_order")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_metadata(data: object) -> None | SocialPlatformResponseMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = SocialPlatformResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SocialPlatformResponseMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        social_platform_response = cls(
            id=id,
            name=name,
            slug=slug,
            category=category,
            base_url=base_url,
            icon_url=icon_url,
            description=description,
            supports_dm=supports_dm,
            supports_comments=supports_comments,
            supports_connection=supports_connection,
            supports_posts=supports_posts,
            character_limit_post=character_limit_post,
            character_limit_dm=character_limit_dm,
            api_available=api_available,
            features=features,
            is_active=is_active,
            sort_order=sort_order,
            created_at=created_at,
            updated_at=updated_at,
            metadata=metadata,
        )

        social_platform_response.additional_properties = d
        return social_platform_response

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
