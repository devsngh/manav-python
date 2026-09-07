from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_update_task_input_data_type_0 import ScheduleUpdateTaskInputDataType0


T = TypeVar("T", bound="ScheduleUpdate")


@_attrs_define
class ScheduleUpdate:
    """
    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        task_title (None | str | Unset):
        query (None | str | Unset):
        task_priority (None | str | Unset):
        task_input_data (None | ScheduleUpdateTaskInputDataType0 | Unset):
        cron_expression (None | str | Unset):
        timezone (None | str | Unset):
        expires_at (datetime.datetime | None | Unset):
        max_runs (int | None | Unset):
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    task_title: None | str | Unset = UNSET
    query: None | str | Unset = UNSET
    task_priority: None | str | Unset = UNSET
    task_input_data: None | ScheduleUpdateTaskInputDataType0 | Unset = UNSET
    cron_expression: None | str | Unset = UNSET
    timezone: None | str | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    max_runs: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.schedule_update_task_input_data_type_0 import ScheduleUpdateTaskInputDataType0  # noqa: PLC0415

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

        task_title: None | str | Unset
        if isinstance(self.task_title, Unset):
            task_title = UNSET
        else:
            task_title = self.task_title

        query: None | str | Unset
        if isinstance(self.query, Unset):
            query = UNSET
        else:
            query = self.query

        task_priority: None | str | Unset
        if isinstance(self.task_priority, Unset):
            task_priority = UNSET
        else:
            task_priority = self.task_priority

        task_input_data: dict[str, Any] | None | Unset
        if isinstance(self.task_input_data, Unset):
            task_input_data = UNSET
        elif isinstance(self.task_input_data, ScheduleUpdateTaskInputDataType0):
            task_input_data = self.task_input_data.to_dict()
        else:
            task_input_data = self.task_input_data

        cron_expression: None | str | Unset
        if isinstance(self.cron_expression, Unset):
            cron_expression = UNSET
        else:
            cron_expression = self.cron_expression

        timezone: None | str | Unset
        if isinstance(self.timezone, Unset):
            timezone = UNSET
        else:
            timezone = self.timezone

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        max_runs: int | None | Unset
        if isinstance(self.max_runs, Unset):
            max_runs = UNSET
        else:
            max_runs = self.max_runs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if task_title is not UNSET:
            field_dict["task_title"] = task_title
        if query is not UNSET:
            field_dict["query"] = query
        if task_priority is not UNSET:
            field_dict["task_priority"] = task_priority
        if task_input_data is not UNSET:
            field_dict["task_input_data"] = task_input_data
        if cron_expression is not UNSET:
            field_dict["cron_expression"] = cron_expression
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if max_runs is not UNSET:
            field_dict["max_runs"] = max_runs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schedule_update_task_input_data_type_0 import ScheduleUpdateTaskInputDataType0  # noqa: PLC0415

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

        def _parse_task_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_title = _parse_task_title(d.pop("task_title", UNSET))

        def _parse_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        query = _parse_query(d.pop("query", UNSET))

        def _parse_task_priority(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_priority = _parse_task_priority(d.pop("task_priority", UNSET))

        def _parse_task_input_data(data: object) -> None | ScheduleUpdateTaskInputDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_input_data_type_0 = ScheduleUpdateTaskInputDataType0.from_dict(data)

                return task_input_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ScheduleUpdateTaskInputDataType0 | Unset, data)

        task_input_data = _parse_task_input_data(d.pop("task_input_data", UNSET))

        def _parse_cron_expression(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cron_expression = _parse_cron_expression(d.pop("cron_expression", UNSET))

        def _parse_timezone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timezone = _parse_timezone(d.pop("timezone", UNSET))

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        def _parse_max_runs(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_runs = _parse_max_runs(d.pop("max_runs", UNSET))

        schedule_update = cls(
            name=name,
            description=description,
            task_title=task_title,
            query=query,
            task_priority=task_priority,
            task_input_data=task_input_data,
            cron_expression=cron_expression,
            timezone=timezone,
            expires_at=expires_at,
            max_runs=max_runs,
        )

        schedule_update.additional_properties = d
        return schedule_update

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
