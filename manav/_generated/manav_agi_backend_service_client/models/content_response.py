from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.content_response_content import ContentResponseContent


T = TypeVar("T", bound="ContentResponse")


@_attrs_define
class ContentResponse:
    """
    Attributes:
        id (UUID):
        page (str):
        section_key (str):
        content (ContentResponseContent):
        sort_order (int):
        is_active (bool):
        updated_at (datetime.datetime):
    """

    id: UUID
    page: str
    section_key: str
    content: ContentResponseContent
    sort_order: int
    is_active: bool
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        page = self.page

        section_key = self.section_key

        content = self.content.to_dict()

        sort_order = self.sort_order

        is_active = self.is_active

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "page": page,
                "section_key": section_key,
                "content": content,
                "sort_order": sort_order,
                "is_active": is_active,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_response_content import ContentResponseContent  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        page = d.pop("page")

        section_key = d.pop("section_key")

        content = ContentResponseContent.from_dict(d.pop("content"))

        sort_order = d.pop("sort_order")

        is_active = d.pop("is_active")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        content_response = cls(
            id=id,
            page=page,
            section_key=section_key,
            content=content,
            sort_order=sort_order,
            is_active=is_active,
            updated_at=updated_at,
        )

        content_response.additional_properties = d
        return content_response

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
