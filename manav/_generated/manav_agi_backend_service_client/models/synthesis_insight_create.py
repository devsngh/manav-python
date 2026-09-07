from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.insight_severity import InsightSeverity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.synthesis_insight_create_affected_bots_type_0_item import SynthesisInsightCreateAffectedBotsType0Item
    from ..models.synthesis_insight_create_cited_streams_item import SynthesisInsightCreateCitedStreamsItem


T = TypeVar("T", bound="SynthesisInsightCreate")


@_attrs_define
class SynthesisInsightCreate:
    """
    Attributes:
        authoring_bot_id (UUID):
        pattern_type (str):
        observed_cluster (str):
        synthesis_claim (str):
        recommended_investigation (str):
        cited_streams (list[SynthesisInsightCreateCitedStreamsItem]):
        time_window_start (datetime.datetime):
        time_window_end (datetime.datetime):
        org_id (UUID):
        counter_position (None | str | Unset):
        affected_bots (list[SynthesisInsightCreateAffectedBotsType0Item] | None | Unset):
        severity (InsightSeverity | Unset): anveshana_insights.severity — how urgent the pattern is. Default:
            InsightSeverity.MEDIUM.
    """

    authoring_bot_id: UUID
    pattern_type: str
    observed_cluster: str
    synthesis_claim: str
    recommended_investigation: str
    cited_streams: list[SynthesisInsightCreateCitedStreamsItem]
    time_window_start: datetime.datetime
    time_window_end: datetime.datetime
    org_id: UUID
    counter_position: None | str | Unset = UNSET
    affected_bots: list[SynthesisInsightCreateAffectedBotsType0Item] | None | Unset = UNSET
    severity: InsightSeverity | Unset = InsightSeverity.MEDIUM
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        org_id = str(self.org_id)

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

        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authoring_bot_id": authoring_bot_id,
                "pattern_type": pattern_type,
                "observed_cluster": observed_cluster,
                "synthesis_claim": synthesis_claim,
                "recommended_investigation": recommended_investigation,
                "cited_streams": cited_streams,
                "time_window_start": time_window_start,
                "time_window_end": time_window_end,
                "org_id": org_id,
            }
        )
        if counter_position is not UNSET:
            field_dict["counter_position"] = counter_position
        if affected_bots is not UNSET:
            field_dict["affected_bots"] = affected_bots
        if severity is not UNSET:
            field_dict["severity"] = severity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.synthesis_insight_create_affected_bots_type_0_item import (
            SynthesisInsightCreateAffectedBotsType0Item,  # noqa: PLC0415
        )
        from ..models.synthesis_insight_create_cited_streams_item import (
            SynthesisInsightCreateCitedStreamsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        authoring_bot_id = UUID(d.pop("authoring_bot_id"))

        pattern_type = d.pop("pattern_type")

        observed_cluster = d.pop("observed_cluster")

        synthesis_claim = d.pop("synthesis_claim")

        recommended_investigation = d.pop("recommended_investigation")

        cited_streams = []
        _cited_streams = d.pop("cited_streams")
        for cited_streams_item_data in _cited_streams:
            cited_streams_item = SynthesisInsightCreateCitedStreamsItem.from_dict(cited_streams_item_data)

            cited_streams.append(cited_streams_item)

        time_window_start = datetime.datetime.fromisoformat(d.pop("time_window_start"))

        time_window_end = datetime.datetime.fromisoformat(d.pop("time_window_end"))

        org_id = UUID(d.pop("org_id"))

        def _parse_counter_position(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        counter_position = _parse_counter_position(d.pop("counter_position", UNSET))

        def _parse_affected_bots(data: object) -> list[SynthesisInsightCreateAffectedBotsType0Item] | None | Unset:
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
                    affected_bots_type_0_item = SynthesisInsightCreateAffectedBotsType0Item.from_dict(
                        affected_bots_type_0_item_data
                    )

                    affected_bots_type_0.append(affected_bots_type_0_item)

                return affected_bots_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SynthesisInsightCreateAffectedBotsType0Item] | None | Unset, data)

        affected_bots = _parse_affected_bots(d.pop("affected_bots", UNSET))

        _severity = d.pop("severity", UNSET)
        severity: InsightSeverity | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = InsightSeverity(_severity)

        synthesis_insight_create = cls(
            authoring_bot_id=authoring_bot_id,
            pattern_type=pattern_type,
            observed_cluster=observed_cluster,
            synthesis_claim=synthesis_claim,
            recommended_investigation=recommended_investigation,
            cited_streams=cited_streams,
            time_window_start=time_window_start,
            time_window_end=time_window_end,
            org_id=org_id,
            counter_position=counter_position,
            affected_bots=affected_bots,
            severity=severity,
        )

        synthesis_insight_create.additional_properties = d
        return synthesis_insight_create

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
