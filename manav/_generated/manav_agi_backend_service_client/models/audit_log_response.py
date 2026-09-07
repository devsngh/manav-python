from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.audit_log_response_changes_type_0 import AuditLogResponseChangesType0
    from ..models.audit_log_response_extra_metadata_type_0 import AuditLogResponseExtraMetadataType0


T = TypeVar("T", bound="AuditLogResponse")


@_attrs_define
class AuditLogResponse:
    """
    Attributes:
        id (UUID):
        user_id (None | UUID):
        user_email (None | str):
        action (str):
        resource_type (str):
        resource_id (None | UUID):
        resource_name (None | str):
        changes (AuditLogResponseChangesType0 | None):
        extra_metadata (AuditLogResponseExtraMetadataType0 | None):
        org_id (None | UUID):
        created_at (datetime.datetime):
    """

    id: UUID
    user_id: None | UUID
    user_email: None | str
    action: str
    resource_type: str
    resource_id: None | UUID
    resource_name: None | str
    changes: AuditLogResponseChangesType0 | None
    extra_metadata: AuditLogResponseExtraMetadataType0 | None
    org_id: None | UUID
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.audit_log_response_changes_type_0 import AuditLogResponseChangesType0  # noqa: PLC0415
        from ..models.audit_log_response_extra_metadata_type_0 import (
            AuditLogResponseExtraMetadataType0,  # noqa: PLC0415
        )

        id = str(self.id)

        user_id: None | str
        if isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        user_email: None | str
        user_email = self.user_email

        action = self.action

        resource_type = self.resource_type

        resource_id: None | str
        if isinstance(self.resource_id, UUID):
            resource_id = str(self.resource_id)
        else:
            resource_id = self.resource_id

        resource_name: None | str
        resource_name = self.resource_name

        changes: dict[str, Any] | None
        if isinstance(self.changes, AuditLogResponseChangesType0):
            changes = self.changes.to_dict()
        else:
            changes = self.changes

        extra_metadata: dict[str, Any] | None
        if isinstance(self.extra_metadata, AuditLogResponseExtraMetadataType0):
            extra_metadata = self.extra_metadata.to_dict()
        else:
            extra_metadata = self.extra_metadata

        org_id: None | str
        if isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "user_email": user_email,
                "action": action,
                "resource_type": resource_type,
                "resource_id": resource_id,
                "resource_name": resource_name,
                "changes": changes,
                "extra_metadata": extra_metadata,
                "org_id": org_id,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_log_response_changes_type_0 import AuditLogResponseChangesType0  # noqa: PLC0415
        from ..models.audit_log_response_extra_metadata_type_0 import (
            AuditLogResponseExtraMetadataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_user_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        user_id = _parse_user_id(d.pop("user_id"))

        def _parse_user_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        user_email = _parse_user_email(d.pop("user_email"))

        action = d.pop("action")

        resource_type = d.pop("resource_type")

        def _parse_resource_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resource_id_type_0 = UUID(data)

                return resource_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        resource_id = _parse_resource_id(d.pop("resource_id"))

        def _parse_resource_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resource_name = _parse_resource_name(d.pop("resource_name"))

        def _parse_changes(data: object) -> AuditLogResponseChangesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                changes_type_0 = AuditLogResponseChangesType0.from_dict(data)

                return changes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AuditLogResponseChangesType0 | None, data)

        changes = _parse_changes(d.pop("changes"))

        def _parse_extra_metadata(data: object) -> AuditLogResponseExtraMetadataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extra_metadata_type_0 = AuditLogResponseExtraMetadataType0.from_dict(data)

                return extra_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AuditLogResponseExtraMetadataType0 | None, data)

        extra_metadata = _parse_extra_metadata(d.pop("extra_metadata"))

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

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        audit_log_response = cls(
            id=id,
            user_id=user_id,
            user_email=user_email,
            action=action,
            resource_type=resource_type,
            resource_id=resource_id,
            resource_name=resource_name,
            changes=changes,
            extra_metadata=extra_metadata,
            org_id=org_id,
            created_at=created_at,
        )

        audit_log_response.additional_properties = d
        return audit_log_response

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
