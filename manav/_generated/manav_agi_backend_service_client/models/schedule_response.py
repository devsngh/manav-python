from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleResponse")


@_attrs_define
class ScheduleResponse:
    """
    Attributes:
        id (str):
        workspace_id (str):
        schedule_type (str):
        cron_expression (str):
        is_active (bool):
        created_at (datetime.datetime):
        source_id (None | str | Unset):
        last_run_at (datetime.datetime | None | Unset):
        next_run_at (datetime.datetime | None | Unset):
    """

    id: str
    workspace_id: str
    schedule_type: str
    cron_expression: str
    is_active: bool
    created_at: datetime.datetime
    source_id: None | str | Unset = UNSET
    last_run_at: datetime.datetime | None | Unset = UNSET
    next_run_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workspace_id = self.workspace_id

        schedule_type = self.schedule_type

        cron_expression = self.cron_expression

        is_active = self.is_active

        created_at = self.created_at.isoformat()

        source_id: None | str | Unset
        if isinstance(self.source_id, Unset):
            source_id = UNSET
        else:
            source_id = self.source_id

        last_run_at: None | str | Unset
        if isinstance(self.last_run_at, Unset):
            last_run_at = UNSET
        elif isinstance(self.last_run_at, datetime.datetime):
            last_run_at = self.last_run_at.isoformat()
        else:
            last_run_at = self.last_run_at

        next_run_at: None | str | Unset
        if isinstance(self.next_run_at, Unset):
            next_run_at = UNSET
        elif isinstance(self.next_run_at, datetime.datetime):
            next_run_at = self.next_run_at.isoformat()
        else:
            next_run_at = self.next_run_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "workspace_id": workspace_id,
                "schedule_type": schedule_type,
                "cron_expression": cron_expression,
                "is_active": is_active,
                "created_at": created_at,
            }
        )
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if last_run_at is not UNSET:
            field_dict["last_run_at"] = last_run_at
        if next_run_at is not UNSET:
            field_dict["next_run_at"] = next_run_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        workspace_id = d.pop("workspace_id")

        schedule_type = d.pop("schedule_type")

        cron_expression = d.pop("cron_expression")

        is_active = d.pop("is_active")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_source_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_id = _parse_source_id(d.pop("source_id", UNSET))

        def _parse_last_run_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_run_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_run_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_run_at = _parse_last_run_at(d.pop("last_run_at", UNSET))

        def _parse_next_run_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_run_at_type_0 = datetime.datetime.fromisoformat(data)

                return next_run_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_run_at = _parse_next_run_at(d.pop("next_run_at", UNSET))

        schedule_response = cls(
            id=id,
            workspace_id=workspace_id,
            schedule_type=schedule_type,
            cron_expression=cron_expression,
            is_active=is_active,
            created_at=created_at,
            source_id=source_id,
            last_run_at=last_run_at,
            next_run_at=next_run_at,
        )

        schedule_response.additional_properties = d
        return schedule_response

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
