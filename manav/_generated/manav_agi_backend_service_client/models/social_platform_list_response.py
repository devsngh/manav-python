from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.social_platform_response import SocialPlatformResponse


T = TypeVar("T", bound="SocialPlatformListResponse")


@_attrs_define
class SocialPlatformListResponse:
    """
    Attributes:
        platforms (list[SocialPlatformResponse]):
        total (int):
    """

    platforms: list[SocialPlatformResponse]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platforms = []
        for platforms_item_data in self.platforms:
            platforms_item = platforms_item_data.to_dict()
            platforms.append(platforms_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platforms": platforms,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_platform_response import SocialPlatformResponse  # noqa: PLC0415

        d = dict(src_dict)
        platforms = []
        _platforms = d.pop("platforms")
        for platforms_item_data in _platforms:
            platforms_item = SocialPlatformResponse.from_dict(platforms_item_data)

            platforms.append(platforms_item)

        total = d.pop("total")

        social_platform_list_response = cls(
            platforms=platforms,
            total=total,
        )

        social_platform_list_response.additional_properties = d
        return social_platform_list_response

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
