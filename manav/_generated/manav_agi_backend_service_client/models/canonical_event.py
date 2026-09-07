from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.source_track import SourceTrack
from ..models.subject_type import SubjectType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.canonical_event_detail import CanonicalEventDetail


T = TypeVar("T", bound="CanonicalEvent")


@_attrs_define
class CanonicalEvent:
    """The universal event shape every timeline surface renders.

    Fields:
      ts:            wall-clock timestamp (UTC, tz-aware)
      kind:          canonical event kind (see ALL_EVENT_KINDS)
      subject_type:  which axis this event was pulled FOR (redundant with
                     query context but useful for multi-subject views)
      subject_id:    the entity we're building a timeline for
      sender_id:     which bot/user/system caused this event (optional)
      summary:       1-line human summary — "Cyra called read_file(/notes.md)"
      detail:        rich per-kind payload — full JSON body for the drill-down panel
      anomalies:     ['slow', 'expensive', 'errored', 'high-tokens', ...]
      source_track:  which of the 3 tracks emitted this — for debugging + provenance
      source_row_id: original row's PK — so caller can drill into the raw source
      duration_ms:   optional — for latency-aware rendering
      cost_usd:      optional — for cost-aware rendering

        Attributes:
            ts (datetime.datetime):
            kind (str):
            subject_type (SubjectType): What kind of thing we're pulling a timeline FOR.
            subject_id (UUID):
            summary (str):
            source_track (SourceTrack): Which of the 3 tracks emitted this event.
            sender_id (None | Unset | UUID):
            detail (CanonicalEventDetail | Unset):
            anomalies (list[str] | Unset):
            source_row_id (None | str | Unset):
            duration_ms (float | None | Unset):
            cost_usd (float | None | Unset):
    """

    ts: datetime.datetime
    kind: str
    subject_type: SubjectType
    subject_id: UUID
    summary: str
    source_track: SourceTrack
    sender_id: None | Unset | UUID = UNSET
    detail: CanonicalEventDetail | Unset = UNSET
    anomalies: list[str] | Unset = UNSET
    source_row_id: None | str | Unset = UNSET
    duration_ms: float | None | Unset = UNSET
    cost_usd: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ts = self.ts.isoformat()

        kind = self.kind

        subject_type = self.subject_type.value

        subject_id = str(self.subject_id)

        summary = self.summary

        source_track = self.source_track.value

        sender_id: None | str | Unset
        if isinstance(self.sender_id, Unset):
            sender_id = UNSET
        elif isinstance(self.sender_id, UUID):
            sender_id = str(self.sender_id)
        else:
            sender_id = self.sender_id

        detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.detail, Unset):
            detail = self.detail.to_dict()

        anomalies: list[str] | Unset = UNSET
        if not isinstance(self.anomalies, Unset):
            anomalies = self.anomalies

        source_row_id: None | str | Unset
        if isinstance(self.source_row_id, Unset):
            source_row_id = UNSET
        else:
            source_row_id = self.source_row_id

        duration_ms: float | None | Unset
        if isinstance(self.duration_ms, Unset):
            duration_ms = UNSET
        else:
            duration_ms = self.duration_ms

        cost_usd: float | None | Unset
        if isinstance(self.cost_usd, Unset):
            cost_usd = UNSET
        else:
            cost_usd = self.cost_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ts": ts,
                "kind": kind,
                "subject_type": subject_type,
                "subject_id": subject_id,
                "summary": summary,
                "source_track": source_track,
            }
        )
        if sender_id is not UNSET:
            field_dict["sender_id"] = sender_id
        if detail is not UNSET:
            field_dict["detail"] = detail
        if anomalies is not UNSET:
            field_dict["anomalies"] = anomalies
        if source_row_id is not UNSET:
            field_dict["source_row_id"] = source_row_id
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if cost_usd is not UNSET:
            field_dict["cost_usd"] = cost_usd

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.canonical_event_detail import CanonicalEventDetail  # noqa: PLC0415

        d = dict(src_dict)
        ts = datetime.datetime.fromisoformat(d.pop("ts"))

        kind = d.pop("kind")

        subject_type = SubjectType(d.pop("subject_type"))

        subject_id = UUID(d.pop("subject_id"))

        summary = d.pop("summary")

        source_track = SourceTrack(d.pop("source_track"))

        def _parse_sender_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sender_id_type_0 = UUID(data)

                return sender_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        sender_id = _parse_sender_id(d.pop("sender_id", UNSET))

        _detail = d.pop("detail", UNSET)
        detail: CanonicalEventDetail | Unset
        if isinstance(_detail, Unset):
            detail = UNSET
        else:
            detail = CanonicalEventDetail.from_dict(_detail)

        anomalies = cast(list[str], d.pop("anomalies", UNSET))

        def _parse_source_row_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_row_id = _parse_source_row_id(d.pop("source_row_id", UNSET))

        def _parse_duration_ms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration_ms = _parse_duration_ms(d.pop("duration_ms", UNSET))

        def _parse_cost_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cost_usd = _parse_cost_usd(d.pop("cost_usd", UNSET))

        canonical_event = cls(
            ts=ts,
            kind=kind,
            subject_type=subject_type,
            subject_id=subject_id,
            summary=summary,
            source_track=source_track,
            sender_id=sender_id,
            detail=detail,
            anomalies=anomalies,
            source_row_id=source_row_id,
            duration_ms=duration_ms,
            cost_usd=cost_usd,
        )

        canonical_event.additional_properties = d
        return canonical_event

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
