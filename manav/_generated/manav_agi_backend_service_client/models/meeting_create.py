from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meeting_create_agenda_template import MeetingCreateAgendaTemplate
    from ..models.meeting_create_participants_optional_item import MeetingCreateParticipantsOptionalItem
    from ..models.meeting_create_participants_required_item import MeetingCreateParticipantsRequiredItem


T = TypeVar("T", bound="MeetingCreate")


@_attrs_define
class MeetingCreate:
    """
    Attributes:
        name (str):
        meeting_type (str):
        chair_id (UUID):
        group_id (UUID):
        org_id (UUID):
        description (None | str | Unset):
        chair_type (str | Unset):  Default: 'bot'.
        kind (str | Unset):  Default: 'text_thread'.
        scheduled_cron_expr (None | str | Unset):
        scheduled_next_at (datetime.datetime | None | Unset):
        duration_minutes (int | Unset):  Default: 30.
        agenda_template (MeetingCreateAgendaTemplate | Unset):
        participants_required (list[MeetingCreateParticipantsRequiredItem] | Unset):
        participants_optional (list[MeetingCreateParticipantsOptionalItem] | Unset):
        prep_lead_time_minutes (int | Unset):  Default: 0.
        prep_files_shared (bool | Unset):  Default: False.
        department_id (None | Unset | UUID):
    """

    name: str
    meeting_type: str
    chair_id: UUID
    group_id: UUID
    org_id: UUID
    description: None | str | Unset = UNSET
    chair_type: str | Unset = "bot"
    kind: str | Unset = "text_thread"
    scheduled_cron_expr: None | str | Unset = UNSET
    scheduled_next_at: datetime.datetime | None | Unset = UNSET
    duration_minutes: int | Unset = 30
    agenda_template: MeetingCreateAgendaTemplate | Unset = UNSET
    participants_required: list[MeetingCreateParticipantsRequiredItem] | Unset = UNSET
    participants_optional: list[MeetingCreateParticipantsOptionalItem] | Unset = UNSET
    prep_lead_time_minutes: int | Unset = 0
    prep_files_shared: bool | Unset = False
    department_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        meeting_type = self.meeting_type

        chair_id = str(self.chair_id)

        group_id = str(self.group_id)

        org_id = str(self.org_id)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        chair_type = self.chair_type

        kind = self.kind

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

        duration_minutes = self.duration_minutes

        agenda_template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.agenda_template, Unset):
            agenda_template = self.agenda_template.to_dict()

        participants_required: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.participants_required, Unset):
            participants_required = []
            for participants_required_item_data in self.participants_required:
                participants_required_item = participants_required_item_data.to_dict()
                participants_required.append(participants_required_item)

        participants_optional: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.participants_optional, Unset):
            participants_optional = []
            for participants_optional_item_data in self.participants_optional:
                participants_optional_item = participants_optional_item_data.to_dict()
                participants_optional.append(participants_optional_item)

        prep_lead_time_minutes = self.prep_lead_time_minutes

        prep_files_shared = self.prep_files_shared

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
                "name": name,
                "meeting_type": meeting_type,
                "chair_id": chair_id,
                "group_id": group_id,
                "org_id": org_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if chair_type is not UNSET:
            field_dict["chair_type"] = chair_type
        if kind is not UNSET:
            field_dict["kind"] = kind
        if scheduled_cron_expr is not UNSET:
            field_dict["scheduled_cron_expr"] = scheduled_cron_expr
        if scheduled_next_at is not UNSET:
            field_dict["scheduled_next_at"] = scheduled_next_at
        if duration_minutes is not UNSET:
            field_dict["duration_minutes"] = duration_minutes
        if agenda_template is not UNSET:
            field_dict["agenda_template"] = agenda_template
        if participants_required is not UNSET:
            field_dict["participants_required"] = participants_required
        if participants_optional is not UNSET:
            field_dict["participants_optional"] = participants_optional
        if prep_lead_time_minutes is not UNSET:
            field_dict["prep_lead_time_minutes"] = prep_lead_time_minutes
        if prep_files_shared is not UNSET:
            field_dict["prep_files_shared"] = prep_files_shared
        if department_id is not UNSET:
            field_dict["department_id"] = department_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meeting_create_agenda_template import MeetingCreateAgendaTemplate  # noqa: PLC0415
        from ..models.meeting_create_participants_optional_item import (
            MeetingCreateParticipantsOptionalItem,  # noqa: PLC0415
        )
        from ..models.meeting_create_participants_required_item import (
            MeetingCreateParticipantsRequiredItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        name = d.pop("name")

        meeting_type = d.pop("meeting_type")

        chair_id = UUID(d.pop("chair_id"))

        group_id = UUID(d.pop("group_id"))

        org_id = UUID(d.pop("org_id"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        chair_type = d.pop("chair_type", UNSET)

        kind = d.pop("kind", UNSET)

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

        duration_minutes = d.pop("duration_minutes", UNSET)

        _agenda_template = d.pop("agenda_template", UNSET)
        agenda_template: MeetingCreateAgendaTemplate | Unset
        if isinstance(_agenda_template, Unset):
            agenda_template = UNSET
        else:
            agenda_template = MeetingCreateAgendaTemplate.from_dict(_agenda_template)

        _participants_required = d.pop("participants_required", UNSET)
        participants_required: list[MeetingCreateParticipantsRequiredItem] | Unset = UNSET
        if _participants_required is not UNSET:
            participants_required = []
            for participants_required_item_data in _participants_required:
                participants_required_item = MeetingCreateParticipantsRequiredItem.from_dict(
                    participants_required_item_data
                )

                participants_required.append(participants_required_item)

        _participants_optional = d.pop("participants_optional", UNSET)
        participants_optional: list[MeetingCreateParticipantsOptionalItem] | Unset = UNSET
        if _participants_optional is not UNSET:
            participants_optional = []
            for participants_optional_item_data in _participants_optional:
                participants_optional_item = MeetingCreateParticipantsOptionalItem.from_dict(
                    participants_optional_item_data
                )

                participants_optional.append(participants_optional_item)

        prep_lead_time_minutes = d.pop("prep_lead_time_minutes", UNSET)

        prep_files_shared = d.pop("prep_files_shared", UNSET)

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

        meeting_create = cls(
            name=name,
            meeting_type=meeting_type,
            chair_id=chair_id,
            group_id=group_id,
            org_id=org_id,
            description=description,
            chair_type=chair_type,
            kind=kind,
            scheduled_cron_expr=scheduled_cron_expr,
            scheduled_next_at=scheduled_next_at,
            duration_minutes=duration_minutes,
            agenda_template=agenda_template,
            participants_required=participants_required,
            participants_optional=participants_optional,
            prep_lead_time_minutes=prep_lead_time_minutes,
            prep_files_shared=prep_files_shared,
            department_id=department_id,
        )

        meeting_create.additional_properties = d
        return meeting_create

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
