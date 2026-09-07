from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LegalConsentRecord")


@_attrs_define
class LegalConsentRecord:
    """Server-emitted record of a stored consent — used as the response shape
    for the standalone re-consent endpoint.

        Attributes:
            id (UUID):
            user_id (UUID):
            document_type (str):
            document_version (str):
            accepted (bool):
            accepted_at (datetime.datetime):
    """

    id: UUID
    user_id: UUID
    document_type: str
    document_version: str
    accepted: bool
    accepted_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        user_id = str(self.user_id)

        document_type = self.document_type

        document_version = self.document_version

        accepted = self.accepted

        accepted_at = self.accepted_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "document_type": document_type,
                "document_version": document_version,
                "accepted": accepted,
                "accepted_at": accepted_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        user_id = UUID(d.pop("user_id"))

        document_type = d.pop("document_type")

        document_version = d.pop("document_version")

        accepted = d.pop("accepted")

        accepted_at = datetime.datetime.fromisoformat(d.pop("accepted_at"))

        legal_consent_record = cls(
            id=id,
            user_id=user_id,
            document_type=document_type,
            document_version=document_version,
            accepted=accepted,
            accepted_at=accepted_at,
        )

        legal_consent_record.additional_properties = d
        return legal_consent_record

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
