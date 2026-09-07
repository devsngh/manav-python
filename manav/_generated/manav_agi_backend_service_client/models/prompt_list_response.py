from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.prompt_response import PromptResponse


T = TypeVar("T", bound="PromptListResponse")


@_attrs_define
class PromptListResponse:
    """
    Attributes:
        prompts (list[PromptResponse]):
        total (int):
        page (int):
        page_size (int):
        total_pages (int):
    """

    prompts: list[PromptResponse]
    total: int
    page: int
    page_size: int
    total_pages: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prompts = []
        for prompts_item_data in self.prompts:
            prompts_item = prompts_item_data.to_dict()
            prompts.append(prompts_item)

        total = self.total

        page = self.page

        page_size = self.page_size

        total_pages = self.total_pages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prompts": prompts,
                "total": total,
                "page": page,
                "page_size": page_size,
                "total_pages": total_pages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_response import PromptResponse  # noqa: PLC0415

        d = dict(src_dict)
        prompts = []
        _prompts = d.pop("prompts")
        for prompts_item_data in _prompts:
            prompts_item = PromptResponse.from_dict(prompts_item_data)

            prompts.append(prompts_item)

        total = d.pop("total")

        page = d.pop("page")

        page_size = d.pop("page_size")

        total_pages = d.pop("total_pages")

        prompt_list_response = cls(
            prompts=prompts,
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages,
        )

        prompt_list_response.additional_properties = d
        return prompt_list_response

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
