from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ActivationCohort")


@_attrs_define
class ActivationCohort:
    """
    Attributes:
        month (str):
        signups (int):
        activated (int):
        rate (float):
    """

    month: str
    signups: int
    activated: int
    rate: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        month = self.month

        signups = self.signups

        activated = self.activated

        rate = self.rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "month": month,
                "signups": signups,
                "activated": activated,
                "rate": rate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        month = d.pop("month")

        signups = d.pop("signups")

        activated = d.pop("activated")

        rate = d.pop("rate")

        activation_cohort = cls(
            month=month,
            signups=signups,
            activated=activated,
            rate=rate,
        )

        activation_cohort.additional_properties = d
        return activation_cohort

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
