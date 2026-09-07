from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BlogPostListItem")


@_attrs_define
class BlogPostListItem:
    """Lightweight item for listing pages (no slide bodies).

    Attributes:
        id (UUID):
        type_ (str):
        title (str):
        slug (str):
        summary (str):
        cover_image_url (str):
        author_name (str):
        theme (str):
        status (str):
        updated_at (datetime.datetime):
        published_at (datetime.datetime | None | Unset):
    """

    id: UUID
    type_: str
    title: str
    slug: str
    summary: str
    cover_image_url: str
    author_name: str
    theme: str
    status: str
    updated_at: datetime.datetime
    published_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        type_ = self.type_

        title = self.title

        slug = self.slug

        summary = self.summary

        cover_image_url = self.cover_image_url

        author_name = self.author_name

        theme = self.theme

        status = self.status

        updated_at = self.updated_at.isoformat()

        published_at: None | str | Unset
        if isinstance(self.published_at, Unset):
            published_at = UNSET
        elif isinstance(self.published_at, datetime.datetime):
            published_at = self.published_at.isoformat()
        else:
            published_at = self.published_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "title": title,
                "slug": slug,
                "summary": summary,
                "cover_image_url": cover_image_url,
                "author_name": author_name,
                "theme": theme,
                "status": status,
                "updated_at": updated_at,
            }
        )
        if published_at is not UNSET:
            field_dict["published_at"] = published_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = d.pop("type")

        title = d.pop("title")

        slug = d.pop("slug")

        summary = d.pop("summary")

        cover_image_url = d.pop("cover_image_url")

        author_name = d.pop("author_name")

        theme = d.pop("theme")

        status = d.pop("status")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_published_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_at_type_0 = datetime.datetime.fromisoformat(data)

                return published_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        published_at = _parse_published_at(d.pop("published_at", UNSET))

        blog_post_list_item = cls(
            id=id,
            type_=type_,
            title=title,
            slug=slug,
            summary=summary,
            cover_image_url=cover_image_url,
            author_name=author_name,
            theme=theme,
            status=status,
            updated_at=updated_at,
            published_at=published_at,
        )

        blog_post_list_item.additional_properties = d
        return blog_post_list_item

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
