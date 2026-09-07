from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.report_period import ReportPeriod
from ..models.report_status import ReportStatus
from ..models.task_priority import TaskPriority
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task_create_input_data_type_0 import TaskCreateInputDataType0
    from ..models.task_create_metadata_type_0 import TaskCreateMetadataType0
    from ..models.task_create_report_images_type_0 import TaskCreateReportImagesType0
    from ..models.task_create_source_ref_type_0 import TaskCreateSourceRefType0
    from ..models.task_create_trigger_next_type_0_item import TaskCreateTriggerNextType0Item


T = TypeVar("T", bound="TaskCreate")


@_attrs_define
class TaskCreate:
    """
    Attributes:
        title (str):
        description (None | str | Unset):
        priority (TaskPriority | Unset):  Default: TaskPriority.NORMAL.
        assigned_to_user_id (None | Unset | UUID):
        assigned_to_bot_id (None | Unset | UUID):
        deepagent_config_id (None | Unset | UUID):
        department_id (None | Unset | UUID):
        thread_id (None | str | Unset):
        parent_task_id (None | Unset | UUID):
        input_data (None | TaskCreateInputDataType0 | Unset):
        max_retries (int | Unset):  Default: 3.
        source_type (None | str | Unset):
        source_ref (None | TaskCreateSourceRefType0 | Unset):
        trigger_next (list[TaskCreateTriggerNextType0Item] | None | Unset):
        scheduled_at (datetime.datetime | None | Unset):
        due_at (datetime.datetime | None | Unset):
        metadata (None | TaskCreateMetadataType0 | Unset):
        dependency_ids (list[UUID] | None | Unset):
        report_period (None | ReportPeriod | Unset):
        target_recipient_id (None | Unset | UUID):
        report_status (None | ReportStatus | Unset):
        report_images (None | TaskCreateReportImagesType0 | Unset):
    """

    title: str
    description: None | str | Unset = UNSET
    priority: TaskPriority | Unset = TaskPriority.NORMAL
    assigned_to_user_id: None | Unset | UUID = UNSET
    assigned_to_bot_id: None | Unset | UUID = UNSET
    deepagent_config_id: None | Unset | UUID = UNSET
    department_id: None | Unset | UUID = UNSET
    thread_id: None | str | Unset = UNSET
    parent_task_id: None | Unset | UUID = UNSET
    input_data: None | TaskCreateInputDataType0 | Unset = UNSET
    max_retries: int | Unset = 3
    source_type: None | str | Unset = UNSET
    source_ref: None | TaskCreateSourceRefType0 | Unset = UNSET
    trigger_next: list[TaskCreateTriggerNextType0Item] | None | Unset = UNSET
    scheduled_at: datetime.datetime | None | Unset = UNSET
    due_at: datetime.datetime | None | Unset = UNSET
    metadata: None | TaskCreateMetadataType0 | Unset = UNSET
    dependency_ids: list[UUID] | None | Unset = UNSET
    report_period: None | ReportPeriod | Unset = UNSET
    target_recipient_id: None | Unset | UUID = UNSET
    report_status: None | ReportStatus | Unset = UNSET
    report_images: None | TaskCreateReportImagesType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.task_create_input_data_type_0 import TaskCreateInputDataType0  # noqa: PLC0415
        from ..models.task_create_metadata_type_0 import TaskCreateMetadataType0  # noqa: PLC0415
        from ..models.task_create_report_images_type_0 import TaskCreateReportImagesType0  # noqa: PLC0415
        from ..models.task_create_source_ref_type_0 import TaskCreateSourceRefType0  # noqa: PLC0415

        title = self.title

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        priority: str | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        assigned_to_user_id: None | str | Unset
        if isinstance(self.assigned_to_user_id, Unset):
            assigned_to_user_id = UNSET
        elif isinstance(self.assigned_to_user_id, UUID):
            assigned_to_user_id = str(self.assigned_to_user_id)
        else:
            assigned_to_user_id = self.assigned_to_user_id

        assigned_to_bot_id: None | str | Unset
        if isinstance(self.assigned_to_bot_id, Unset):
            assigned_to_bot_id = UNSET
        elif isinstance(self.assigned_to_bot_id, UUID):
            assigned_to_bot_id = str(self.assigned_to_bot_id)
        else:
            assigned_to_bot_id = self.assigned_to_bot_id

        deepagent_config_id: None | str | Unset
        if isinstance(self.deepagent_config_id, Unset):
            deepagent_config_id = UNSET
        elif isinstance(self.deepagent_config_id, UUID):
            deepagent_config_id = str(self.deepagent_config_id)
        else:
            deepagent_config_id = self.deepagent_config_id

        department_id: None | str | Unset
        if isinstance(self.department_id, Unset):
            department_id = UNSET
        elif isinstance(self.department_id, UUID):
            department_id = str(self.department_id)
        else:
            department_id = self.department_id

        thread_id: None | str | Unset
        if isinstance(self.thread_id, Unset):
            thread_id = UNSET
        else:
            thread_id = self.thread_id

        parent_task_id: None | str | Unset
        if isinstance(self.parent_task_id, Unset):
            parent_task_id = UNSET
        elif isinstance(self.parent_task_id, UUID):
            parent_task_id = str(self.parent_task_id)
        else:
            parent_task_id = self.parent_task_id

        input_data: dict[str, Any] | None | Unset
        if isinstance(self.input_data, Unset):
            input_data = UNSET
        elif isinstance(self.input_data, TaskCreateInputDataType0):
            input_data = self.input_data.to_dict()
        else:
            input_data = self.input_data

        max_retries = self.max_retries

        source_type: None | str | Unset
        if isinstance(self.source_type, Unset):
            source_type = UNSET
        else:
            source_type = self.source_type

        source_ref: dict[str, Any] | None | Unset
        if isinstance(self.source_ref, Unset):
            source_ref = UNSET
        elif isinstance(self.source_ref, TaskCreateSourceRefType0):
            source_ref = self.source_ref.to_dict()
        else:
            source_ref = self.source_ref

        trigger_next: list[dict[str, Any]] | None | Unset
        if isinstance(self.trigger_next, Unset):
            trigger_next = UNSET
        elif isinstance(self.trigger_next, list):
            trigger_next = []
            for trigger_next_type_0_item_data in self.trigger_next:
                trigger_next_type_0_item = trigger_next_type_0_item_data.to_dict()
                trigger_next.append(trigger_next_type_0_item)

        else:
            trigger_next = self.trigger_next

        scheduled_at: None | str | Unset
        if isinstance(self.scheduled_at, Unset):
            scheduled_at = UNSET
        elif isinstance(self.scheduled_at, datetime.datetime):
            scheduled_at = self.scheduled_at.isoformat()
        else:
            scheduled_at = self.scheduled_at

        due_at: None | str | Unset
        if isinstance(self.due_at, Unset):
            due_at = UNSET
        elif isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, TaskCreateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        dependency_ids: list[str] | None | Unset
        if isinstance(self.dependency_ids, Unset):
            dependency_ids = UNSET
        elif isinstance(self.dependency_ids, list):
            dependency_ids = []
            for dependency_ids_type_0_item_data in self.dependency_ids:
                dependency_ids_type_0_item = str(dependency_ids_type_0_item_data)
                dependency_ids.append(dependency_ids_type_0_item)

        else:
            dependency_ids = self.dependency_ids

        report_period: None | str | Unset
        if isinstance(self.report_period, Unset):
            report_period = UNSET
        elif isinstance(self.report_period, ReportPeriod):
            report_period = self.report_period.value
        else:
            report_period = self.report_period

        target_recipient_id: None | str | Unset
        if isinstance(self.target_recipient_id, Unset):
            target_recipient_id = UNSET
        elif isinstance(self.target_recipient_id, UUID):
            target_recipient_id = str(self.target_recipient_id)
        else:
            target_recipient_id = self.target_recipient_id

        report_status: None | str | Unset
        if isinstance(self.report_status, Unset):
            report_status = UNSET
        elif isinstance(self.report_status, ReportStatus):
            report_status = self.report_status.value
        else:
            report_status = self.report_status

        report_images: dict[str, Any] | None | Unset
        if isinstance(self.report_images, Unset):
            report_images = UNSET
        elif isinstance(self.report_images, TaskCreateReportImagesType0):
            report_images = self.report_images.to_dict()
        else:
            report_images = self.report_images

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if priority is not UNSET:
            field_dict["priority"] = priority
        if assigned_to_user_id is not UNSET:
            field_dict["assigned_to_user_id"] = assigned_to_user_id
        if assigned_to_bot_id is not UNSET:
            field_dict["assigned_to_bot_id"] = assigned_to_bot_id
        if deepagent_config_id is not UNSET:
            field_dict["deepagent_config_id"] = deepagent_config_id
        if department_id is not UNSET:
            field_dict["department_id"] = department_id
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id
        if parent_task_id is not UNSET:
            field_dict["parent_task_id"] = parent_task_id
        if input_data is not UNSET:
            field_dict["input_data"] = input_data
        if max_retries is not UNSET:
            field_dict["max_retries"] = max_retries
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if source_ref is not UNSET:
            field_dict["source_ref"] = source_ref
        if trigger_next is not UNSET:
            field_dict["trigger_next"] = trigger_next
        if scheduled_at is not UNSET:
            field_dict["scheduled_at"] = scheduled_at
        if due_at is not UNSET:
            field_dict["due_at"] = due_at
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if dependency_ids is not UNSET:
            field_dict["dependency_ids"] = dependency_ids
        if report_period is not UNSET:
            field_dict["report_period"] = report_period
        if target_recipient_id is not UNSET:
            field_dict["target_recipient_id"] = target_recipient_id
        if report_status is not UNSET:
            field_dict["report_status"] = report_status
        if report_images is not UNSET:
            field_dict["report_images"] = report_images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.task_create_input_data_type_0 import TaskCreateInputDataType0  # noqa: PLC0415
        from ..models.task_create_metadata_type_0 import TaskCreateMetadataType0  # noqa: PLC0415
        from ..models.task_create_report_images_type_0 import TaskCreateReportImagesType0  # noqa: PLC0415
        from ..models.task_create_source_ref_type_0 import TaskCreateSourceRefType0  # noqa: PLC0415
        from ..models.task_create_trigger_next_type_0_item import TaskCreateTriggerNextType0Item  # noqa: PLC0415

        d = dict(src_dict)
        title = d.pop("title")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _priority = d.pop("priority", UNSET)
        priority: TaskPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = TaskPriority(_priority)

        def _parse_assigned_to_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assigned_to_user_id_type_0 = UUID(data)

                return assigned_to_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        assigned_to_user_id = _parse_assigned_to_user_id(d.pop("assigned_to_user_id", UNSET))

        def _parse_assigned_to_bot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assigned_to_bot_id_type_0 = UUID(data)

                return assigned_to_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        assigned_to_bot_id = _parse_assigned_to_bot_id(d.pop("assigned_to_bot_id", UNSET))

        def _parse_deepagent_config_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deepagent_config_id_type_0 = UUID(data)

                return deepagent_config_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        deepagent_config_id = _parse_deepagent_config_id(d.pop("deepagent_config_id", UNSET))

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

        def _parse_thread_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thread_id = _parse_thread_id(d.pop("thread_id", UNSET))

        def _parse_parent_task_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_task_id_type_0 = UUID(data)

                return parent_task_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_task_id = _parse_parent_task_id(d.pop("parent_task_id", UNSET))

        def _parse_input_data(data: object) -> None | TaskCreateInputDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_data_type_0 = TaskCreateInputDataType0.from_dict(data)

                return input_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskCreateInputDataType0 | Unset, data)

        input_data = _parse_input_data(d.pop("input_data", UNSET))

        max_retries = d.pop("max_retries", UNSET)

        def _parse_source_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_type = _parse_source_type(d.pop("source_type", UNSET))

        def _parse_source_ref(data: object) -> None | TaskCreateSourceRefType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_ref_type_0 = TaskCreateSourceRefType0.from_dict(data)

                return source_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskCreateSourceRefType0 | Unset, data)

        source_ref = _parse_source_ref(d.pop("source_ref", UNSET))

        def _parse_trigger_next(data: object) -> list[TaskCreateTriggerNextType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                trigger_next_type_0 = []
                _trigger_next_type_0 = data
                for trigger_next_type_0_item_data in _trigger_next_type_0:
                    trigger_next_type_0_item = TaskCreateTriggerNextType0Item.from_dict(trigger_next_type_0_item_data)

                    trigger_next_type_0.append(trigger_next_type_0_item)

                return trigger_next_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TaskCreateTriggerNextType0Item] | None | Unset, data)

        trigger_next = _parse_trigger_next(d.pop("trigger_next", UNSET))

        def _parse_scheduled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_at_type_0 = datetime.datetime.fromisoformat(data)

                return scheduled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        scheduled_at = _parse_scheduled_at(d.pop("scheduled_at", UNSET))

        def _parse_due_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_at_type_0 = datetime.datetime.fromisoformat(data)

                return due_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        due_at = _parse_due_at(d.pop("due_at", UNSET))

        def _parse_metadata(data: object) -> None | TaskCreateMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = TaskCreateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskCreateMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_dependency_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dependency_ids_type_0 = []
                _dependency_ids_type_0 = data
                for dependency_ids_type_0_item_data in _dependency_ids_type_0:
                    dependency_ids_type_0_item = UUID(dependency_ids_type_0_item_data)

                    dependency_ids_type_0.append(dependency_ids_type_0_item)

                return dependency_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        dependency_ids = _parse_dependency_ids(d.pop("dependency_ids", UNSET))

        def _parse_report_period(data: object) -> None | ReportPeriod | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                report_period_type_0 = ReportPeriod(data)

                return report_period_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReportPeriod | Unset, data)

        report_period = _parse_report_period(d.pop("report_period", UNSET))

        def _parse_target_recipient_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                target_recipient_id_type_0 = UUID(data)

                return target_recipient_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        target_recipient_id = _parse_target_recipient_id(d.pop("target_recipient_id", UNSET))

        def _parse_report_status(data: object) -> None | ReportStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                report_status_type_0 = ReportStatus(data)

                return report_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReportStatus | Unset, data)

        report_status = _parse_report_status(d.pop("report_status", UNSET))

        def _parse_report_images(data: object) -> None | TaskCreateReportImagesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                report_images_type_0 = TaskCreateReportImagesType0.from_dict(data)

                return report_images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskCreateReportImagesType0 | Unset, data)

        report_images = _parse_report_images(d.pop("report_images", UNSET))

        task_create = cls(
            title=title,
            description=description,
            priority=priority,
            assigned_to_user_id=assigned_to_user_id,
            assigned_to_bot_id=assigned_to_bot_id,
            deepagent_config_id=deepagent_config_id,
            department_id=department_id,
            thread_id=thread_id,
            parent_task_id=parent_task_id,
            input_data=input_data,
            max_retries=max_retries,
            source_type=source_type,
            source_ref=source_ref,
            trigger_next=trigger_next,
            scheduled_at=scheduled_at,
            due_at=due_at,
            metadata=metadata,
            dependency_ids=dependency_ids,
            report_period=report_period,
            target_recipient_id=target_recipient_id,
            report_status=report_status,
            report_images=report_images,
        )

        task_create.additional_properties = d
        return task_create

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
