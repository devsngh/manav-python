from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.character_reference_create import CharacterReferenceCreate


T = TypeVar("T", bound="SupersedeRequest")


@_attrs_define
class SupersedeRequest:
    """
    Attributes:
        new_reference (CharacterReferenceCreate):
    """

    new_reference: CharacterReferenceCreate
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_reference = self.new_reference.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "new_reference": new_reference,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.character_reference_create import CharacterReferenceCreate  # noqa: PLC0415

        d = dict(src_dict)
        new_reference = CharacterReferenceCreate.from_dict(d.pop("new_reference"))

        supersede_request = cls(
            new_reference=new_reference,
        )

        supersede_request.additional_properties = d
        return supersede_request

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
