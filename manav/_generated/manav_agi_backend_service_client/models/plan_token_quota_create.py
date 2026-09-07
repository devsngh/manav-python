from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlanTokenQuotaCreate")


@_attrs_define
class PlanTokenQuotaCreate:
    """
    Attributes:
        daily_token_limit (int):
        window_hours (int | Unset):  Default: 4.
        window_strategy (str | Unset):  Default: 'equal'.
        overflow_policy (str | Unset):  Default: 'block'.
    """

    daily_token_limit: int
    window_hours: int | Unset = 4
    window_strategy: str | Unset = "equal"
    overflow_policy: str | Unset = "block"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        daily_token_limit = self.daily_token_limit

        window_hours = self.window_hours

        window_strategy = self.window_strategy

        overflow_policy = self.overflow_policy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "daily_token_limit": daily_token_limit,
            }
        )
        if window_hours is not UNSET:
            field_dict["window_hours"] = window_hours
        if window_strategy is not UNSET:
            field_dict["window_strategy"] = window_strategy
        if overflow_policy is not UNSET:
            field_dict["overflow_policy"] = overflow_policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        daily_token_limit = d.pop("daily_token_limit")

        window_hours = d.pop("window_hours", UNSET)

        window_strategy = d.pop("window_strategy", UNSET)

        overflow_policy = d.pop("overflow_policy", UNSET)

        plan_token_quota_create = cls(
            daily_token_limit=daily_token_limit,
            window_hours=window_hours,
            window_strategy=window_strategy,
            overflow_policy=overflow_policy,
        )

        plan_token_quota_create.additional_properties = d
        return plan_token_quota_create

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
