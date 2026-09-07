from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_config_create_user_additional_headers_type_0 import UserConfigCreateUserAdditionalHeadersType0
    from ..models.user_parameter_value_create import UserParameterValueCreate


T = TypeVar("T", bound="UserConfigCreate")


@_attrs_define
class UserConfigCreate:
    """Create user config

    Attributes:
        config_name (str):
        user_api_key (None | str | Unset):
        user_endpoint_url (None | str | Unset):
        user_additional_headers (None | Unset | UserConfigCreateUserAdditionalHeadersType0):
        custom_model_path (None | str | Unset):
        parameter_values (list[UserParameterValueCreate] | Unset):
        is_enabled (bool | Unset):  Default: True.
    """

    config_name: str
    user_api_key: None | str | Unset = UNSET
    user_endpoint_url: None | str | Unset = UNSET
    user_additional_headers: None | Unset | UserConfigCreateUserAdditionalHeadersType0 = UNSET
    custom_model_path: None | str | Unset = UNSET
    parameter_values: list[UserParameterValueCreate] | Unset = UNSET
    is_enabled: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_config_create_user_additional_headers_type_0 import (
            UserConfigCreateUserAdditionalHeadersType0,  # noqa: PLC0415
        )

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
        elif isinstance(self.user_additional_headers, UserConfigCreateUserAdditionalHeadersType0):
            user_additional_headers = self.user_additional_headers.to_dict()
        else:
            user_additional_headers = self.user_additional_headers

        custom_model_path: None | str | Unset
        if isinstance(self.custom_model_path, Unset):
            custom_model_path = UNSET
        else:
            custom_model_path = self.custom_model_path

        parameter_values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameter_values, Unset):
            parameter_values = []
            for parameter_values_item_data in self.parameter_values:
                parameter_values_item = parameter_values_item_data.to_dict()
                parameter_values.append(parameter_values_item)

        is_enabled = self.is_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config_name": config_name,
            }
        )
        if user_api_key is not UNSET:
            field_dict["user_api_key"] = user_api_key
        if user_endpoint_url is not UNSET:
            field_dict["user_endpoint_url"] = user_endpoint_url
        if user_additional_headers is not UNSET:
            field_dict["user_additional_headers"] = user_additional_headers
        if custom_model_path is not UNSET:
            field_dict["custom_model_path"] = custom_model_path
        if parameter_values is not UNSET:
            field_dict["parameter_values"] = parameter_values
        if is_enabled is not UNSET:
            field_dict["is_enabled"] = is_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_config_create_user_additional_headers_type_0 import (
            UserConfigCreateUserAdditionalHeadersType0,  # noqa: PLC0415
        )
        from ..models.user_parameter_value_create import UserParameterValueCreate  # noqa: PLC0415

        d = dict(src_dict)
        config_name = d.pop("config_name")

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

        def _parse_user_additional_headers(data: object) -> None | Unset | UserConfigCreateUserAdditionalHeadersType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_additional_headers_type_0 = UserConfigCreateUserAdditionalHeadersType0.from_dict(data)

                return user_additional_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserConfigCreateUserAdditionalHeadersType0, data)

        user_additional_headers = _parse_user_additional_headers(d.pop("user_additional_headers", UNSET))

        def _parse_custom_model_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_model_path = _parse_custom_model_path(d.pop("custom_model_path", UNSET))

        _parameter_values = d.pop("parameter_values", UNSET)
        parameter_values: list[UserParameterValueCreate] | Unset = UNSET
        if _parameter_values is not UNSET:
            parameter_values = []
            for parameter_values_item_data in _parameter_values:
                parameter_values_item = UserParameterValueCreate.from_dict(parameter_values_item_data)

                parameter_values.append(parameter_values_item)

        is_enabled = d.pop("is_enabled", UNSET)

        user_config_create = cls(
            config_name=config_name,
            user_api_key=user_api_key,
            user_endpoint_url=user_endpoint_url,
            user_additional_headers=user_additional_headers,
            custom_model_path=custom_model_path,
            parameter_values=parameter_values,
            is_enabled=is_enabled,
        )

        user_config_create.additional_properties = d
        return user_config_create

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
