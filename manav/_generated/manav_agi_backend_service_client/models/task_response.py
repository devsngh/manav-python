from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_priority import TaskPriority
from ..models.task_status import TaskStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task_response_execution_context_type_0 import TaskResponseExecutionContextType0
    from ..models.task_response_input_data_type_0 import TaskResponseInputDataType0
    from ..models.task_response_metadata_type_0 import TaskResponseMetadataType0
    from ..models.task_response_monitoring_config_type_0 import TaskResponseMonitoringConfigType0
    from ..models.task_response_output_data_type_0 import TaskResponseOutputDataType0
    from ..models.task_response_report_images_type_0 import TaskResponseReportImagesType0
    from ..models.task_response_source_ref_type_0 import TaskResponseSourceRefType0
    from ..models.task_response_trigger_next_type_0_item import TaskResponseTriggerNextType0Item


T = TypeVar("T", bound="TaskResponse")


@_attrs_define
class TaskResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        title (str):
        status (TaskStatus):
        priority (TaskPriority):
        description (None | str | Unset):
        assigned_to_user_id (None | Unset | UUID):
        assigned_to_bot_id (None | Unset | UUID):
        created_by_user_id (None | Unset | UUID):
        created_by_bot_id (None | Unset | UUID):
        deepagent_config_id (None | Unset | UUID):
        department_id (None | Unset | UUID):
        thread_id (None | str | Unset):
        parent_task_id (None | Unset | UUID):
        input_data (None | TaskResponseInputDataType0 | Unset):
        output_data (None | TaskResponseOutputDataType0 | Unset):
        error_message (None | str | Unset):
        monitoring_config (None | TaskResponseMonitoringConfigType0 | Unset):
        execution_context (None | TaskResponseExecutionContextType0 | Unset):
        retry_count (int | Unset):  Default: 0.
        max_retries (int | Unset):  Default: 3.
        source_type (None | str | Unset):
        source_ref (None | TaskResponseSourceRefType0 | Unset):
        trigger_next (list[TaskResponseTriggerNextType0Item] | None | Unset):
        scheduled_at (datetime.datetime | None | Unset):
        started_at (datetime.datetime | None | Unset):
        completed_at (datetime.datetime | None | Unset):
        due_at (datetime.datetime | None | Unset):
        report_period (None | str | Unset):
        target_recipient_id (None | Unset | UUID):
        report_status (None | str | Unset):
        report_version (int | None | Unset):
        report_images (None | TaskResponseReportImagesType0 | Unset):
        metadata (None | TaskResponseMetadataType0 | Unset):
        created_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
        dependency_count (int | Unset):  Default: 0.
        dependent_count (int | Unset):  Default: 0.
        blocked (bool | Unset):  Default: False.
        assigned_to_bot_name (None | str | Unset):
    """

    id: UUID
    org_id: UUID
    title: str
    status: TaskStatus
    priority: TaskPriority
    description: None | str | Unset = UNSET
    assigned_to_user_id: None | Unset | UUID = UNSET
    assigned_to_bot_id: None | Unset | UUID = UNSET
    created_by_user_id: None | Unset | UUID = UNSET
    created_by_bot_id: None | Unset | UUID = UNSET
    deepagent_config_id: None | Unset | UUID = UNSET
    department_id: None | Unset | UUID = UNSET
    thread_id: None | str | Unset = UNSET
    parent_task_id: None | Unset | UUID = UNSET
    input_data: None | TaskResponseInputDataType0 | Unset = UNSET
    output_data: None | TaskResponseOutputDataType0 | Unset = UNSET
    error_message: None | str | Unset = UNSET
    monitoring_config: None | TaskResponseMonitoringConfigType0 | Unset = UNSET
    execution_context: None | TaskResponseExecutionContextType0 | Unset = UNSET
    retry_count: int | Unset = 0
    max_retries: int | Unset = 3
    source_type: None | str | Unset = UNSET
    source_ref: None | TaskResponseSourceRefType0 | Unset = UNSET
    trigger_next: list[TaskResponseTriggerNextType0Item] | None | Unset = UNSET
    scheduled_at: datetime.datetime | None | Unset = UNSET
    started_at: datetime.datetime | None | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    due_at: datetime.datetime | None | Unset = UNSET
    report_period: None | str | Unset = UNSET
    target_recipient_id: None | Unset | UUID = UNSET
    report_status: None | str | Unset = UNSET
    report_version: int | None | Unset = UNSET
    report_images: None | TaskResponseReportImagesType0 | Unset = UNSET
    metadata: None | TaskResponseMetadataType0 | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    dependency_count: int | Unset = 0
    dependent_count: int | Unset = 0
    blocked: bool | Unset = False
    assigned_to_bot_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.task_response_execution_context_type_0 import TaskResponseExecutionContextType0  # noqa: PLC0415
        from ..models.task_response_input_data_type_0 import TaskResponseInputDataType0  # noqa: PLC0415
        from ..models.task_response_metadata_type_0 import TaskResponseMetadataType0  # noqa: PLC0415
        from ..models.task_response_monitoring_config_type_0 import TaskResponseMonitoringConfigType0  # noqa: PLC0415
        from ..models.task_response_output_data_type_0 import TaskResponseOutputDataType0  # noqa: PLC0415
        from ..models.task_response_report_images_type_0 import TaskResponseReportImagesType0  # noqa: PLC0415
        from ..models.task_response_source_ref_type_0 import TaskResponseSourceRefType0  # noqa: PLC0415

        id = str(self.id)

        org_id = str(self.org_id)

        title = self.title

        status = self.status.value

        priority = self.priority.value

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

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

        created_by_user_id: None | str | Unset
        if isinstance(self.created_by_user_id, Unset):
            created_by_user_id = UNSET
        elif isinstance(self.created_by_user_id, UUID):
            created_by_user_id = str(self.created_by_user_id)
        else:
            created_by_user_id = self.created_by_user_id

        created_by_bot_id: None | str | Unset
        if isinstance(self.created_by_bot_id, Unset):
            created_by_bot_id = UNSET
        elif isinstance(self.created_by_bot_id, UUID):
            created_by_bot_id = str(self.created_by_bot_id)
        else:
            created_by_bot_id = self.created_by_bot_id

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
        elif isinstance(self.input_data, TaskResponseInputDataType0):
            input_data = self.input_data.to_dict()
        else:
            input_data = self.input_data

        output_data: dict[str, Any] | None | Unset
        if isinstance(self.output_data, Unset):
            output_data = UNSET
        elif isinstance(self.output_data, TaskResponseOutputDataType0):
            output_data = self.output_data.to_dict()
        else:
            output_data = self.output_data

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        monitoring_config: dict[str, Any] | None | Unset
        if isinstance(self.monitoring_config, Unset):
            monitoring_config = UNSET
        elif isinstance(self.monitoring_config, TaskResponseMonitoringConfigType0):
            monitoring_config = self.monitoring_config.to_dict()
        else:
            monitoring_config = self.monitoring_config

        execution_context: dict[str, Any] | None | Unset
        if isinstance(self.execution_context, Unset):
            execution_context = UNSET
        elif isinstance(self.execution_context, TaskResponseExecutionContextType0):
            execution_context = self.execution_context.to_dict()
        else:
            execution_context = self.execution_context

        retry_count = self.retry_count

        max_retries = self.max_retries

        source_type: None | str | Unset
        if isinstance(self.source_type, Unset):
            source_type = UNSET
        else:
            source_type = self.source_type

        source_ref: dict[str, Any] | None | Unset
        if isinstance(self.source_ref, Unset):
            source_ref = UNSET
        elif isinstance(self.source_ref, TaskResponseSourceRefType0):
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

        due_at: None | str | Unset
        if isinstance(self.due_at, Unset):
            due_at = UNSET
        elif isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        report_period: None | str | Unset
        if isinstance(self.report_period, Unset):
            report_period = UNSET
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
        else:
            report_status = self.report_status

        report_version: int | None | Unset
        if isinstance(self.report_version, Unset):
            report_version = UNSET
        else:
            report_version = self.report_version

        report_images: dict[str, Any] | None | Unset
        if isinstance(self.report_images, Unset):
            report_images = UNSET
        elif isinstance(self.report_images, TaskResponseReportImagesType0):
            report_images = self.report_images.to_dict()
        else:
            report_images = self.report_images

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, TaskResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        dependency_count = self.dependency_count

        dependent_count = self.dependent_count

        blocked = self.blocked

        assigned_to_bot_name: None | str | Unset
        if isinstance(self.assigned_to_bot_name, Unset):
            assigned_to_bot_name = UNSET
        else:
            assigned_to_bot_name = self.assigned_to_bot_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "title": title,
                "status": status,
                "priority": priority,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if assigned_to_user_id is not UNSET:
            field_dict["assigned_to_user_id"] = assigned_to_user_id
        if assigned_to_bot_id is not UNSET:
            field_dict["assigned_to_bot_id"] = assigned_to_bot_id
        if created_by_user_id is not UNSET:
            field_dict["created_by_user_id"] = created_by_user_id
        if created_by_bot_id is not UNSET:
            field_dict["created_by_bot_id"] = created_by_bot_id
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
        if output_data is not UNSET:
            field_dict["output_data"] = output_data
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if monitoring_config is not UNSET:
            field_dict["monitoring_config"] = monitoring_config
        if execution_context is not UNSET:
            field_dict["execution_context"] = execution_context
        if retry_count is not UNSET:
            field_dict["retry_count"] = retry_count
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
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if due_at is not UNSET:
            field_dict["due_at"] = due_at
        if report_period is not UNSET:
            field_dict["report_period"] = report_period
        if target_recipient_id is not UNSET:
            field_dict["target_recipient_id"] = target_recipient_id
        if report_status is not UNSET:
            field_dict["report_status"] = report_status
        if report_version is not UNSET:
            field_dict["report_version"] = report_version
        if report_images is not UNSET:
            field_dict["report_images"] = report_images
        if metadata is not UNSET:
            field_dict["metadata_"] = metadata
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if dependency_count is not UNSET:
            field_dict["dependency_count"] = dependency_count
        if dependent_count is not UNSET:
            field_dict["dependent_count"] = dependent_count
        if blocked is not UNSET:
            field_dict["blocked"] = blocked
        if assigned_to_bot_name is not UNSET:
            field_dict["assigned_to_bot_name"] = assigned_to_bot_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.task_response_execution_context_type_0 import TaskResponseExecutionContextType0  # noqa: PLC0415
        from ..models.task_response_input_data_type_0 import TaskResponseInputDataType0  # noqa: PLC0415
        from ..models.task_response_metadata_type_0 import TaskResponseMetadataType0  # noqa: PLC0415
        from ..models.task_response_monitoring_config_type_0 import TaskResponseMonitoringConfigType0  # noqa: PLC0415
        from ..models.task_response_output_data_type_0 import TaskResponseOutputDataType0  # noqa: PLC0415
        from ..models.task_response_report_images_type_0 import TaskResponseReportImagesType0  # noqa: PLC0415
        from ..models.task_response_source_ref_type_0 import TaskResponseSourceRefType0  # noqa: PLC0415
        from ..models.task_response_trigger_next_type_0_item import TaskResponseTriggerNextType0Item  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        title = d.pop("title")

        status = TaskStatus(d.pop("status"))

        priority = TaskPriority(d.pop("priority"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

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

        def _parse_created_by_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_user_id_type_0 = UUID(data)

                return created_by_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        created_by_user_id = _parse_created_by_user_id(d.pop("created_by_user_id", UNSET))

        def _parse_created_by_bot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_bot_id_type_0 = UUID(data)

                return created_by_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        created_by_bot_id = _parse_created_by_bot_id(d.pop("created_by_bot_id", UNSET))

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

        def _parse_input_data(data: object) -> None | TaskResponseInputDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_data_type_0 = TaskResponseInputDataType0.from_dict(data)

                return input_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskResponseInputDataType0 | Unset, data)

        input_data = _parse_input_data(d.pop("input_data", UNSET))

        def _parse_output_data(data: object) -> None | TaskResponseOutputDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                output_data_type_0 = TaskResponseOutputDataType0.from_dict(data)

                return output_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskResponseOutputDataType0 | Unset, data)

        output_data = _parse_output_data(d.pop("output_data", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        def _parse_monitoring_config(data: object) -> None | TaskResponseMonitoringConfigType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                monitoring_config_type_0 = TaskResponseMonitoringConfigType0.from_dict(data)

                return monitoring_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskResponseMonitoringConfigType0 | Unset, data)

        monitoring_config = _parse_monitoring_config(d.pop("monitoring_config", UNSET))

        def _parse_execution_context(data: object) -> None | TaskResponseExecutionContextType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                execution_context_type_0 = TaskResponseExecutionContextType0.from_dict(data)

                return execution_context_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskResponseExecutionContextType0 | Unset, data)

        execution_context = _parse_execution_context(d.pop("execution_context", UNSET))

        retry_count = d.pop("retry_count", UNSET)

        max_retries = d.pop("max_retries", UNSET)

        def _parse_source_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_type = _parse_source_type(d.pop("source_type", UNSET))

        def _parse_source_ref(data: object) -> None | TaskResponseSourceRefType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_ref_type_0 = TaskResponseSourceRefType0.from_dict(data)

                return source_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskResponseSourceRefType0 | Unset, data)

        source_ref = _parse_source_ref(d.pop("source_ref", UNSET))

        def _parse_trigger_next(data: object) -> list[TaskResponseTriggerNextType0Item] | None | Unset:
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
                    trigger_next_type_0_item = TaskResponseTriggerNextType0Item.from_dict(trigger_next_type_0_item_data)

                    trigger_next_type_0.append(trigger_next_type_0_item)

                return trigger_next_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TaskResponseTriggerNextType0Item] | None | Unset, data)

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

        def _parse_report_period(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

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

        def _parse_report_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        report_status = _parse_report_status(d.pop("report_status", UNSET))

        def _parse_report_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        report_version = _parse_report_version(d.pop("report_version", UNSET))

        def _parse_report_images(data: object) -> None | TaskResponseReportImagesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                report_images_type_0 = TaskResponseReportImagesType0.from_dict(data)

                return report_images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskResponseReportImagesType0 | Unset, data)

        report_images = _parse_report_images(d.pop("report_images", UNSET))

        def _parse_metadata(data: object) -> None | TaskResponseMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = TaskResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskResponseMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata_", UNSET))

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        dependency_count = d.pop("dependency_count", UNSET)

        dependent_count = d.pop("dependent_count", UNSET)

        blocked = d.pop("blocked", UNSET)

        def _parse_assigned_to_bot_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assigned_to_bot_name = _parse_assigned_to_bot_name(d.pop("assigned_to_bot_name", UNSET))

        task_response = cls(
            id=id,
            org_id=org_id,
            title=title,
            status=status,
            priority=priority,
            description=description,
            assigned_to_user_id=assigned_to_user_id,
            assigned_to_bot_id=assigned_to_bot_id,
            created_by_user_id=created_by_user_id,
            created_by_bot_id=created_by_bot_id,
            deepagent_config_id=deepagent_config_id,
            department_id=department_id,
            thread_id=thread_id,
            parent_task_id=parent_task_id,
            input_data=input_data,
            output_data=output_data,
            error_message=error_message,
            monitoring_config=monitoring_config,
            execution_context=execution_context,
            retry_count=retry_count,
            max_retries=max_retries,
            source_type=source_type,
            source_ref=source_ref,
            trigger_next=trigger_next,
            scheduled_at=scheduled_at,
            started_at=started_at,
            completed_at=completed_at,
            due_at=due_at,
            report_period=report_period,
            target_recipient_id=target_recipient_id,
            report_status=report_status,
            report_version=report_version,
            report_images=report_images,
            metadata=metadata,
            created_at=created_at,
            updated_at=updated_at,
            dependency_count=dependency_count,
            dependent_count=dependent_count,
            blocked=blocked,
            assigned_to_bot_name=assigned_to_bot_name,
        )

        task_response.additional_properties = d
        return task_response

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
