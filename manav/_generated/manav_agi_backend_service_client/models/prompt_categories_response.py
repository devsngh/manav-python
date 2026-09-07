from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.prompt_categories_response_sub_categories import PromptCategoriesResponseSubCategories


T = TypeVar("T", bound="PromptCategoriesResponse")


@_attrs_define
class PromptCategoriesResponse:
    """
    Attributes:
        categories (list[str]):
        sub_categories (PromptCategoriesResponseSubCategories):
    """

    categories: list[str]
    sub_categories: PromptCategoriesResponseSubCategories
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        categories = self.categories

        sub_categories = self.sub_categories.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "categories": categories,
                "sub_categories": sub_categories,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_categories_response_sub_categories import (
            PromptCategoriesResponseSubCategories,  # noqa: PLC0415
        )

        d = dict(src_dict)
        categories = cast(list[str], d.pop("categories"))

        sub_categories = PromptCategoriesResponseSubCategories.from_dict(d.pop("sub_categories"))

        prompt_categories_response = cls(
            categories=categories,
            sub_categories=sub_categories,
        )

        prompt_categories_response.additional_properties = d
        return prompt_categories_response

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
