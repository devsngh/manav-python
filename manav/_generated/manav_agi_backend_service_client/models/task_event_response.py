from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_event_type import TaskEventType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task_event_response_event_data_type_0 import TaskEventResponseEventDataType0


T = TypeVar("T", bound="TaskEventResponse")


@_attrs_define
class TaskEventResponse:
    """
    Attributes:
        id (UUID):
        task_id (UUID):
        event_type (TaskEventType):
        actor_user_id (None | Unset | UUID):
        actor_bot_id (None | Unset | UUID):
        message (None | str | Unset):
        event_data (None | TaskEventResponseEventDataType0 | Unset):
        created_at (datetime.datetime | None | Unset):
    """

    id: UUID
    task_id: UUID
    event_type: TaskEventType
    actor_user_id: None | Unset | UUID = UNSET
    actor_bot_id: None | Unset | UUID = UNSET
    message: None | str | Unset = UNSET
    event_data: None | TaskEventResponseEventDataType0 | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.task_event_response_event_data_type_0 import TaskEventResponseEventDataType0  # noqa: PLC0415

        id = str(self.id)

        task_id = str(self.task_id)

        event_type = self.event_type.value

        actor_user_id: None | str | Unset
        if isinstance(self.actor_user_id, Unset):
            actor_user_id = UNSET
        elif isinstance(self.actor_user_id, UUID):
            actor_user_id = str(self.actor_user_id)
        else:
            actor_user_id = self.actor_user_id

        actor_bot_id: None | str | Unset
        if isinstance(self.actor_bot_id, Unset):
            actor_bot_id = UNSET
        elif isinstance(self.actor_bot_id, UUID):
            actor_bot_id = str(self.actor_bot_id)
        else:
            actor_bot_id = self.actor_bot_id

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        event_data: dict[str, Any] | None | Unset
        if isinstance(self.event_data, Unset):
            event_data = UNSET
        elif isinstance(self.event_data, TaskEventResponseEventDataType0):
            event_data = self.event_data.to_dict()
        else:
            event_data = self.event_data

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "task_id": task_id,
                "event_type": event_type,
            }
        )
        if actor_user_id is not UNSET:
            field_dict["actor_user_id"] = actor_user_id
        if actor_bot_id is not UNSET:
            field_dict["actor_bot_id"] = actor_bot_id
        if message is not UNSET:
            field_dict["message"] = message
        if event_data is not UNSET:
            field_dict["event_data"] = event_data
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.task_event_response_event_data_type_0 import TaskEventResponseEventDataType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        task_id = UUID(d.pop("task_id"))

        event_type = TaskEventType(d.pop("event_type"))

        def _parse_actor_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                actor_user_id_type_0 = UUID(data)

                return actor_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        actor_user_id = _parse_actor_user_id(d.pop("actor_user_id", UNSET))

        def _parse_actor_bot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                actor_bot_id_type_0 = UUID(data)

                return actor_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        actor_bot_id = _parse_actor_bot_id(d.pop("actor_bot_id", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_event_data(data: object) -> None | TaskEventResponseEventDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                event_data_type_0 = TaskEventResponseEventDataType0.from_dict(data)

                return event_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskEventResponseEventDataType0 | Unset, data)

        event_data = _parse_event_data(d.pop("event_data", UNSET))

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        task_event_response = cls(
            id=id,
            task_id=task_id,
            event_type=event_type,
            actor_user_id=actor_user_id,
            actor_bot_id=actor_bot_id,
            message=message,
            event_data=event_data,
            created_at=created_at,
        )

        task_event_response.additional_properties = d
        return task_event_response

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
