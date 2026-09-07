from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connection_status import ConnectionStatus
from ..models.database_type import DatabaseType
from ..models.ssl_mode import SSLMode

T = TypeVar("T", bound="ConnectionProfileResponse")


@_attrs_define
class ConnectionProfileResponse:
    """
    Attributes:
        id (str):
        profile_name (str):
        db_type (DatabaseType):
        host (str):
        port (int):
        username (str):
        ssl_mode (SSLMode):
        connection_status (ConnectionStatus):
        is_default (bool):
        last_connected_at (datetime.datetime | None):
        last_error (None | str):
        created_at (datetime.datetime):
    """

    id: str
    profile_name: str
    db_type: DatabaseType
    host: str
    port: int
    username: str
    ssl_mode: SSLMode
    connection_status: ConnectionStatus
    is_default: bool
    last_connected_at: datetime.datetime | None
    last_error: None | str
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        profile_name = self.profile_name

        db_type = self.db_type.value

        host = self.host

        port = self.port

        username = self.username

        ssl_mode = self.ssl_mode.value

        connection_status = self.connection_status.value

        is_default = self.is_default

        last_connected_at: None | str
        if isinstance(self.last_connected_at, datetime.datetime):
            last_connected_at = self.last_connected_at.isoformat()
        else:
            last_connected_at = self.last_connected_at

        last_error: None | str
        last_error = self.last_error

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "profile_name": profile_name,
                "db_type": db_type,
                "host": host,
                "port": port,
                "username": username,
                "ssl_mode": ssl_mode,
                "connection_status": connection_status,
                "is_default": is_default,
                "last_connected_at": last_connected_at,
                "last_error": last_error,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        profile_name = d.pop("profile_name")

        db_type = DatabaseType(d.pop("db_type"))

        host = d.pop("host")

        port = d.pop("port")

        username = d.pop("username")

        ssl_mode = SSLMode(d.pop("ssl_mode"))

        connection_status = ConnectionStatus(d.pop("connection_status"))

        is_default = d.pop("is_default")

        def _parse_last_connected_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_connected_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_connected_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_connected_at = _parse_last_connected_at(d.pop("last_connected_at"))

        def _parse_last_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_error = _parse_last_error(d.pop("last_error"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        connection_profile_response = cls(
            id=id,
            profile_name=profile_name,
            db_type=db_type,
            host=host,
            port=port,
            username=username,
            ssl_mode=ssl_mode,
            connection_status=connection_status,
            is_default=is_default,
            last_connected_at=last_connected_at,
            last_error=last_error,
            created_at=created_at,
        )

        connection_profile_response.additional_properties = d
        return connection_profile_response

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
