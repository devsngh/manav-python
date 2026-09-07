from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usage_day import UsageDay


T = TypeVar("T", bound="UsageResponse")


@_attrs_define
class UsageResponse:
    """
    Attributes:
        key_id (str):
        total_today (int):
        rate_limit (int):
        days (list[UsageDay] | Unset):
    """

    key_id: str
    total_today: int
    rate_limit: int
    days: list[UsageDay] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key_id = self.key_id

        total_today = self.total_today

        rate_limit = self.rate_limit

        days: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.days, Unset):
            days = []
            for days_item_data in self.days:
                days_item = days_item_data.to_dict()
                days.append(days_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key_id": key_id,
                "total_today": total_today,
                "rate_limit": rate_limit,
            }
        )
        if days is not UNSET:
            field_dict["days"] = days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usage_day import UsageDay  # noqa: PLC0415

        d = dict(src_dict)
        key_id = d.pop("key_id")

        total_today = d.pop("total_today")

        rate_limit = d.pop("rate_limit")

        _days = d.pop("days", UNSET)
        days: list[UsageDay] | Unset = UNSET
        if _days is not UNSET:
            days = []
            for days_item_data in _days:
                days_item = UsageDay.from_dict(days_item_data)

                days.append(days_item)

        usage_response = cls(
            key_id=key_id,
            total_today=total_today,
            rate_limit=rate_limit,
            days=days,
        )

        usage_response.additional_properties = d
        return usage_response

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
