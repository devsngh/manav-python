from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.env_var_update_env_vars import EnvVarUpdateEnvVars


T = TypeVar("T", bound="EnvVarUpdate")


@_attrs_define
class EnvVarUpdate:
    """
    Attributes:
        service_name (str):
        env_vars (EnvVarUpdateEnvVars):
    """

    service_name: str
    env_vars: EnvVarUpdateEnvVars
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_name = self.service_name

        env_vars = self.env_vars.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "service_name": service_name,
                "env_vars": env_vars,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.env_var_update_env_vars import EnvVarUpdateEnvVars  # noqa: PLC0415

        d = dict(src_dict)
        service_name = d.pop("service_name")

        env_vars = EnvVarUpdateEnvVars.from_dict(d.pop("env_vars"))

        env_var_update = cls(
            service_name=service_name,
            env_vars=env_vars,
        )

        env_var_update.additional_properties = d
        return env_var_update

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
