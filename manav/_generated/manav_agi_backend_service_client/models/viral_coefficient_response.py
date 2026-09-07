from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ViralCoefficientResponse")


@_attrs_define
class ViralCoefficientResponse:
    """GET /api/analytics/growth/viral-coefficient

    Attributes:
        k_factor (float):
        new_users (int):
        referrals (int):
        window_months (int):
    """

    k_factor: float
    new_users: int
    referrals: int
    window_months: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        k_factor = self.k_factor

        new_users = self.new_users

        referrals = self.referrals

        window_months = self.window_months

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "k_factor": k_factor,
                "new_users": new_users,
                "referrals": referrals,
                "window_months": window_months,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        k_factor = d.pop("k_factor")

        new_users = d.pop("new_users")

        referrals = d.pop("referrals")

        window_months = d.pop("window_months")

        viral_coefficient_response = cls(
            k_factor=k_factor,
            new_users=new_users,
            referrals=referrals,
            window_months=window_months,
        )

        viral_coefficient_response.additional_properties = d
        return viral_coefficient_response

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
