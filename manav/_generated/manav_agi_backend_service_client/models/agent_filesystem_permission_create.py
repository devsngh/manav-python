from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_filesystem_permission_create_mode import AgentFilesystemPermissionCreateMode
from ..models.agent_filesystem_permission_create_operations_item import AgentFilesystemPermissionCreateOperationsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentFilesystemPermissionCreate")


@_attrs_define
class AgentFilesystemPermissionCreate:
    """Create a new rule. Bind to exactly one of agent_id / role_id.

    Attributes:
        operations (list[AgentFilesystemPermissionCreateOperationsItem]):
        paths (list[str]):
        agent_id (None | Unset | UUID):
        role_id (None | Unset | UUID):
        mode (AgentFilesystemPermissionCreateMode | Unset):  Default: AgentFilesystemPermissionCreateMode.ALLOW.
        description (None | str | Unset):
        priority (int | Unset):  Default: 100.
        is_active (bool | Unset):  Default: True.
        approver_user_ids (list[UUID] | Unset):
        interrupt_message (None | str | Unset):
    """

    operations: list[AgentFilesystemPermissionCreateOperationsItem]
    paths: list[str]
    agent_id: None | Unset | UUID = UNSET
    role_id: None | Unset | UUID = UNSET
    mode: AgentFilesystemPermissionCreateMode | Unset = AgentFilesystemPermissionCreateMode.ALLOW
    description: None | str | Unset = UNSET
    priority: int | Unset = 100
    is_active: bool | Unset = True
    approver_user_ids: list[UUID] | Unset = UNSET
    interrupt_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operations = []
        for operations_item_data in self.operations:
            operations_item = operations_item_data.value
            operations.append(operations_item)

        paths = self.paths

        agent_id: None | str | Unset
        if isinstance(self.agent_id, Unset):
            agent_id = UNSET
        elif isinstance(self.agent_id, UUID):
            agent_id = str(self.agent_id)
        else:
            agent_id = self.agent_id

        role_id: None | str | Unset
        if isinstance(self.role_id, Unset):
            role_id = UNSET
        elif isinstance(self.role_id, UUID):
            role_id = str(self.role_id)
        else:
            role_id = self.role_id

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        priority = self.priority

        is_active = self.is_active

        approver_user_ids: list[str] | Unset = UNSET
        if not isinstance(self.approver_user_ids, Unset):
            approver_user_ids = []
            for approver_user_ids_item_data in self.approver_user_ids:
                approver_user_ids_item = str(approver_user_ids_item_data)
                approver_user_ids.append(approver_user_ids_item)

        interrupt_message: None | str | Unset
        if isinstance(self.interrupt_message, Unset):
            interrupt_message = UNSET
        else:
            interrupt_message = self.interrupt_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operations": operations,
                "paths": paths,
            }
        )
        if agent_id is not UNSET:
            field_dict["agent_id"] = agent_id
        if role_id is not UNSET:
            field_dict["role_id"] = role_id
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
        operations = []
        _operations = d.pop("operations")
        for operations_item_data in _operations:
            operations_item = AgentFilesystemPermissionCreateOperationsItem(operations_item_data)

            operations.append(operations_item)

        paths = cast(list[str], d.pop("paths"))

        def _parse_agent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                agent_id_type_0 = UUID(data)

                return agent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        agent_id = _parse_agent_id(d.pop("agent_id", UNSET))

        def _parse_role_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_id_type_0 = UUID(data)

                return role_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        role_id = _parse_role_id(d.pop("role_id", UNSET))

        _mode = d.pop("mode", UNSET)
        mode: AgentFilesystemPermissionCreateMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = AgentFilesystemPermissionCreateMode(_mode)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        priority = d.pop("priority", UNSET)

        is_active = d.pop("is_active", UNSET)

        _approver_user_ids = d.pop("approver_user_ids", UNSET)
        approver_user_ids: list[UUID] | Unset = UNSET
        if _approver_user_ids is not UNSET:
            approver_user_ids = []
            for approver_user_ids_item_data in _approver_user_ids:
                approver_user_ids_item = UUID(approver_user_ids_item_data)

                approver_user_ids.append(approver_user_ids_item)

        def _parse_interrupt_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        interrupt_message = _parse_interrupt_message(d.pop("interrupt_message", UNSET))

        agent_filesystem_permission_create = cls(
            operations=operations,
            paths=paths,
            agent_id=agent_id,
            role_id=role_id,
            mode=mode,
            description=description,
            priority=priority,
            is_active=is_active,
            approver_user_ids=approver_user_ids,
            interrupt_message=interrupt_message,
        )

        agent_filesystem_permission_create.additional_properties = d
        return agent_filesystem_permission_create

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
