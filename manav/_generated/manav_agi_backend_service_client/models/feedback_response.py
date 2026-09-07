from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feedback_response_source_metadata_type_0 import FeedbackResponseSourceMetadataType0


T = TypeVar("T", bound="FeedbackResponse")


@_attrs_define
class FeedbackResponse:
    """
    Attributes:
        id (UUID):
        target_entity_type (str):
        target_entity_id (UUID):
        kind (str):
        comment (str):
        author_id (UUID):
        author_type (str):
        author_role (str):
        source_channel (str):
        apply_status (str):
        org_id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        target_field (None | str | Unset):
        original_value (Any | None | Unset):
        corrected_value (Any | None | Unset):
        source_message_id (None | Unset | UUID):
        source_metadata (FeedbackResponseSourceMetadataType0 | None | Unset):
        applied_at (datetime.datetime | None | Unset):
        applied_error (None | str | Unset):
        applied_compensating_id (None | Unset | UUID):
    """

    id: UUID
    target_entity_type: str
    target_entity_id: UUID
    kind: str
    comment: str
    author_id: UUID
    author_type: str
    author_role: str
    source_channel: str
    apply_status: str
    org_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    target_field: None | str | Unset = UNSET
    original_value: Any | None | Unset = UNSET
    corrected_value: Any | None | Unset = UNSET
    source_message_id: None | Unset | UUID = UNSET
    source_metadata: FeedbackResponseSourceMetadataType0 | None | Unset = UNSET
    applied_at: datetime.datetime | None | Unset = UNSET
    applied_error: None | str | Unset = UNSET
    applied_compensating_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.feedback_response_source_metadata_type_0 import (
            FeedbackResponseSourceMetadataType0,  # noqa: PLC0415
        )

        id = str(self.id)

        target_entity_type = self.target_entity_type

        target_entity_id = str(self.target_entity_id)

        kind = self.kind

        comment = self.comment

        author_id = str(self.author_id)

        author_type = self.author_type

        author_role = self.author_role

        source_channel = self.source_channel

        apply_status = self.apply_status

        org_id = str(self.org_id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        target_field: None | str | Unset
        if isinstance(self.target_field, Unset):
            target_field = UNSET
        else:
            target_field = self.target_field

        original_value: Any | None | Unset
        if isinstance(self.original_value, Unset):
            original_value = UNSET
        else:
            original_value = self.original_value

        corrected_value: Any | None | Unset
        if isinstance(self.corrected_value, Unset):
            corrected_value = UNSET
        else:
            corrected_value = self.corrected_value

        source_message_id: None | str | Unset
        if isinstance(self.source_message_id, Unset):
            source_message_id = UNSET
        elif isinstance(self.source_message_id, UUID):
            source_message_id = str(self.source_message_id)
        else:
            source_message_id = self.source_message_id

        source_metadata: dict[str, Any] | None | Unset
        if isinstance(self.source_metadata, Unset):
            source_metadata = UNSET
        elif isinstance(self.source_metadata, FeedbackResponseSourceMetadataType0):
            source_metadata = self.source_metadata.to_dict()
        else:
            source_metadata = self.source_metadata

        applied_at: None | str | Unset
        if isinstance(self.applied_at, Unset):
            applied_at = UNSET
        elif isinstance(self.applied_at, datetime.datetime):
            applied_at = self.applied_at.isoformat()
        else:
            applied_at = self.applied_at

        applied_error: None | str | Unset
        if isinstance(self.applied_error, Unset):
            applied_error = UNSET
        else:
            applied_error = self.applied_error

        applied_compensating_id: None | str | Unset
        if isinstance(self.applied_compensating_id, Unset):
            applied_compensating_id = UNSET
        elif isinstance(self.applied_compensating_id, UUID):
            applied_compensating_id = str(self.applied_compensating_id)
        else:
            applied_compensating_id = self.applied_compensating_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "target_entity_type": target_entity_type,
                "target_entity_id": target_entity_id,
                "kind": kind,
                "comment": comment,
                "author_id": author_id,
                "author_type": author_type,
                "author_role": author_role,
                "source_channel": source_channel,
                "apply_status": apply_status,
                "org_id": org_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if target_field is not UNSET:
            field_dict["target_field"] = target_field
        if original_value is not UNSET:
            field_dict["original_value"] = original_value
        if corrected_value is not UNSET:
            field_dict["corrected_value"] = corrected_value
        if source_message_id is not UNSET:
            field_dict["source_message_id"] = source_message_id
        if source_metadata is not UNSET:
            field_dict["source_metadata"] = source_metadata
        if applied_at is not UNSET:
            field_dict["applied_at"] = applied_at
        if applied_error is not UNSET:
            field_dict["applied_error"] = applied_error
        if applied_compensating_id is not UNSET:
            field_dict["applied_compensating_id"] = applied_compensating_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.feedback_response_source_metadata_type_0 import (
            FeedbackResponseSourceMetadataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        target_entity_type = d.pop("target_entity_type")

        target_entity_id = UUID(d.pop("target_entity_id"))

        kind = d.pop("kind")

        comment = d.pop("comment")

        author_id = UUID(d.pop("author_id"))

        author_type = d.pop("author_type")

        author_role = d.pop("author_role")

        source_channel = d.pop("source_channel")

        apply_status = d.pop("apply_status")

        org_id = UUID(d.pop("org_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_target_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_field = _parse_target_field(d.pop("target_field", UNSET))

        def _parse_original_value(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        original_value = _parse_original_value(d.pop("original_value", UNSET))

        def _parse_corrected_value(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        corrected_value = _parse_corrected_value(d.pop("corrected_value", UNSET))

        def _parse_source_message_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_message_id_type_0 = UUID(data)

                return source_message_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_message_id = _parse_source_message_id(d.pop("source_message_id", UNSET))

        def _parse_source_metadata(data: object) -> FeedbackResponseSourceMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_metadata_type_0 = FeedbackResponseSourceMetadataType0.from_dict(data)

                return source_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FeedbackResponseSourceMetadataType0 | None | Unset, data)

        source_metadata = _parse_source_metadata(d.pop("source_metadata", UNSET))

        def _parse_applied_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                applied_at_type_0 = datetime.datetime.fromisoformat(data)

                return applied_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        applied_at = _parse_applied_at(d.pop("applied_at", UNSET))

        def _parse_applied_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        applied_error = _parse_applied_error(d.pop("applied_error", UNSET))

        def _parse_applied_compensating_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                applied_compensating_id_type_0 = UUID(data)

                return applied_compensating_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        applied_compensating_id = _parse_applied_compensating_id(d.pop("applied_compensating_id", UNSET))

        feedback_response = cls(
            id=id,
            target_entity_type=target_entity_type,
            target_entity_id=target_entity_id,
            kind=kind,
            comment=comment,
            author_id=author_id,
            author_type=author_type,
            author_role=author_role,
            source_channel=source_channel,
            apply_status=apply_status,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            target_field=target_field,
            original_value=original_value,
            corrected_value=corrected_value,
            source_message_id=source_message_id,
            source_metadata=source_metadata,
            applied_at=applied_at,
            applied_error=applied_error,
            applied_compensating_id=applied_compensating_id,
        )

        feedback_response.additional_properties = d
        return feedback_response

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
