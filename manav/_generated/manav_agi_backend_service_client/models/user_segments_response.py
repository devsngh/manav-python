from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.segment_item import SegmentItem


T = TypeVar("T", bound="UserSegmentsResponse")


@_attrs_define
class UserSegmentsResponse:
    """
    Attributes:
        total_users (int):
        segments (list[SegmentItem]):
    """

    total_users: int
    segments: list[SegmentItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_users = self.total_users

        segments = []
        for segments_item_data in self.segments:
            segments_item = segments_item_data.to_dict()
            segments.append(segments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_users": total_users,
                "segments": segments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.segment_item import SegmentItem  # noqa: PLC0415

        d = dict(src_dict)
        total_users = d.pop("total_users")

        segments = []
        _segments = d.pop("segments")
        for segments_item_data in _segments:
            segments_item = SegmentItem.from_dict(segments_item_data)

            segments.append(segments_item)

        user_segments_response = cls(
            total_users=total_users,
            segments=segments,
        )

        user_segments_response.additional_properties = d
        return user_segments_response

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
