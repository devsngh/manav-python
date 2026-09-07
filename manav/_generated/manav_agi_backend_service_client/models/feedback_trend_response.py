from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feedback_trend_point import FeedbackTrendPoint


T = TypeVar("T", bound="FeedbackTrendResponse")


@_attrs_define
class FeedbackTrendResponse:
    """
    Attributes:
        data (list[FeedbackTrendPoint] | Unset):
        total_likes (int | Unset):  Default: 0.
        total_dislikes (int | Unset):  Default: 0.
        overall_rating (float | Unset):  Default: 0.0.
    """

    data: list[FeedbackTrendPoint] | Unset = UNSET
    total_likes: int | Unset = 0
    total_dislikes: int | Unset = 0
    overall_rating: float | Unset = 0.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        total_likes = self.total_likes

        total_dislikes = self.total_dislikes

        overall_rating = self.overall_rating

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if total_likes is not UNSET:
            field_dict["total_likes"] = total_likes
        if total_dislikes is not UNSET:
            field_dict["total_dislikes"] = total_dislikes
        if overall_rating is not UNSET:
            field_dict["overall_rating"] = overall_rating

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.feedback_trend_point import FeedbackTrendPoint  # noqa: PLC0415

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[FeedbackTrendPoint] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = FeedbackTrendPoint.from_dict(data_item_data)

                data.append(data_item)

        total_likes = d.pop("total_likes", UNSET)

        total_dislikes = d.pop("total_dislikes", UNSET)

        overall_rating = d.pop("overall_rating", UNSET)

        feedback_trend_response = cls(
            data=data,
            total_likes=total_likes,
            total_dislikes=total_dislikes,
            overall_rating=overall_rating,
        )

        feedback_trend_response.additional_properties = d
        return feedback_trend_response

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
