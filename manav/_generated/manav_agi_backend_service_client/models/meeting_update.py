from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meeting_update_agenda_template_type_0 import MeetingUpdateAgendaTemplateType0
    from ..models.meeting_update_participants_optional_type_0_item import MeetingUpdateParticipantsOptionalType0Item
    from ..models.meeting_update_participants_required_type_0_item import MeetingUpdateParticipantsRequiredType0Item


T = TypeVar("T", bound="MeetingUpdate")


@_attrs_define
class MeetingUpdate:
    """
    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        scheduled_cron_expr (None | str | Unset):
        scheduled_next_at (datetime.datetime | None | Unset):
        duration_minutes (int | None | Unset):
        agenda_template (MeetingUpdateAgendaTemplateType0 | None | Unset):
        participants_required (list[MeetingUpdateParticipantsRequiredType0Item] | None | Unset):
        participants_optional (list[MeetingUpdateParticipantsOptionalType0Item] | None | Unset):
        prep_lead_time_minutes (int | None | Unset):
        prep_files_shared (bool | None | Unset):
        is_active (bool | None | Unset):
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    scheduled_cron_expr: None | str | Unset = UNSET
    scheduled_next_at: datetime.datetime | None | Unset = UNSET
    duration_minutes: int | None | Unset = UNSET
    agenda_template: MeetingUpdateAgendaTemplateType0 | None | Unset = UNSET
    participants_required: list[MeetingUpdateParticipantsRequiredType0Item] | None | Unset = UNSET
    participants_optional: list[MeetingUpdateParticipantsOptionalType0Item] | None | Unset = UNSET
    prep_lead_time_minutes: int | None | Unset = UNSET
    prep_files_shared: bool | None | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.meeting_update_agenda_template_type_0 import MeetingUpdateAgendaTemplateType0  # noqa: PLC0415

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

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

        duration_minutes: int | None | Unset
        if isinstance(self.duration_minutes, Unset):
            duration_minutes = UNSET
        else:
            duration_minutes = self.duration_minutes

        agenda_template: dict[str, Any] | None | Unset
        if isinstance(self.agenda_template, Unset):
            agenda_template = UNSET
        elif isinstance(self.agenda_template, MeetingUpdateAgendaTemplateType0):
            agenda_template = self.agenda_template.to_dict()
        else:
            agenda_template = self.agenda_template

        participants_required: list[dict[str, Any]] | None | Unset
        if isinstance(self.participants_required, Unset):
            participants_required = UNSET
        elif isinstance(self.participants_required, list):
            participants_required = []
            for participants_required_type_0_item_data in self.participants_required:
                participants_required_type_0_item = participants_required_type_0_item_data.to_dict()
                participants_required.append(participants_required_type_0_item)

        else:
            participants_required = self.participants_required

        participants_optional: list[dict[str, Any]] | None | Unset
        if isinstance(self.participants_optional, Unset):
            participants_optional = UNSET
        elif isinstance(self.participants_optional, list):
            participants_optional = []
            for participants_optional_type_0_item_data in self.participants_optional:
                participants_optional_type_0_item = participants_optional_type_0_item_data.to_dict()
                participants_optional.append(participants_optional_type_0_item)

        else:
            participants_optional = self.participants_optional

        prep_lead_time_minutes: int | None | Unset
        if isinstance(self.prep_lead_time_minutes, Unset):
            prep_lead_time_minutes = UNSET
        else:
            prep_lead_time_minutes = self.prep_lead_time_minutes

        prep_files_shared: bool | None | Unset
        if isinstance(self.prep_files_shared, Unset):
            prep_files_shared = UNSET
        else:
            prep_files_shared = self.prep_files_shared

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
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
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meeting_update_agenda_template_type_0 import MeetingUpdateAgendaTemplateType0  # noqa: PLC0415
        from ..models.meeting_update_participants_optional_type_0_item import (
            MeetingUpdateParticipantsOptionalType0Item,  # noqa: PLC0415
        )
        from ..models.meeting_update_participants_required_type_0_item import (
            MeetingUpdateParticipantsRequiredType0Item,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

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

        def _parse_duration_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_minutes = _parse_duration_minutes(d.pop("duration_minutes", UNSET))

        def _parse_agenda_template(data: object) -> MeetingUpdateAgendaTemplateType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                agenda_template_type_0 = MeetingUpdateAgendaTemplateType0.from_dict(data)

                return agenda_template_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MeetingUpdateAgendaTemplateType0 | None | Unset, data)

        agenda_template = _parse_agenda_template(d.pop("agenda_template", UNSET))

        def _parse_participants_required(
            data: object,
        ) -> list[MeetingUpdateParticipantsRequiredType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                participants_required_type_0 = []
                _participants_required_type_0 = data
                for participants_required_type_0_item_data in _participants_required_type_0:
                    participants_required_type_0_item = MeetingUpdateParticipantsRequiredType0Item.from_dict(
                        participants_required_type_0_item_data
                    )

                    participants_required_type_0.append(participants_required_type_0_item)

                return participants_required_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MeetingUpdateParticipantsRequiredType0Item] | None | Unset, data)

        participants_required = _parse_participants_required(d.pop("participants_required", UNSET))

        def _parse_participants_optional(
            data: object,
        ) -> list[MeetingUpdateParticipantsOptionalType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                participants_optional_type_0 = []
                _participants_optional_type_0 = data
                for participants_optional_type_0_item_data in _participants_optional_type_0:
                    participants_optional_type_0_item = MeetingUpdateParticipantsOptionalType0Item.from_dict(
                        participants_optional_type_0_item_data
                    )

                    participants_optional_type_0.append(participants_optional_type_0_item)

                return participants_optional_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MeetingUpdateParticipantsOptionalType0Item] | None | Unset, data)

        participants_optional = _parse_participants_optional(d.pop("participants_optional", UNSET))

        def _parse_prep_lead_time_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        prep_lead_time_minutes = _parse_prep_lead_time_minutes(d.pop("prep_lead_time_minutes", UNSET))

        def _parse_prep_files_shared(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        prep_files_shared = _parse_prep_files_shared(d.pop("prep_files_shared", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        meeting_update = cls(
            name=name,
            description=description,
            scheduled_cron_expr=scheduled_cron_expr,
            scheduled_next_at=scheduled_next_at,
            duration_minutes=duration_minutes,
            agenda_template=agenda_template,
            participants_required=participants_required,
            participants_optional=participants_optional,
            prep_lead_time_minutes=prep_lead_time_minutes,
            prep_files_shared=prep_files_shared,
            is_active=is_active,
        )

        meeting_update.additional_properties = d
        return meeting_update

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
