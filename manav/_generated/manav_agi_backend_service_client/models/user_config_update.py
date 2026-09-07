from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_config_update_user_additional_headers_type_0 import UserConfigUpdateUserAdditionalHeadersType0


T = TypeVar("T", bound="UserConfigUpdate")


@_attrs_define
class UserConfigUpdate:
    """Update user config

    Attributes:
        config_name (None | str | Unset):
        user_api_key (None | str | Unset):
        user_endpoint_url (None | str | Unset):
        user_additional_headers (None | Unset | UserConfigUpdateUserAdditionalHeadersType0):
        custom_model_path (None | str | Unset):
        is_enabled (bool | None | Unset):
    """

    config_name: None | str | Unset = UNSET
    user_api_key: None | str | Unset = UNSET
    user_endpoint_url: None | str | Unset = UNSET
    user_additional_headers: None | Unset | UserConfigUpdateUserAdditionalHeadersType0 = UNSET
    custom_model_path: None | str | Unset = UNSET
    is_enabled: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_config_update_user_additional_headers_type_0 import (
            UserConfigUpdateUserAdditionalHeadersType0,  # noqa: PLC0415
        )

        config_name: None | str | Unset
        if isinstance(self.config_name, Unset):
            config_name = UNSET
        else:
            config_name = self.config_name

        user_api_key: None | str | Unset
        if isinstance(self.user_api_key, Unset):
            user_api_key = UNSET
        else:
            user_api_key = self.user_api_key

        user_endpoint_url: None | str | Unset
        if isinstance(self.user_endpoint_url, Unset):
            user_endpoint_url = UNSET
        else:
            user_endpoint_url = self.user_endpoint_url

        user_additional_headers: dict[str, Any] | None | Unset
        if isinstance(self.user_additional_headers, Unset):
            user_additional_headers = UNSET
        elif isinstance(self.user_additional_headers, UserConfigUpdateUserAdditionalHeadersType0):
            user_additional_headers = self.user_additional_headers.to_dict()
        else:
            user_additional_headers = self.user_additional_headers

        custom_model_path: None | str | Unset
        if isinstance(self.custom_model_path, Unset):
            custom_model_path = UNSET
        else:
            custom_model_path = self.custom_model_path

        is_enabled: bool | None | Unset
        if isinstance(self.is_enabled, Unset):
            is_enabled = UNSET
        else:
            is_enabled = self.is_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config_name is not UNSET:
            field_dict["config_name"] = config_name
        if user_api_key is not UNSET:
            field_dict["user_api_key"] = user_api_key
        if user_endpoint_url is not UNSET:
            field_dict["user_endpoint_url"] = user_endpoint_url
        if user_additional_headers is not UNSET:
            field_dict["user_additional_headers"] = user_additional_headers
        if custom_model_path is not UNSET:
            field_dict["custom_model_path"] = custom_model_path
        if is_enabled is not UNSET:
            field_dict["is_enabled"] = is_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_config_update_user_additional_headers_type_0 import (
            UserConfigUpdateUserAdditionalHeadersType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_config_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        config_name = _parse_config_name(d.pop("config_name", UNSET))

        def _parse_user_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_api_key = _parse_user_api_key(d.pop("user_api_key", UNSET))

        def _parse_user_endpoint_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_endpoint_url = _parse_user_endpoint_url(d.pop("user_endpoint_url", UNSET))

        def _parse_user_additional_headers(data: object) -> None | Unset | UserConfigUpdateUserAdditionalHeadersType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_additional_headers_type_0 = UserConfigUpdateUserAdditionalHeadersType0.from_dict(data)

                return user_additional_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserConfigUpdateUserAdditionalHeadersType0, data)

        user_additional_headers = _parse_user_additional_headers(d.pop("user_additional_headers", UNSET))

        def _parse_custom_model_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_model_path = _parse_custom_model_path(d.pop("custom_model_path", UNSET))

        def _parse_is_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_enabled = _parse_is_enabled(d.pop("is_enabled", UNSET))

        user_config_update = cls(
            config_name=config_name,
            user_api_key=user_api_key,
            user_endpoint_url=user_endpoint_url,
            user_additional_headers=user_additional_headers,
            custom_model_path=custom_model_path,
            is_enabled=is_enabled,
        )

        user_config_update.additional_properties = d
        return user_config_update

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
