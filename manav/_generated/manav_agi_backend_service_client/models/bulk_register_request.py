from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bulk_register_item import BulkRegisterItem


T = TypeVar("T", bound="BulkRegisterRequest")


@_attrs_define
class BulkRegisterRequest:
    """
    Attributes:
        elements (list[BulkRegisterItem]):
    """

    elements: list[BulkRegisterItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        elements = []
        for elements_item_data in self.elements:
            elements_item = elements_item_data.to_dict()
            elements.append(elements_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "elements": elements,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_register_item import BulkRegisterItem  # noqa: PLC0415

        d = dict(src_dict)
        elements = []
        _elements = d.pop("elements")
        for elements_item_data in _elements:
            elements_item = BulkRegisterItem.from_dict(elements_item_data)

            elements.append(elements_item)

        bulk_register_request = cls(
            elements=elements,
        )

        bulk_register_request.additional_properties = d
        return bulk_register_request

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
