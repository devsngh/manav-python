from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connect_request_config_parameters_type_0 import ConnectRequestConfigParametersType0
    from ..models.connect_request_credentials import ConnectRequestCredentials


T = TypeVar("T", bound="ConnectRequest")


@_attrs_define
class ConnectRequest:
    """
    Attributes:
        credentials (ConnectRequestCredentials): Key-value pairs of credentials
        config_parameters (ConnectRequestConfigParametersType0 | None | Unset): Key-value pairs of per-channel config
            parameters (from config_parameters_schema)
    """

    credentials: ConnectRequestCredentials
    config_parameters: ConnectRequestConfigParametersType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.connect_request_config_parameters_type_0 import (
            ConnectRequestConfigParametersType0,  # noqa: PLC0415
        )

        credentials = self.credentials.to_dict()

        config_parameters: dict[str, Any] | None | Unset
        if isinstance(self.config_parameters, Unset):
            config_parameters = UNSET
        elif isinstance(self.config_parameters, ConnectRequestConfigParametersType0):
            config_parameters = self.config_parameters.to_dict()
        else:
            config_parameters = self.config_parameters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentials": credentials,
            }
        )
        if config_parameters is not UNSET:
            field_dict["config_parameters"] = config_parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connect_request_config_parameters_type_0 import (
            ConnectRequestConfigParametersType0,  # noqa: PLC0415
        )
        from ..models.connect_request_credentials import ConnectRequestCredentials  # noqa: PLC0415

        d = dict(src_dict)
        credentials = ConnectRequestCredentials.from_dict(d.pop("credentials"))

        def _parse_config_parameters(data: object) -> ConnectRequestConfigParametersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_parameters_type_0 = ConnectRequestConfigParametersType0.from_dict(data)

                return config_parameters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConnectRequestConfigParametersType0 | None | Unset, data)

        config_parameters = _parse_config_parameters(d.pop("config_parameters", UNSET))

        connect_request = cls(
            credentials=credentials,
            config_parameters=config_parameters,
        )

        connect_request.additional_properties = d
        return connect_request

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
