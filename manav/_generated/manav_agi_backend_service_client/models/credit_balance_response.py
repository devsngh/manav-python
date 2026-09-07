from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditBalanceResponse")


@_attrs_define
class CreditBalanceResponse:
    """
    Attributes:
        org_id (UUID):
        plan_credits (int):
        purchased_credits (int):
        used_credits_cycle (int):
        available_credits (int):
        cycle_reset_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    org_id: UUID
    plan_credits: int
    purchased_credits: int
    used_credits_cycle: int
    available_credits: int
    cycle_reset_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_id = str(self.org_id)

        plan_credits = self.plan_credits

        purchased_credits = self.purchased_credits

        used_credits_cycle = self.used_credits_cycle

        available_credits = self.available_credits

        cycle_reset_at: None | str | Unset
        if isinstance(self.cycle_reset_at, Unset):
            cycle_reset_at = UNSET
        elif isinstance(self.cycle_reset_at, datetime.datetime):
            cycle_reset_at = self.cycle_reset_at.isoformat()
        else:
            cycle_reset_at = self.cycle_reset_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "org_id": org_id,
                "plan_credits": plan_credits,
                "purchased_credits": purchased_credits,
                "used_credits_cycle": used_credits_cycle,
                "available_credits": available_credits,
            }
        )
        if cycle_reset_at is not UNSET:
            field_dict["cycle_reset_at"] = cycle_reset_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        org_id = UUID(d.pop("org_id"))

        plan_credits = d.pop("plan_credits")

        purchased_credits = d.pop("purchased_credits")

        used_credits_cycle = d.pop("used_credits_cycle")

        available_credits = d.pop("available_credits")

        def _parse_cycle_reset_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cycle_reset_at_type_0 = datetime.datetime.fromisoformat(data)

                return cycle_reset_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        cycle_reset_at = _parse_cycle_reset_at(d.pop("cycle_reset_at", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        credit_balance_response = cls(
            org_id=org_id,
            plan_credits=plan_credits,
            purchased_credits=purchased_credits,
            used_credits_cycle=used_credits_cycle,
            available_credits=available_credits,
            cycle_reset_at=cycle_reset_at,
            updated_at=updated_at,
        )

        credit_balance_response.additional_properties = d
        return credit_balance_response

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
