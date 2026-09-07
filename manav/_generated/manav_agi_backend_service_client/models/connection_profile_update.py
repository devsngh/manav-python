from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ssl_mode import SSLMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectionProfileUpdate")


@_attrs_define
class ConnectionProfileUpdate:
    """
    Attributes:
        profile_name (None | str | Unset):
        host (None | str | Unset):
        port (int | None | Unset):
        username (None | str | Unset):
        password (None | str | Unset):
        ssl_mode (None | SSLMode | Unset):
        is_default (bool | None | Unset):
    """

    profile_name: None | str | Unset = UNSET
    host: None | str | Unset = UNSET
    port: int | None | Unset = UNSET
    username: None | str | Unset = UNSET
    password: None | str | Unset = UNSET
    ssl_mode: None | SSLMode | Unset = UNSET
    is_default: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_name: None | str | Unset
        if isinstance(self.profile_name, Unset):
            profile_name = UNSET
        else:
            profile_name = self.profile_name

        host: None | str | Unset
        if isinstance(self.host, Unset):
            host = UNSET
        else:
            host = self.host

        port: int | None | Unset
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        ssl_mode: None | str | Unset
        if isinstance(self.ssl_mode, Unset):
            ssl_mode = UNSET
        elif isinstance(self.ssl_mode, SSLMode):
            ssl_mode = self.ssl_mode.value
        else:
            ssl_mode = self.ssl_mode

        is_default: bool | None | Unset
        if isinstance(self.is_default, Unset):
            is_default = UNSET
        else:
            is_default = self.is_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if profile_name is not UNSET:
            field_dict["profile_name"] = profile_name
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if ssl_mode is not UNSET:
            field_dict["ssl_mode"] = ssl_mode
        if is_default is not UNSET:
            field_dict["is_default"] = is_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_profile_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_name = _parse_profile_name(d.pop("profile_name", UNSET))

        def _parse_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host = _parse_host(d.pop("host", UNSET))

        def _parse_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        port = _parse_port(d.pop("port", UNSET))

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        def _parse_ssl_mode(data: object) -> None | SSLMode | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ssl_mode_type_0 = SSLMode(data)

                return ssl_mode_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SSLMode | Unset, data)

        ssl_mode = _parse_ssl_mode(d.pop("ssl_mode", UNSET))

        def _parse_is_default(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_default = _parse_is_default(d.pop("is_default", UNSET))

        connection_profile_update = cls(
            profile_name=profile_name,
            host=host,
            port=port,
            username=username,
            password=password,
            ssl_mode=ssl_mode,
            is_default=is_default,
        )

        connection_profile_update.additional_properties = d
        return connection_profile_update

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
