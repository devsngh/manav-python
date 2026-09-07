from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.py_mu_pdf_response_pages_item import PyMuPDFResponsePagesItem


T = TypeVar("T", bound="PyMuPDFResponse")


@_attrs_define
class PyMuPDFResponse:
    """
    Attributes:
        text (str):
        page_count (int):
        char_count (int):
        has_images (bool):
        image_count (int):
        pages (list[PyMuPDFResponsePagesItem]):
    """

    text: str
    page_count: int
    char_count: int
    has_images: bool
    image_count: int
    pages: list[PyMuPDFResponsePagesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        page_count = self.page_count

        char_count = self.char_count

        has_images = self.has_images

        image_count = self.image_count

        pages = []
        for pages_item_data in self.pages:
            pages_item = pages_item_data.to_dict()
            pages.append(pages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "page_count": page_count,
                "char_count": char_count,
                "has_images": has_images,
                "image_count": image_count,
                "pages": pages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.py_mu_pdf_response_pages_item import PyMuPDFResponsePagesItem  # noqa: PLC0415

        d = dict(src_dict)
        text = d.pop("text")

        page_count = d.pop("page_count")

        char_count = d.pop("char_count")

        has_images = d.pop("has_images")

        image_count = d.pop("image_count")

        pages = []
        _pages = d.pop("pages")
        for pages_item_data in _pages:
            pages_item = PyMuPDFResponsePagesItem.from_dict(pages_item_data)

            pages.append(pages_item)

        py_mu_pdf_response = cls(
            text=text,
            page_count=page_count,
            char_count=char_count,
            has_images=has_images,
            image_count=image_count,
            pages=pages,
        )

        py_mu_pdf_response.additional_properties = d
        return py_mu_pdf_response

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
