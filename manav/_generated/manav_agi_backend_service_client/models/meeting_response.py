from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meeting_response_agenda_template import MeetingResponseAgendaTemplate
    from ..models.meeting_response_participants_optional_item import MeetingResponseParticipantsOptionalItem
    from ..models.meeting_response_participants_required_item import MeetingResponseParticipantsRequiredItem


T = TypeVar("T", bound="MeetingResponse")


@_attrs_define
class MeetingResponse:
    """
    Attributes:
        id (UUID):
        name (str):
        meeting_type (str):
        chair_id (UUID):
        chair_type (str):
        group_id (UUID):
        kind (str):
        duration_minutes (int):
        agenda_template (MeetingResponseAgendaTemplate):
        participants_required (list[MeetingResponseParticipantsRequiredItem]):
        participants_optional (list[MeetingResponseParticipantsOptionalItem]):
        prep_lead_time_minutes (int):
        prep_files_shared (bool):
        org_id (UUID):
        is_active (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        description (None | str | Unset):
        scheduled_cron_expr (None | str | Unset):
        scheduled_next_at (datetime.datetime | None | Unset):
        department_id (None | Unset | UUID):
    """

    id: UUID
    name: str
    meeting_type: str
    chair_id: UUID
    chair_type: str
    group_id: UUID
    kind: str
    duration_minutes: int
    agenda_template: MeetingResponseAgendaTemplate
    participants_required: list[MeetingResponseParticipantsRequiredItem]
    participants_optional: list[MeetingResponseParticipantsOptionalItem]
    prep_lead_time_minutes: int
    prep_files_shared: bool
    org_id: UUID
    is_active: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: None | str | Unset = UNSET
    scheduled_cron_expr: None | str | Unset = UNSET
    scheduled_next_at: datetime.datetime | None | Unset = UNSET
    department_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        meeting_type = self.meeting_type

        chair_id = str(self.chair_id)

        chair_type = self.chair_type

        group_id = str(self.group_id)

        kind = self.kind

        duration_minutes = self.duration_minutes

        agenda_template = self.agenda_template.to_dict()

        participants_required = []
        for participants_required_item_data in self.participants_required:
            participants_required_item = participants_required_item_data.to_dict()
            participants_required.append(participants_required_item)

        participants_optional = []
        for participants_optional_item_data in self.participants_optional:
            participants_optional_item = participants_optional_item_data.to_dict()
            participants_optional.append(participants_optional_item)

        prep_lead_time_minutes = self.prep_lead_time_minutes

        prep_files_shared = self.prep_files_shared

        org_id = str(self.org_id)

        is_active = self.is_active

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        scheduled_cron_expr: None | str | Unset
        if isinstance(self.scheduled_cron_expr, Unset):
            scheduled_cron_expr = UNSET
        else:
            scheduled_cron_expr = self.scheduled_cron_expr

        scheduled_next_at: None | str | Unset
        if isinstance(self.scheduled_next_at, Unset):
            scheduled_next_at = UNSET
        elif isinstance(self.scheduled_next_at, datetime.datetime):
            scheduled_next_at = self.scheduled_next_at.isoformat()
        else:
            scheduled_next_at = self.scheduled_next_at

        department_id: None | str | Unset
        if isinstance(self.department_id, Unset):
            department_id = UNSET
        elif isinstance(self.department_id, UUID):
            department_id = str(self.department_id)
        else:
            department_id = self.department_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "meeting_type": meeting_type,
                "chair_id": chair_id,
                "chair_type": chair_type,
                "group_id": group_id,
                "kind": kind,
                "duration_minutes": duration_minutes,
                "agenda_template": agenda_template,
                "participants_required": participants_required,
                "participants_optional": participants_optional,
                "prep_lead_time_minutes": prep_lead_time_minutes,
                "prep_files_shared": prep_files_shared,
                "org_id": org_id,
                "is_active": is_active,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if scheduled_cron_expr is not UNSET:
            field_dict["scheduled_cron_expr"] = scheduled_cron_expr
        if scheduled_next_at is not UNSET:
            field_dict["scheduled_next_at"] = scheduled_next_at
        if department_id is not UNSET:
            field_dict["department_id"] = department_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meeting_response_agenda_template import MeetingResponseAgendaTemplate  # noqa: PLC0415
        from ..models.meeting_response_participants_optional_item import (
            MeetingResponseParticipantsOptionalItem,  # noqa: PLC0415
        )
        from ..models.meeting_response_participants_required_item import (
            MeetingResponseParticipantsRequiredItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        meeting_type = d.pop("meeting_type")

        chair_id = UUID(d.pop("chair_id"))

        chair_type = d.pop("chair_type")

        group_id = UUID(d.pop("group_id"))

        kind = d.pop("kind")

        duration_minutes = d.pop("duration_minutes")

        agenda_template = MeetingResponseAgendaTemplate.from_dict(d.pop("agenda_template"))

        participants_required = []
        _participants_required = d.pop("participants_required")
        for participants_required_item_data in _participants_required:
            participants_required_item = MeetingResponseParticipantsRequiredItem.from_dict(
                participants_required_item_data
            )

            participants_required.append(participants_required_item)

        participants_optional = []
        _participants_optional = d.pop("participants_optional")
        for participants_optional_item_data in _participants_optional:
            participants_optional_item = MeetingResponseParticipantsOptionalItem.from_dict(
                participants_optional_item_data
            )

            participants_optional.append(participants_optional_item)

        prep_lead_time_minutes = d.pop("prep_lead_time_minutes")

        prep_files_shared = d.pop("prep_files_shared")

        org_id = UUID(d.pop("org_id"))

        is_active = d.pop("is_active")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_scheduled_cron_expr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scheduled_cron_expr = _parse_scheduled_cron_expr(d.pop("scheduled_cron_expr", UNSET))

        def _parse_scheduled_next_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_next_at_type_0 = datetime.datetime.fromisoformat(data)

                return scheduled_next_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        scheduled_next_at = _parse_scheduled_next_at(d.pop("scheduled_next_at", UNSET))

        def _parse_department_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                department_id_type_0 = UUID(data)

                return department_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        department_id = _parse_department_id(d.pop("department_id", UNSET))

        meeting_response = cls(
            id=id,
            name=name,
            meeting_type=meeting_type,
            chair_id=chair_id,
            chair_type=chair_type,
            group_id=group_id,
            kind=kind,
            duration_minutes=duration_minutes,
            agenda_template=agenda_template,
            participants_required=participants_required,
            participants_optional=participants_optional,
            prep_lead_time_minutes=prep_lead_time_minutes,
            prep_files_shared=prep_files_shared,
            org_id=org_id,
            is_active=is_active,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            scheduled_cron_expr=scheduled_cron_expr,
            scheduled_next_at=scheduled_next_at,
            department_id=department_id,
        )

        meeting_response.additional_properties = d
        return meeting_response

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
