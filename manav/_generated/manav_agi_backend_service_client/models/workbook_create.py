from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workbook_create_metadata_type_0 import WorkbookCreateMetadataType0


T = TypeVar("T", bound="WorkbookCreate")


@_attrs_define
class WorkbookCreate:
    """
    Attributes:
        bot_id (UUID):
        title (str):
        workbook_type (str | Unset):  Default: 'personal'.
        content (None | str | Unset):
        metadata (None | Unset | WorkbookCreateMetadataType0):
    """

    bot_id: UUID
    title: str
    workbook_type: str | Unset = "personal"
    content: None | str | Unset = UNSET
    metadata: None | Unset | WorkbookCreateMetadataType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.workbook_create_metadata_type_0 import WorkbookCreateMetadataType0  # noqa: PLC0415

        bot_id = str(self.bot_id)

        title = self.title

        workbook_type = self.workbook_type

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, WorkbookCreateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bot_id": bot_id,
                "title": title,
            }
        )
        if workbook_type is not UNSET:
            field_dict["workbook_type"] = workbook_type
        if content is not UNSET:
            field_dict["content"] = content
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workbook_create_metadata_type_0 import WorkbookCreateMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        bot_id = UUID(d.pop("bot_id"))

        title = d.pop("title")

        workbook_type = d.pop("workbook_type", UNSET)

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        def _parse_metadata(data: object) -> None | Unset | WorkbookCreateMetadataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = WorkbookCreateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WorkbookCreateMetadataType0, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        workbook_create = cls(
            bot_id=bot_id,
            title=title,
            workbook_type=workbook_type,
            content=content,
            metadata=metadata,
        )

        workbook_create.additional_properties = d
        return workbook_create

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
