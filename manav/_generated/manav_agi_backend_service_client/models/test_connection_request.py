from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.database_type import DatabaseType
from ..models.ssl_mode import SSLMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="TestConnectionRequest")


@_attrs_define
class TestConnectionRequest:
    """
    Attributes:
        db_type (DatabaseType):
        host (str):
        port (int):
        username (str):
        password (str):
        ssl_mode (SSLMode | Unset):  Default: SSLMode.PREFER.
        database (None | str | Unset):
    """

    db_type: DatabaseType
    host: str
    port: int
    username: str
    password: str
    ssl_mode: SSLMode | Unset = SSLMode.PREFER
    database: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        db_type = self.db_type.value

        host = self.host

        port = self.port

        username = self.username

        password = self.password

        ssl_mode: str | Unset = UNSET
        if not isinstance(self.ssl_mode, Unset):
            ssl_mode = self.ssl_mode.value

        database: None | str | Unset
        if isinstance(self.database, Unset):
            database = UNSET
        else:
            database = self.database

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "db_type": db_type,
                "host": host,
                "port": port,
                "username": username,
                "password": password,
            }
        )
        if ssl_mode is not UNSET:
            field_dict["ssl_mode"] = ssl_mode
        if database is not UNSET:
            field_dict["database"] = database

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        db_type = DatabaseType(d.pop("db_type"))

        host = d.pop("host")

        port = d.pop("port")

        username = d.pop("username")

        password = d.pop("password")

        _ssl_mode = d.pop("ssl_mode", UNSET)
        ssl_mode: SSLMode | Unset
        if isinstance(_ssl_mode, Unset):
            ssl_mode = UNSET
        else:
            ssl_mode = SSLMode(_ssl_mode)

        def _parse_database(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        database = _parse_database(d.pop("database", UNSET))

        test_connection_request = cls(
            db_type=db_type,
            host=host,
            port=port,
            username=username,
            password=password,
            ssl_mode=ssl_mode,
            database=database,
        )

        test_connection_request.additional_properties = d
        return test_connection_request

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
