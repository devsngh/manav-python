from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.treasury_alert_response_affected_resource import TreasuryAlertResponseAffectedResource
    from ..models.treasury_alert_response_cited_evidence_item import TreasuryAlertResponseCitedEvidenceItem
    from ..models.treasury_alert_response_metric_observed import TreasuryAlertResponseMetricObserved
    from ..models.treasury_alert_response_projection_type_0 import TreasuryAlertResponseProjectionType0


T = TypeVar("T", bound="TreasuryAlertResponse")


@_attrs_define
class TreasuryAlertResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        authoring_bot_id (UUID):
        alert_type (str):
        severity (str):
        affected_resource (TreasuryAlertResponseAffectedResource):
        metric_observed (TreasuryAlertResponseMetricObserved):
        cited_evidence (list[TreasuryAlertResponseCitedEvidenceItem]):
        status (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        projection (None | TreasuryAlertResponseProjectionType0 | Unset):
        recommended_action (None | str | Unset):
        acknowledged_by (None | Unset | UUID):
        acknowledged_at (datetime.datetime | None | Unset):
        resolved_at (datetime.datetime | None | Unset):
        retracted_at (datetime.datetime | None | Unset):
        retraction_reason (None | str | Unset):
    """

    id: UUID
    org_id: UUID
    authoring_bot_id: UUID
    alert_type: str
    severity: str
    affected_resource: TreasuryAlertResponseAffectedResource
    metric_observed: TreasuryAlertResponseMetricObserved
    cited_evidence: list[TreasuryAlertResponseCitedEvidenceItem]
    status: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    projection: None | TreasuryAlertResponseProjectionType0 | Unset = UNSET
    recommended_action: None | str | Unset = UNSET
    acknowledged_by: None | Unset | UUID = UNSET
    acknowledged_at: datetime.datetime | None | Unset = UNSET
    resolved_at: datetime.datetime | None | Unset = UNSET
    retracted_at: datetime.datetime | None | Unset = UNSET
    retraction_reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.treasury_alert_response_projection_type_0 import (
            TreasuryAlertResponseProjectionType0,  # noqa: PLC0415
        )

        id = str(self.id)

        org_id = str(self.org_id)

        authoring_bot_id = str(self.authoring_bot_id)

        alert_type = self.alert_type

        severity = self.severity

        affected_resource = self.affected_resource.to_dict()

        metric_observed = self.metric_observed.to_dict()

        cited_evidence = []
        for cited_evidence_item_data in self.cited_evidence:
            cited_evidence_item = cited_evidence_item_data.to_dict()
            cited_evidence.append(cited_evidence_item)

        status = self.status

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        projection: dict[str, Any] | None | Unset
        if isinstance(self.projection, Unset):
            projection = UNSET
        elif isinstance(self.projection, TreasuryAlertResponseProjectionType0):
            projection = self.projection.to_dict()
        else:
            projection = self.projection

        recommended_action: None | str | Unset
        if isinstance(self.recommended_action, Unset):
            recommended_action = UNSET
        else:
            recommended_action = self.recommended_action

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
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "authoring_bot_id": authoring_bot_id,
                "alert_type": alert_type,
                "severity": severity,
                "affected_resource": affected_resource,
                "metric_observed": metric_observed,
                "cited_evidence": cited_evidence,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if projection is not UNSET:
            field_dict["projection"] = projection
        if recommended_action is not UNSET:
            field_dict["recommended_action"] = recommended_action
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
        from ..models.treasury_alert_response_affected_resource import (
            TreasuryAlertResponseAffectedResource,  # noqa: PLC0415
        )
        from ..models.treasury_alert_response_cited_evidence_item import (
            TreasuryAlertResponseCitedEvidenceItem,  # noqa: PLC0415
        )
        from ..models.treasury_alert_response_metric_observed import (
            TreasuryAlertResponseMetricObserved,  # noqa: PLC0415
        )
        from ..models.treasury_alert_response_projection_type_0 import (
            TreasuryAlertResponseProjectionType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        authoring_bot_id = UUID(d.pop("authoring_bot_id"))

        alert_type = d.pop("alert_type")

        severity = d.pop("severity")

        affected_resource = TreasuryAlertResponseAffectedResource.from_dict(d.pop("affected_resource"))

        metric_observed = TreasuryAlertResponseMetricObserved.from_dict(d.pop("metric_observed"))

        cited_evidence = []
        _cited_evidence = d.pop("cited_evidence")
        for cited_evidence_item_data in _cited_evidence:
            cited_evidence_item = TreasuryAlertResponseCitedEvidenceItem.from_dict(cited_evidence_item_data)

            cited_evidence.append(cited_evidence_item)

        status = d.pop("status")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_projection(data: object) -> None | TreasuryAlertResponseProjectionType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                projection_type_0 = TreasuryAlertResponseProjectionType0.from_dict(data)

                return projection_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TreasuryAlertResponseProjectionType0 | Unset, data)

        projection = _parse_projection(d.pop("projection", UNSET))

        def _parse_recommended_action(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recommended_action = _parse_recommended_action(d.pop("recommended_action", UNSET))

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

        treasury_alert_response = cls(
            id=id,
            org_id=org_id,
            authoring_bot_id=authoring_bot_id,
            alert_type=alert_type,
            severity=severity,
            affected_resource=affected_resource,
            metric_observed=metric_observed,
            cited_evidence=cited_evidence,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            projection=projection,
            recommended_action=recommended_action,
            acknowledged_by=acknowledged_by,
            acknowledged_at=acknowledged_at,
            resolved_at=resolved_at,
            retracted_at=retracted_at,
            retraction_reason=retraction_reason,
        )

        treasury_alert_response.additional_properties = d
        return treasury_alert_response

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
