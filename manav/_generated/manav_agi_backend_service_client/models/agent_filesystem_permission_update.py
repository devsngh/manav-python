from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_filesystem_permission_update_mode_type_0 import AgentFilesystemPermissionUpdateModeType0
from ..models.agent_filesystem_permission_update_operations_type_0_item import (
    AgentFilesystemPermissionUpdateOperationsType0Item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentFilesystemPermissionUpdate")


@_attrs_define
class AgentFilesystemPermissionUpdate:
    """Partial update — only the fields you pass are mutated.

    Attributes:
        operations (list[AgentFilesystemPermissionUpdateOperationsType0Item] | None | Unset):
        paths (list[str] | None | Unset):
        mode (AgentFilesystemPermissionUpdateModeType0 | None | Unset):
        description (None | str | Unset):
        priority (int | None | Unset):
        is_active (bool | None | Unset):
        approver_user_ids (list[UUID] | None | Unset):
        interrupt_message (None | str | Unset):
    """

    operations: list[AgentFilesystemPermissionUpdateOperationsType0Item] | None | Unset = UNSET
    paths: list[str] | None | Unset = UNSET
    mode: AgentFilesystemPermissionUpdateModeType0 | None | Unset = UNSET
    description: None | str | Unset = UNSET
    priority: int | None | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    approver_user_ids: list[UUID] | None | Unset = UNSET
    interrupt_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operations: list[str] | None | Unset
        if isinstance(self.operations, Unset):
            operations = UNSET
        elif isinstance(self.operations, list):
            operations = []
            for operations_type_0_item_data in self.operations:
                operations_type_0_item = operations_type_0_item_data.value
                operations.append(operations_type_0_item)

        else:
            operations = self.operations

        paths: list[str] | None | Unset
        if isinstance(self.paths, Unset):
            paths = UNSET
        elif isinstance(self.paths, list):
            paths = self.paths

        else:
            paths = self.paths

        mode: None | str | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        elif isinstance(self.mode, AgentFilesystemPermissionUpdateModeType0):
            mode = self.mode.value
        else:
            mode = self.mode

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        approver_user_ids: list[str] | None | Unset
        if isinstance(self.approver_user_ids, Unset):
            approver_user_ids = UNSET
        elif isinstance(self.approver_user_ids, list):
            approver_user_ids = []
            for approver_user_ids_type_0_item_data in self.approver_user_ids:
                approver_user_ids_type_0_item = str(approver_user_ids_type_0_item_data)
                approver_user_ids.append(approver_user_ids_type_0_item)

        else:
            approver_user_ids = self.approver_user_ids

        interrupt_message: None | str | Unset
        if isinstance(self.interrupt_message, Unset):
            interrupt_message = UNSET
        else:
            interrupt_message = self.interrupt_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operations is not UNSET:
            field_dict["operations"] = operations
        if paths is not UNSET:
            field_dict["paths"] = paths
        if mode is not UNSET:
            field_dict["mode"] = mode
        if description is not UNSET:
            field_dict["description"] = description
        if priority is not UNSET:
            field_dict["priority"] = priority
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if approver_user_ids is not UNSET:
            field_dict["approver_user_ids"] = approver_user_ids
        if interrupt_message is not UNSET:
            field_dict["interrupt_message"] = interrupt_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_operations(data: object) -> list[AgentFilesystemPermissionUpdateOperationsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                operations_type_0 = []
                _operations_type_0 = data
                for operations_type_0_item_data in _operations_type_0:
                    operations_type_0_item = AgentFilesystemPermissionUpdateOperationsType0Item(
                        operations_type_0_item_data
                    )

                    operations_type_0.append(operations_type_0_item)

                return operations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AgentFilesystemPermissionUpdateOperationsType0Item] | None | Unset, data)

        operations = _parse_operations(d.pop("operations", UNSET))

        def _parse_paths(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                paths_type_0 = cast(list[str], data)

                return paths_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        paths = _parse_paths(d.pop("paths", UNSET))

        def _parse_mode(data: object) -> AgentFilesystemPermissionUpdateModeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_0 = AgentFilesystemPermissionUpdateModeType0(data)

                return mode_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentFilesystemPermissionUpdateModeType0 | None | Unset, data)

        mode = _parse_mode(d.pop("mode", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        def _parse_approver_user_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                approver_user_ids_type_0 = []
                _approver_user_ids_type_0 = data
                for approver_user_ids_type_0_item_data in _approver_user_ids_type_0:
                    approver_user_ids_type_0_item = UUID(approver_user_ids_type_0_item_data)

                    approver_user_ids_type_0.append(approver_user_ids_type_0_item)

                return approver_user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        approver_user_ids = _parse_approver_user_ids(d.pop("approver_user_ids", UNSET))

        def _parse_interrupt_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        interrupt_message = _parse_interrupt_message(d.pop("interrupt_message", UNSET))

        agent_filesystem_permission_update = cls(
            operations=operations,
            paths=paths,
            mode=mode,
            description=description,
            priority=priority,
            is_active=is_active,
            approver_user_ids=approver_user_ids,
            interrupt_message=interrupt_message,
        )

        agent_filesystem_permission_update.additional_properties = d
        return agent_filesystem_permission_update

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
