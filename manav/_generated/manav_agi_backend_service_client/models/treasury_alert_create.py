from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.treasury_alert_severity import TreasuryAlertSeverity
from ..models.treasury_alert_type import TreasuryAlertType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.treasury_alert_create_affected_resource import TreasuryAlertCreateAffectedResource
    from ..models.treasury_alert_create_cited_evidence_item import TreasuryAlertCreateCitedEvidenceItem
    from ..models.treasury_alert_create_metric_observed import TreasuryAlertCreateMetricObserved
    from ..models.treasury_alert_create_projection_type_0 import TreasuryAlertCreateProjectionType0


T = TypeVar("T", bound="TreasuryAlertCreate")


@_attrs_define
class TreasuryAlertCreate:
    """
    Attributes:
        org_id (UUID):
        authoring_bot_id (UUID):
        alert_type (TreasuryAlertType): treasury_alerts.alert_type — what Kosha flagged.
        affected_resource (TreasuryAlertCreateAffectedResource):
        metric_observed (TreasuryAlertCreateMetricObserved):
        cited_evidence (list[TreasuryAlertCreateCitedEvidenceItem]):
        severity (TreasuryAlertSeverity | Unset): treasury_alerts.severity — how urgent. Default:
            TreasuryAlertSeverity.MEDIUM.
        projection (None | TreasuryAlertCreateProjectionType0 | Unset):
        recommended_action (None | str | Unset):
    """

    org_id: UUID
    authoring_bot_id: UUID
    alert_type: TreasuryAlertType
    affected_resource: TreasuryAlertCreateAffectedResource
    metric_observed: TreasuryAlertCreateMetricObserved
    cited_evidence: list[TreasuryAlertCreateCitedEvidenceItem]
    severity: TreasuryAlertSeverity | Unset = TreasuryAlertSeverity.MEDIUM
    projection: None | TreasuryAlertCreateProjectionType0 | Unset = UNSET
    recommended_action: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.treasury_alert_create_projection_type_0 import TreasuryAlertCreateProjectionType0  # noqa: PLC0415

        org_id = str(self.org_id)

        authoring_bot_id = str(self.authoring_bot_id)

        alert_type = self.alert_type.value

        affected_resource = self.affected_resource.to_dict()

        metric_observed = self.metric_observed.to_dict()

        cited_evidence = []
        for cited_evidence_item_data in self.cited_evidence:
            cited_evidence_item = cited_evidence_item_data.to_dict()
            cited_evidence.append(cited_evidence_item)

        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        projection: dict[str, Any] | None | Unset
        if isinstance(self.projection, Unset):
            projection = UNSET
        elif isinstance(self.projection, TreasuryAlertCreateProjectionType0):
            projection = self.projection.to_dict()
        else:
            projection = self.projection

        recommended_action: None | str | Unset
        if isinstance(self.recommended_action, Unset):
            recommended_action = UNSET
        else:
            recommended_action = self.recommended_action

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "org_id": org_id,
                "authoring_bot_id": authoring_bot_id,
                "alert_type": alert_type,
                "affected_resource": affected_resource,
                "metric_observed": metric_observed,
                "cited_evidence": cited_evidence,
            }
        )
        if severity is not UNSET:
            field_dict["severity"] = severity
        if projection is not UNSET:
            field_dict["projection"] = projection
        if recommended_action is not UNSET:
            field_dict["recommended_action"] = recommended_action

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.treasury_alert_create_affected_resource import (
            TreasuryAlertCreateAffectedResource,  # noqa: PLC0415
        )
        from ..models.treasury_alert_create_cited_evidence_item import (
            TreasuryAlertCreateCitedEvidenceItem,  # noqa: PLC0415
        )
        from ..models.treasury_alert_create_metric_observed import TreasuryAlertCreateMetricObserved  # noqa: PLC0415
        from ..models.treasury_alert_create_projection_type_0 import TreasuryAlertCreateProjectionType0  # noqa: PLC0415

        d = dict(src_dict)
        org_id = UUID(d.pop("org_id"))

        authoring_bot_id = UUID(d.pop("authoring_bot_id"))

        alert_type = TreasuryAlertType(d.pop("alert_type"))

        affected_resource = TreasuryAlertCreateAffectedResource.from_dict(d.pop("affected_resource"))

        metric_observed = TreasuryAlertCreateMetricObserved.from_dict(d.pop("metric_observed"))

        cited_evidence = []
        _cited_evidence = d.pop("cited_evidence")
        for cited_evidence_item_data in _cited_evidence:
            cited_evidence_item = TreasuryAlertCreateCitedEvidenceItem.from_dict(cited_evidence_item_data)

            cited_evidence.append(cited_evidence_item)

        _severity = d.pop("severity", UNSET)
        severity: TreasuryAlertSeverity | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = TreasuryAlertSeverity(_severity)

        def _parse_projection(data: object) -> None | TreasuryAlertCreateProjectionType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                projection_type_0 = TreasuryAlertCreateProjectionType0.from_dict(data)

                return projection_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TreasuryAlertCreateProjectionType0 | Unset, data)

        projection = _parse_projection(d.pop("projection", UNSET))

        def _parse_recommended_action(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recommended_action = _parse_recommended_action(d.pop("recommended_action", UNSET))

        treasury_alert_create = cls(
            org_id=org_id,
            authoring_bot_id=authoring_bot_id,
            alert_type=alert_type,
            affected_resource=affected_resource,
            metric_observed=metric_observed,
            cited_evidence=cited_evidence,
            severity=severity,
            projection=projection,
            recommended_action=recommended_action,
        )

        treasury_alert_create.additional_properties = d
        return treasury_alert_create

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
