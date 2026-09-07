from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pattern_read_evidence import PatternReadEvidence


T = TypeVar("T", bound="PatternRead")


@_attrs_define
class PatternRead:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        pattern_type (str):
        signature (str):
        severity (str):
        title (str):
        occurrence_count (int):
        first_seen_at (datetime.datetime):
        last_seen_at (datetime.datetime):
        status (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        description (None | str | Unset):
        affected_bots (list[str] | Unset):
        evidence (PatternReadEvidence | Unset):
        dismissed_by (None | Unset | UUID):
        dismissed_at (datetime.datetime | None | Unset):
        dismiss_reason (None | str | Unset):
    """

    id: UUID
    org_id: UUID
    pattern_type: str
    signature: str
    severity: str
    title: str
    occurrence_count: int
    first_seen_at: datetime.datetime
    last_seen_at: datetime.datetime
    status: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: None | str | Unset = UNSET
    affected_bots: list[str] | Unset = UNSET
    evidence: PatternReadEvidence | Unset = UNSET
    dismissed_by: None | Unset | UUID = UNSET
    dismissed_at: datetime.datetime | None | Unset = UNSET
    dismiss_reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        org_id = str(self.org_id)

        pattern_type = self.pattern_type

        signature = self.signature

        severity = self.severity

        title = self.title

        occurrence_count = self.occurrence_count

        first_seen_at = self.first_seen_at.isoformat()

        last_seen_at = self.last_seen_at.isoformat()

        status = self.status

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        affected_bots: list[str] | Unset = UNSET
        if not isinstance(self.affected_bots, Unset):
            affected_bots = self.affected_bots

        evidence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.evidence, Unset):
            evidence = self.evidence.to_dict()

        dismissed_by: None | str | Unset
        if isinstance(self.dismissed_by, Unset):
            dismissed_by = UNSET
        elif isinstance(self.dismissed_by, UUID):
            dismissed_by = str(self.dismissed_by)
        else:
            dismissed_by = self.dismissed_by

        dismissed_at: None | str | Unset
        if isinstance(self.dismissed_at, Unset):
            dismissed_at = UNSET
        elif isinstance(self.dismissed_at, datetime.datetime):
            dismissed_at = self.dismissed_at.isoformat()
        else:
            dismissed_at = self.dismissed_at

        dismiss_reason: None | str | Unset
        if isinstance(self.dismiss_reason, Unset):
            dismiss_reason = UNSET
        else:
            dismiss_reason = self.dismiss_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "pattern_type": pattern_type,
                "signature": signature,
                "severity": severity,
                "title": title,
                "occurrence_count": occurrence_count,
                "first_seen_at": first_seen_at,
                "last_seen_at": last_seen_at,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if affected_bots is not UNSET:
            field_dict["affected_bots"] = affected_bots
        if evidence is not UNSET:
            field_dict["evidence"] = evidence
        if dismissed_by is not UNSET:
            field_dict["dismissed_by"] = dismissed_by
        if dismissed_at is not UNSET:
            field_dict["dismissed_at"] = dismissed_at
        if dismiss_reason is not UNSET:
            field_dict["dismiss_reason"] = dismiss_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pattern_read_evidence import PatternReadEvidence  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        pattern_type = d.pop("pattern_type")

        signature = d.pop("signature")

        severity = d.pop("severity")

        title = d.pop("title")

        occurrence_count = d.pop("occurrence_count")

        first_seen_at = datetime.datetime.fromisoformat(d.pop("first_seen_at"))

        last_seen_at = datetime.datetime.fromisoformat(d.pop("last_seen_at"))

        status = d.pop("status")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        affected_bots = cast(list[str], d.pop("affected_bots", UNSET))

        _evidence = d.pop("evidence", UNSET)
        evidence: PatternReadEvidence | Unset
        if isinstance(_evidence, Unset):
            evidence = UNSET
        else:
            evidence = PatternReadEvidence.from_dict(_evidence)

        def _parse_dismissed_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dismissed_by_type_0 = UUID(data)

                return dismissed_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        dismissed_by = _parse_dismissed_by(d.pop("dismissed_by", UNSET))

        def _parse_dismissed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dismissed_at_type_0 = datetime.datetime.fromisoformat(data)

                return dismissed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        dismissed_at = _parse_dismissed_at(d.pop("dismissed_at", UNSET))

        def _parse_dismiss_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dismiss_reason = _parse_dismiss_reason(d.pop("dismiss_reason", UNSET))

        pattern_read = cls(
            id=id,
            org_id=org_id,
            pattern_type=pattern_type,
            signature=signature,
            severity=severity,
            title=title,
            occurrence_count=occurrence_count,
            first_seen_at=first_seen_at,
            last_seen_at=last_seen_at,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            affected_bots=affected_bots,
            evidence=evidence,
            dismissed_by=dismissed_by,
            dismissed_at=dismissed_at,
            dismiss_reason=dismiss_reason,
        )

        pattern_read.additional_properties = d
        return pattern_read

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
