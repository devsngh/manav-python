from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExpansionRateResponse")


@_attrs_define
class ExpansionRateResponse:
    """GET /api/analytics/growth/expansion-rate

    Attributes:
        expansion_rate (float):
        expanding_orgs (int):
        paying_orgs (int):
        window_months (int):
    """

    expansion_rate: float
    expanding_orgs: int
    paying_orgs: int
    window_months: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expansion_rate = self.expansion_rate

        expanding_orgs = self.expanding_orgs

        paying_orgs = self.paying_orgs

        window_months = self.window_months

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expansion_rate": expansion_rate,
                "expanding_orgs": expanding_orgs,
                "paying_orgs": paying_orgs,
                "window_months": window_months,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expansion_rate = d.pop("expansion_rate")

        expanding_orgs = d.pop("expanding_orgs")

        paying_orgs = d.pop("paying_orgs")

        window_months = d.pop("window_months")

        expansion_rate_response = cls(
            expansion_rate=expansion_rate,
            expanding_orgs=expanding_orgs,
            paying_orgs=paying_orgs,
            window_months=window_months,
        )

        expansion_rate_response.additional_properties = d
        return expansion_rate_response

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
