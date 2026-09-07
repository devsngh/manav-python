from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slide import Slide


T = TypeVar("T", bound="BlogPostCreate")


@_attrs_define
class BlogPostCreate:
    """
    Attributes:
        title (str):
        type_ (str | Unset):  Default: 'blog'.
        summary (str | Unset):  Default: ''.
        cover_image_url (str | Unset):  Default: ''.
        author_name (str | Unset):  Default: ''.
        theme (str | Unset):  Default: 'black'.
        status (str | Unset):  Default: 'draft'.
        slides (list[Slide] | Unset):
    """

    title: str
    type_: str | Unset = "blog"
    summary: str | Unset = ""
    cover_image_url: str | Unset = ""
    author_name: str | Unset = ""
    theme: str | Unset = "black"
    status: str | Unset = "draft"
    slides: list[Slide] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        type_ = self.type_

        summary = self.summary

        cover_image_url = self.cover_image_url

        author_name = self.author_name

        theme = self.theme

        status = self.status

        slides: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.slides, Unset):
            slides = []
            for slides_item_data in self.slides:
                slides_item = slides_item_data.to_dict()
                slides.append(slides_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if summary is not UNSET:
            field_dict["summary"] = summary
        if cover_image_url is not UNSET:
            field_dict["cover_image_url"] = cover_image_url
        if author_name is not UNSET:
            field_dict["author_name"] = author_name
        if theme is not UNSET:
            field_dict["theme"] = theme
        if status is not UNSET:
            field_dict["status"] = status
        if slides is not UNSET:
            field_dict["slides"] = slides

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slide import Slide  # noqa: PLC0415

        d = dict(src_dict)
        title = d.pop("title")

        type_ = d.pop("type", UNSET)

        summary = d.pop("summary", UNSET)

        cover_image_url = d.pop("cover_image_url", UNSET)

        author_name = d.pop("author_name", UNSET)

        theme = d.pop("theme", UNSET)

        status = d.pop("status", UNSET)

        _slides = d.pop("slides", UNSET)
        slides: list[Slide] | Unset = UNSET
        if _slides is not UNSET:
            slides = []
            for slides_item_data in _slides:
                slides_item = Slide.from_dict(slides_item_data)

                slides.append(slides_item)

        blog_post_create = cls(
            title=title,
            type_=type_,
            summary=summary,
            cover_image_url=cover_image_url,
            author_name=author_name,
            theme=theme,
            status=status,
            slides=slides,
        )

        blog_post_create.additional_properties = d
        return blog_post_create

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
