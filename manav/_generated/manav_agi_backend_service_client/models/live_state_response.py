from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.current_task_summary import CurrentTaskSummary
    from ..models.pending_hil_summary import PendingHILSummary
    from ..models.recent_event_summary import RecentEventSummary
    from ..models.subtask_summary import SubtaskSummary


T = TypeVar("T", bound="LiveStateResponse")


@_attrs_define
class LiveStateResponse:
    """
    Attributes:
        bot_id (str):
        bot_name (str):
        is_active (bool):
        is_online (bool):
        last_active_at (datetime.datetime | None):
        current_task (CurrentTaskSummary | None):
        last_event_at (datetime.datetime | None):
        idle_seconds (int | None):
        state (str): active | idle | blocked_hil | stuck | errored | completed
        state_reason (str):
        generated_at (datetime.datetime):
        spawned_subtasks (list[SubtaskSummary] | Unset):
        recent_events (list[RecentEventSummary] | Unset):
        pending_hil (list[PendingHILSummary] | Unset):
        recent_error_count (int | Unset):  Default: 0.
    """

    bot_id: str
    bot_name: str
    is_active: bool
    is_online: bool
    last_active_at: datetime.datetime | None
    current_task: CurrentTaskSummary | None
    last_event_at: datetime.datetime | None
    idle_seconds: int | None
    state: str
    state_reason: str
    generated_at: datetime.datetime
    spawned_subtasks: list[SubtaskSummary] | Unset = UNSET
    recent_events: list[RecentEventSummary] | Unset = UNSET
    pending_hil: list[PendingHILSummary] | Unset = UNSET
    recent_error_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.current_task_summary import CurrentTaskSummary  # noqa: PLC0415

        bot_id = self.bot_id

        bot_name = self.bot_name

        is_active = self.is_active

        is_online = self.is_online

        last_active_at: None | str
        if isinstance(self.last_active_at, datetime.datetime):
            last_active_at = self.last_active_at.isoformat()
        else:
            last_active_at = self.last_active_at

        current_task: dict[str, Any] | None
        if isinstance(self.current_task, CurrentTaskSummary):
            current_task = self.current_task.to_dict()
        else:
            current_task = self.current_task

        last_event_at: None | str
        if isinstance(self.last_event_at, datetime.datetime):
            last_event_at = self.last_event_at.isoformat()
        else:
            last_event_at = self.last_event_at

        idle_seconds: int | None
        idle_seconds = self.idle_seconds

        state = self.state

        state_reason = self.state_reason

        generated_at = self.generated_at.isoformat()

        spawned_subtasks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.spawned_subtasks, Unset):
            spawned_subtasks = []
            for spawned_subtasks_item_data in self.spawned_subtasks:
                spawned_subtasks_item = spawned_subtasks_item_data.to_dict()
                spawned_subtasks.append(spawned_subtasks_item)

        recent_events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.recent_events, Unset):
            recent_events = []
            for recent_events_item_data in self.recent_events:
                recent_events_item = recent_events_item_data.to_dict()
                recent_events.append(recent_events_item)

        pending_hil: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pending_hil, Unset):
            pending_hil = []
            for pending_hil_item_data in self.pending_hil:
                pending_hil_item = pending_hil_item_data.to_dict()
                pending_hil.append(pending_hil_item)

        recent_error_count = self.recent_error_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bot_id": bot_id,
                "bot_name": bot_name,
                "is_active": is_active,
                "is_online": is_online,
                "last_active_at": last_active_at,
                "current_task": current_task,
                "last_event_at": last_event_at,
                "idle_seconds": idle_seconds,
                "state": state,
                "state_reason": state_reason,
                "generated_at": generated_at,
            }
        )
        if spawned_subtasks is not UNSET:
            field_dict["spawned_subtasks"] = spawned_subtasks
        if recent_events is not UNSET:
            field_dict["recent_events"] = recent_events
        if pending_hil is not UNSET:
            field_dict["pending_hil"] = pending_hil
        if recent_error_count is not UNSET:
            field_dict["recent_error_count"] = recent_error_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.current_task_summary import CurrentTaskSummary  # noqa: PLC0415
        from ..models.pending_hil_summary import PendingHILSummary  # noqa: PLC0415
        from ..models.recent_event_summary import RecentEventSummary  # noqa: PLC0415
        from ..models.subtask_summary import SubtaskSummary  # noqa: PLC0415

        d = dict(src_dict)
        bot_id = d.pop("bot_id")

        bot_name = d.pop("bot_name")

        is_active = d.pop("is_active")

        is_online = d.pop("is_online")

        def _parse_last_active_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_active_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_active_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_active_at = _parse_last_active_at(d.pop("last_active_at"))

        def _parse_current_task(data: object) -> CurrentTaskSummary | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_task_type_0 = CurrentTaskSummary.from_dict(data)

                return current_task_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CurrentTaskSummary | None, data)

        current_task = _parse_current_task(d.pop("current_task"))

        def _parse_last_event_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_event_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_event_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_event_at = _parse_last_event_at(d.pop("last_event_at"))

        def _parse_idle_seconds(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        idle_seconds = _parse_idle_seconds(d.pop("idle_seconds"))

        state = d.pop("state")

        state_reason = d.pop("state_reason")

        generated_at = datetime.datetime.fromisoformat(d.pop("generated_at"))

        _spawned_subtasks = d.pop("spawned_subtasks", UNSET)
        spawned_subtasks: list[SubtaskSummary] | Unset = UNSET
        if _spawned_subtasks is not UNSET:
            spawned_subtasks = []
            for spawned_subtasks_item_data in _spawned_subtasks:
                spawned_subtasks_item = SubtaskSummary.from_dict(spawned_subtasks_item_data)

                spawned_subtasks.append(spawned_subtasks_item)

        _recent_events = d.pop("recent_events", UNSET)
        recent_events: list[RecentEventSummary] | Unset = UNSET
        if _recent_events is not UNSET:
            recent_events = []
            for recent_events_item_data in _recent_events:
                recent_events_item = RecentEventSummary.from_dict(recent_events_item_data)

                recent_events.append(recent_events_item)

        _pending_hil = d.pop("pending_hil", UNSET)
        pending_hil: list[PendingHILSummary] | Unset = UNSET
        if _pending_hil is not UNSET:
            pending_hil = []
            for pending_hil_item_data in _pending_hil:
                pending_hil_item = PendingHILSummary.from_dict(pending_hil_item_data)

                pending_hil.append(pending_hil_item)

        recent_error_count = d.pop("recent_error_count", UNSET)

        live_state_response = cls(
            bot_id=bot_id,
            bot_name=bot_name,
            is_active=is_active,
            is_online=is_online,
            last_active_at=last_active_at,
            current_task=current_task,
            last_event_at=last_event_at,
            idle_seconds=idle_seconds,
            state=state,
            state_reason=state_reason,
            generated_at=generated_at,
            spawned_subtasks=spawned_subtasks,
            recent_events=recent_events,
            pending_hil=pending_hil,
            recent_error_count=recent_error_count,
        )

        live_state_response.additional_properties = d
        return live_state_response

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
