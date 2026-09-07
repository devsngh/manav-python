from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkspaceUpdate")


@_attrs_define
class WorkspaceUpdate:
    """All fields optional — PATCH semantics.

    Attributes:
        name (None | str | Unset):
        domain (None | str | Unset):
        department (None | str | Unset):
        ingestion_bot_id (None | str | Unset):
        description (None | str | Unset):
        primary_entities (list[str] | None | Unset):
        primary_metrics (list[str] | None | Unset):
        primary_use_cases (list[str] | None | Unset):
        domain_tags (list[str] | None | Unset):
    """

    name: None | str | Unset = UNSET
    domain: None | str | Unset = UNSET
    department: None | str | Unset = UNSET
    ingestion_bot_id: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    primary_entities: list[str] | None | Unset = UNSET
    primary_metrics: list[str] | None | Unset = UNSET
    primary_use_cases: list[str] | None | Unset = UNSET
    domain_tags: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        domain: None | str | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        department: None | str | Unset
        if isinstance(self.department, Unset):
            department = UNSET
        else:
            department = self.department

        ingestion_bot_id: None | str | Unset
        if isinstance(self.ingestion_bot_id, Unset):
            ingestion_bot_id = UNSET
        else:
            ingestion_bot_id = self.ingestion_bot_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        primary_entities: list[str] | None | Unset
        if isinstance(self.primary_entities, Unset):
            primary_entities = UNSET
        elif isinstance(self.primary_entities, list):
            primary_entities = self.primary_entities

        else:
            primary_entities = self.primary_entities

        primary_metrics: list[str] | None | Unset
        if isinstance(self.primary_metrics, Unset):
            primary_metrics = UNSET
        elif isinstance(self.primary_metrics, list):
            primary_metrics = self.primary_metrics

        else:
            primary_metrics = self.primary_metrics

        primary_use_cases: list[str] | None | Unset
        if isinstance(self.primary_use_cases, Unset):
            primary_use_cases = UNSET
        elif isinstance(self.primary_use_cases, list):
            primary_use_cases = self.primary_use_cases

        else:
            primary_use_cases = self.primary_use_cases

        domain_tags: list[str] | None | Unset
        if isinstance(self.domain_tags, Unset):
            domain_tags = UNSET
        elif isinstance(self.domain_tags, list):
            domain_tags = self.domain_tags

        else:
            domain_tags = self.domain_tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if domain is not UNSET:
            field_dict["domain"] = domain
        if department is not UNSET:
            field_dict["department"] = department
        if ingestion_bot_id is not UNSET:
            field_dict["ingestion_bot_id"] = ingestion_bot_id
        if description is not UNSET:
            field_dict["description"] = description
        if primary_entities is not UNSET:
            field_dict["primary_entities"] = primary_entities
        if primary_metrics is not UNSET:
            field_dict["primary_metrics"] = primary_metrics
        if primary_use_cases is not UNSET:
            field_dict["primary_use_cases"] = primary_use_cases
        if domain_tags is not UNSET:
            field_dict["domain_tags"] = domain_tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain = _parse_domain(d.pop("domain", UNSET))

        def _parse_department(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        department = _parse_department(d.pop("department", UNSET))

        def _parse_ingestion_bot_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ingestion_bot_id = _parse_ingestion_bot_id(d.pop("ingestion_bot_id", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_primary_entities(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                primary_entities_type_0 = cast(list[str], data)

                return primary_entities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        primary_entities = _parse_primary_entities(d.pop("primary_entities", UNSET))

        def _parse_primary_metrics(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                primary_metrics_type_0 = cast(list[str], data)

                return primary_metrics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        primary_metrics = _parse_primary_metrics(d.pop("primary_metrics", UNSET))

        def _parse_primary_use_cases(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                primary_use_cases_type_0 = cast(list[str], data)

                return primary_use_cases_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        primary_use_cases = _parse_primary_use_cases(d.pop("primary_use_cases", UNSET))

        def _parse_domain_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                domain_tags_type_0 = cast(list[str], data)

                return domain_tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        domain_tags = _parse_domain_tags(d.pop("domain_tags", UNSET))

        workspace_update = cls(
            name=name,
            domain=domain,
            department=department,
            ingestion_bot_id=ingestion_bot_id,
            description=description,
            primary_entities=primary_entities,
            primary_metrics=primary_metrics,
            primary_use_cases=primary_use_cases,
            domain_tags=domain_tags,
        )

        workspace_update.additional_properties = d
        return workspace_update

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
