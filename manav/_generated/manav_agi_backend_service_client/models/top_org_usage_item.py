from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopOrgUsageItem")


@_attrs_define
class TopOrgUsageItem:
    """
    Attributes:
        org_id (str):
        org_name (str):
        used_credits_cycle (int):
        available_credits (int):
        plan_credits (int):
        used_pct (float):
        plan (None | str | Unset):
    """

    org_id: str
    org_name: str
    used_credits_cycle: int
    available_credits: int
    plan_credits: int
    used_pct: float
    plan: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_id = self.org_id

        org_name = self.org_name

        used_credits_cycle = self.used_credits_cycle

        available_credits = self.available_credits

        plan_credits = self.plan_credits

        used_pct = self.used_pct

        plan: None | str | Unset
        if isinstance(self.plan, Unset):
            plan = UNSET
        else:
            plan = self.plan

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "org_id": org_id,
                "org_name": org_name,
                "used_credits_cycle": used_credits_cycle,
                "available_credits": available_credits,
                "plan_credits": plan_credits,
                "used_pct": used_pct,
            }
        )
        if plan is not UNSET:
            field_dict["plan"] = plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        org_id = d.pop("org_id")

        org_name = d.pop("org_name")

        used_credits_cycle = d.pop("used_credits_cycle")

        available_credits = d.pop("available_credits")

        plan_credits = d.pop("plan_credits")

        used_pct = d.pop("used_pct")

        def _parse_plan(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plan = _parse_plan(d.pop("plan", UNSET))

        top_org_usage_item = cls(
            org_id=org_id,
            org_name=org_name,
            used_credits_cycle=used_credits_cycle,
            available_credits=available_credits,
            plan_credits=plan_credits,
            used_pct=used_pct,
            plan=plan,
        )

        top_org_usage_item.additional_properties = d
        return top_org_usage_item

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
