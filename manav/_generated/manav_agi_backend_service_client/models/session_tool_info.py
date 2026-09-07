from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SessionToolInfo")


@_attrs_define
class SessionToolInfo:
    """A tool available in this session

    Attributes:
        id (str):
        tool_function_name (str):
        tool_name (str):
        datasource_id (None | str | Unset):
        datasource_name (None | str | Unset):
        mcp_path (None | str | Unset):
        tool_type (str | Unset):  Default: 'mcp'.
    """

    id: str
    tool_function_name: str
    tool_name: str
    datasource_id: None | str | Unset = UNSET
    datasource_name: None | str | Unset = UNSET
    mcp_path: None | str | Unset = UNSET
    tool_type: str | Unset = "mcp"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tool_function_name = self.tool_function_name

        tool_name = self.tool_name

        datasource_id: None | str | Unset
        if isinstance(self.datasource_id, Unset):
            datasource_id = UNSET
        else:
            datasource_id = self.datasource_id

        datasource_name: None | str | Unset
        if isinstance(self.datasource_name, Unset):
            datasource_name = UNSET
        else:
            datasource_name = self.datasource_name

        mcp_path: None | str | Unset
        if isinstance(self.mcp_path, Unset):
            mcp_path = UNSET
        else:
            mcp_path = self.mcp_path

        tool_type = self.tool_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "tool_function_name": tool_function_name,
                "tool_name": tool_name,
            }
        )
        if datasource_id is not UNSET:
            field_dict["datasource_id"] = datasource_id
        if datasource_name is not UNSET:
            field_dict["datasource_name"] = datasource_name
        if mcp_path is not UNSET:
            field_dict["mcp_path"] = mcp_path
        if tool_type is not UNSET:
            field_dict["tool_type"] = tool_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        tool_function_name = d.pop("tool_function_name")

        tool_name = d.pop("tool_name")

        def _parse_datasource_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        datasource_id = _parse_datasource_id(d.pop("datasource_id", UNSET))

        def _parse_datasource_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        datasource_name = _parse_datasource_name(d.pop("datasource_name", UNSET))

        def _parse_mcp_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mcp_path = _parse_mcp_path(d.pop("mcp_path", UNSET))

        tool_type = d.pop("tool_type", UNSET)

        session_tool_info = cls(
            id=id,
            tool_function_name=tool_function_name,
            tool_name=tool_name,
            datasource_id=datasource_id,
            datasource_name=datasource_name,
            mcp_path=mcp_path,
            tool_type=tool_type,
        )

        session_tool_info.additional_properties = d
        return session_tool_info

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
