from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SessionDatasourceInfo")


@_attrs_define
class SessionDatasourceInfo:
    """A datasource (MCP server) available in this session

    Attributes:
        datasource_id (str):
        datasource_name (str):
        mcp_path (str):
        datasource_ui_name (None | str | Unset):
        description (None | str | Unset):
        description_short (None | str | Unset):
        transport (str | Unset):  Default: 'http'.
        mcp_command (None | str | Unset):
    """

    datasource_id: str
    datasource_name: str
    mcp_path: str
    datasource_ui_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    description_short: None | str | Unset = UNSET
    transport: str | Unset = "http"
    mcp_command: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        datasource_id = self.datasource_id

        datasource_name = self.datasource_name

        mcp_path = self.mcp_path

        datasource_ui_name: None | str | Unset
        if isinstance(self.datasource_ui_name, Unset):
            datasource_ui_name = UNSET
        else:
            datasource_ui_name = self.datasource_ui_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        description_short: None | str | Unset
        if isinstance(self.description_short, Unset):
            description_short = UNSET
        else:
            description_short = self.description_short

        transport = self.transport

        mcp_command: None | str | Unset
        if isinstance(self.mcp_command, Unset):
            mcp_command = UNSET
        else:
            mcp_command = self.mcp_command

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasource_id": datasource_id,
                "datasource_name": datasource_name,
                "mcp_path": mcp_path,
            }
        )
        if datasource_ui_name is not UNSET:
            field_dict["datasource_ui_name"] = datasource_ui_name
        if description is not UNSET:
            field_dict["description"] = description
        if description_short is not UNSET:
            field_dict["description_short"] = description_short
        if transport is not UNSET:
            field_dict["transport"] = transport
        if mcp_command is not UNSET:
            field_dict["mcp_command"] = mcp_command

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        datasource_id = d.pop("datasource_id")

        datasource_name = d.pop("datasource_name")

        mcp_path = d.pop("mcp_path")

        def _parse_datasource_ui_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        datasource_ui_name = _parse_datasource_ui_name(d.pop("datasource_ui_name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_description_short(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description_short = _parse_description_short(d.pop("description_short", UNSET))

        transport = d.pop("transport", UNSET)

        def _parse_mcp_command(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mcp_command = _parse_mcp_command(d.pop("mcp_command", UNSET))

        session_datasource_info = cls(
            datasource_id=datasource_id,
            datasource_name=datasource_name,
            mcp_path=mcp_path,
            datasource_ui_name=datasource_ui_name,
            description=description,
            description_short=description_short,
            transport=transport,
            mcp_command=mcp_command,
        )

        session_datasource_info.additional_properties = d
        return session_datasource_info

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
