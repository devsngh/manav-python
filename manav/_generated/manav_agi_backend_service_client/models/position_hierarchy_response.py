from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.position_response import PositionResponse


T = TypeVar("T", bound="PositionHierarchyResponse")


@_attrs_define
class PositionHierarchyResponse:
    """Full reporting chain from a position to the root

    Attributes:
        position (PositionResponse): Position response schema
        ancestors (list[PositionResponse]):
    """

    position: PositionResponse
    ancestors: list[PositionResponse]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position = self.position.to_dict()

        ancestors = []
        for ancestors_item_data in self.ancestors:
            ancestors_item = ancestors_item_data.to_dict()
            ancestors.append(ancestors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
                "ancestors": ancestors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.position_response import PositionResponse  # noqa: PLC0415

        d = dict(src_dict)
        position = PositionResponse.from_dict(d.pop("position"))

        ancestors = []
        _ancestors = d.pop("ancestors")
        for ancestors_item_data in _ancestors:
            ancestors_item = PositionResponse.from_dict(ancestors_item_data)

            ancestors.append(ancestors_item)

        position_hierarchy_response = cls(
            position=position,
            ancestors=ancestors,
        )

        position_hierarchy_response.additional_properties = d
        return position_hierarchy_response

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
