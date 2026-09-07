from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.investor_update_update_metrics_snapshot_type_0 import InvestorUpdateUpdateMetricsSnapshotType0


T = TypeVar("T", bound="InvestorUpdateUpdate")


@_attrs_define
class InvestorUpdateUpdate:
    """
    Attributes:
        title (None | str | Unset):
        period_start (datetime.date | None | Unset):
        period_end (datetime.date | None | Unset):
        content_asset_id (None | Unset | UUID):
        summary (None | str | Unset):
        metrics_snapshot (InvestorUpdateUpdateMetricsSnapshotType0 | None | Unset):
    """

    title: None | str | Unset = UNSET
    period_start: datetime.date | None | Unset = UNSET
    period_end: datetime.date | None | Unset = UNSET
    content_asset_id: None | Unset | UUID = UNSET
    summary: None | str | Unset = UNSET
    metrics_snapshot: InvestorUpdateUpdateMetricsSnapshotType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.investor_update_update_metrics_snapshot_type_0 import (
            InvestorUpdateUpdateMetricsSnapshotType0,  # noqa: PLC0415
        )

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        period_start: None | str | Unset
        if isinstance(self.period_start, Unset):
            period_start = UNSET
        elif isinstance(self.period_start, datetime.date):
            period_start = self.period_start.isoformat()
        else:
            period_start = self.period_start

        period_end: None | str | Unset
        if isinstance(self.period_end, Unset):
            period_end = UNSET
        elif isinstance(self.period_end, datetime.date):
            period_end = self.period_end.isoformat()
        else:
            period_end = self.period_end

        content_asset_id: None | str | Unset
        if isinstance(self.content_asset_id, Unset):
            content_asset_id = UNSET
        elif isinstance(self.content_asset_id, UUID):
            content_asset_id = str(self.content_asset_id)
        else:
            content_asset_id = self.content_asset_id

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        metrics_snapshot: dict[str, Any] | None | Unset
        if isinstance(self.metrics_snapshot, Unset):
            metrics_snapshot = UNSET
        elif isinstance(self.metrics_snapshot, InvestorUpdateUpdateMetricsSnapshotType0):
            metrics_snapshot = self.metrics_snapshot.to_dict()
        else:
            metrics_snapshot = self.metrics_snapshot

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if period_start is not UNSET:
            field_dict["period_start"] = period_start
        if period_end is not UNSET:
            field_dict["period_end"] = period_end
        if content_asset_id is not UNSET:
            field_dict["content_asset_id"] = content_asset_id
        if summary is not UNSET:
            field_dict["summary"] = summary
        if metrics_snapshot is not UNSET:
            field_dict["metrics_snapshot"] = metrics_snapshot

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investor_update_update_metrics_snapshot_type_0 import (
            InvestorUpdateUpdateMetricsSnapshotType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_period_start(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_start_type_0 = datetime.date.fromisoformat(data)

                return period_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        period_start = _parse_period_start(d.pop("period_start", UNSET))

        def _parse_period_end(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_end_type_0 = datetime.date.fromisoformat(data)

                return period_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        period_end = _parse_period_end(d.pop("period_end", UNSET))

        def _parse_content_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                content_asset_id_type_0 = UUID(data)

                return content_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        content_asset_id = _parse_content_asset_id(d.pop("content_asset_id", UNSET))

        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))

        def _parse_metrics_snapshot(data: object) -> InvestorUpdateUpdateMetricsSnapshotType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metrics_snapshot_type_0 = InvestorUpdateUpdateMetricsSnapshotType0.from_dict(data)

                return metrics_snapshot_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvestorUpdateUpdateMetricsSnapshotType0 | None | Unset, data)

        metrics_snapshot = _parse_metrics_snapshot(d.pop("metrics_snapshot", UNSET))

        investor_update_update = cls(
            title=title,
            period_start=period_start,
            period_end=period_end,
            content_asset_id=content_asset_id,
            summary=summary,
            metrics_snapshot=metrics_snapshot,
        )

        investor_update_update.additional_properties = d
        return investor_update_update

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
