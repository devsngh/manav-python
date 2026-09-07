from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.funnel_stage import FunnelStage
    from ..models.weekly_signup_point import WeeklySignupPoint


T = TypeVar("T", bound="GrowthSignupsResponse")


@_attrs_define
class GrowthSignupsResponse:
    """GET /api/analytics/growth/signups — weekly signups + snapshot funnel.

    NOTE: the funnel here is a *current-state snapshot* (orgs currently at each
    stage), not a cohort-based time-to-stage funnel. True cohort funnels need
    a lifecycle_events table tracking when each org crosses each stage.

        Attributes:
            last_7d (int):
            last_30d (int):
            weekly (list[WeeklySignupPoint]):
            funnel (list[FunnelStage]):
    """

    last_7d: int
    last_30d: int
    weekly: list[WeeklySignupPoint]
    funnel: list[FunnelStage]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_7d = self.last_7d

        last_30d = self.last_30d

        weekly = []
        for weekly_item_data in self.weekly:
            weekly_item = weekly_item_data.to_dict()
            weekly.append(weekly_item)

        funnel = []
        for funnel_item_data in self.funnel:
            funnel_item = funnel_item_data.to_dict()
            funnel.append(funnel_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "last_7d": last_7d,
                "last_30d": last_30d,
                "weekly": weekly,
                "funnel": funnel,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.funnel_stage import FunnelStage  # noqa: PLC0415
        from ..models.weekly_signup_point import WeeklySignupPoint  # noqa: PLC0415

        d = dict(src_dict)
        last_7d = d.pop("last_7d")

        last_30d = d.pop("last_30d")

        weekly = []
        _weekly = d.pop("weekly")
        for weekly_item_data in _weekly:
            weekly_item = WeeklySignupPoint.from_dict(weekly_item_data)

            weekly.append(weekly_item)

        funnel = []
        _funnel = d.pop("funnel")
        for funnel_item_data in _funnel:
            funnel_item = FunnelStage.from_dict(funnel_item_data)

            funnel.append(funnel_item)

        growth_signups_response = cls(
            last_7d=last_7d,
            last_30d=last_30d,
            weekly=weekly,
            funnel=funnel,
        )

        growth_signups_response.additional_properties = d
        return growth_signups_response

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
