from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_account_response_metadata_type_0 import SocialAccountResponseMetadataType0


T = TypeVar("T", bound="SocialAccountResponse")


@_attrs_define
class SocialAccountResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        platform (str):
        handle (str):
        display_name (None | str):
        external_account_id (None | str):
        account_purpose (None | str):
        is_active (bool):
        is_verified (bool):
        follower_count (int | None):
        follower_count_updated_at (datetime.datetime | None):
        posting_cadence (None | str):
        profile_image_asset_id (None | UUID):
        cover_image_asset_id (None | UUID):
        created_by_bot_id (None | UUID):
        approved_by_user_id (None | UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        deleted_at (datetime.datetime | None):
        metadata (None | SocialAccountResponseMetadataType0 | Unset):
    """

    id: UUID
    org_id: UUID
    platform: str
    handle: str
    display_name: None | str
    external_account_id: None | str
    account_purpose: None | str
    is_active: bool
    is_verified: bool
    follower_count: int | None
    follower_count_updated_at: datetime.datetime | None
    posting_cadence: None | str
    profile_image_asset_id: None | UUID
    cover_image_asset_id: None | UUID
    created_by_bot_id: None | UUID
    approved_by_user_id: None | UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    metadata: None | SocialAccountResponseMetadataType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.social_account_response_metadata_type_0 import SocialAccountResponseMetadataType0  # noqa: PLC0415

        id = str(self.id)

        org_id = str(self.org_id)

        platform = self.platform

        handle = self.handle

        display_name: None | str
        display_name = self.display_name

        external_account_id: None | str
        external_account_id = self.external_account_id

        account_purpose: None | str
        account_purpose = self.account_purpose

        is_active = self.is_active

        is_verified = self.is_verified

        follower_count: int | None
        follower_count = self.follower_count

        follower_count_updated_at: None | str
        if isinstance(self.follower_count_updated_at, datetime.datetime):
            follower_count_updated_at = self.follower_count_updated_at.isoformat()
        else:
            follower_count_updated_at = self.follower_count_updated_at

        posting_cadence: None | str
        posting_cadence = self.posting_cadence

        profile_image_asset_id: None | str
        if isinstance(self.profile_image_asset_id, UUID):
            profile_image_asset_id = str(self.profile_image_asset_id)
        else:
            profile_image_asset_id = self.profile_image_asset_id

        cover_image_asset_id: None | str
        if isinstance(self.cover_image_asset_id, UUID):
            cover_image_asset_id = str(self.cover_image_asset_id)
        else:
            cover_image_asset_id = self.cover_image_asset_id

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
        elif isinstance(self.metadata, SocialAccountResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "platform": platform,
                "handle": handle,
                "display_name": display_name,
                "external_account_id": external_account_id,
                "account_purpose": account_purpose,
                "is_active": is_active,
                "is_verified": is_verified,
                "follower_count": follower_count,
                "follower_count_updated_at": follower_count_updated_at,
                "posting_cadence": posting_cadence,
                "profile_image_asset_id": profile_image_asset_id,
                "cover_image_asset_id": cover_image_asset_id,
                "created_by_bot_id": created_by_bot_id,
                "approved_by_user_id": approved_by_user_id,
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
        from ..models.social_account_response_metadata_type_0 import SocialAccountResponseMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        platform = d.pop("platform")

        handle = d.pop("handle")

        def _parse_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        display_name = _parse_display_name(d.pop("display_name"))

        def _parse_external_account_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_account_id = _parse_external_account_id(d.pop("external_account_id"))

        def _parse_account_purpose(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        account_purpose = _parse_account_purpose(d.pop("account_purpose"))

        is_active = d.pop("is_active")

        is_verified = d.pop("is_verified")

        def _parse_follower_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        follower_count = _parse_follower_count(d.pop("follower_count"))

        def _parse_follower_count_updated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                follower_count_updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return follower_count_updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        follower_count_updated_at = _parse_follower_count_updated_at(d.pop("follower_count_updated_at"))

        def _parse_posting_cadence(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        posting_cadence = _parse_posting_cadence(d.pop("posting_cadence"))

        def _parse_profile_image_asset_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                profile_image_asset_id_type_0 = UUID(data)

                return profile_image_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        profile_image_asset_id = _parse_profile_image_asset_id(d.pop("profile_image_asset_id"))

        def _parse_cover_image_asset_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cover_image_asset_id_type_0 = UUID(data)

                return cover_image_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        cover_image_asset_id = _parse_cover_image_asset_id(d.pop("cover_image_asset_id"))

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

        def _parse_metadata(data: object) -> None | SocialAccountResponseMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = SocialAccountResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SocialAccountResponseMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        social_account_response = cls(
            id=id,
            org_id=org_id,
            platform=platform,
            handle=handle,
            display_name=display_name,
            external_account_id=external_account_id,
            account_purpose=account_purpose,
            is_active=is_active,
            is_verified=is_verified,
            follower_count=follower_count,
            follower_count_updated_at=follower_count_updated_at,
            posting_cadence=posting_cadence,
            profile_image_asset_id=profile_image_asset_id,
            cover_image_asset_id=cover_image_asset_id,
            created_by_bot_id=created_by_bot_id,
            approved_by_user_id=approved_by_user_id,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            metadata=metadata,
        )

        social_account_response.additional_properties = d
        return social_account_response

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
