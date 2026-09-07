from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ChatTrendDay")


@_attrs_define
class ChatTrendDay:
    """
    Attributes:
        date (str):
        dialogues (int):
        threads (int):
        likes (int):
        dislikes (int):
        avg_rating (float):
        interrupted (int):
    """

    date: str
    dialogues: int
    threads: int
    likes: int
    dislikes: int
    avg_rating: float
    interrupted: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        dialogues = self.dialogues

        threads = self.threads

        likes = self.likes

        dislikes = self.dislikes

        avg_rating = self.avg_rating

        interrupted = self.interrupted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "dialogues": dialogues,
                "threads": threads,
                "likes": likes,
                "dislikes": dislikes,
                "avg_rating": avg_rating,
                "interrupted": interrupted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date")

        dialogues = d.pop("dialogues")

        threads = d.pop("threads")

        likes = d.pop("likes")

        dislikes = d.pop("dislikes")

        avg_rating = d.pop("avg_rating")

        interrupted = d.pop("interrupted")

        chat_trend_day = cls(
            date=date,
            dialogues=dialogues,
            threads=threads,
            likes=likes,
            dislikes=dislikes,
            avg_rating=avg_rating,
            interrupted=interrupted,
        )

        chat_trend_day.additional_properties = d
        return chat_trend_day

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
