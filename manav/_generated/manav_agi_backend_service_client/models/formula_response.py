from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.formula_response_api_config_type_0 import FormulaResponseApiConfigType0
    from ..models.formula_response_input_schema_type_0 import FormulaResponseInputSchemaType0
    from ..models.formula_response_output_schema_type_0 import FormulaResponseOutputSchemaType0


T = TypeVar("T", bound="FormulaResponse")


@_attrs_define
class FormulaResponse:
    """
    Attributes:
        id (UUID):
        name (str):
        display_name (str):
        description (None | str):
        version (str):
        executor_type (str):
        module_ref (None | str):
        function_ref (None | str):
        sql_template (None | str):
        api_config (FormulaResponseApiConfigType0 | None):
        input_schema (FormulaResponseInputSchemaType0 | None):
        output_schema (FormulaResponseOutputSchemaType0 | None):
        domain_tags (list[str] | None):
        category (None | str):
        is_active (bool):
        created_by (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: UUID
    name: str
    display_name: str
    description: None | str
    version: str
    executor_type: str
    module_ref: None | str
    function_ref: None | str
    sql_template: None | str
    api_config: FormulaResponseApiConfigType0 | None
    input_schema: FormulaResponseInputSchemaType0 | None
    output_schema: FormulaResponseOutputSchemaType0 | None
    domain_tags: list[str] | None
    category: None | str
    is_active: bool
    created_by: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.formula_response_api_config_type_0 import FormulaResponseApiConfigType0  # noqa: PLC0415
        from ..models.formula_response_input_schema_type_0 import FormulaResponseInputSchemaType0  # noqa: PLC0415
        from ..models.formula_response_output_schema_type_0 import FormulaResponseOutputSchemaType0  # noqa: PLC0415

        id = str(self.id)

        name = self.name

        display_name = self.display_name

        description: None | str
        description = self.description

        version = self.version

        executor_type = self.executor_type

        module_ref: None | str
        module_ref = self.module_ref

        function_ref: None | str
        function_ref = self.function_ref

        sql_template: None | str
        sql_template = self.sql_template

        api_config: dict[str, Any] | None
        if isinstance(self.api_config, FormulaResponseApiConfigType0):
            api_config = self.api_config.to_dict()
        else:
            api_config = self.api_config

        input_schema: dict[str, Any] | None
        if isinstance(self.input_schema, FormulaResponseInputSchemaType0):
            input_schema = self.input_schema.to_dict()
        else:
            input_schema = self.input_schema

        output_schema: dict[str, Any] | None
        if isinstance(self.output_schema, FormulaResponseOutputSchemaType0):
            output_schema = self.output_schema.to_dict()
        else:
            output_schema = self.output_schema

        domain_tags: list[str] | None
        if isinstance(self.domain_tags, list):
            domain_tags = self.domain_tags

        else:
            domain_tags = self.domain_tags

        category: None | str
        category = self.category

        is_active = self.is_active

        created_by = str(self.created_by)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

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
                "module_ref": module_ref,
                "function_ref": function_ref,
                "sql_template": sql_template,
                "api_config": api_config,
                "input_schema": input_schema,
                "output_schema": output_schema,
                "domain_tags": domain_tags,
                "category": category,
                "is_active": is_active,
                "created_by": created_by,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.formula_response_api_config_type_0 import FormulaResponseApiConfigType0  # noqa: PLC0415
        from ..models.formula_response_input_schema_type_0 import FormulaResponseInputSchemaType0  # noqa: PLC0415
        from ..models.formula_response_output_schema_type_0 import FormulaResponseOutputSchemaType0  # noqa: PLC0415

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

        def _parse_module_ref(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        module_ref = _parse_module_ref(d.pop("module_ref"))

        def _parse_function_ref(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        function_ref = _parse_function_ref(d.pop("function_ref"))

        def _parse_sql_template(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sql_template = _parse_sql_template(d.pop("sql_template"))

        def _parse_api_config(data: object) -> FormulaResponseApiConfigType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                api_config_type_0 = FormulaResponseApiConfigType0.from_dict(data)

                return api_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FormulaResponseApiConfigType0 | None, data)

        api_config = _parse_api_config(d.pop("api_config"))

        def _parse_input_schema(data: object) -> FormulaResponseInputSchemaType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_schema_type_0 = FormulaResponseInputSchemaType0.from_dict(data)

                return input_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FormulaResponseInputSchemaType0 | None, data)

        input_schema = _parse_input_schema(d.pop("input_schema"))

        def _parse_output_schema(data: object) -> FormulaResponseOutputSchemaType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                output_schema_type_0 = FormulaResponseOutputSchemaType0.from_dict(data)

                return output_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FormulaResponseOutputSchemaType0 | None, data)

        output_schema = _parse_output_schema(d.pop("output_schema"))

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

        created_by = UUID(d.pop("created_by"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        formula_response = cls(
            id=id,
            name=name,
            display_name=display_name,
            description=description,
            version=version,
            executor_type=executor_type,
            module_ref=module_ref,
            function_ref=function_ref,
            sql_template=sql_template,
            api_config=api_config,
            input_schema=input_schema,
            output_schema=output_schema,
            domain_tags=domain_tags,
            category=category,
            is_active=is_active,
            created_by=created_by,
            created_at=created_at,
            updated_at=updated_at,
        )

        formula_response.additional_properties = d
        return formula_response

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
