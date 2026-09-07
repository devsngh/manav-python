from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.permission_request_response_status import PermissionRequestResponseStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PermissionRequestResponse")


@_attrs_define
class PermissionRequestResponse:
    """
    Attributes:
        id (UUID):
        org_id (None | UUID):
        requester_user_id (UUID):
        requester_bot_id (None | UUID):
        resource (str):
        action (str):
        scope (str):
        justification (str):
        session_id (None | UUID):
        task_id (None | UUID):
        status (PermissionRequestResponseStatus):
        reviewer_user_id (None | UUID):
        reviewer_comment (None | str):
        created_at (datetime.datetime):
        reviewed_at (datetime.datetime | None):
        requester_name (None | str | Unset):
        requester_email (None | str | Unset):
        reviewer_name (None | str | Unset):
    """

    id: UUID
    org_id: None | UUID
    requester_user_id: UUID
    requester_bot_id: None | UUID
    resource: str
    action: str
    scope: str
    justification: str
    session_id: None | UUID
    task_id: None | UUID
    status: PermissionRequestResponseStatus
    reviewer_user_id: None | UUID
    reviewer_comment: None | str
    created_at: datetime.datetime
    reviewed_at: datetime.datetime | None
    requester_name: None | str | Unset = UNSET
    requester_email: None | str | Unset = UNSET
    reviewer_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        org_id: None | str
        if isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

        requester_user_id = str(self.requester_user_id)

        requester_bot_id: None | str
        if isinstance(self.requester_bot_id, UUID):
            requester_bot_id = str(self.requester_bot_id)
        else:
            requester_bot_id = self.requester_bot_id

        resource = self.resource

        action = self.action

        scope = self.scope

        justification = self.justification

        session_id: None | str
        if isinstance(self.session_id, UUID):
            session_id = str(self.session_id)
        else:
            session_id = self.session_id

        task_id: None | str
        if isinstance(self.task_id, UUID):
            task_id = str(self.task_id)
        else:
            task_id = self.task_id

        status = self.status.value

        reviewer_user_id: None | str
        if isinstance(self.reviewer_user_id, UUID):
            reviewer_user_id = str(self.reviewer_user_id)
        else:
            reviewer_user_id = self.reviewer_user_id

        reviewer_comment: None | str
        reviewer_comment = self.reviewer_comment

        created_at = self.created_at.isoformat()

        reviewed_at: None | str
        if isinstance(self.reviewed_at, datetime.datetime):
            reviewed_at = self.reviewed_at.isoformat()
        else:
            reviewed_at = self.reviewed_at

        requester_name: None | str | Unset
        if isinstance(self.requester_name, Unset):
            requester_name = UNSET
        else:
            requester_name = self.requester_name

        requester_email: None | str | Unset
        if isinstance(self.requester_email, Unset):
            requester_email = UNSET
        else:
            requester_email = self.requester_email

        reviewer_name: None | str | Unset
        if isinstance(self.reviewer_name, Unset):
            reviewer_name = UNSET
        else:
            reviewer_name = self.reviewer_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "requester_user_id": requester_user_id,
                "requester_bot_id": requester_bot_id,
                "resource": resource,
                "action": action,
                "scope": scope,
                "justification": justification,
                "session_id": session_id,
                "task_id": task_id,
                "status": status,
                "reviewer_user_id": reviewer_user_id,
                "reviewer_comment": reviewer_comment,
                "created_at": created_at,
                "reviewed_at": reviewed_at,
            }
        )
        if requester_name is not UNSET:
            field_dict["requester_name"] = requester_name
        if requester_email is not UNSET:
            field_dict["requester_email"] = requester_email
        if reviewer_name is not UNSET:
            field_dict["reviewer_name"] = reviewer_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_org_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                org_id_type_0 = UUID(data)

                return org_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        org_id = _parse_org_id(d.pop("org_id"))

        requester_user_id = UUID(d.pop("requester_user_id"))

        def _parse_requester_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                requester_bot_id_type_0 = UUID(data)

                return requester_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        requester_bot_id = _parse_requester_bot_id(d.pop("requester_bot_id"))

        resource = d.pop("resource")

        action = d.pop("action")

        scope = d.pop("scope")

        justification = d.pop("justification")

        def _parse_session_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                session_id_type_0 = UUID(data)

                return session_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        session_id = _parse_session_id(d.pop("session_id"))

        def _parse_task_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                task_id_type_0 = UUID(data)

                return task_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        task_id = _parse_task_id(d.pop("task_id"))

        status = PermissionRequestResponseStatus(d.pop("status"))

        def _parse_reviewer_user_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reviewer_user_id_type_0 = UUID(data)

                return reviewer_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        reviewer_user_id = _parse_reviewer_user_id(d.pop("reviewer_user_id"))

        def _parse_reviewer_comment(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reviewer_comment = _parse_reviewer_comment(d.pop("reviewer_comment"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_reviewed_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reviewed_at_type_0 = datetime.datetime.fromisoformat(data)

                return reviewed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        reviewed_at = _parse_reviewed_at(d.pop("reviewed_at"))

        def _parse_requester_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        requester_name = _parse_requester_name(d.pop("requester_name", UNSET))

        def _parse_requester_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        requester_email = _parse_requester_email(d.pop("requester_email", UNSET))

        def _parse_reviewer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reviewer_name = _parse_reviewer_name(d.pop("reviewer_name", UNSET))

        permission_request_response = cls(
            id=id,
            org_id=org_id,
            requester_user_id=requester_user_id,
            requester_bot_id=requester_bot_id,
            resource=resource,
            action=action,
            scope=scope,
            justification=justification,
            session_id=session_id,
            task_id=task_id,
            status=status,
            reviewer_user_id=reviewer_user_id,
            reviewer_comment=reviewer_comment,
            created_at=created_at,
            reviewed_at=reviewed_at,
            requester_name=requester_name,
            requester_email=requester_email,
            reviewer_name=reviewer_name,
        )

        permission_request_response.additional_properties = d
        return permission_request_response

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
