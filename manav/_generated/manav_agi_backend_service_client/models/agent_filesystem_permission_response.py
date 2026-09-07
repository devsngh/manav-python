from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_filesystem_permission_response_mode import AgentFilesystemPermissionResponseMode
from ..models.agent_filesystem_permission_response_operations_item import (
    AgentFilesystemPermissionResponseOperationsItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentFilesystemPermissionResponse")


@_attrs_define
class AgentFilesystemPermissionResponse:
    """Full row, returned by GET / list endpoints.

    Attributes:
        id (UUID):
        agent_id (None | UUID):
        role_id (None | UUID):
        operations (list[AgentFilesystemPermissionResponseOperationsItem]):
        paths (list[str]):
        mode (AgentFilesystemPermissionResponseMode):
        description (None | str):
        priority (int):
        is_active (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        created_by (None | UUID):
        approver_user_ids (list[UUID] | Unset):
        interrupt_message (None | str | Unset):
    """

    id: UUID
    agent_id: None | UUID
    role_id: None | UUID
    operations: list[AgentFilesystemPermissionResponseOperationsItem]
    paths: list[str]
    mode: AgentFilesystemPermissionResponseMode
    description: None | str
    priority: int
    is_active: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    created_by: None | UUID
    approver_user_ids: list[UUID] | Unset = UNSET
    interrupt_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        agent_id: None | str
        if isinstance(self.agent_id, UUID):
            agent_id = str(self.agent_id)
        else:
            agent_id = self.agent_id

        role_id: None | str
        if isinstance(self.role_id, UUID):
            role_id = str(self.role_id)
        else:
            role_id = self.role_id

        operations = []
        for operations_item_data in self.operations:
            operations_item = operations_item_data.value
            operations.append(operations_item)

        paths = self.paths

        mode = self.mode.value

        description: None | str
        description = self.description

        priority = self.priority

        is_active = self.is_active

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        created_by: None | str
        if isinstance(self.created_by, UUID):
            created_by = str(self.created_by)
        else:
            created_by = self.created_by

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
                "id": id,
                "agent_id": agent_id,
                "role_id": role_id,
                "operations": operations,
                "paths": paths,
                "mode": mode,
                "description": description,
                "priority": priority,
                "is_active": is_active,
                "created_at": created_at,
                "updated_at": updated_at,
                "created_by": created_by,
            }
        )
        if approver_user_ids is not UNSET:
            field_dict["approver_user_ids"] = approver_user_ids
        if interrupt_message is not UNSET:
            field_dict["interrupt_message"] = interrupt_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_agent_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                agent_id_type_0 = UUID(data)

                return agent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        agent_id = _parse_agent_id(d.pop("agent_id"))

        def _parse_role_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_id_type_0 = UUID(data)

                return role_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        role_id = _parse_role_id(d.pop("role_id"))

        operations = []
        _operations = d.pop("operations")
        for operations_item_data in _operations:
            operations_item = AgentFilesystemPermissionResponseOperationsItem(operations_item_data)

            operations.append(operations_item)

        paths = cast(list[str], d.pop("paths"))

        mode = AgentFilesystemPermissionResponseMode(d.pop("mode"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        priority = d.pop("priority")

        is_active = d.pop("is_active")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_created_by(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_type_0 = UUID(data)

                return created_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        created_by = _parse_created_by(d.pop("created_by"))

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

        agent_filesystem_permission_response = cls(
            id=id,
            agent_id=agent_id,
            role_id=role_id,
            operations=operations,
            paths=paths,
            mode=mode,
            description=description,
            priority=priority,
            is_active=is_active,
            created_at=created_at,
            updated_at=updated_at,
            created_by=created_by,
            approver_user_ids=approver_user_ids,
            interrupt_message=interrupt_message,
        )

        agent_filesystem_permission_response.additional_properties = d
        return agent_filesystem_permission_response

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
