from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pptx_slide import PptxSlide


T = TypeVar("T", bound="PptxResponse")


@_attrs_define
class PptxResponse:
    """
    Attributes:
        slides (list[PptxSlide]):
        slide_count (int):
    """

    slides: list[PptxSlide]
    slide_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slides = []
        for slides_item_data in self.slides:
            slides_item = slides_item_data.to_dict()
            slides.append(slides_item)

        slide_count = self.slide_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slides": slides,
                "slide_count": slide_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pptx_slide import PptxSlide  # noqa: PLC0415

        d = dict(src_dict)
        slides = []
        _slides = d.pop("slides")
        for slides_item_data in _slides:
            slides_item = PptxSlide.from_dict(slides_item_data)

            slides.append(slides_item)

        slide_count = d.pop("slide_count")

        pptx_response = cls(
            slides=slides,
            slide_count=slide_count,
        )

        pptx_response.additional_properties = d
        return pptx_response

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
