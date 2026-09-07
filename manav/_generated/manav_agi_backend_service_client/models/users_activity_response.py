from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.daily_active_point import DailyActivePoint


T = TypeVar("T", bound="UsersActivityResponse")


@_attrs_define
class UsersActivityResponse:
    """GET /api/analytics/users/activity — DAU/MAU + daily trend + online_now.

    Attributes:
        online_now (int):
        dau (int):
        mau (int):
        dau_mau_ratio (float):
        days (list[DailyActivePoint]):
    """

    online_now: int
    dau: int
    mau: int
    dau_mau_ratio: float
    days: list[DailyActivePoint]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        online_now = self.online_now

        dau = self.dau

        mau = self.mau

        dau_mau_ratio = self.dau_mau_ratio

        days = []
        for days_item_data in self.days:
            days_item = days_item_data.to_dict()
            days.append(days_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "online_now": online_now,
                "dau": dau,
                "mau": mau,
                "dau_mau_ratio": dau_mau_ratio,
                "days": days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.daily_active_point import DailyActivePoint  # noqa: PLC0415

        d = dict(src_dict)
        online_now = d.pop("online_now")

        dau = d.pop("dau")

        mau = d.pop("mau")

        dau_mau_ratio = d.pop("dau_mau_ratio")

        days = []
        _days = d.pop("days")
        for days_item_data in _days:
            days_item = DailyActivePoint.from_dict(days_item_data)

            days.append(days_item)

        users_activity_response = cls(
            online_now=online_now,
            dau=dau,
            mau=mau,
            dau_mau_ratio=dau_mau_ratio,
            days=days,
        )

        users_activity_response.additional_properties = d
        return users_activity_response

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
