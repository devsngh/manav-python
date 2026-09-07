from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.treasury_alert_status import TreasuryAlertStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="TreasuryAlertUpdate")


@_attrs_define
class TreasuryAlertUpdate:
    """Patch — lifecycle transitions + retraction.

    Attributes:
        status (None | TreasuryAlertStatus | Unset):
        acknowledged_by (None | Unset | UUID):
        acknowledged_at (datetime.datetime | None | Unset):
        resolved_at (datetime.datetime | None | Unset):
        retracted_at (datetime.datetime | None | Unset):
        retraction_reason (None | str | Unset):
    """

    status: None | TreasuryAlertStatus | Unset = UNSET
    acknowledged_by: None | Unset | UUID = UNSET
    acknowledged_at: datetime.datetime | None | Unset = UNSET
    resolved_at: datetime.datetime | None | Unset = UNSET
    retracted_at: datetime.datetime | None | Unset = UNSET
    retraction_reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, TreasuryAlertStatus):
            status = self.status.value
        else:
            status = self.status

        acknowledged_by: None | str | Unset
        if isinstance(self.acknowledged_by, Unset):
            acknowledged_by = UNSET
        elif isinstance(self.acknowledged_by, UUID):
            acknowledged_by = str(self.acknowledged_by)
        else:
            acknowledged_by = self.acknowledged_by

        acknowledged_at: None | str | Unset
        if isinstance(self.acknowledged_at, Unset):
            acknowledged_at = UNSET
        elif isinstance(self.acknowledged_at, datetime.datetime):
            acknowledged_at = self.acknowledged_at.isoformat()
        else:
            acknowledged_at = self.acknowledged_at

        resolved_at: None | str | Unset
        if isinstance(self.resolved_at, Unset):
            resolved_at = UNSET
        elif isinstance(self.resolved_at, datetime.datetime):
            resolved_at = self.resolved_at.isoformat()
        else:
            resolved_at = self.resolved_at

        retracted_at: None | str | Unset
        if isinstance(self.retracted_at, Unset):
            retracted_at = UNSET
        elif isinstance(self.retracted_at, datetime.datetime):
            retracted_at = self.retracted_at.isoformat()
        else:
            retracted_at = self.retracted_at

        retraction_reason: None | str | Unset
        if isinstance(self.retraction_reason, Unset):
            retraction_reason = UNSET
        else:
            retraction_reason = self.retraction_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if acknowledged_by is not UNSET:
            field_dict["acknowledged_by"] = acknowledged_by
        if acknowledged_at is not UNSET:
            field_dict["acknowledged_at"] = acknowledged_at
        if resolved_at is not UNSET:
            field_dict["resolved_at"] = resolved_at
        if retracted_at is not UNSET:
            field_dict["retracted_at"] = retracted_at
        if retraction_reason is not UNSET:
            field_dict["retraction_reason"] = retraction_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_status(data: object) -> None | TreasuryAlertStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = TreasuryAlertStatus(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TreasuryAlertStatus | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_acknowledged_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acknowledged_by_type_0 = UUID(data)

                return acknowledged_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        acknowledged_by = _parse_acknowledged_by(d.pop("acknowledged_by", UNSET))

        def _parse_acknowledged_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acknowledged_at_type_0 = datetime.datetime.fromisoformat(data)

                return acknowledged_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        acknowledged_at = _parse_acknowledged_at(d.pop("acknowledged_at", UNSET))

        def _parse_resolved_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_at_type_0 = datetime.datetime.fromisoformat(data)

                return resolved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        resolved_at = _parse_resolved_at(d.pop("resolved_at", UNSET))

        def _parse_retracted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                retracted_at_type_0 = datetime.datetime.fromisoformat(data)

                return retracted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        retracted_at = _parse_retracted_at(d.pop("retracted_at", UNSET))

        def _parse_retraction_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        retraction_reason = _parse_retraction_reason(d.pop("retraction_reason", UNSET))

        treasury_alert_update = cls(
            status=status,
            acknowledged_by=acknowledged_by,
            acknowledged_at=acknowledged_at,
            resolved_at=resolved_at,
            retracted_at=retracted_at,
            retraction_reason=retraction_reason,
        )

        treasury_alert_update.additional_properties = d
        return treasury_alert_update

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
