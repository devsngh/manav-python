from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PptxSlide")


@_attrs_define
class PptxSlide:
    """
    Attributes:
        slide_number (int):
        title (str):
        bullets (list[str]):
        speaker_notes (str):
        has_charts (bool):
        has_images (bool):
    """

    slide_number: int
    title: str
    bullets: list[str]
    speaker_notes: str
    has_charts: bool
    has_images: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slide_number = self.slide_number

        title = self.title

        bullets = self.bullets

        speaker_notes = self.speaker_notes

        has_charts = self.has_charts

        has_images = self.has_images

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slide_number": slide_number,
                "title": title,
                "bullets": bullets,
                "speaker_notes": speaker_notes,
                "has_charts": has_charts,
                "has_images": has_images,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slide_number = d.pop("slide_number")

        title = d.pop("title")

        bullets = cast(list[str], d.pop("bullets"))

        speaker_notes = d.pop("speaker_notes")

        has_charts = d.pop("has_charts")

        has_images = d.pop("has_images")

        pptx_slide = cls(
            slide_number=slide_number,
            title=title,
            bullets=bullets,
            speaker_notes=speaker_notes,
            has_charts=has_charts,
            has_images=has_images,
        )

        pptx_slide.additional_properties = d
        return pptx_slide

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
