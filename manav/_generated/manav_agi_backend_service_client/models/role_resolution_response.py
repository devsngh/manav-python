from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.role_resolution_response_map import RoleResolutionResponseMap


T = TypeVar("T", bound="RoleResolutionResponse")


@_attrs_define
class RoleResolutionResponse:
    """
    Attributes:
        map_ (RoleResolutionResponseMap):
    """

    map_: RoleResolutionResponseMap
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        map_ = self.map_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "map": map_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.role_resolution_response_map import RoleResolutionResponseMap  # noqa: PLC0415

        d = dict(src_dict)
        map_ = RoleResolutionResponseMap.from_dict(d.pop("map"))

        role_resolution_response = cls(
            map_=map_,
        )

        role_resolution_response.additional_properties = d
        return role_resolution_response

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
