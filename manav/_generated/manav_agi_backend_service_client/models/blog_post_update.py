from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slide import Slide


T = TypeVar("T", bound="BlogPostUpdate")


@_attrs_define
class BlogPostUpdate:
    """
    Attributes:
        type_ (None | str | Unset):
        title (None | str | Unset):
        summary (None | str | Unset):
        cover_image_url (None | str | Unset):
        author_name (None | str | Unset):
        theme (None | str | Unset):
        status (None | str | Unset):
        slides (list[Slide] | None | Unset):
    """

    type_: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    summary: None | str | Unset = UNSET
    cover_image_url: None | str | Unset = UNSET
    author_name: None | str | Unset = UNSET
    theme: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    slides: list[Slide] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        cover_image_url: None | str | Unset
        if isinstance(self.cover_image_url, Unset):
            cover_image_url = UNSET
        else:
            cover_image_url = self.cover_image_url

        author_name: None | str | Unset
        if isinstance(self.author_name, Unset):
            author_name = UNSET
        else:
            author_name = self.author_name

        theme: None | str | Unset
        if isinstance(self.theme, Unset):
            theme = UNSET
        else:
            theme = self.theme

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        slides: list[dict[str, Any]] | None | Unset
        if isinstance(self.slides, Unset):
            slides = UNSET
        elif isinstance(self.slides, list):
            slides = []
            for slides_type_0_item_data in self.slides:
                slides_type_0_item = slides_type_0_item_data.to_dict()
                slides.append(slides_type_0_item)

        else:
            slides = self.slides

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if title is not UNSET:
            field_dict["title"] = title
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

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))

        def _parse_cover_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cover_image_url = _parse_cover_image_url(d.pop("cover_image_url", UNSET))

        def _parse_author_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author_name = _parse_author_name(d.pop("author_name", UNSET))

        def _parse_theme(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        theme = _parse_theme(d.pop("theme", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_slides(data: object) -> list[Slide] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                slides_type_0 = []
                _slides_type_0 = data
                for slides_type_0_item_data in _slides_type_0:
                    slides_type_0_item = Slide.from_dict(slides_type_0_item_data)

                    slides_type_0.append(slides_type_0_item)

                return slides_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Slide] | None | Unset, data)

        slides = _parse_slides(d.pop("slides", UNSET))

        blog_post_update = cls(
            type_=type_,
            title=title,
            summary=summary,
            cover_image_url=cover_image_url,
            author_name=author_name,
            theme=theme,
            status=status,
            slides=slides,
        )

        blog_post_update.additional_properties = d
        return blog_post_update

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
