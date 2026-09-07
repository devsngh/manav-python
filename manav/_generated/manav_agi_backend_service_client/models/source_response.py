from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceResponse")


@_attrs_define
class SourceResponse:
    """
    Attributes:
        id (str):
        workspace_id (str):
        name (str):
        type_ (str):
        source_category (str):
        status (str):
        enrichment_status (str):
        created_at (datetime.datetime):
        connection_id (None | str | Unset):
        uri (None | str | Unset):
        trigger_agent_id (None | str | Unset):
        total_tables (int | None | Unset):
        total_columns (int | None | Unset):
        total_relationships (int | None | Unset):
        total_rows_approx (int | None | Unset):
        last_synced_at (datetime.datetime | None | Unset):
    """

    id: str
    workspace_id: str
    name: str
    type_: str
    source_category: str
    status: str
    enrichment_status: str
    created_at: datetime.datetime
    connection_id: None | str | Unset = UNSET
    uri: None | str | Unset = UNSET
    trigger_agent_id: None | str | Unset = UNSET
    total_tables: int | None | Unset = UNSET
    total_columns: int | None | Unset = UNSET
    total_relationships: int | None | Unset = UNSET
    total_rows_approx: int | None | Unset = UNSET
    last_synced_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workspace_id = self.workspace_id

        name = self.name

        type_ = self.type_

        source_category = self.source_category

        status = self.status

        enrichment_status = self.enrichment_status

        created_at = self.created_at.isoformat()

        connection_id: None | str | Unset
        if isinstance(self.connection_id, Unset):
            connection_id = UNSET
        else:
            connection_id = self.connection_id

        uri: None | str | Unset
        if isinstance(self.uri, Unset):
            uri = UNSET
        else:
            uri = self.uri

        trigger_agent_id: None | str | Unset
        if isinstance(self.trigger_agent_id, Unset):
            trigger_agent_id = UNSET
        else:
            trigger_agent_id = self.trigger_agent_id

        total_tables: int | None | Unset
        if isinstance(self.total_tables, Unset):
            total_tables = UNSET
        else:
            total_tables = self.total_tables

        total_columns: int | None | Unset
        if isinstance(self.total_columns, Unset):
            total_columns = UNSET
        else:
            total_columns = self.total_columns

        total_relationships: int | None | Unset
        if isinstance(self.total_relationships, Unset):
            total_relationships = UNSET
        else:
            total_relationships = self.total_relationships

        total_rows_approx: int | None | Unset
        if isinstance(self.total_rows_approx, Unset):
            total_rows_approx = UNSET
        else:
            total_rows_approx = self.total_rows_approx

        last_synced_at: None | str | Unset
        if isinstance(self.last_synced_at, Unset):
            last_synced_at = UNSET
        elif isinstance(self.last_synced_at, datetime.datetime):
            last_synced_at = self.last_synced_at.isoformat()
        else:
            last_synced_at = self.last_synced_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "workspace_id": workspace_id,
                "name": name,
                "type": type_,
                "source_category": source_category,
                "status": status,
                "enrichment_status": enrichment_status,
                "created_at": created_at,
            }
        )
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if uri is not UNSET:
            field_dict["uri"] = uri
        if trigger_agent_id is not UNSET:
            field_dict["trigger_agent_id"] = trigger_agent_id
        if total_tables is not UNSET:
            field_dict["total_tables"] = total_tables
        if total_columns is not UNSET:
            field_dict["total_columns"] = total_columns
        if total_relationships is not UNSET:
            field_dict["total_relationships"] = total_relationships
        if total_rows_approx is not UNSET:
            field_dict["total_rows_approx"] = total_rows_approx
        if last_synced_at is not UNSET:
            field_dict["last_synced_at"] = last_synced_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        workspace_id = d.pop("workspace_id")

        name = d.pop("name")

        type_ = d.pop("type")

        source_category = d.pop("source_category")

        status = d.pop("status")

        enrichment_status = d.pop("enrichment_status")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_connection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connection_id = _parse_connection_id(d.pop("connection_id", UNSET))

        def _parse_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uri = _parse_uri(d.pop("uri", UNSET))

        def _parse_trigger_agent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trigger_agent_id = _parse_trigger_agent_id(d.pop("trigger_agent_id", UNSET))

        def _parse_total_tables(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_tables = _parse_total_tables(d.pop("total_tables", UNSET))

        def _parse_total_columns(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_columns = _parse_total_columns(d.pop("total_columns", UNSET))

        def _parse_total_relationships(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_relationships = _parse_total_relationships(d.pop("total_relationships", UNSET))

        def _parse_total_rows_approx(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_rows_approx = _parse_total_rows_approx(d.pop("total_rows_approx", UNSET))

        def _parse_last_synced_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_synced_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_synced_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_synced_at = _parse_last_synced_at(d.pop("last_synced_at", UNSET))

        source_response = cls(
            id=id,
            workspace_id=workspace_id,
            name=name,
            type_=type_,
            source_category=source_category,
            status=status,
            enrichment_status=enrichment_status,
            created_at=created_at,
            connection_id=connection_id,
            uri=uri,
            trigger_agent_id=trigger_agent_id,
            total_tables=total_tables,
            total_columns=total_columns,
            total_relationships=total_relationships,
            total_rows_approx=total_rows_approx,
            last_synced_at=last_synced_at,
        )

        source_response.additional_properties = d
        return source_response

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
