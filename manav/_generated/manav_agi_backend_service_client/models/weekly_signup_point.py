from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WeeklySignupPoint")


@_attrs_define
class WeeklySignupPoint:
    """
    Attributes:
        week (str):
        signups (int):
        free (int):
        paid (int):
    """

    week: str
    signups: int
    free: int
    paid: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        week = self.week

        signups = self.signups

        free = self.free

        paid = self.paid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "week": week,
                "signups": signups,
                "free": free,
                "paid": paid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        week = d.pop("week")

        signups = d.pop("signups")

        free = d.pop("free")

        paid = d.pop("paid")

        weekly_signup_point = cls(
            week=week,
            signups=signups,
            free=free,
            paid=paid,
        )

        weekly_signup_point.additional_properties = d
        return weekly_signup_point

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
