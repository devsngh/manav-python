from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CabinetTemplateCreate")


@_attrs_define
class CabinetTemplateCreate:
    """Body for `POST /api/cabinet/templates`.

    The route fills in `created_by_user_id` from the auth dependency and
    sets `source='ui'` (UI authoring) or `source='agent'` (when called via
    `cabinet_writer_mcp` — that path uses a different internal entrypoint).

        Attributes:
            bucket (str): One of CABINET_BUCKETS
            path (str): Filename within bucket — e.g. 'principal.yaml' or 'creative_specialist/persona.yaml'
            content (str): The raw YAML text
            agent_name (None | str | Unset):
            role (None | str | Unset):
            org_id (None | Unset | UUID): NULL = platform default; UUID = this org's override
            department_id (None | Unset | UUID): Used only for team_master to scope per department
            description (None | str | Unset):
    """

    bucket: str
    path: str
    content: str
    agent_name: None | str | Unset = UNSET
    role: None | str | Unset = UNSET
    org_id: None | Unset | UUID = UNSET
    department_id: None | Unset | UUID = UNSET
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket = self.bucket

        path = self.path

        content = self.content

        agent_name: None | str | Unset
        if isinstance(self.agent_name, Unset):
            agent_name = UNSET
        else:
            agent_name = self.agent_name

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        org_id: None | str | Unset
        if isinstance(self.org_id, Unset):
            org_id = UNSET
        elif isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

        department_id: None | str | Unset
        if isinstance(self.department_id, Unset):
            department_id = UNSET
        elif isinstance(self.department_id, UUID):
            department_id = str(self.department_id)
        else:
            department_id = self.department_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket": bucket,
                "path": path,
                "content": content,
            }
        )
        if agent_name is not UNSET:
            field_dict["agent_name"] = agent_name
        if role is not UNSET:
            field_dict["role"] = role
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if department_id is not UNSET:
            field_dict["department_id"] = department_id
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket = d.pop("bucket")

        path = d.pop("path")

        content = d.pop("content")

        def _parse_agent_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agent_name = _parse_agent_name(d.pop("agent_name", UNSET))

        def _parse_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role = _parse_role(d.pop("role", UNSET))

        def _parse_org_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                org_id_type_0 = UUID(data)

                return org_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        org_id = _parse_org_id(d.pop("org_id", UNSET))

        def _parse_department_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                department_id_type_0 = UUID(data)

                return department_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        department_id = _parse_department_id(d.pop("department_id", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        cabinet_template_create = cls(
            bucket=bucket,
            path=path,
            content=content,
            agent_name=agent_name,
            role=role,
            org_id=org_id,
            department_id=department_id,
            description=description,
        )

        cabinet_template_create.additional_properties = d
        return cabinet_template_create

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
