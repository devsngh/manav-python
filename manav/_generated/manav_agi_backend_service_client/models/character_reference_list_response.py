from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.character_reference_response import CharacterReferenceResponse


T = TypeVar("T", bound="CharacterReferenceListResponse")


@_attrs_define
class CharacterReferenceListResponse:
    """
    Attributes:
        references (list[CharacterReferenceResponse]):
        total (int):
        page (int):
        page_size (int):
    """

    references: list[CharacterReferenceResponse]
    total: int
    page: int
    page_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        references = []
        for references_item_data in self.references:
            references_item = references_item_data.to_dict()
            references.append(references_item)

        total = self.total

        page = self.page

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "references": references,
                "total": total,
                "page": page,
                "page_size": page_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.character_reference_response import CharacterReferenceResponse  # noqa: PLC0415

        d = dict(src_dict)
        references = []
        _references = d.pop("references")
        for references_item_data in _references:
            references_item = CharacterReferenceResponse.from_dict(references_item_data)

            references.append(references_item)

        total = d.pop("total")

        page = d.pop("page")

        page_size = d.pop("page_size")

        character_reference_list_response = cls(
            references=references,
            total=total,
            page=page,
            page_size=page_size,
        )

        character_reference_list_response.additional_properties = d
        return character_reference_list_response

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
