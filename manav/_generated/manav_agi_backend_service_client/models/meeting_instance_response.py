from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meeting_instance_response_action_items_item import MeetingInstanceResponseActionItemsItem
    from ..models.meeting_instance_response_decisions_made_item import MeetingInstanceResponseDecisionsMadeItem
    from ..models.meeting_instance_response_participants_attended_item import (
        MeetingInstanceResponseParticipantsAttendedItem,
    )
    from ..models.meeting_instance_response_prep_completion_status import MeetingInstanceResponsePrepCompletionStatus


T = TypeVar("T", bound="MeetingInstanceResponse")


@_attrs_define
class MeetingInstanceResponse:
    """
    Attributes:
        id (UUID):
        meeting_id (UUID):
        instance_date (datetime.date):
        participants_attended (list[MeetingInstanceResponseParticipantsAttendedItem]):
        prep_task_ids (list[UUID]):
        prep_completion_status (MeetingInstanceResponsePrepCompletionStatus):
        notes_message_ids (list[UUID]):
        action_items (list[MeetingInstanceResponseActionItemsItem]):
        decisions_made (list[MeetingInstanceResponseDecisionsMadeItem]):
        status (str):
        org_id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        started_at (datetime.datetime | None | Unset):
        ended_at (datetime.datetime | None | Unset):
    """

    id: UUID
    meeting_id: UUID
    instance_date: datetime.date
    participants_attended: list[MeetingInstanceResponseParticipantsAttendedItem]
    prep_task_ids: list[UUID]
    prep_completion_status: MeetingInstanceResponsePrepCompletionStatus
    notes_message_ids: list[UUID]
    action_items: list[MeetingInstanceResponseActionItemsItem]
    decisions_made: list[MeetingInstanceResponseDecisionsMadeItem]
    status: str
    org_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    started_at: datetime.datetime | None | Unset = UNSET
    ended_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        meeting_id = str(self.meeting_id)

        instance_date = self.instance_date.isoformat()

        participants_attended = []
        for participants_attended_item_data in self.participants_attended:
            participants_attended_item = participants_attended_item_data.to_dict()
            participants_attended.append(participants_attended_item)

        prep_task_ids = []
        for prep_task_ids_item_data in self.prep_task_ids:
            prep_task_ids_item = str(prep_task_ids_item_data)
            prep_task_ids.append(prep_task_ids_item)

        prep_completion_status = self.prep_completion_status.to_dict()

        notes_message_ids = []
        for notes_message_ids_item_data in self.notes_message_ids:
            notes_message_ids_item = str(notes_message_ids_item_data)
            notes_message_ids.append(notes_message_ids_item)

        action_items = []
        for action_items_item_data in self.action_items:
            action_items_item = action_items_item_data.to_dict()
            action_items.append(action_items_item)

        decisions_made = []
        for decisions_made_item_data in self.decisions_made:
            decisions_made_item = decisions_made_item_data.to_dict()
            decisions_made.append(decisions_made_item)

        status = self.status

        org_id = str(self.org_id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        ended_at: None | str | Unset
        if isinstance(self.ended_at, Unset):
            ended_at = UNSET
        elif isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "meeting_id": meeting_id,
                "instance_date": instance_date,
                "participants_attended": participants_attended,
                "prep_task_ids": prep_task_ids,
                "prep_completion_status": prep_completion_status,
                "notes_message_ids": notes_message_ids,
                "action_items": action_items,
                "decisions_made": decisions_made,
                "status": status,
                "org_id": org_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if ended_at is not UNSET:
            field_dict["ended_at"] = ended_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meeting_instance_response_action_items_item import (
            MeetingInstanceResponseActionItemsItem,  # noqa: PLC0415
        )
        from ..models.meeting_instance_response_decisions_made_item import (
            MeetingInstanceResponseDecisionsMadeItem,  # noqa: PLC0415
        )
        from ..models.meeting_instance_response_participants_attended_item import (
            MeetingInstanceResponseParticipantsAttendedItem,  # noqa: PLC0415
        )
        from ..models.meeting_instance_response_prep_completion_status import (
            MeetingInstanceResponsePrepCompletionStatus,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        meeting_id = UUID(d.pop("meeting_id"))

        instance_date = datetime.date.fromisoformat(d.pop("instance_date"))

        participants_attended = []
        _participants_attended = d.pop("participants_attended")
        for participants_attended_item_data in _participants_attended:
            participants_attended_item = MeetingInstanceResponseParticipantsAttendedItem.from_dict(
                participants_attended_item_data
            )

            participants_attended.append(participants_attended_item)

        prep_task_ids = []
        _prep_task_ids = d.pop("prep_task_ids")
        for prep_task_ids_item_data in _prep_task_ids:
            prep_task_ids_item = UUID(prep_task_ids_item_data)

            prep_task_ids.append(prep_task_ids_item)

        prep_completion_status = MeetingInstanceResponsePrepCompletionStatus.from_dict(d.pop("prep_completion_status"))

        notes_message_ids = []
        _notes_message_ids = d.pop("notes_message_ids")
        for notes_message_ids_item_data in _notes_message_ids:
            notes_message_ids_item = UUID(notes_message_ids_item_data)

            notes_message_ids.append(notes_message_ids_item)

        action_items = []
        _action_items = d.pop("action_items")
        for action_items_item_data in _action_items:
            action_items_item = MeetingInstanceResponseActionItemsItem.from_dict(action_items_item_data)

            action_items.append(action_items_item)

        decisions_made = []
        _decisions_made = d.pop("decisions_made")
        for decisions_made_item_data in _decisions_made:
            decisions_made_item = MeetingInstanceResponseDecisionsMadeItem.from_dict(decisions_made_item_data)

            decisions_made.append(decisions_made_item)

        status = d.pop("status")

        org_id = UUID(d.pop("org_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_started_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = datetime.datetime.fromisoformat(data)

                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_ended_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_at_type_0 = datetime.datetime.fromisoformat(data)

                return ended_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        ended_at = _parse_ended_at(d.pop("ended_at", UNSET))

        meeting_instance_response = cls(
            id=id,
            meeting_id=meeting_id,
            instance_date=instance_date,
            participants_attended=participants_attended,
            prep_task_ids=prep_task_ids,
            prep_completion_status=prep_completion_status,
            notes_message_ids=notes_message_ids,
            action_items=action_items,
            decisions_made=decisions_made,
            status=status,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            started_at=started_at,
            ended_at=ended_at,
        )

        meeting_instance_response.additional_properties = d
        return meeting_instance_response

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
