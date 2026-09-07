from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.insight_status import InsightStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SynthesisInsightUpdate")


@_attrs_define
class SynthesisInsightUpdate:
    """Patch — status transitions, surfacing flags, retraction.

    Attributes:
        status (InsightStatus | None | Unset):
        surfaced_to_transformer (bool | None | Unset):
        surfaced_to_principal (bool | None | Unset):
        retracted_at (datetime.datetime | None | Unset):
        retraction_reason (None | str | Unset):
    """

    status: InsightStatus | None | Unset = UNSET
    surfaced_to_transformer: bool | None | Unset = UNSET
    surfaced_to_principal: bool | None | Unset = UNSET
    retracted_at: datetime.datetime | None | Unset = UNSET
    retraction_reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, InsightStatus):
            status = self.status.value
        else:
            status = self.status

        surfaced_to_transformer: bool | None | Unset
        if isinstance(self.surfaced_to_transformer, Unset):
            surfaced_to_transformer = UNSET
        else:
            surfaced_to_transformer = self.surfaced_to_transformer

        surfaced_to_principal: bool | None | Unset
        if isinstance(self.surfaced_to_principal, Unset):
            surfaced_to_principal = UNSET
        else:
            surfaced_to_principal = self.surfaced_to_principal

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
        if surfaced_to_transformer is not UNSET:
            field_dict["surfaced_to_transformer"] = surfaced_to_transformer
        if surfaced_to_principal is not UNSET:
            field_dict["surfaced_to_principal"] = surfaced_to_principal
        if retracted_at is not UNSET:
            field_dict["retracted_at"] = retracted_at
        if retraction_reason is not UNSET:
            field_dict["retraction_reason"] = retraction_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_status(data: object) -> InsightStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = InsightStatus(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InsightStatus | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_surfaced_to_transformer(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        surfaced_to_transformer = _parse_surfaced_to_transformer(d.pop("surfaced_to_transformer", UNSET))

        def _parse_surfaced_to_principal(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        surfaced_to_principal = _parse_surfaced_to_principal(d.pop("surfaced_to_principal", UNSET))

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

        synthesis_insight_update = cls(
            status=status,
            surfaced_to_transformer=surfaced_to_transformer,
            surfaced_to_principal=surfaced_to_principal,
            retracted_at=retracted_at,
            retraction_reason=retraction_reason,
        )

        synthesis_insight_update.additional_properties = d
        return synthesis_insight_update

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
