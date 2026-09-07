from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meeting_instance_create_participants_attended_item import (
        MeetingInstanceCreateParticipantsAttendedItem,
    )
    from ..models.meeting_instance_create_prep_completion_status import MeetingInstanceCreatePrepCompletionStatus


T = TypeVar("T", bound="MeetingInstanceCreate")


@_attrs_define
class MeetingInstanceCreate:
    """
    Attributes:
        meeting_id (UUID):
        instance_date (datetime.date):
        org_id (UUID):
        started_at (datetime.datetime | None | Unset):
        participants_attended (list[MeetingInstanceCreateParticipantsAttendedItem] | Unset):
        prep_task_ids (list[UUID] | Unset):
        prep_completion_status (MeetingInstanceCreatePrepCompletionStatus | Unset):
    """

    meeting_id: UUID
    instance_date: datetime.date
    org_id: UUID
    started_at: datetime.datetime | None | Unset = UNSET
    participants_attended: list[MeetingInstanceCreateParticipantsAttendedItem] | Unset = UNSET
    prep_task_ids: list[UUID] | Unset = UNSET
    prep_completion_status: MeetingInstanceCreatePrepCompletionStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meeting_id = str(self.meeting_id)

        instance_date = self.instance_date.isoformat()

        org_id = str(self.org_id)

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        participants_attended: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.participants_attended, Unset):
            participants_attended = []
            for participants_attended_item_data in self.participants_attended:
                participants_attended_item = participants_attended_item_data.to_dict()
                participants_attended.append(participants_attended_item)

        prep_task_ids: list[str] | Unset = UNSET
        if not isinstance(self.prep_task_ids, Unset):
            prep_task_ids = []
            for prep_task_ids_item_data in self.prep_task_ids:
                prep_task_ids_item = str(prep_task_ids_item_data)
                prep_task_ids.append(prep_task_ids_item)

        prep_completion_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prep_completion_status, Unset):
            prep_completion_status = self.prep_completion_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meeting_id": meeting_id,
                "instance_date": instance_date,
                "org_id": org_id,
            }
        )
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if participants_attended is not UNSET:
            field_dict["participants_attended"] = participants_attended
        if prep_task_ids is not UNSET:
            field_dict["prep_task_ids"] = prep_task_ids
        if prep_completion_status is not UNSET:
            field_dict["prep_completion_status"] = prep_completion_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meeting_instance_create_participants_attended_item import (
            MeetingInstanceCreateParticipantsAttendedItem,  # noqa: PLC0415
        )
        from ..models.meeting_instance_create_prep_completion_status import (
            MeetingInstanceCreatePrepCompletionStatus,  # noqa: PLC0415
        )

        d = dict(src_dict)
        meeting_id = UUID(d.pop("meeting_id"))

        instance_date = datetime.date.fromisoformat(d.pop("instance_date"))

        org_id = UUID(d.pop("org_id"))

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

        _participants_attended = d.pop("participants_attended", UNSET)
        participants_attended: list[MeetingInstanceCreateParticipantsAttendedItem] | Unset = UNSET
        if _participants_attended is not UNSET:
            participants_attended = []
            for participants_attended_item_data in _participants_attended:
                participants_attended_item = MeetingInstanceCreateParticipantsAttendedItem.from_dict(
                    participants_attended_item_data
                )

                participants_attended.append(participants_attended_item)

        _prep_task_ids = d.pop("prep_task_ids", UNSET)
        prep_task_ids: list[UUID] | Unset = UNSET
        if _prep_task_ids is not UNSET:
            prep_task_ids = []
            for prep_task_ids_item_data in _prep_task_ids:
                prep_task_ids_item = UUID(prep_task_ids_item_data)

                prep_task_ids.append(prep_task_ids_item)

        _prep_completion_status = d.pop("prep_completion_status", UNSET)
        prep_completion_status: MeetingInstanceCreatePrepCompletionStatus | Unset
        if isinstance(_prep_completion_status, Unset):
            prep_completion_status = UNSET
        else:
            prep_completion_status = MeetingInstanceCreatePrepCompletionStatus.from_dict(_prep_completion_status)

        meeting_instance_create = cls(
            meeting_id=meeting_id,
            instance_date=instance_date,
            org_id=org_id,
            started_at=started_at,
            participants_attended=participants_attended,
            prep_task_ids=prep_task_ids,
            prep_completion_status=prep_completion_status,
        )

        meeting_instance_create.additional_properties = d
        return meeting_instance_create

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
