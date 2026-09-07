from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_create_content import ContentCreateContent


T = TypeVar("T", bound="ContentCreate")


@_attrs_define
class ContentCreate:
    """
    Attributes:
        page (str):
        section_key (str):
        content (ContentCreateContent | Unset):
        sort_order (int | Unset):  Default: 0.
        is_active (bool | Unset):  Default: True.
    """

    page: str
    section_key: str
    content: ContentCreateContent | Unset = UNSET
    sort_order: int | Unset = 0
    is_active: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        section_key = self.section_key

        content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        sort_order = self.sort_order

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page": page,
                "section_key": section_key,
            }
        )
        if content is not UNSET:
            field_dict["content"] = content
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_create_content import ContentCreateContent  # noqa: PLC0415

        d = dict(src_dict)
        page = d.pop("page")

        section_key = d.pop("section_key")

        _content = d.pop("content", UNSET)
        content: ContentCreateContent | Unset
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = ContentCreateContent.from_dict(_content)

        sort_order = d.pop("sort_order", UNSET)

        is_active = d.pop("is_active", UNSET)

        content_create = cls(
            page=page,
            section_key=section_key,
            content=content,
            sort_order=sort_order,
            is_active=is_active,
        )

        content_create.additional_properties = d
        return content_create

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
