from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.permission_request_create_scope import PermissionRequestCreateScope
from ..types import UNSET, Unset

T = TypeVar("T", bound="PermissionRequestCreate")


@_attrs_define
class PermissionRequestCreate:
    """Body for POST /api/permission-requests — either a human or an
    agent submitting a self-service request.

        Attributes:
            resource (str): Backend resource name (e.g. 'email')
            action (str): Action verb (create/read/update/delete/execute/etc.)
            justification (str): Why the requester needs this permission
            scope (PermissionRequestCreateScope | Unset):  Default: PermissionRequestCreateScope.OWN.
            session_id (None | Unset | UUID):
            task_id (None | Unset | UUID):
    """

    resource: str
    action: str
    justification: str
    scope: PermissionRequestCreateScope | Unset = PermissionRequestCreateScope.OWN
    session_id: None | Unset | UUID = UNSET
    task_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource = self.resource

        action = self.action

        justification = self.justification

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        session_id: None | str | Unset
        if isinstance(self.session_id, Unset):
            session_id = UNSET
        elif isinstance(self.session_id, UUID):
            session_id = str(self.session_id)
        else:
            session_id = self.session_id

        task_id: None | str | Unset
        if isinstance(self.task_id, Unset):
            task_id = UNSET
        elif isinstance(self.task_id, UUID):
            task_id = str(self.task_id)
        else:
            task_id = self.task_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource": resource,
                "action": action,
                "justification": justification,
            }
        )
        if scope is not UNSET:
            field_dict["scope"] = scope
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if task_id is not UNSET:
            field_dict["task_id"] = task_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource = d.pop("resource")

        action = d.pop("action")

        justification = d.pop("justification")

        _scope = d.pop("scope", UNSET)
        scope: PermissionRequestCreateScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = PermissionRequestCreateScope(_scope)

        def _parse_session_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                session_id_type_0 = UUID(data)

                return session_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        session_id = _parse_session_id(d.pop("session_id", UNSET))

        def _parse_task_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                task_id_type_0 = UUID(data)

                return task_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        task_id = _parse_task_id(d.pop("task_id", UNSET))

        permission_request_create = cls(
            resource=resource,
            action=action,
            justification=justification,
            scope=scope,
            session_id=session_id,
            task_id=task_id,
        )

        permission_request_create.additional_properties = d
        return permission_request_create

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
