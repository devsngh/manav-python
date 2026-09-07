from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transition_row_identity_card_type_0 import TransitionRowIdentityCardType0
    from ..models.transition_row_other_mode_snapshot_type_0 import TransitionRowOtherModeSnapshotType0
    from ..models.transition_row_time_context_type_0 import TransitionRowTimeContextType0


T = TypeVar("T", bound="TransitionRow")


@_attrs_define
class TransitionRow:
    """One row from agent_mode_transitions — the 7-item backpack + meta.

    Attributes:
        id (str):
        from_mode (str):
        to_mode (str):
        transitioned_at (datetime.datetime):
        duration_in_from_mode_seconds (int | None | Unset):
        identity_card (None | TransitionRowIdentityCardType0 | Unset):
        bookmark (None | str | Unset):
        residual_mood (None | str | Unset):
        todo_for_entering_mode (Any | None | Unset):
        time_context (None | TransitionRowTimeContextType0 | Unset):
        open_loops (Any | None | Unset):
        other_mode_snapshot (None | TransitionRowOtherModeSnapshotType0 | Unset):
    """

    id: str
    from_mode: str
    to_mode: str
    transitioned_at: datetime.datetime
    duration_in_from_mode_seconds: int | None | Unset = UNSET
    identity_card: None | TransitionRowIdentityCardType0 | Unset = UNSET
    bookmark: None | str | Unset = UNSET
    residual_mood: None | str | Unset = UNSET
    todo_for_entering_mode: Any | None | Unset = UNSET
    time_context: None | TransitionRowTimeContextType0 | Unset = UNSET
    open_loops: Any | None | Unset = UNSET
    other_mode_snapshot: None | TransitionRowOtherModeSnapshotType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.transition_row_identity_card_type_0 import TransitionRowIdentityCardType0  # noqa: PLC0415
        from ..models.transition_row_other_mode_snapshot_type_0 import (
            TransitionRowOtherModeSnapshotType0,  # noqa: PLC0415
        )
        from ..models.transition_row_time_context_type_0 import TransitionRowTimeContextType0  # noqa: PLC0415

        id = self.id

        from_mode = self.from_mode

        to_mode = self.to_mode

        transitioned_at = self.transitioned_at.isoformat()

        duration_in_from_mode_seconds: int | None | Unset
        if isinstance(self.duration_in_from_mode_seconds, Unset):
            duration_in_from_mode_seconds = UNSET
        else:
            duration_in_from_mode_seconds = self.duration_in_from_mode_seconds

        identity_card: dict[str, Any] | None | Unset
        if isinstance(self.identity_card, Unset):
            identity_card = UNSET
        elif isinstance(self.identity_card, TransitionRowIdentityCardType0):
            identity_card = self.identity_card.to_dict()
        else:
            identity_card = self.identity_card

        bookmark: None | str | Unset
        if isinstance(self.bookmark, Unset):
            bookmark = UNSET
        else:
            bookmark = self.bookmark

        residual_mood: None | str | Unset
        if isinstance(self.residual_mood, Unset):
            residual_mood = UNSET
        else:
            residual_mood = self.residual_mood

        todo_for_entering_mode: Any | None | Unset
        if isinstance(self.todo_for_entering_mode, Unset):
            todo_for_entering_mode = UNSET
        else:
            todo_for_entering_mode = self.todo_for_entering_mode

        time_context: dict[str, Any] | None | Unset
        if isinstance(self.time_context, Unset):
            time_context = UNSET
        elif isinstance(self.time_context, TransitionRowTimeContextType0):
            time_context = self.time_context.to_dict()
        else:
            time_context = self.time_context

        open_loops: Any | None | Unset
        if isinstance(self.open_loops, Unset):
            open_loops = UNSET
        else:
            open_loops = self.open_loops

        other_mode_snapshot: dict[str, Any] | None | Unset
        if isinstance(self.other_mode_snapshot, Unset):
            other_mode_snapshot = UNSET
        elif isinstance(self.other_mode_snapshot, TransitionRowOtherModeSnapshotType0):
            other_mode_snapshot = self.other_mode_snapshot.to_dict()
        else:
            other_mode_snapshot = self.other_mode_snapshot

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "from_mode": from_mode,
                "to_mode": to_mode,
                "transitioned_at": transitioned_at,
            }
        )
        if duration_in_from_mode_seconds is not UNSET:
            field_dict["duration_in_from_mode_seconds"] = duration_in_from_mode_seconds
        if identity_card is not UNSET:
            field_dict["identity_card"] = identity_card
        if bookmark is not UNSET:
            field_dict["bookmark"] = bookmark
        if residual_mood is not UNSET:
            field_dict["residual_mood"] = residual_mood
        if todo_for_entering_mode is not UNSET:
            field_dict["todo_for_entering_mode"] = todo_for_entering_mode
        if time_context is not UNSET:
            field_dict["time_context"] = time_context
        if open_loops is not UNSET:
            field_dict["open_loops"] = open_loops
        if other_mode_snapshot is not UNSET:
            field_dict["other_mode_snapshot"] = other_mode_snapshot

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transition_row_identity_card_type_0 import TransitionRowIdentityCardType0  # noqa: PLC0415
        from ..models.transition_row_other_mode_snapshot_type_0 import (
            TransitionRowOtherModeSnapshotType0,  # noqa: PLC0415
        )
        from ..models.transition_row_time_context_type_0 import TransitionRowTimeContextType0  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        from_mode = d.pop("from_mode")

        to_mode = d.pop("to_mode")

        transitioned_at = datetime.datetime.fromisoformat(d.pop("transitioned_at"))

        def _parse_duration_in_from_mode_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_in_from_mode_seconds = _parse_duration_in_from_mode_seconds(
            d.pop("duration_in_from_mode_seconds", UNSET)
        )

        def _parse_identity_card(data: object) -> None | TransitionRowIdentityCardType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                identity_card_type_0 = TransitionRowIdentityCardType0.from_dict(data)

                return identity_card_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransitionRowIdentityCardType0 | Unset, data)

        identity_card = _parse_identity_card(d.pop("identity_card", UNSET))

        def _parse_bookmark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bookmark = _parse_bookmark(d.pop("bookmark", UNSET))

        def _parse_residual_mood(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        residual_mood = _parse_residual_mood(d.pop("residual_mood", UNSET))

        def _parse_todo_for_entering_mode(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        todo_for_entering_mode = _parse_todo_for_entering_mode(d.pop("todo_for_entering_mode", UNSET))

        def _parse_time_context(data: object) -> None | TransitionRowTimeContextType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_context_type_0 = TransitionRowTimeContextType0.from_dict(data)

                return time_context_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransitionRowTimeContextType0 | Unset, data)

        time_context = _parse_time_context(d.pop("time_context", UNSET))

        def _parse_open_loops(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        open_loops = _parse_open_loops(d.pop("open_loops", UNSET))

        def _parse_other_mode_snapshot(data: object) -> None | TransitionRowOtherModeSnapshotType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                other_mode_snapshot_type_0 = TransitionRowOtherModeSnapshotType0.from_dict(data)

                return other_mode_snapshot_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransitionRowOtherModeSnapshotType0 | Unset, data)

        other_mode_snapshot = _parse_other_mode_snapshot(d.pop("other_mode_snapshot", UNSET))

        transition_row = cls(
            id=id,
            from_mode=from_mode,
            to_mode=to_mode,
            transitioned_at=transitioned_at,
            duration_in_from_mode_seconds=duration_in_from_mode_seconds,
            identity_card=identity_card,
            bookmark=bookmark,
            residual_mood=residual_mood,
            todo_for_entering_mode=todo_for_entering_mode,
            time_context=time_context,
            open_loops=open_loops,
            other_mode_snapshot=other_mode_snapshot,
        )

        transition_row.additional_properties = d
        return transition_row

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
