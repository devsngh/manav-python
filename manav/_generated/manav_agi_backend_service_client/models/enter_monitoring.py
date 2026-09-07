from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.enter_monitoring_execution_context_type_0 import EnterMonitoringExecutionContextType0


T = TypeVar("T", bound="EnterMonitoring")


@_attrs_define
class EnterMonitoring:
    """Request to put a task into MONITORING state.

    Attributes:
        check_interval_seconds (int | Unset):  Default: 300.
        max_duration_seconds (int | Unset):  Default: 7200.
        watch_task_ids (list[UUID] | None | Unset):
        execution_context (EnterMonitoringExecutionContextType0 | None | Unset):
    """

    check_interval_seconds: int | Unset = 300
    max_duration_seconds: int | Unset = 7200
    watch_task_ids: list[UUID] | None | Unset = UNSET
    execution_context: EnterMonitoringExecutionContextType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.enter_monitoring_execution_context_type_0 import (
            EnterMonitoringExecutionContextType0,  # noqa: PLC0415
        )

        check_interval_seconds = self.check_interval_seconds

        max_duration_seconds = self.max_duration_seconds

        watch_task_ids: list[str] | None | Unset
        if isinstance(self.watch_task_ids, Unset):
            watch_task_ids = UNSET
        elif isinstance(self.watch_task_ids, list):
            watch_task_ids = []
            for watch_task_ids_type_0_item_data in self.watch_task_ids:
                watch_task_ids_type_0_item = str(watch_task_ids_type_0_item_data)
                watch_task_ids.append(watch_task_ids_type_0_item)

        else:
            watch_task_ids = self.watch_task_ids

        execution_context: dict[str, Any] | None | Unset
        if isinstance(self.execution_context, Unset):
            execution_context = UNSET
        elif isinstance(self.execution_context, EnterMonitoringExecutionContextType0):
            execution_context = self.execution_context.to_dict()
        else:
            execution_context = self.execution_context

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if check_interval_seconds is not UNSET:
            field_dict["check_interval_seconds"] = check_interval_seconds
        if max_duration_seconds is not UNSET:
            field_dict["max_duration_seconds"] = max_duration_seconds
        if watch_task_ids is not UNSET:
            field_dict["watch_task_ids"] = watch_task_ids
        if execution_context is not UNSET:
            field_dict["execution_context"] = execution_context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.enter_monitoring_execution_context_type_0 import (
            EnterMonitoringExecutionContextType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        check_interval_seconds = d.pop("check_interval_seconds", UNSET)

        max_duration_seconds = d.pop("max_duration_seconds", UNSET)

        def _parse_watch_task_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                watch_task_ids_type_0 = []
                _watch_task_ids_type_0 = data
                for watch_task_ids_type_0_item_data in _watch_task_ids_type_0:
                    watch_task_ids_type_0_item = UUID(watch_task_ids_type_0_item_data)

                    watch_task_ids_type_0.append(watch_task_ids_type_0_item)

                return watch_task_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        watch_task_ids = _parse_watch_task_ids(d.pop("watch_task_ids", UNSET))

        def _parse_execution_context(data: object) -> EnterMonitoringExecutionContextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                execution_context_type_0 = EnterMonitoringExecutionContextType0.from_dict(data)

                return execution_context_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnterMonitoringExecutionContextType0 | None | Unset, data)

        execution_context = _parse_execution_context(d.pop("execution_context", UNSET))

        enter_monitoring = cls(
            check_interval_seconds=check_interval_seconds,
            max_duration_seconds=max_duration_seconds,
            watch_task_ids=watch_task_ids,
            execution_context=execution_context,
        )

        enter_monitoring.additional_properties = d
        return enter_monitoring

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
