from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.proposal_status import ProposalStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="TransformationProposalUpdate")


@_attrs_define
class TransformationProposalUpdate:
    """Patch — status transitions + lifecycle timestamps + actors.

    Attributes:
        status (None | ProposalStatus | Unset):
        surfaced_at (datetime.datetime | None | Unset):
        ratified_at (datetime.datetime | None | Unset):
        ratified_by (None | Unset | UUID):
        committed_at (datetime.datetime | None | Unset):
        committed_deepagent_id (None | Unset | UUID):
        certified_at (datetime.datetime | None | Unset):
        certification_round_id (None | Unset | UUID):
        rejected_reason (None | str | Unset):
        withdrawn_reason (None | str | Unset):
    """

    status: None | ProposalStatus | Unset = UNSET
    surfaced_at: datetime.datetime | None | Unset = UNSET
    ratified_at: datetime.datetime | None | Unset = UNSET
    ratified_by: None | Unset | UUID = UNSET
    committed_at: datetime.datetime | None | Unset = UNSET
    committed_deepagent_id: None | Unset | UUID = UNSET
    certified_at: datetime.datetime | None | Unset = UNSET
    certification_round_id: None | Unset | UUID = UNSET
    rejected_reason: None | str | Unset = UNSET
    withdrawn_reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, ProposalStatus):
            status = self.status.value
        else:
            status = self.status

        surfaced_at: None | str | Unset
        if isinstance(self.surfaced_at, Unset):
            surfaced_at = UNSET
        elif isinstance(self.surfaced_at, datetime.datetime):
            surfaced_at = self.surfaced_at.isoformat()
        else:
            surfaced_at = self.surfaced_at

        ratified_at: None | str | Unset
        if isinstance(self.ratified_at, Unset):
            ratified_at = UNSET
        elif isinstance(self.ratified_at, datetime.datetime):
            ratified_at = self.ratified_at.isoformat()
        else:
            ratified_at = self.ratified_at

        ratified_by: None | str | Unset
        if isinstance(self.ratified_by, Unset):
            ratified_by = UNSET
        elif isinstance(self.ratified_by, UUID):
            ratified_by = str(self.ratified_by)
        else:
            ratified_by = self.ratified_by

        committed_at: None | str | Unset
        if isinstance(self.committed_at, Unset):
            committed_at = UNSET
        elif isinstance(self.committed_at, datetime.datetime):
            committed_at = self.committed_at.isoformat()
        else:
            committed_at = self.committed_at

        committed_deepagent_id: None | str | Unset
        if isinstance(self.committed_deepagent_id, Unset):
            committed_deepagent_id = UNSET
        elif isinstance(self.committed_deepagent_id, UUID):
            committed_deepagent_id = str(self.committed_deepagent_id)
        else:
            committed_deepagent_id = self.committed_deepagent_id

        certified_at: None | str | Unset
        if isinstance(self.certified_at, Unset):
            certified_at = UNSET
        elif isinstance(self.certified_at, datetime.datetime):
            certified_at = self.certified_at.isoformat()
        else:
            certified_at = self.certified_at

        certification_round_id: None | str | Unset
        if isinstance(self.certification_round_id, Unset):
            certification_round_id = UNSET
        elif isinstance(self.certification_round_id, UUID):
            certification_round_id = str(self.certification_round_id)
        else:
            certification_round_id = self.certification_round_id

        rejected_reason: None | str | Unset
        if isinstance(self.rejected_reason, Unset):
            rejected_reason = UNSET
        else:
            rejected_reason = self.rejected_reason

        withdrawn_reason: None | str | Unset
        if isinstance(self.withdrawn_reason, Unset):
            withdrawn_reason = UNSET
        else:
            withdrawn_reason = self.withdrawn_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if surfaced_at is not UNSET:
            field_dict["surfaced_at"] = surfaced_at
        if ratified_at is not UNSET:
            field_dict["ratified_at"] = ratified_at
        if ratified_by is not UNSET:
            field_dict["ratified_by"] = ratified_by
        if committed_at is not UNSET:
            field_dict["committed_at"] = committed_at
        if committed_deepagent_id is not UNSET:
            field_dict["committed_deepagent_id"] = committed_deepagent_id
        if certified_at is not UNSET:
            field_dict["certified_at"] = certified_at
        if certification_round_id is not UNSET:
            field_dict["certification_round_id"] = certification_round_id
        if rejected_reason is not UNSET:
            field_dict["rejected_reason"] = rejected_reason
        if withdrawn_reason is not UNSET:
            field_dict["withdrawn_reason"] = withdrawn_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_status(data: object) -> None | ProposalStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = ProposalStatus(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProposalStatus | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_surfaced_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                surfaced_at_type_0 = datetime.datetime.fromisoformat(data)

                return surfaced_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        surfaced_at = _parse_surfaced_at(d.pop("surfaced_at", UNSET))

        def _parse_ratified_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ratified_at_type_0 = datetime.datetime.fromisoformat(data)

                return ratified_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        ratified_at = _parse_ratified_at(d.pop("ratified_at", UNSET))

        def _parse_ratified_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ratified_by_type_0 = UUID(data)

                return ratified_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        ratified_by = _parse_ratified_by(d.pop("ratified_by", UNSET))

        def _parse_committed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                committed_at_type_0 = datetime.datetime.fromisoformat(data)

                return committed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        committed_at = _parse_committed_at(d.pop("committed_at", UNSET))

        def _parse_committed_deepagent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                committed_deepagent_id_type_0 = UUID(data)

                return committed_deepagent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        committed_deepagent_id = _parse_committed_deepagent_id(d.pop("committed_deepagent_id", UNSET))

        def _parse_certified_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                certified_at_type_0 = datetime.datetime.fromisoformat(data)

                return certified_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        certified_at = _parse_certified_at(d.pop("certified_at", UNSET))

        def _parse_certification_round_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                certification_round_id_type_0 = UUID(data)

                return certification_round_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        certification_round_id = _parse_certification_round_id(d.pop("certification_round_id", UNSET))

        def _parse_rejected_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rejected_reason = _parse_rejected_reason(d.pop("rejected_reason", UNSET))

        def _parse_withdrawn_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        withdrawn_reason = _parse_withdrawn_reason(d.pop("withdrawn_reason", UNSET))

        transformation_proposal_update = cls(
            status=status,
            surfaced_at=surfaced_at,
            ratified_at=ratified_at,
            ratified_by=ratified_by,
            committed_at=committed_at,
            committed_deepagent_id=committed_deepagent_id,
            certified_at=certified_at,
            certification_round_id=certification_round_id,
            rejected_reason=rejected_reason,
            withdrawn_reason=withdrawn_reason,
        )

        transformation_proposal_update.additional_properties = d
        return transformation_proposal_update

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
