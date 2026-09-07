from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.banner_response import BannerResponse


T = TypeVar("T", bound="ActiveBannersResponse")


@_attrs_define
class ActiveBannersResponse:
    """
    Attributes:
        hero_top (list[BannerResponse] | Unset):
        inline_row (list[BannerResponse] | Unset):
        bottom (list[BannerResponse] | Unset):
        floating_right (list[BannerResponse] | Unset):
    """

    hero_top: list[BannerResponse] | Unset = UNSET
    inline_row: list[BannerResponse] | Unset = UNSET
    bottom: list[BannerResponse] | Unset = UNSET
    floating_right: list[BannerResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hero_top: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hero_top, Unset):
            hero_top = []
            for hero_top_item_data in self.hero_top:
                hero_top_item = hero_top_item_data.to_dict()
                hero_top.append(hero_top_item)

        inline_row: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inline_row, Unset):
            inline_row = []
            for inline_row_item_data in self.inline_row:
                inline_row_item = inline_row_item_data.to_dict()
                inline_row.append(inline_row_item)

        bottom: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bottom, Unset):
            bottom = []
            for bottom_item_data in self.bottom:
                bottom_item = bottom_item_data.to_dict()
                bottom.append(bottom_item)

        floating_right: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.floating_right, Unset):
            floating_right = []
            for floating_right_item_data in self.floating_right:
                floating_right_item = floating_right_item_data.to_dict()
                floating_right.append(floating_right_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hero_top is not UNSET:
            field_dict["hero_top"] = hero_top
        if inline_row is not UNSET:
            field_dict["inline_row"] = inline_row
        if bottom is not UNSET:
            field_dict["bottom"] = bottom
        if floating_right is not UNSET:
            field_dict["floating_right"] = floating_right

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.banner_response import BannerResponse  # noqa: PLC0415

        d = dict(src_dict)
        _hero_top = d.pop("hero_top", UNSET)
        hero_top: list[BannerResponse] | Unset = UNSET
        if _hero_top is not UNSET:
            hero_top = []
            for hero_top_item_data in _hero_top:
                hero_top_item = BannerResponse.from_dict(hero_top_item_data)

                hero_top.append(hero_top_item)

        _inline_row = d.pop("inline_row", UNSET)
        inline_row: list[BannerResponse] | Unset = UNSET
        if _inline_row is not UNSET:
            inline_row = []
            for inline_row_item_data in _inline_row:
                inline_row_item = BannerResponse.from_dict(inline_row_item_data)

                inline_row.append(inline_row_item)

        _bottom = d.pop("bottom", UNSET)
        bottom: list[BannerResponse] | Unset = UNSET
        if _bottom is not UNSET:
            bottom = []
            for bottom_item_data in _bottom:
                bottom_item = BannerResponse.from_dict(bottom_item_data)

                bottom.append(bottom_item)

        _floating_right = d.pop("floating_right", UNSET)
        floating_right: list[BannerResponse] | Unset = UNSET
        if _floating_right is not UNSET:
            floating_right = []
            for floating_right_item_data in _floating_right:
                floating_right_item = BannerResponse.from_dict(floating_right_item_data)

                floating_right.append(floating_right_item)

        active_banners_response = cls(
            hero_top=hero_top,
            inline_row=inline_row,
            bottom=bottom,
            floating_right=floating_right,
        )

        active_banners_response.additional_properties = d
        return active_banners_response

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
