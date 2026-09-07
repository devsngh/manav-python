from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meeting_instance_update_action_items_type_0_item import MeetingInstanceUpdateActionItemsType0Item
    from ..models.meeting_instance_update_decisions_made_type_0_item import MeetingInstanceUpdateDecisionsMadeType0Item
    from ..models.meeting_instance_update_participants_attended_type_0_item import (
        MeetingInstanceUpdateParticipantsAttendedType0Item,
    )
    from ..models.meeting_instance_update_prep_completion_status_type_0 import (
        MeetingInstanceUpdatePrepCompletionStatusType0,
    )


T = TypeVar("T", bound="MeetingInstanceUpdate")


@_attrs_define
class MeetingInstanceUpdate:
    """Patch — set any subset of fields.

    Attributes:
        started_at (datetime.datetime | None | Unset):
        ended_at (datetime.datetime | None | Unset):
        participants_attended (list[MeetingInstanceUpdateParticipantsAttendedType0Item] | None | Unset):
        prep_task_ids (list[UUID] | None | Unset):
        prep_completion_status (MeetingInstanceUpdatePrepCompletionStatusType0 | None | Unset):
        notes_message_ids (list[UUID] | None | Unset):
        action_items (list[MeetingInstanceUpdateActionItemsType0Item] | None | Unset):
        decisions_made (list[MeetingInstanceUpdateDecisionsMadeType0Item] | None | Unset):
        status (None | str | Unset):
    """

    started_at: datetime.datetime | None | Unset = UNSET
    ended_at: datetime.datetime | None | Unset = UNSET
    participants_attended: list[MeetingInstanceUpdateParticipantsAttendedType0Item] | None | Unset = UNSET
    prep_task_ids: list[UUID] | None | Unset = UNSET
    prep_completion_status: MeetingInstanceUpdatePrepCompletionStatusType0 | None | Unset = UNSET
    notes_message_ids: list[UUID] | None | Unset = UNSET
    action_items: list[MeetingInstanceUpdateActionItemsType0Item] | None | Unset = UNSET
    decisions_made: list[MeetingInstanceUpdateDecisionsMadeType0Item] | None | Unset = UNSET
    status: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.meeting_instance_update_prep_completion_status_type_0 import (
            MeetingInstanceUpdatePrepCompletionStatusType0,  # noqa: PLC0415
        )

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

        participants_attended: list[dict[str, Any]] | None | Unset
        if isinstance(self.participants_attended, Unset):
            participants_attended = UNSET
        elif isinstance(self.participants_attended, list):
            participants_attended = []
            for participants_attended_type_0_item_data in self.participants_attended:
                participants_attended_type_0_item = participants_attended_type_0_item_data.to_dict()
                participants_attended.append(participants_attended_type_0_item)

        else:
            participants_attended = self.participants_attended

        prep_task_ids: list[str] | None | Unset
        if isinstance(self.prep_task_ids, Unset):
            prep_task_ids = UNSET
        elif isinstance(self.prep_task_ids, list):
            prep_task_ids = []
            for prep_task_ids_type_0_item_data in self.prep_task_ids:
                prep_task_ids_type_0_item = str(prep_task_ids_type_0_item_data)
                prep_task_ids.append(prep_task_ids_type_0_item)

        else:
            prep_task_ids = self.prep_task_ids

        prep_completion_status: dict[str, Any] | None | Unset
        if isinstance(self.prep_completion_status, Unset):
            prep_completion_status = UNSET
        elif isinstance(self.prep_completion_status, MeetingInstanceUpdatePrepCompletionStatusType0):
            prep_completion_status = self.prep_completion_status.to_dict()
        else:
            prep_completion_status = self.prep_completion_status

        notes_message_ids: list[str] | None | Unset
        if isinstance(self.notes_message_ids, Unset):
            notes_message_ids = UNSET
        elif isinstance(self.notes_message_ids, list):
            notes_message_ids = []
            for notes_message_ids_type_0_item_data in self.notes_message_ids:
                notes_message_ids_type_0_item = str(notes_message_ids_type_0_item_data)
                notes_message_ids.append(notes_message_ids_type_0_item)

        else:
            notes_message_ids = self.notes_message_ids

        action_items: list[dict[str, Any]] | None | Unset
        if isinstance(self.action_items, Unset):
            action_items = UNSET
        elif isinstance(self.action_items, list):
            action_items = []
            for action_items_type_0_item_data in self.action_items:
                action_items_type_0_item = action_items_type_0_item_data.to_dict()
                action_items.append(action_items_type_0_item)

        else:
            action_items = self.action_items

        decisions_made: list[dict[str, Any]] | None | Unset
        if isinstance(self.decisions_made, Unset):
            decisions_made = UNSET
        elif isinstance(self.decisions_made, list):
            decisions_made = []
            for decisions_made_type_0_item_data in self.decisions_made:
                decisions_made_type_0_item = decisions_made_type_0_item_data.to_dict()
                decisions_made.append(decisions_made_type_0_item)

        else:
            decisions_made = self.decisions_made

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if ended_at is not UNSET:
            field_dict["ended_at"] = ended_at
        if participants_attended is not UNSET:
            field_dict["participants_attended"] = participants_attended
        if prep_task_ids is not UNSET:
            field_dict["prep_task_ids"] = prep_task_ids
        if prep_completion_status is not UNSET:
            field_dict["prep_completion_status"] = prep_completion_status
        if notes_message_ids is not UNSET:
            field_dict["notes_message_ids"] = notes_message_ids
        if action_items is not UNSET:
            field_dict["action_items"] = action_items
        if decisions_made is not UNSET:
            field_dict["decisions_made"] = decisions_made
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meeting_instance_update_action_items_type_0_item import (
            MeetingInstanceUpdateActionItemsType0Item,  # noqa: PLC0415
        )
        from ..models.meeting_instance_update_decisions_made_type_0_item import (
            MeetingInstanceUpdateDecisionsMadeType0Item,  # noqa: PLC0415
        )
        from ..models.meeting_instance_update_participants_attended_type_0_item import (
            MeetingInstanceUpdateParticipantsAttendedType0Item,  # noqa: PLC0415
        )
        from ..models.meeting_instance_update_prep_completion_status_type_0 import (
            MeetingInstanceUpdatePrepCompletionStatusType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

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

        def _parse_participants_attended(
            data: object,
        ) -> list[MeetingInstanceUpdateParticipantsAttendedType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                participants_attended_type_0 = []
                _participants_attended_type_0 = data
                for participants_attended_type_0_item_data in _participants_attended_type_0:
                    participants_attended_type_0_item = MeetingInstanceUpdateParticipantsAttendedType0Item.from_dict(
                        participants_attended_type_0_item_data
                    )

                    participants_attended_type_0.append(participants_attended_type_0_item)

                return participants_attended_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MeetingInstanceUpdateParticipantsAttendedType0Item] | None | Unset, data)

        participants_attended = _parse_participants_attended(d.pop("participants_attended", UNSET))

        def _parse_prep_task_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                prep_task_ids_type_0 = []
                _prep_task_ids_type_0 = data
                for prep_task_ids_type_0_item_data in _prep_task_ids_type_0:
                    prep_task_ids_type_0_item = UUID(prep_task_ids_type_0_item_data)

                    prep_task_ids_type_0.append(prep_task_ids_type_0_item)

                return prep_task_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        prep_task_ids = _parse_prep_task_ids(d.pop("prep_task_ids", UNSET))

        def _parse_prep_completion_status(
            data: object,
        ) -> MeetingInstanceUpdatePrepCompletionStatusType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                prep_completion_status_type_0 = MeetingInstanceUpdatePrepCompletionStatusType0.from_dict(data)

                return prep_completion_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MeetingInstanceUpdatePrepCompletionStatusType0 | None | Unset, data)

        prep_completion_status = _parse_prep_completion_status(d.pop("prep_completion_status", UNSET))

        def _parse_notes_message_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                notes_message_ids_type_0 = []
                _notes_message_ids_type_0 = data
                for notes_message_ids_type_0_item_data in _notes_message_ids_type_0:
                    notes_message_ids_type_0_item = UUID(notes_message_ids_type_0_item_data)

                    notes_message_ids_type_0.append(notes_message_ids_type_0_item)

                return notes_message_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        notes_message_ids = _parse_notes_message_ids(d.pop("notes_message_ids", UNSET))

        def _parse_action_items(data: object) -> list[MeetingInstanceUpdateActionItemsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                action_items_type_0 = []
                _action_items_type_0 = data
                for action_items_type_0_item_data in _action_items_type_0:
                    action_items_type_0_item = MeetingInstanceUpdateActionItemsType0Item.from_dict(
                        action_items_type_0_item_data
                    )

                    action_items_type_0.append(action_items_type_0_item)

                return action_items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MeetingInstanceUpdateActionItemsType0Item] | None | Unset, data)

        action_items = _parse_action_items(d.pop("action_items", UNSET))

        def _parse_decisions_made(data: object) -> list[MeetingInstanceUpdateDecisionsMadeType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                decisions_made_type_0 = []
                _decisions_made_type_0 = data
                for decisions_made_type_0_item_data in _decisions_made_type_0:
                    decisions_made_type_0_item = MeetingInstanceUpdateDecisionsMadeType0Item.from_dict(
                        decisions_made_type_0_item_data
                    )

                    decisions_made_type_0.append(decisions_made_type_0_item)

                return decisions_made_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MeetingInstanceUpdateDecisionsMadeType0Item] | None | Unset, data)

        decisions_made = _parse_decisions_made(d.pop("decisions_made", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        meeting_instance_update = cls(
            started_at=started_at,
            ended_at=ended_at,
            participants_attended=participants_attended,
            prep_task_ids=prep_task_ids,
            prep_completion_status=prep_completion_status,
            notes_message_ids=notes_message_ids,
            action_items=action_items,
            decisions_made=decisions_made,
            status=status,
        )

        meeting_instance_update.additional_properties = d
        return meeting_instance_update

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
