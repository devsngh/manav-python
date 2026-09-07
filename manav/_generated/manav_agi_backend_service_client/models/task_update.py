from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.report_status import ReportStatus
from ..models.task_priority import TaskPriority
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task_update_input_data_type_0 import TaskUpdateInputDataType0
    from ..models.task_update_metadata_type_0 import TaskUpdateMetadataType0
    from ..models.task_update_report_images_type_0 import TaskUpdateReportImagesType0
    from ..models.task_update_trigger_next_type_0_item import TaskUpdateTriggerNextType0Item


T = TypeVar("T", bound="TaskUpdate")


@_attrs_define
class TaskUpdate:
    """
    Attributes:
        title (None | str | Unset):
        description (None | str | Unset):
        priority (None | TaskPriority | Unset):
        assigned_to_user_id (None | Unset | UUID):
        assigned_to_bot_id (None | Unset | UUID):
        deepagent_config_id (None | Unset | UUID):
        department_id (None | Unset | UUID):
        thread_id (None | str | Unset):
        input_data (None | TaskUpdateInputDataType0 | Unset):
        trigger_next (list[TaskUpdateTriggerNextType0Item] | None | Unset):
        due_at (datetime.datetime | None | Unset):
        metadata (None | TaskUpdateMetadataType0 | Unset):
        report_status (None | ReportStatus | Unset):
        report_images (None | TaskUpdateReportImagesType0 | Unset):
    """

    title: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    priority: None | TaskPriority | Unset = UNSET
    assigned_to_user_id: None | Unset | UUID = UNSET
    assigned_to_bot_id: None | Unset | UUID = UNSET
    deepagent_config_id: None | Unset | UUID = UNSET
    department_id: None | Unset | UUID = UNSET
    thread_id: None | str | Unset = UNSET
    input_data: None | TaskUpdateInputDataType0 | Unset = UNSET
    trigger_next: list[TaskUpdateTriggerNextType0Item] | None | Unset = UNSET
    due_at: datetime.datetime | None | Unset = UNSET
    metadata: None | TaskUpdateMetadataType0 | Unset = UNSET
    report_status: None | ReportStatus | Unset = UNSET
    report_images: None | TaskUpdateReportImagesType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.task_update_input_data_type_0 import TaskUpdateInputDataType0  # noqa: PLC0415
        from ..models.task_update_metadata_type_0 import TaskUpdateMetadataType0  # noqa: PLC0415
        from ..models.task_update_report_images_type_0 import TaskUpdateReportImagesType0  # noqa: PLC0415

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        priority: None | str | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        elif isinstance(self.priority, TaskPriority):
            priority = self.priority.value
        else:
            priority = self.priority

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

        input_data: dict[str, Any] | None | Unset
        if isinstance(self.input_data, Unset):
            input_data = UNSET
        elif isinstance(self.input_data, TaskUpdateInputDataType0):
            input_data = self.input_data.to_dict()
        else:
            input_data = self.input_data

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
        elif isinstance(self.metadata, TaskUpdateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

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
        elif isinstance(self.report_images, TaskUpdateReportImagesType0):
            report_images = self.report_images.to_dict()
        else:
            report_images = self.report_images

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
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
        if input_data is not UNSET:
            field_dict["input_data"] = input_data
        if trigger_next is not UNSET:
            field_dict["trigger_next"] = trigger_next
        if due_at is not UNSET:
            field_dict["due_at"] = due_at
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if report_status is not UNSET:
            field_dict["report_status"] = report_status
        if report_images is not UNSET:
            field_dict["report_images"] = report_images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.task_update_input_data_type_0 import TaskUpdateInputDataType0  # noqa: PLC0415
        from ..models.task_update_metadata_type_0 import TaskUpdateMetadataType0  # noqa: PLC0415
        from ..models.task_update_report_images_type_0 import TaskUpdateReportImagesType0  # noqa: PLC0415
        from ..models.task_update_trigger_next_type_0_item import TaskUpdateTriggerNextType0Item  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_priority(data: object) -> None | TaskPriority | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                priority_type_0 = TaskPriority(data)

                return priority_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskPriority | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

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

        def _parse_input_data(data: object) -> None | TaskUpdateInputDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_data_type_0 = TaskUpdateInputDataType0.from_dict(data)

                return input_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskUpdateInputDataType0 | Unset, data)

        input_data = _parse_input_data(d.pop("input_data", UNSET))

        def _parse_trigger_next(data: object) -> list[TaskUpdateTriggerNextType0Item] | None | Unset:
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
                    trigger_next_type_0_item = TaskUpdateTriggerNextType0Item.from_dict(trigger_next_type_0_item_data)

                    trigger_next_type_0.append(trigger_next_type_0_item)

                return trigger_next_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TaskUpdateTriggerNextType0Item] | None | Unset, data)

        trigger_next = _parse_trigger_next(d.pop("trigger_next", UNSET))

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

        def _parse_metadata(data: object) -> None | TaskUpdateMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = TaskUpdateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskUpdateMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

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

        def _parse_report_images(data: object) -> None | TaskUpdateReportImagesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                report_images_type_0 = TaskUpdateReportImagesType0.from_dict(data)

                return report_images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskUpdateReportImagesType0 | Unset, data)

        report_images = _parse_report_images(d.pop("report_images", UNSET))

        task_update = cls(
            title=title,
            description=description,
            priority=priority,
            assigned_to_user_id=assigned_to_user_id,
            assigned_to_bot_id=assigned_to_bot_id,
            deepagent_config_id=deepagent_config_id,
            department_id=department_id,
            thread_id=thread_id,
            input_data=input_data,
            trigger_next=trigger_next,
            due_at=due_at,
            metadata=metadata,
            report_status=report_status,
            report_images=report_images,
        )

        task_update.additional_properties = d
        return task_update

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
