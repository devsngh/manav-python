from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.location_item import LocationItem


T = TypeVar("T", bound="LocationListResponse")


@_attrs_define
class LocationListResponse:
    """
    Attributes:
        locations (list[LocationItem]):
        total (int):
    """

    locations: list[LocationItem]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        locations = []
        for locations_item_data in self.locations:
            locations_item = locations_item_data.to_dict()
            locations.append(locations_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "locations": locations,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_item import LocationItem  # noqa: PLC0415

        d = dict(src_dict)
        locations = []
        _locations = d.pop("locations")
        for locations_item_data in _locations:
            locations_item = LocationItem.from_dict(locations_item_data)

            locations.append(locations_item)

        total = d.pop("total")

        location_list_response = cls(
            locations=locations,
            total=total,
        )

        location_list_response.additional_properties = d
        return location_list_response

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
