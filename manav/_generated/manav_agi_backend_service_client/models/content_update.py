from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_update_content_type_0 import ContentUpdateContentType0


T = TypeVar("T", bound="ContentUpdate")


@_attrs_define
class ContentUpdate:
    """
    Attributes:
        content (ContentUpdateContentType0 | None | Unset):
        sort_order (int | None | Unset):
        is_active (bool | None | Unset):
    """

    content: ContentUpdateContentType0 | None | Unset = UNSET
    sort_order: int | None | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.content_update_content_type_0 import ContentUpdateContentType0  # noqa: PLC0415

        content: dict[str, Any] | None | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        elif isinstance(self.content, ContentUpdateContentType0):
            content = self.content.to_dict()
        else:
            content = self.content

        sort_order: int | None | Unset
        if isinstance(self.sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = self.sort_order

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_update_content_type_0 import ContentUpdateContentType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_content(data: object) -> ContentUpdateContentType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_0 = ContentUpdateContentType0.from_dict(data)

                return content_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContentUpdateContentType0 | None | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        def _parse_sort_order(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sort_order = _parse_sort_order(d.pop("sort_order", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        content_update = cls(
            content=content,
            sort_order=sort_order,
            is_active=is_active,
        )

        content_update.additional_properties = d
        return content_update

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
