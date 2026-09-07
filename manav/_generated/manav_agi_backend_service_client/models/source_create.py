from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceCreate")


@_attrs_define
class SourceCreate:
    """
    Attributes:
        workspace_id (str):
        name (str):
        type_ (str):
        source_category (str):
        connection_id (None | str | Unset):
        uri (None | str | Unset):
        trigger_agent_id (None | str | Unset):
    """

    workspace_id: str
    name: str
    type_: str
    source_category: str
    connection_id: None | str | Unset = UNSET
    uri: None | str | Unset = UNSET
    trigger_agent_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        name = self.name

        type_ = self.type_

        source_category = self.source_category

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspace_id": workspace_id,
                "name": name,
                "type": type_,
                "source_category": source_category,
            }
        )
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if uri is not UNSET:
            field_dict["uri"] = uri
        if trigger_agent_id is not UNSET:
            field_dict["trigger_agent_id"] = trigger_agent_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        workspace_id = d.pop("workspace_id")

        name = d.pop("name")

        type_ = d.pop("type")

        source_category = d.pop("source_category")

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

        source_create = cls(
            workspace_id=workspace_id,
            name=name,
            type_=type_,
            source_category=source_category,
            connection_id=connection_id,
            uri=uri,
            trigger_agent_id=trigger_agent_id,
        )

        source_create.additional_properties = d
        return source_create

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
