from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FeedbackTrendPoint")


@_attrs_define
class FeedbackTrendPoint:
    """
    Attributes:
        date (str):
        likes (int | Unset):  Default: 0.
        dislikes (int | Unset):  Default: 0.
        avg_rating (float | None | Unset):
        total_feedback (int | Unset):  Default: 0.
    """

    date: str
    likes: int | Unset = 0
    dislikes: int | Unset = 0
    avg_rating: float | None | Unset = UNSET
    total_feedback: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        likes = self.likes

        dislikes = self.dislikes

        avg_rating: float | None | Unset
        if isinstance(self.avg_rating, Unset):
            avg_rating = UNSET
        else:
            avg_rating = self.avg_rating

        total_feedback = self.total_feedback

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
            }
        )
        if likes is not UNSET:
            field_dict["likes"] = likes
        if dislikes is not UNSET:
            field_dict["dislikes"] = dislikes
        if avg_rating is not UNSET:
            field_dict["avg_rating"] = avg_rating
        if total_feedback is not UNSET:
            field_dict["total_feedback"] = total_feedback

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date")

        likes = d.pop("likes", UNSET)

        dislikes = d.pop("dislikes", UNSET)

        def _parse_avg_rating(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        avg_rating = _parse_avg_rating(d.pop("avg_rating", UNSET))

        total_feedback = d.pop("total_feedback", UNSET)

        feedback_trend_point = cls(
            date=date,
            likes=likes,
            dislikes=dislikes,
            avg_rating=avg_rating,
            total_feedback=total_feedback,
        )

        feedback_trend_point.additional_properties = d
        return feedback_trend_point

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
