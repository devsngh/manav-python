from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.investor_update_create_metrics_snapshot_type_0 import InvestorUpdateCreateMetricsSnapshotType0


T = TypeVar("T", bound="InvestorUpdateCreate")


@_attrs_define
class InvestorUpdateCreate:
    """
    Attributes:
        title (str):
        period_type (str): monthly / quarterly / ad_hoc / annual
        period_start (datetime.date | None | Unset):
        period_end (datetime.date | None | Unset):
        content_asset_id (None | Unset | UUID):
        summary (None | str | Unset):
        metrics_snapshot (InvestorUpdateCreateMetricsSnapshotType0 | None | Unset):
        status (str | Unset):  Default: 'draft'.
    """

    title: str
    period_type: str
    period_start: datetime.date | None | Unset = UNSET
    period_end: datetime.date | None | Unset = UNSET
    content_asset_id: None | Unset | UUID = UNSET
    summary: None | str | Unset = UNSET
    metrics_snapshot: InvestorUpdateCreateMetricsSnapshotType0 | None | Unset = UNSET
    status: str | Unset = "draft"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.investor_update_create_metrics_snapshot_type_0 import (
            InvestorUpdateCreateMetricsSnapshotType0,  # noqa: PLC0415
        )

        title = self.title

        period_type = self.period_type

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
        elif isinstance(self.metrics_snapshot, InvestorUpdateCreateMetricsSnapshotType0):
            metrics_snapshot = self.metrics_snapshot.to_dict()
        else:
            metrics_snapshot = self.metrics_snapshot

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "period_type": period_type,
            }
        )
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
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investor_update_create_metrics_snapshot_type_0 import (
            InvestorUpdateCreateMetricsSnapshotType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        title = d.pop("title")

        period_type = d.pop("period_type")

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

        def _parse_metrics_snapshot(data: object) -> InvestorUpdateCreateMetricsSnapshotType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metrics_snapshot_type_0 = InvestorUpdateCreateMetricsSnapshotType0.from_dict(data)

                return metrics_snapshot_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvestorUpdateCreateMetricsSnapshotType0 | None | Unset, data)

        metrics_snapshot = _parse_metrics_snapshot(d.pop("metrics_snapshot", UNSET))

        status = d.pop("status", UNSET)

        investor_update_create = cls(
            title=title,
            period_type=period_type,
            period_start=period_start,
            period_end=period_end,
            content_asset_id=content_asset_id,
            summary=summary,
            metrics_snapshot=metrics_snapshot,
            status=status,
        )

        investor_update_create.additional_properties = d
        return investor_update_create

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
