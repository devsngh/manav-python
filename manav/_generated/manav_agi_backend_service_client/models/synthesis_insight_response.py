from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.synthesis_insight_response_affected_bots_type_0_item import (
        SynthesisInsightResponseAffectedBotsType0Item,
    )
    from ..models.synthesis_insight_response_cited_streams_item import SynthesisInsightResponseCitedStreamsItem


T = TypeVar("T", bound="SynthesisInsightResponse")


@_attrs_define
class SynthesisInsightResponse:
    """
    Attributes:
        id (UUID):
        authoring_bot_id (UUID):
        pattern_type (str):
        observed_cluster (str):
        synthesis_claim (str):
        recommended_investigation (str):
        cited_streams (list[SynthesisInsightResponseCitedStreamsItem]):
        time_window_start (datetime.datetime):
        time_window_end (datetime.datetime):
        severity (str):
        surfaced_to_transformer (bool):
        surfaced_to_principal (bool):
        status (str):
        org_id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        counter_position (None | str | Unset):
        affected_bots (list[SynthesisInsightResponseAffectedBotsType0Item] | None | Unset):
        retracted_at (datetime.datetime | None | Unset):
        retraction_reason (None | str | Unset):
    """

    id: UUID
    authoring_bot_id: UUID
    pattern_type: str
    observed_cluster: str
    synthesis_claim: str
    recommended_investigation: str
    cited_streams: list[SynthesisInsightResponseCitedStreamsItem]
    time_window_start: datetime.datetime
    time_window_end: datetime.datetime
    severity: str
    surfaced_to_transformer: bool
    surfaced_to_principal: bool
    status: str
    org_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    counter_position: None | str | Unset = UNSET
    affected_bots: list[SynthesisInsightResponseAffectedBotsType0Item] | None | Unset = UNSET
    retracted_at: datetime.datetime | None | Unset = UNSET
    retraction_reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        authoring_bot_id = str(self.authoring_bot_id)

        pattern_type = self.pattern_type

        observed_cluster = self.observed_cluster

        synthesis_claim = self.synthesis_claim

        recommended_investigation = self.recommended_investigation

        cited_streams = []
        for cited_streams_item_data in self.cited_streams:
            cited_streams_item = cited_streams_item_data.to_dict()
            cited_streams.append(cited_streams_item)

        time_window_start = self.time_window_start.isoformat()

        time_window_end = self.time_window_end.isoformat()

        severity = self.severity

        surfaced_to_transformer = self.surfaced_to_transformer

        surfaced_to_principal = self.surfaced_to_principal

        status = self.status

        org_id = str(self.org_id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        counter_position: None | str | Unset
        if isinstance(self.counter_position, Unset):
            counter_position = UNSET
        else:
            counter_position = self.counter_position

        affected_bots: list[dict[str, Any]] | None | Unset
        if isinstance(self.affected_bots, Unset):
            affected_bots = UNSET
        elif isinstance(self.affected_bots, list):
            affected_bots = []
            for affected_bots_type_0_item_data in self.affected_bots:
                affected_bots_type_0_item = affected_bots_type_0_item_data.to_dict()
                affected_bots.append(affected_bots_type_0_item)

        else:
            affected_bots = self.affected_bots

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
                "authoring_bot_id": authoring_bot_id,
                "pattern_type": pattern_type,
                "observed_cluster": observed_cluster,
                "synthesis_claim": synthesis_claim,
                "recommended_investigation": recommended_investigation,
                "cited_streams": cited_streams,
                "time_window_start": time_window_start,
                "time_window_end": time_window_end,
                "severity": severity,
                "surfaced_to_transformer": surfaced_to_transformer,
                "surfaced_to_principal": surfaced_to_principal,
                "status": status,
                "org_id": org_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if counter_position is not UNSET:
            field_dict["counter_position"] = counter_position
        if affected_bots is not UNSET:
            field_dict["affected_bots"] = affected_bots
        if retracted_at is not UNSET:
            field_dict["retracted_at"] = retracted_at
        if retraction_reason is not UNSET:
            field_dict["retraction_reason"] = retraction_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.synthesis_insight_response_affected_bots_type_0_item import (
            SynthesisInsightResponseAffectedBotsType0Item,  # noqa: PLC0415
        )
        from ..models.synthesis_insight_response_cited_streams_item import (
            SynthesisInsightResponseCitedStreamsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        authoring_bot_id = UUID(d.pop("authoring_bot_id"))

        pattern_type = d.pop("pattern_type")

        observed_cluster = d.pop("observed_cluster")

        synthesis_claim = d.pop("synthesis_claim")

        recommended_investigation = d.pop("recommended_investigation")

        cited_streams = []
        _cited_streams = d.pop("cited_streams")
        for cited_streams_item_data in _cited_streams:
            cited_streams_item = SynthesisInsightResponseCitedStreamsItem.from_dict(cited_streams_item_data)

            cited_streams.append(cited_streams_item)

        time_window_start = datetime.datetime.fromisoformat(d.pop("time_window_start"))

        time_window_end = datetime.datetime.fromisoformat(d.pop("time_window_end"))

        severity = d.pop("severity")

        surfaced_to_transformer = d.pop("surfaced_to_transformer")

        surfaced_to_principal = d.pop("surfaced_to_principal")

        status = d.pop("status")

        org_id = UUID(d.pop("org_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_counter_position(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        counter_position = _parse_counter_position(d.pop("counter_position", UNSET))

        def _parse_affected_bots(data: object) -> list[SynthesisInsightResponseAffectedBotsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                affected_bots_type_0 = []
                _affected_bots_type_0 = data
                for affected_bots_type_0_item_data in _affected_bots_type_0:
                    affected_bots_type_0_item = SynthesisInsightResponseAffectedBotsType0Item.from_dict(
                        affected_bots_type_0_item_data
                    )

                    affected_bots_type_0.append(affected_bots_type_0_item)

                return affected_bots_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SynthesisInsightResponseAffectedBotsType0Item] | None | Unset, data)

        affected_bots = _parse_affected_bots(d.pop("affected_bots", UNSET))

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

        synthesis_insight_response = cls(
            id=id,
            authoring_bot_id=authoring_bot_id,
            pattern_type=pattern_type,
            observed_cluster=observed_cluster,
            synthesis_claim=synthesis_claim,
            recommended_investigation=recommended_investigation,
            cited_streams=cited_streams,
            time_window_start=time_window_start,
            time_window_end=time_window_end,
            severity=severity,
            surfaced_to_transformer=surfaced_to_transformer,
            surfaced_to_principal=surfaced_to_principal,
            status=status,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            counter_position=counter_position,
            affected_bots=affected_bots,
            retracted_at=retracted_at,
            retraction_reason=retraction_reason,
        )

        synthesis_insight_response.additional_properties = d
        return synthesis_insight_response

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
