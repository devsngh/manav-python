from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_account_create_metadata_type_0 import SocialAccountCreateMetadataType0


T = TypeVar("T", bound="SocialAccountCreate")


@_attrs_define
class SocialAccountCreate:
    """
    Attributes:
        platform (str): linkedin / twitter / instagram / etc.
        handle (str):
        display_name (None | str | Unset):
        external_account_id (None | str | Unset):
        account_purpose (None | str | Unset): brand / agent_persona / human_persona / product
        oauth_credentials_ref (None | str | Unset):
        is_active (bool | Unset):  Default: True.
        is_verified (bool | Unset):  Default: False.
        follower_count (int | None | Unset):
        follower_count_updated_at (datetime.datetime | None | Unset):
        posting_cadence (None | str | Unset):
        profile_image_asset_id (None | Unset | UUID):
        cover_image_asset_id (None | Unset | UUID):
        metadata (None | SocialAccountCreateMetadataType0 | Unset):
    """

    platform: str
    handle: str
    display_name: None | str | Unset = UNSET
    external_account_id: None | str | Unset = UNSET
    account_purpose: None | str | Unset = UNSET
    oauth_credentials_ref: None | str | Unset = UNSET
    is_active: bool | Unset = True
    is_verified: bool | Unset = False
    follower_count: int | None | Unset = UNSET
    follower_count_updated_at: datetime.datetime | None | Unset = UNSET
    posting_cadence: None | str | Unset = UNSET
    profile_image_asset_id: None | Unset | UUID = UNSET
    cover_image_asset_id: None | Unset | UUID = UNSET
    metadata: None | SocialAccountCreateMetadataType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.social_account_create_metadata_type_0 import SocialAccountCreateMetadataType0  # noqa: PLC0415

        platform = self.platform

        handle = self.handle

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        external_account_id: None | str | Unset
        if isinstance(self.external_account_id, Unset):
            external_account_id = UNSET
        else:
            external_account_id = self.external_account_id

        account_purpose: None | str | Unset
        if isinstance(self.account_purpose, Unset):
            account_purpose = UNSET
        else:
            account_purpose = self.account_purpose

        oauth_credentials_ref: None | str | Unset
        if isinstance(self.oauth_credentials_ref, Unset):
            oauth_credentials_ref = UNSET
        else:
            oauth_credentials_ref = self.oauth_credentials_ref

        is_active = self.is_active

        is_verified = self.is_verified

        follower_count: int | None | Unset
        if isinstance(self.follower_count, Unset):
            follower_count = UNSET
        else:
            follower_count = self.follower_count

        follower_count_updated_at: None | str | Unset
        if isinstance(self.follower_count_updated_at, Unset):
            follower_count_updated_at = UNSET
        elif isinstance(self.follower_count_updated_at, datetime.datetime):
            follower_count_updated_at = self.follower_count_updated_at.isoformat()
        else:
            follower_count_updated_at = self.follower_count_updated_at

        posting_cadence: None | str | Unset
        if isinstance(self.posting_cadence, Unset):
            posting_cadence = UNSET
        else:
            posting_cadence = self.posting_cadence

        profile_image_asset_id: None | str | Unset
        if isinstance(self.profile_image_asset_id, Unset):
            profile_image_asset_id = UNSET
        elif isinstance(self.profile_image_asset_id, UUID):
            profile_image_asset_id = str(self.profile_image_asset_id)
        else:
            profile_image_asset_id = self.profile_image_asset_id

        cover_image_asset_id: None | str | Unset
        if isinstance(self.cover_image_asset_id, Unset):
            cover_image_asset_id = UNSET
        elif isinstance(self.cover_image_asset_id, UUID):
            cover_image_asset_id = str(self.cover_image_asset_id)
        else:
            cover_image_asset_id = self.cover_image_asset_id

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, SocialAccountCreateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform": platform,
                "handle": handle,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if external_account_id is not UNSET:
            field_dict["external_account_id"] = external_account_id
        if account_purpose is not UNSET:
            field_dict["account_purpose"] = account_purpose
        if oauth_credentials_ref is not UNSET:
            field_dict["oauth_credentials_ref"] = oauth_credentials_ref
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_verified is not UNSET:
            field_dict["is_verified"] = is_verified
        if follower_count is not UNSET:
            field_dict["follower_count"] = follower_count
        if follower_count_updated_at is not UNSET:
            field_dict["follower_count_updated_at"] = follower_count_updated_at
        if posting_cadence is not UNSET:
            field_dict["posting_cadence"] = posting_cadence
        if profile_image_asset_id is not UNSET:
            field_dict["profile_image_asset_id"] = profile_image_asset_id
        if cover_image_asset_id is not UNSET:
            field_dict["cover_image_asset_id"] = cover_image_asset_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_account_create_metadata_type_0 import SocialAccountCreateMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        platform = d.pop("platform")

        handle = d.pop("handle")

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        def _parse_external_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_account_id = _parse_external_account_id(d.pop("external_account_id", UNSET))

        def _parse_account_purpose(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_purpose = _parse_account_purpose(d.pop("account_purpose", UNSET))

        def _parse_oauth_credentials_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        oauth_credentials_ref = _parse_oauth_credentials_ref(d.pop("oauth_credentials_ref", UNSET))

        is_active = d.pop("is_active", UNSET)

        is_verified = d.pop("is_verified", UNSET)

        def _parse_follower_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        follower_count = _parse_follower_count(d.pop("follower_count", UNSET))

        def _parse_follower_count_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                follower_count_updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return follower_count_updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        follower_count_updated_at = _parse_follower_count_updated_at(d.pop("follower_count_updated_at", UNSET))

        def _parse_posting_cadence(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        posting_cadence = _parse_posting_cadence(d.pop("posting_cadence", UNSET))

        def _parse_profile_image_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                profile_image_asset_id_type_0 = UUID(data)

                return profile_image_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        profile_image_asset_id = _parse_profile_image_asset_id(d.pop("profile_image_asset_id", UNSET))

        def _parse_cover_image_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cover_image_asset_id_type_0 = UUID(data)

                return cover_image_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        cover_image_asset_id = _parse_cover_image_asset_id(d.pop("cover_image_asset_id", UNSET))

        def _parse_metadata(data: object) -> None | SocialAccountCreateMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = SocialAccountCreateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SocialAccountCreateMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        social_account_create = cls(
            platform=platform,
            handle=handle,
            display_name=display_name,
            external_account_id=external_account_id,
            account_purpose=account_purpose,
            oauth_credentials_ref=oauth_credentials_ref,
            is_active=is_active,
            is_verified=is_verified,
            follower_count=follower_count,
            follower_count_updated_at=follower_count_updated_at,
            posting_cadence=posting_cadence,
            profile_image_asset_id=profile_image_asset_id,
            cover_image_asset_id=cover_image_asset_id,
            metadata=metadata,
        )

        social_account_create.additional_properties = d
        return social_account_create

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
