from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobResponse")


@_attrs_define
class JobResponse:
    """
    Attributes:
        id (str):
        workspace_id (str):
        trigger (str):
        status (str):
        objects_extracted (int):
        objects_enriched (int):
        objects_written (int):
        failed_objects (int):
        created_at (datetime.datetime):
        source_id (None | str | Unset):
        bot_id (None | str | Unset):
        error_message (None | str | Unset):
        started_at (datetime.datetime | None | Unset):
        completed_at (datetime.datetime | None | Unset):
    """

    id: str
    workspace_id: str
    trigger: str
    status: str
    objects_extracted: int
    objects_enriched: int
    objects_written: int
    failed_objects: int
    created_at: datetime.datetime
    source_id: None | str | Unset = UNSET
    bot_id: None | str | Unset = UNSET
    error_message: None | str | Unset = UNSET
    started_at: datetime.datetime | None | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workspace_id = self.workspace_id

        trigger = self.trigger

        status = self.status

        objects_extracted = self.objects_extracted

        objects_enriched = self.objects_enriched

        objects_written = self.objects_written

        failed_objects = self.failed_objects

        created_at = self.created_at.isoformat()

        source_id: None | str | Unset
        if isinstance(self.source_id, Unset):
            source_id = UNSET
        else:
            source_id = self.source_id

        bot_id: None | str | Unset
        if isinstance(self.bot_id, Unset):
            bot_id = UNSET
        else:
            bot_id = self.bot_id

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "workspace_id": workspace_id,
                "trigger": trigger,
                "status": status,
                "objects_extracted": objects_extracted,
                "objects_enriched": objects_enriched,
                "objects_written": objects_written,
                "failed_objects": failed_objects,
                "created_at": created_at,
            }
        )
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if bot_id is not UNSET:
            field_dict["bot_id"] = bot_id
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        workspace_id = d.pop("workspace_id")

        trigger = d.pop("trigger")

        status = d.pop("status")

        objects_extracted = d.pop("objects_extracted")

        objects_enriched = d.pop("objects_enriched")

        objects_written = d.pop("objects_written")

        failed_objects = d.pop("failed_objects")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_source_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_id = _parse_source_id(d.pop("source_id", UNSET))

        def _parse_bot_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bot_id = _parse_bot_id(d.pop("bot_id", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

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

        def _parse_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = datetime.datetime.fromisoformat(data)

                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completed_at", UNSET))

        job_response = cls(
            id=id,
            workspace_id=workspace_id,
            trigger=trigger,
            status=status,
            objects_extracted=objects_extracted,
            objects_enriched=objects_enriched,
            objects_written=objects_written,
            failed_objects=failed_objects,
            created_at=created_at,
            source_id=source_id,
            bot_id=bot_id,
            error_message=error_message,
            started_at=started_at,
            completed_at=completed_at,
        )

        job_response.additional_properties = d
        return job_response

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
