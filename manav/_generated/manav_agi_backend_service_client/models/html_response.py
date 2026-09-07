from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.html_link import HtmlLink


T = TypeVar("T", bound="HtmlResponse")


@_attrs_define
class HtmlResponse:
    """
    Attributes:
        text (str):
        title (str):
        links (list[HtmlLink]):
        char_count (int):
    """

    text: str
    title: str
    links: list[HtmlLink]
    char_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        title = self.title

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        char_count = self.char_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "title": title,
                "links": links,
                "char_count": char_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.html_link import HtmlLink  # noqa: PLC0415

        d = dict(src_dict)
        text = d.pop("text")

        title = d.pop("title")

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = HtmlLink.from_dict(links_item_data)

            links.append(links_item)

        char_count = d.pop("char_count")

        html_response = cls(
            text=text,
            title=title,
            links=links,
            char_count=char_count,
        )

        html_response.additional_properties = d
        return html_response

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
