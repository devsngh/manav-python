from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_platform_update_features_type_0 import SocialPlatformUpdateFeaturesType0
    from ..models.social_platform_update_metadata_type_0 import SocialPlatformUpdateMetadataType0


T = TypeVar("T", bound="SocialPlatformUpdate")


@_attrs_define
class SocialPlatformUpdate:
    """
    Attributes:
        name (None | str | Unset):
        category (None | str | Unset):
        base_url (None | str | Unset):
        icon_url (None | str | Unset):
        description (None | str | Unset):
        supports_dm (bool | None | Unset):
        supports_comments (bool | None | Unset):
        supports_connection (bool | None | Unset):
        supports_posts (bool | None | Unset):
        character_limit_post (int | None | Unset):
        character_limit_dm (int | None | Unset):
        api_available (bool | None | Unset):
        features (None | SocialPlatformUpdateFeaturesType0 | Unset):
        is_active (bool | None | Unset):
        sort_order (int | None | Unset):
        metadata (None | SocialPlatformUpdateMetadataType0 | Unset):
    """

    name: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    base_url: None | str | Unset = UNSET
    icon_url: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    supports_dm: bool | None | Unset = UNSET
    supports_comments: bool | None | Unset = UNSET
    supports_connection: bool | None | Unset = UNSET
    supports_posts: bool | None | Unset = UNSET
    character_limit_post: int | None | Unset = UNSET
    character_limit_dm: int | None | Unset = UNSET
    api_available: bool | None | Unset = UNSET
    features: None | SocialPlatformUpdateFeaturesType0 | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    sort_order: int | None | Unset = UNSET
    metadata: None | SocialPlatformUpdateMetadataType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.social_platform_update_features_type_0 import SocialPlatformUpdateFeaturesType0  # noqa: PLC0415
        from ..models.social_platform_update_metadata_type_0 import SocialPlatformUpdateMetadataType0  # noqa: PLC0415

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        base_url: None | str | Unset
        if isinstance(self.base_url, Unset):
            base_url = UNSET
        else:
            base_url = self.base_url

        icon_url: None | str | Unset
        if isinstance(self.icon_url, Unset):
            icon_url = UNSET
        else:
            icon_url = self.icon_url

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        supports_dm: bool | None | Unset
        if isinstance(self.supports_dm, Unset):
            supports_dm = UNSET
        else:
            supports_dm = self.supports_dm

        supports_comments: bool | None | Unset
        if isinstance(self.supports_comments, Unset):
            supports_comments = UNSET
        else:
            supports_comments = self.supports_comments

        supports_connection: bool | None | Unset
        if isinstance(self.supports_connection, Unset):
            supports_connection = UNSET
        else:
            supports_connection = self.supports_connection

        supports_posts: bool | None | Unset
        if isinstance(self.supports_posts, Unset):
            supports_posts = UNSET
        else:
            supports_posts = self.supports_posts

        character_limit_post: int | None | Unset
        if isinstance(self.character_limit_post, Unset):
            character_limit_post = UNSET
        else:
            character_limit_post = self.character_limit_post

        character_limit_dm: int | None | Unset
        if isinstance(self.character_limit_dm, Unset):
            character_limit_dm = UNSET
        else:
            character_limit_dm = self.character_limit_dm

        api_available: bool | None | Unset
        if isinstance(self.api_available, Unset):
            api_available = UNSET
        else:
            api_available = self.api_available

        features: dict[str, Any] | None | Unset
        if isinstance(self.features, Unset):
            features = UNSET
        elif isinstance(self.features, SocialPlatformUpdateFeaturesType0):
            features = self.features.to_dict()
        else:
            features = self.features

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

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, SocialPlatformUpdateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if category is not UNSET:
            field_dict["category"] = category
        if base_url is not UNSET:
            field_dict["base_url"] = base_url
        if icon_url is not UNSET:
            field_dict["icon_url"] = icon_url
        if description is not UNSET:
            field_dict["description"] = description
        if supports_dm is not UNSET:
            field_dict["supports_dm"] = supports_dm
        if supports_comments is not UNSET:
            field_dict["supports_comments"] = supports_comments
        if supports_connection is not UNSET:
            field_dict["supports_connection"] = supports_connection
        if supports_posts is not UNSET:
            field_dict["supports_posts"] = supports_posts
        if character_limit_post is not UNSET:
            field_dict["character_limit_post"] = character_limit_post
        if character_limit_dm is not UNSET:
            field_dict["character_limit_dm"] = character_limit_dm
        if api_available is not UNSET:
            field_dict["api_available"] = api_available
        if features is not UNSET:
            field_dict["features"] = features
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_platform_update_features_type_0 import SocialPlatformUpdateFeaturesType0  # noqa: PLC0415
        from ..models.social_platform_update_metadata_type_0 import SocialPlatformUpdateMetadataType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_base_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        base_url = _parse_base_url(d.pop("base_url", UNSET))

        def _parse_icon_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon_url = _parse_icon_url(d.pop("icon_url", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_supports_dm(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        supports_dm = _parse_supports_dm(d.pop("supports_dm", UNSET))

        def _parse_supports_comments(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        supports_comments = _parse_supports_comments(d.pop("supports_comments", UNSET))

        def _parse_supports_connection(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        supports_connection = _parse_supports_connection(d.pop("supports_connection", UNSET))

        def _parse_supports_posts(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        supports_posts = _parse_supports_posts(d.pop("supports_posts", UNSET))

        def _parse_character_limit_post(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        character_limit_post = _parse_character_limit_post(d.pop("character_limit_post", UNSET))

        def _parse_character_limit_dm(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        character_limit_dm = _parse_character_limit_dm(d.pop("character_limit_dm", UNSET))

        def _parse_api_available(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        api_available = _parse_api_available(d.pop("api_available", UNSET))

        def _parse_features(data: object) -> None | SocialPlatformUpdateFeaturesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                features_type_0 = SocialPlatformUpdateFeaturesType0.from_dict(data)

                return features_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SocialPlatformUpdateFeaturesType0 | Unset, data)

        features = _parse_features(d.pop("features", UNSET))

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

        def _parse_metadata(data: object) -> None | SocialPlatformUpdateMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = SocialPlatformUpdateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SocialPlatformUpdateMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        social_platform_update = cls(
            name=name,
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
            metadata=metadata,
        )

        social_platform_update.additional_properties = d
        return social_platform_update

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
