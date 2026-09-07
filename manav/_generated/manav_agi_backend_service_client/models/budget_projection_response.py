from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BudgetProjectionResponse")


@_attrs_define
class BudgetProjectionResponse:
    """
    Attributes:
        credits_remaining (int):
        avg_daily_burn (float):
        projected_exhaustion_date (datetime.date | None | Unset):
        days_remaining (int | None | Unset):
        current_period_end (None | str | Unset):
    """

    credits_remaining: int
    avg_daily_burn: float
    projected_exhaustion_date: datetime.date | None | Unset = UNSET
    days_remaining: int | None | Unset = UNSET
    current_period_end: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credits_remaining = self.credits_remaining

        avg_daily_burn = self.avg_daily_burn

        projected_exhaustion_date: None | str | Unset
        if isinstance(self.projected_exhaustion_date, Unset):
            projected_exhaustion_date = UNSET
        elif isinstance(self.projected_exhaustion_date, datetime.date):
            projected_exhaustion_date = self.projected_exhaustion_date.isoformat()
        else:
            projected_exhaustion_date = self.projected_exhaustion_date

        days_remaining: int | None | Unset
        if isinstance(self.days_remaining, Unset):
            days_remaining = UNSET
        else:
            days_remaining = self.days_remaining

        current_period_end: None | str | Unset
        if isinstance(self.current_period_end, Unset):
            current_period_end = UNSET
        else:
            current_period_end = self.current_period_end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credits_remaining": credits_remaining,
                "avg_daily_burn": avg_daily_burn,
            }
        )
        if projected_exhaustion_date is not UNSET:
            field_dict["projected_exhaustion_date"] = projected_exhaustion_date
        if days_remaining is not UNSET:
            field_dict["days_remaining"] = days_remaining
        if current_period_end is not UNSET:
            field_dict["current_period_end"] = current_period_end

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credits_remaining = d.pop("credits_remaining")

        avg_daily_burn = d.pop("avg_daily_burn")

        def _parse_projected_exhaustion_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                projected_exhaustion_date_type_0 = datetime.date.fromisoformat(data)

                return projected_exhaustion_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        projected_exhaustion_date = _parse_projected_exhaustion_date(d.pop("projected_exhaustion_date", UNSET))

        def _parse_days_remaining(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        days_remaining = _parse_days_remaining(d.pop("days_remaining", UNSET))

        def _parse_current_period_end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_period_end = _parse_current_period_end(d.pop("current_period_end", UNSET))

        budget_projection_response = cls(
            credits_remaining=credits_remaining,
            avg_daily_burn=avg_daily_burn,
            projected_exhaustion_date=projected_exhaustion_date,
            days_remaining=days_remaining,
            current_period_end=current_period_end,
        )

        budget_projection_response.additional_properties = d
        return budget_projection_response

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
