from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AssetResponse")


@_attrs_define
class AssetResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        asset_type (str):
        asset_role (None | str):
        url (str):
        mime_type (None | str):
        file_size_bytes (int | None):
        dimensions_width (int | None):
        dimensions_height (int | None):
        duration_sec (None | str):
        page_count (int | None):
        source (str):
        parent_asset_id (None | UUID):
        version (int):
        status (str):
        visibility (str):
        created_by_bot_id (None | UUID):
        created_by_user_id (None | UUID):
        approved_by_bot_id (None | UUID):
        approved_by_user_id (None | UUID):
        approved_at (datetime.datetime | None):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        archived_at (datetime.datetime | None):
        deleted_at (datetime.datetime | None):
    """

    id: UUID
    org_id: UUID
    asset_type: str
    asset_role: None | str
    url: str
    mime_type: None | str
    file_size_bytes: int | None
    dimensions_width: int | None
    dimensions_height: int | None
    duration_sec: None | str
    page_count: int | None
    source: str
    parent_asset_id: None | UUID
    version: int
    status: str
    visibility: str
    created_by_bot_id: None | UUID
    created_by_user_id: None | UUID
    approved_by_bot_id: None | UUID
    approved_by_user_id: None | UUID
    approved_at: datetime.datetime | None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    archived_at: datetime.datetime | None
    deleted_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        org_id = str(self.org_id)

        asset_type = self.asset_type

        asset_role: None | str
        asset_role = self.asset_role

        url = self.url

        mime_type: None | str
        mime_type = self.mime_type

        file_size_bytes: int | None
        file_size_bytes = self.file_size_bytes

        dimensions_width: int | None
        dimensions_width = self.dimensions_width

        dimensions_height: int | None
        dimensions_height = self.dimensions_height

        duration_sec: None | str
        duration_sec = self.duration_sec

        page_count: int | None
        page_count = self.page_count

        source = self.source

        parent_asset_id: None | str
        if isinstance(self.parent_asset_id, UUID):
            parent_asset_id = str(self.parent_asset_id)
        else:
            parent_asset_id = self.parent_asset_id

        version = self.version

        status = self.status

        visibility = self.visibility

        created_by_bot_id: None | str
        if isinstance(self.created_by_bot_id, UUID):
            created_by_bot_id = str(self.created_by_bot_id)
        else:
            created_by_bot_id = self.created_by_bot_id

        created_by_user_id: None | str
        if isinstance(self.created_by_user_id, UUID):
            created_by_user_id = str(self.created_by_user_id)
        else:
            created_by_user_id = self.created_by_user_id

        approved_by_bot_id: None | str
        if isinstance(self.approved_by_bot_id, UUID):
            approved_by_bot_id = str(self.approved_by_bot_id)
        else:
            approved_by_bot_id = self.approved_by_bot_id

        approved_by_user_id: None | str
        if isinstance(self.approved_by_user_id, UUID):
            approved_by_user_id = str(self.approved_by_user_id)
        else:
            approved_by_user_id = self.approved_by_user_id

        approved_at: None | str
        if isinstance(self.approved_at, datetime.datetime):
            approved_at = self.approved_at.isoformat()
        else:
            approved_at = self.approved_at

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        archived_at: None | str
        if isinstance(self.archived_at, datetime.datetime):
            archived_at = self.archived_at.isoformat()
        else:
            archived_at = self.archived_at

        deleted_at: None | str
        if isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "asset_type": asset_type,
                "asset_role": asset_role,
                "url": url,
                "mime_type": mime_type,
                "file_size_bytes": file_size_bytes,
                "dimensions_width": dimensions_width,
                "dimensions_height": dimensions_height,
                "duration_sec": duration_sec,
                "page_count": page_count,
                "source": source,
                "parent_asset_id": parent_asset_id,
                "version": version,
                "status": status,
                "visibility": visibility,
                "created_by_bot_id": created_by_bot_id,
                "created_by_user_id": created_by_user_id,
                "approved_by_bot_id": approved_by_bot_id,
                "approved_by_user_id": approved_by_user_id,
                "approved_at": approved_at,
                "created_at": created_at,
                "updated_at": updated_at,
                "archived_at": archived_at,
                "deleted_at": deleted_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        asset_type = d.pop("asset_type")

        def _parse_asset_role(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        asset_role = _parse_asset_role(d.pop("asset_role"))

        url = d.pop("url")

        def _parse_mime_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        mime_type = _parse_mime_type(d.pop("mime_type"))

        def _parse_file_size_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        file_size_bytes = _parse_file_size_bytes(d.pop("file_size_bytes"))

        def _parse_dimensions_width(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        dimensions_width = _parse_dimensions_width(d.pop("dimensions_width"))

        def _parse_dimensions_height(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        dimensions_height = _parse_dimensions_height(d.pop("dimensions_height"))

        def _parse_duration_sec(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        duration_sec = _parse_duration_sec(d.pop("duration_sec"))

        def _parse_page_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        page_count = _parse_page_count(d.pop("page_count"))

        source = d.pop("source")

        def _parse_parent_asset_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_asset_id_type_0 = UUID(data)

                return parent_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        parent_asset_id = _parse_parent_asset_id(d.pop("parent_asset_id"))

        version = d.pop("version")

        status = d.pop("status")

        visibility = d.pop("visibility")

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

        def _parse_created_by_user_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_user_id_type_0 = UUID(data)

                return created_by_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        created_by_user_id = _parse_created_by_user_id(d.pop("created_by_user_id"))

        def _parse_approved_by_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_by_bot_id_type_0 = UUID(data)

                return approved_by_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        approved_by_bot_id = _parse_approved_by_bot_id(d.pop("approved_by_bot_id"))

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

        def _parse_approved_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_at_type_0 = datetime.datetime.fromisoformat(data)

                return approved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        approved_at = _parse_approved_at(d.pop("approved_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_archived_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                archived_at_type_0 = datetime.datetime.fromisoformat(data)

                return archived_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        archived_at = _parse_archived_at(d.pop("archived_at"))

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

        asset_response = cls(
            id=id,
            org_id=org_id,
            asset_type=asset_type,
            asset_role=asset_role,
            url=url,
            mime_type=mime_type,
            file_size_bytes=file_size_bytes,
            dimensions_width=dimensions_width,
            dimensions_height=dimensions_height,
            duration_sec=duration_sec,
            page_count=page_count,
            source=source,
            parent_asset_id=parent_asset_id,
            version=version,
            status=status,
            visibility=visibility,
            created_by_bot_id=created_by_bot_id,
            created_by_user_id=created_by_user_id,
            approved_by_bot_id=approved_by_bot_id,
            approved_by_user_id=approved_by_user_id,
            approved_at=approved_at,
            created_at=created_at,
            updated_at=updated_at,
            archived_at=archived_at,
            deleted_at=deleted_at,
        )

        asset_response.additional_properties = d
        return asset_response

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
