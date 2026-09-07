from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_create_env_vars import ServiceCreateEnvVars


T = TypeVar("T", bound="ServiceCreate")


@_attrs_define
class ServiceCreate:
    """
    Attributes:
        name (str): Service name (e.g. mcp-calendar)
        image (str): Container image (e.g. ghcr.io/manavagi/mcp-calendar:latest)
        port (int): Container port
        replicas (int | Unset):  Default: 1.
        env_vars (ServiceCreateEnvVars | Unset):
        repo_url (None | str | Unset): GitHub repo URL for auto-deploy
        service_type (str | Unset): mcp | core | database | infra Default: 'mcp'.
        namespace (str | Unset):  Default: 'manav'.
    """

    name: str
    image: str
    port: int
    replicas: int | Unset = 1
    env_vars: ServiceCreateEnvVars | Unset = UNSET
    repo_url: None | str | Unset = UNSET
    service_type: str | Unset = "mcp"
    namespace: str | Unset = "manav"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        image = self.image

        port = self.port

        replicas = self.replicas

        env_vars: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        repo_url: None | str | Unset
        if isinstance(self.repo_url, Unset):
            repo_url = UNSET
        else:
            repo_url = self.repo_url

        service_type = self.service_type

        namespace = self.namespace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "image": image,
                "port": port,
            }
        )
        if replicas is not UNSET:
            field_dict["replicas"] = replicas
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if repo_url is not UNSET:
            field_dict["repo_url"] = repo_url
        if service_type is not UNSET:
            field_dict["service_type"] = service_type
        if namespace is not UNSET:
            field_dict["namespace"] = namespace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_create_env_vars import ServiceCreateEnvVars  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        image = d.pop("image")

        port = d.pop("port")

        replicas = d.pop("replicas", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: ServiceCreateEnvVars | Unset
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = ServiceCreateEnvVars.from_dict(_env_vars)

        def _parse_repo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repo_url = _parse_repo_url(d.pop("repo_url", UNSET))

        service_type = d.pop("service_type", UNSET)

        namespace = d.pop("namespace", UNSET)

        service_create = cls(
            name=name,
            image=image,
            port=port,
            replicas=replicas,
            env_vars=env_vars,
            repo_url=repo_url,
            service_type=service_type,
            namespace=namespace,
        )

        service_create.additional_properties = d
        return service_create

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
