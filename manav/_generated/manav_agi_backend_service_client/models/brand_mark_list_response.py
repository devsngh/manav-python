from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.brand_mark_response import BrandMarkResponse


T = TypeVar("T", bound="BrandMarkListResponse")


@_attrs_define
class BrandMarkListResponse:
    """
    Attributes:
        marks (list[BrandMarkResponse]):
        total (int):
    """

    marks: list[BrandMarkResponse]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        marks = []
        for marks_item_data in self.marks:
            marks_item = marks_item_data.to_dict()
            marks.append(marks_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marks": marks,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brand_mark_response import BrandMarkResponse  # noqa: PLC0415

        d = dict(src_dict)
        marks = []
        _marks = d.pop("marks")
        for marks_item_data in _marks:
            marks_item = BrandMarkResponse.from_dict(marks_item_data)

            marks.append(marks_item)

        total = d.pop("total")

        brand_mark_list_response = cls(
            marks=marks,
            total=total,
        )

        brand_mark_list_response.additional_properties = d
        return brand_mark_list_response

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
