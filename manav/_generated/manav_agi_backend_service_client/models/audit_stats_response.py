from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.action_count import ActionCount
    from ..models.active_user_count import ActiveUserCount
    from ..models.activity_over_time import ActivityOverTime
    from ..models.resource_count import ResourceCount


T = TypeVar("T", bound="AuditStatsResponse")


@_attrs_define
class AuditStatsResponse:
    """
    Attributes:
        total_events (int):
        by_action (list[ActionCount]):
        by_resource (list[ResourceCount]):
        most_active_users (list[ActiveUserCount]):
        activity_over_time (list[ActivityOverTime]):
    """

    total_events: int
    by_action: list[ActionCount]
    by_resource: list[ResourceCount]
    most_active_users: list[ActiveUserCount]
    activity_over_time: list[ActivityOverTime]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_events = self.total_events

        by_action = []
        for by_action_item_data in self.by_action:
            by_action_item = by_action_item_data.to_dict()
            by_action.append(by_action_item)

        by_resource = []
        for by_resource_item_data in self.by_resource:
            by_resource_item = by_resource_item_data.to_dict()
            by_resource.append(by_resource_item)

        most_active_users = []
        for most_active_users_item_data in self.most_active_users:
            most_active_users_item = most_active_users_item_data.to_dict()
            most_active_users.append(most_active_users_item)

        activity_over_time = []
        for activity_over_time_item_data in self.activity_over_time:
            activity_over_time_item = activity_over_time_item_data.to_dict()
            activity_over_time.append(activity_over_time_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_events": total_events,
                "by_action": by_action,
                "by_resource": by_resource,
                "most_active_users": most_active_users,
                "activity_over_time": activity_over_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_count import ActionCount  # noqa: PLC0415
        from ..models.active_user_count import ActiveUserCount  # noqa: PLC0415
        from ..models.activity_over_time import ActivityOverTime  # noqa: PLC0415
        from ..models.resource_count import ResourceCount  # noqa: PLC0415

        d = dict(src_dict)
        total_events = d.pop("total_events")

        by_action = []
        _by_action = d.pop("by_action")
        for by_action_item_data in _by_action:
            by_action_item = ActionCount.from_dict(by_action_item_data)

            by_action.append(by_action_item)

        by_resource = []
        _by_resource = d.pop("by_resource")
        for by_resource_item_data in _by_resource:
            by_resource_item = ResourceCount.from_dict(by_resource_item_data)

            by_resource.append(by_resource_item)

        most_active_users = []
        _most_active_users = d.pop("most_active_users")
        for most_active_users_item_data in _most_active_users:
            most_active_users_item = ActiveUserCount.from_dict(most_active_users_item_data)

            most_active_users.append(most_active_users_item)

        activity_over_time = []
        _activity_over_time = d.pop("activity_over_time")
        for activity_over_time_item_data in _activity_over_time:
            activity_over_time_item = ActivityOverTime.from_dict(activity_over_time_item_data)

            activity_over_time.append(activity_over_time_item)

        audit_stats_response = cls(
            total_events=total_events,
            by_action=by_action,
            by_resource=by_resource,
            most_active_users=most_active_users,
            activity_over_time=activity_over_time,
        )

        audit_stats_response.additional_properties = d
        return audit_stats_response

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
