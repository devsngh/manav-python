from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.formula_search_response_input_schema_type_0 import FormulaSearchResponseInputSchemaType0


T = TypeVar("T", bound="FormulaSearchResponse")


@_attrs_define
class FormulaSearchResponse:
    """Lightweight response for search / discovery — no sql_template / api_config

    Attributes:
        id (UUID):
        name (str):
        display_name (str):
        description (None | str):
        version (str):
        executor_type (str):
        input_schema (FormulaSearchResponseInputSchemaType0 | None):
        domain_tags (list[str] | None):
        category (None | str):
        is_active (bool):
    """

    id: UUID
    name: str
    display_name: str
    description: None | str
    version: str
    executor_type: str
    input_schema: FormulaSearchResponseInputSchemaType0 | None
    domain_tags: list[str] | None
    category: None | str
    is_active: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.formula_search_response_input_schema_type_0 import (
            FormulaSearchResponseInputSchemaType0,  # noqa: PLC0415
        )

        id = str(self.id)

        name = self.name

        display_name = self.display_name

        description: None | str
        description = self.description

        version = self.version

        executor_type = self.executor_type

        input_schema: dict[str, Any] | None
        if isinstance(self.input_schema, FormulaSearchResponseInputSchemaType0):
            input_schema = self.input_schema.to_dict()
        else:
            input_schema = self.input_schema

        domain_tags: list[str] | None
        if isinstance(self.domain_tags, list):
            domain_tags = self.domain_tags

        else:
            domain_tags = self.domain_tags

        category: None | str
        category = self.category

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "display_name": display_name,
                "description": description,
                "version": version,
                "executor_type": executor_type,
                "input_schema": input_schema,
                "domain_tags": domain_tags,
                "category": category,
                "is_active": is_active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.formula_search_response_input_schema_type_0 import (
            FormulaSearchResponseInputSchemaType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        display_name = d.pop("display_name")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        version = d.pop("version")

        executor_type = d.pop("executor_type")

        def _parse_input_schema(data: object) -> FormulaSearchResponseInputSchemaType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_schema_type_0 = FormulaSearchResponseInputSchemaType0.from_dict(data)

                return input_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FormulaSearchResponseInputSchemaType0 | None, data)

        input_schema = _parse_input_schema(d.pop("input_schema"))

        def _parse_domain_tags(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                domain_tags_type_0 = cast(list[str], data)

                return domain_tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        domain_tags = _parse_domain_tags(d.pop("domain_tags"))

        def _parse_category(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        category = _parse_category(d.pop("category"))

        is_active = d.pop("is_active")

        formula_search_response = cls(
            id=id,
            name=name,
            display_name=display_name,
            description=description,
            version=version,
            executor_type=executor_type,
            input_schema=input_schema,
            domain_tags=domain_tags,
            category=category,
            is_active=is_active,
        )

        formula_search_response.additional_properties = d
        return formula_search_response

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
