from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.database_type import DatabaseType
from ..models.ssl_mode import SSLMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectionProfileCreate")


@_attrs_define
class ConnectionProfileCreate:
    """
    Attributes:
        profile_name (str):
        db_type (DatabaseType):
        host (str):
        port (int):
        username (str):
        password (str):
        ssl_mode (SSLMode | Unset):  Default: SSLMode.PREFER.
        is_default (bool | Unset):  Default: False.
    """

    profile_name: str
    db_type: DatabaseType
    host: str
    port: int
    username: str
    password: str
    ssl_mode: SSLMode | Unset = SSLMode.PREFER
    is_default: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_name = self.profile_name

        db_type = self.db_type.value

        host = self.host

        port = self.port

        username = self.username

        password = self.password

        ssl_mode: str | Unset = UNSET
        if not isinstance(self.ssl_mode, Unset):
            ssl_mode = self.ssl_mode.value

        is_default = self.is_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "profile_name": profile_name,
                "db_type": db_type,
                "host": host,
                "port": port,
                "username": username,
                "password": password,
            }
        )
        if ssl_mode is not UNSET:
            field_dict["ssl_mode"] = ssl_mode
        if is_default is not UNSET:
            field_dict["is_default"] = is_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        profile_name = d.pop("profile_name")

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

        is_default = d.pop("is_default", UNSET)

        connection_profile_create = cls(
            profile_name=profile_name,
            db_type=db_type,
            host=host,
            port=port,
            username=username,
            password=password,
            ssl_mode=ssl_mode,
            is_default=is_default,
        )

        connection_profile_create.additional_properties = d
        return connection_profile_create

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
