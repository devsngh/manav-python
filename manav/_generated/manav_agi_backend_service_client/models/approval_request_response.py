from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_request_response_metadata_type_0 import ApprovalRequestResponseMetadataType0


T = TypeVar("T", bound="ApprovalRequestResponse")


@_attrs_define
class ApprovalRequestResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        policy_id (UUID):
        resource_type (str):
        resource_id (UUID):
        resource_summary (None | str):
        requested_amount (None | str):
        requested_currency_id (None | UUID):
        requested_by_bot_id (None | UUID):
        status (str):
        resolved_at (datetime.datetime | None):
        resolution_note (None | str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        metadata (ApprovalRequestResponseMetadataType0 | None | Unset):
    """

    id: UUID
    org_id: UUID
    policy_id: UUID
    resource_type: str
    resource_id: UUID
    resource_summary: None | str
    requested_amount: None | str
    requested_currency_id: None | UUID
    requested_by_bot_id: None | UUID
    status: str
    resolved_at: datetime.datetime | None
    resolution_note: None | str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata: ApprovalRequestResponseMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.approval_request_response_metadata_type_0 import (
            ApprovalRequestResponseMetadataType0,  # noqa: PLC0415
        )

        id = str(self.id)

        org_id = str(self.org_id)

        policy_id = str(self.policy_id)

        resource_type = self.resource_type

        resource_id = str(self.resource_id)

        resource_summary: None | str
        resource_summary = self.resource_summary

        requested_amount: None | str
        requested_amount = self.requested_amount

        requested_currency_id: None | str
        if isinstance(self.requested_currency_id, UUID):
            requested_currency_id = str(self.requested_currency_id)
        else:
            requested_currency_id = self.requested_currency_id

        requested_by_bot_id: None | str
        if isinstance(self.requested_by_bot_id, UUID):
            requested_by_bot_id = str(self.requested_by_bot_id)
        else:
            requested_by_bot_id = self.requested_by_bot_id

        status = self.status

        resolved_at: None | str
        if isinstance(self.resolved_at, datetime.datetime):
            resolved_at = self.resolved_at.isoformat()
        else:
            resolved_at = self.resolved_at

        resolution_note: None | str
        resolution_note = self.resolution_note

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, ApprovalRequestResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "policy_id": policy_id,
                "resource_type": resource_type,
                "resource_id": resource_id,
                "resource_summary": resource_summary,
                "requested_amount": requested_amount,
                "requested_currency_id": requested_currency_id,
                "requested_by_bot_id": requested_by_bot_id,
                "status": status,
                "resolved_at": resolved_at,
                "resolution_note": resolution_note,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.approval_request_response_metadata_type_0 import (
            ApprovalRequestResponseMetadataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        policy_id = UUID(d.pop("policy_id"))

        resource_type = d.pop("resource_type")

        resource_id = UUID(d.pop("resource_id"))

        def _parse_resource_summary(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resource_summary = _parse_resource_summary(d.pop("resource_summary"))

        def _parse_requested_amount(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        requested_amount = _parse_requested_amount(d.pop("requested_amount"))

        def _parse_requested_currency_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                requested_currency_id_type_0 = UUID(data)

                return requested_currency_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        requested_currency_id = _parse_requested_currency_id(d.pop("requested_currency_id"))

        def _parse_requested_by_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                requested_by_bot_id_type_0 = UUID(data)

                return requested_by_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        requested_by_bot_id = _parse_requested_by_bot_id(d.pop("requested_by_bot_id"))

        status = d.pop("status")

        def _parse_resolved_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_at_type_0 = datetime.datetime.fromisoformat(data)

                return resolved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        resolved_at = _parse_resolved_at(d.pop("resolved_at"))

        def _parse_resolution_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolution_note = _parse_resolution_note(d.pop("resolution_note"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_metadata(data: object) -> ApprovalRequestResponseMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = ApprovalRequestResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApprovalRequestResponseMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        approval_request_response = cls(
            id=id,
            org_id=org_id,
            policy_id=policy_id,
            resource_type=resource_type,
            resource_id=resource_id,
            resource_summary=resource_summary,
            requested_amount=requested_amount,
            requested_currency_id=requested_currency_id,
            requested_by_bot_id=requested_by_bot_id,
            status=status,
            resolved_at=resolved_at,
            resolution_note=resolution_note,
            created_at=created_at,
            updated_at=updated_at,
            metadata=metadata,
        )

        approval_request_response.additional_properties = d
        return approval_request_response

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
