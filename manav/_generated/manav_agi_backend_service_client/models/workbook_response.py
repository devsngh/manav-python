from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workbook_response_metadata_type_0 import WorkbookResponseMetadataType0


T = TypeVar("T", bound="WorkbookResponse")


@_attrs_define
class WorkbookResponse:
    """
    Attributes:
        id (UUID):
        bot_id (UUID):
        org_id (UUID):
        workbook_type (str):
        title (str):
        content (None | str | Unset):
        metadata (None | Unset | WorkbookResponseMetadataType0):
        version (int | Unset):  Default: 1.
        updated_at (datetime.datetime | None | Unset):
        created_at (datetime.datetime | None | Unset):
    """

    id: UUID
    bot_id: UUID
    org_id: UUID
    workbook_type: str
    title: str
    content: None | str | Unset = UNSET
    metadata: None | Unset | WorkbookResponseMetadataType0 = UNSET
    version: int | Unset = 1
    updated_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.workbook_response_metadata_type_0 import WorkbookResponseMetadataType0  # noqa: PLC0415

        id = str(self.id)

        bot_id = str(self.bot_id)

        org_id = str(self.org_id)

        workbook_type = self.workbook_type

        title = self.title

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, WorkbookResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        version = self.version

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "bot_id": bot_id,
                "org_id": org_id,
                "workbook_type": workbook_type,
                "title": title,
            }
        )
        if content is not UNSET:
            field_dict["content"] = content
        if metadata is not UNSET:
            field_dict["metadata_"] = metadata
        if version is not UNSET:
            field_dict["version"] = version
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workbook_response_metadata_type_0 import WorkbookResponseMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        bot_id = UUID(d.pop("bot_id"))

        org_id = UUID(d.pop("org_id"))

        workbook_type = d.pop("workbook_type")

        title = d.pop("title")

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        def _parse_metadata(data: object) -> None | Unset | WorkbookResponseMetadataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = WorkbookResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WorkbookResponseMetadataType0, data)

        metadata = _parse_metadata(d.pop("metadata_", UNSET))

        version = d.pop("version", UNSET)

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        workbook_response = cls(
            id=id,
            bot_id=bot_id,
            org_id=org_id,
            workbook_type=workbook_type,
            title=title,
            content=content,
            metadata=metadata,
            version=version,
            updated_at=updated_at,
            created_at=created_at,
        )

        workbook_response.additional_properties = d
        return workbook_response

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
