from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.persona_response import PersonaResponse


T = TypeVar("T", bound="PersonaListResponse")


@_attrs_define
class PersonaListResponse:
    """
    Attributes:
        personas (list[PersonaResponse]):
        total (int):
        page (int):
        page_size (int):
    """

    personas: list[PersonaResponse]
    total: int
    page: int
    page_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        personas = []
        for personas_item_data in self.personas:
            personas_item = personas_item_data.to_dict()
            personas.append(personas_item)

        total = self.total

        page = self.page

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "personas": personas,
                "total": total,
                "page": page,
                "page_size": page_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.persona_response import PersonaResponse  # noqa: PLC0415

        d = dict(src_dict)
        personas = []
        _personas = d.pop("personas")
        for personas_item_data in _personas:
            personas_item = PersonaResponse.from_dict(personas_item_data)

            personas.append(personas_item)

        total = d.pop("total")

        page = d.pop("page")

        page_size = d.pop("page_size")

        persona_list_response = cls(
            personas=personas,
            total=total,
            page=page,
            page_size=page_size,
        )

        persona_list_response.additional_properties = d
        return persona_list_response

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
