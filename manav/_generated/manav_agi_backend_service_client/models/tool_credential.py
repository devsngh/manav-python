from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_credential_credentials_type_0 import ToolCredentialCredentialsType0


T = TypeVar("T", bound="ToolCredential")


@_attrs_define
class ToolCredential:
    """Decrypted credentials for a specific tool, sourced from user's datasource connections.
    Returned to the orchestrator on-demand before each MCP tool invocation.

        Attributes:
            tool_id (str):
            tool_function_name (str):
            has_connection (bool):
            datasource_id (None | str | Unset):
            datasource_name (None | str | Unset):
            credentials (None | ToolCredentialCredentialsType0 | Unset):
    """

    tool_id: str
    tool_function_name: str
    has_connection: bool
    datasource_id: None | str | Unset = UNSET
    datasource_name: None | str | Unset = UNSET
    credentials: None | ToolCredentialCredentialsType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.tool_credential_credentials_type_0 import ToolCredentialCredentialsType0  # noqa: PLC0415

        tool_id = self.tool_id

        tool_function_name = self.tool_function_name

        has_connection = self.has_connection

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

        credentials: dict[str, Any] | None | Unset
        if isinstance(self.credentials, Unset):
            credentials = UNSET
        elif isinstance(self.credentials, ToolCredentialCredentialsType0):
            credentials = self.credentials.to_dict()
        else:
            credentials = self.credentials

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tool_id": tool_id,
                "tool_function_name": tool_function_name,
                "has_connection": has_connection,
            }
        )
        if datasource_id is not UNSET:
            field_dict["datasource_id"] = datasource_id
        if datasource_name is not UNSET:
            field_dict["datasource_name"] = datasource_name
        if credentials is not UNSET:
            field_dict["credentials"] = credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_credential_credentials_type_0 import ToolCredentialCredentialsType0  # noqa: PLC0415

        d = dict(src_dict)
        tool_id = d.pop("tool_id")

        tool_function_name = d.pop("tool_function_name")

        has_connection = d.pop("has_connection")

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

        def _parse_credentials(data: object) -> None | ToolCredentialCredentialsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credentials_type_0 = ToolCredentialCredentialsType0.from_dict(data)

                return credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ToolCredentialCredentialsType0 | Unset, data)

        credentials = _parse_credentials(d.pop("credentials", UNSET))

        tool_credential = cls(
            tool_id=tool_id,
            tool_function_name=tool_function_name,
            has_connection=has_connection,
            datasource_id=datasource_id,
            datasource_name=datasource_name,
            credentials=credentials,
        )

        tool_credential.additional_properties = d
        return tool_credential

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
