from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.investor_update_response_metrics_snapshot_type_0 import InvestorUpdateResponseMetricsSnapshotType0


T = TypeVar("T", bound="InvestorUpdateResponse")


@_attrs_define
class InvestorUpdateResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        title (str):
        period_type (str):
        period_start (datetime.date | None):
        period_end (datetime.date | None):
        content_asset_id (None | UUID):
        summary (None | str):
        metrics_snapshot (InvestorUpdateResponseMetricsSnapshotType0 | None):
        sent_at (datetime.datetime | None):
        sent_to_investor_ids (list[UUID] | None):
        open_count (int):
        reply_count (int):
        status (str):
        authored_by_bot_id (None | UUID):
        approved_by_user_id (None | UUID):
        approved_at (datetime.datetime | None):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: UUID
    org_id: UUID
    title: str
    period_type: str
    period_start: datetime.date | None
    period_end: datetime.date | None
    content_asset_id: None | UUID
    summary: None | str
    metrics_snapshot: InvestorUpdateResponseMetricsSnapshotType0 | None
    sent_at: datetime.datetime | None
    sent_to_investor_ids: list[UUID] | None
    open_count: int
    reply_count: int
    status: str
    authored_by_bot_id: None | UUID
    approved_by_user_id: None | UUID
    approved_at: datetime.datetime | None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.investor_update_response_metrics_snapshot_type_0 import (
            InvestorUpdateResponseMetricsSnapshotType0,  # noqa: PLC0415
        )

        id = str(self.id)

        org_id = str(self.org_id)

        title = self.title

        period_type = self.period_type

        period_start: None | str
        if isinstance(self.period_start, datetime.date):
            period_start = self.period_start.isoformat()
        else:
            period_start = self.period_start

        period_end: None | str
        if isinstance(self.period_end, datetime.date):
            period_end = self.period_end.isoformat()
        else:
            period_end = self.period_end

        content_asset_id: None | str
        if isinstance(self.content_asset_id, UUID):
            content_asset_id = str(self.content_asset_id)
        else:
            content_asset_id = self.content_asset_id

        summary: None | str
        summary = self.summary

        metrics_snapshot: dict[str, Any] | None
        if isinstance(self.metrics_snapshot, InvestorUpdateResponseMetricsSnapshotType0):
            metrics_snapshot = self.metrics_snapshot.to_dict()
        else:
            metrics_snapshot = self.metrics_snapshot

        sent_at: None | str
        if isinstance(self.sent_at, datetime.datetime):
            sent_at = self.sent_at.isoformat()
        else:
            sent_at = self.sent_at

        sent_to_investor_ids: list[str] | None
        if isinstance(self.sent_to_investor_ids, list):
            sent_to_investor_ids = []
            for sent_to_investor_ids_type_0_item_data in self.sent_to_investor_ids:
                sent_to_investor_ids_type_0_item = str(sent_to_investor_ids_type_0_item_data)
                sent_to_investor_ids.append(sent_to_investor_ids_type_0_item)

        else:
            sent_to_investor_ids = self.sent_to_investor_ids

        open_count = self.open_count

        reply_count = self.reply_count

        status = self.status

        authored_by_bot_id: None | str
        if isinstance(self.authored_by_bot_id, UUID):
            authored_by_bot_id = str(self.authored_by_bot_id)
        else:
            authored_by_bot_id = self.authored_by_bot_id

        approved_by_user_id: None | str
        if isinstance(self.approved_by_user_id, UUID):
            approved_by_user_id = str(self.approved_by_user_id)
        else:
            approved_by_user_id = self.approved_by_user_id

        approved_at: None | str
        if isinstance(self.approved_at, datetime.datetime):
            approved_at = self.approved_at.isoformat()
        else:
            approved_at = self.approved_at

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "title": title,
                "period_type": period_type,
                "period_start": period_start,
                "period_end": period_end,
                "content_asset_id": content_asset_id,
                "summary": summary,
                "metrics_snapshot": metrics_snapshot,
                "sent_at": sent_at,
                "sent_to_investor_ids": sent_to_investor_ids,
                "open_count": open_count,
                "reply_count": reply_count,
                "status": status,
                "authored_by_bot_id": authored_by_bot_id,
                "approved_by_user_id": approved_by_user_id,
                "approved_at": approved_at,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investor_update_response_metrics_snapshot_type_0 import (
            InvestorUpdateResponseMetricsSnapshotType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        title = d.pop("title")

        period_type = d.pop("period_type")

        def _parse_period_start(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_start_type_0 = datetime.date.fromisoformat(data)

                return period_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        period_start = _parse_period_start(d.pop("period_start"))

        def _parse_period_end(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_end_type_0 = datetime.date.fromisoformat(data)

                return period_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        period_end = _parse_period_end(d.pop("period_end"))

        def _parse_content_asset_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                content_asset_id_type_0 = UUID(data)

                return content_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        content_asset_id = _parse_content_asset_id(d.pop("content_asset_id"))

        def _parse_summary(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        summary = _parse_summary(d.pop("summary"))

        def _parse_metrics_snapshot(data: object) -> InvestorUpdateResponseMetricsSnapshotType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metrics_snapshot_type_0 = InvestorUpdateResponseMetricsSnapshotType0.from_dict(data)

                return metrics_snapshot_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvestorUpdateResponseMetricsSnapshotType0 | None, data)

        metrics_snapshot = _parse_metrics_snapshot(d.pop("metrics_snapshot"))

        def _parse_sent_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sent_at_type_0 = datetime.datetime.fromisoformat(data)

                return sent_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        sent_at = _parse_sent_at(d.pop("sent_at"))

        def _parse_sent_to_investor_ids(data: object) -> list[UUID] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sent_to_investor_ids_type_0 = []
                _sent_to_investor_ids_type_0 = data
                for sent_to_investor_ids_type_0_item_data in _sent_to_investor_ids_type_0:
                    sent_to_investor_ids_type_0_item = UUID(sent_to_investor_ids_type_0_item_data)

                    sent_to_investor_ids_type_0.append(sent_to_investor_ids_type_0_item)

                return sent_to_investor_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None, data)

        sent_to_investor_ids = _parse_sent_to_investor_ids(d.pop("sent_to_investor_ids"))

        open_count = d.pop("open_count")

        reply_count = d.pop("reply_count")

        status = d.pop("status")

        def _parse_authored_by_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                authored_by_bot_id_type_0 = UUID(data)

                return authored_by_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        authored_by_bot_id = _parse_authored_by_bot_id(d.pop("authored_by_bot_id"))

        def _parse_approved_by_user_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_by_user_id_type_0 = UUID(data)

                return approved_by_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        approved_by_user_id = _parse_approved_by_user_id(d.pop("approved_by_user_id"))

        def _parse_approved_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_at_type_0 = datetime.datetime.fromisoformat(data)

                return approved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        approved_at = _parse_approved_at(d.pop("approved_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        investor_update_response = cls(
            id=id,
            org_id=org_id,
            title=title,
            period_type=period_type,
            period_start=period_start,
            period_end=period_end,
            content_asset_id=content_asset_id,
            summary=summary,
            metrics_snapshot=metrics_snapshot,
            sent_at=sent_at,
            sent_to_investor_ids=sent_to_investor_ids,
            open_count=open_count,
            reply_count=reply_count,
            status=status,
            authored_by_bot_id=authored_by_bot_id,
            approved_by_user_id=approved_by_user_id,
            approved_at=approved_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        investor_update_response.additional_properties = d
        return investor_update_response

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
