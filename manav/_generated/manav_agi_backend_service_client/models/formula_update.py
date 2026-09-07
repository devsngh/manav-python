from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.formula_update_api_config_type_0 import FormulaUpdateApiConfigType0
    from ..models.formula_update_input_schema_type_0 import FormulaUpdateInputSchemaType0
    from ..models.formula_update_output_schema_type_0 import FormulaUpdateOutputSchemaType0


T = TypeVar("T", bound="FormulaUpdate")


@_attrs_define
class FormulaUpdate:
    """
    Attributes:
        display_name (None | str | Unset):
        description (None | str | Unset):
        executor_type (None | str | Unset):
        module_ref (None | str | Unset):
        function_ref (None | str | Unset):
        sql_template (None | str | Unset):
        api_config (FormulaUpdateApiConfigType0 | None | Unset):
        input_schema (FormulaUpdateInputSchemaType0 | None | Unset):
        output_schema (FormulaUpdateOutputSchemaType0 | None | Unset):
        domain_tags (list[str] | None | Unset):
        category (None | str | Unset):
        is_active (bool | None | Unset):
        version (None | str | Unset):
    """

    display_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    executor_type: None | str | Unset = UNSET
    module_ref: None | str | Unset = UNSET
    function_ref: None | str | Unset = UNSET
    sql_template: None | str | Unset = UNSET
    api_config: FormulaUpdateApiConfigType0 | None | Unset = UNSET
    input_schema: FormulaUpdateInputSchemaType0 | None | Unset = UNSET
    output_schema: FormulaUpdateOutputSchemaType0 | None | Unset = UNSET
    domain_tags: list[str] | None | Unset = UNSET
    category: None | str | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    version: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.formula_update_api_config_type_0 import FormulaUpdateApiConfigType0  # noqa: PLC0415
        from ..models.formula_update_input_schema_type_0 import FormulaUpdateInputSchemaType0  # noqa: PLC0415
        from ..models.formula_update_output_schema_type_0 import FormulaUpdateOutputSchemaType0  # noqa: PLC0415

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        executor_type: None | str | Unset
        if isinstance(self.executor_type, Unset):
            executor_type = UNSET
        else:
            executor_type = self.executor_type

        module_ref: None | str | Unset
        if isinstance(self.module_ref, Unset):
            module_ref = UNSET
        else:
            module_ref = self.module_ref

        function_ref: None | str | Unset
        if isinstance(self.function_ref, Unset):
            function_ref = UNSET
        else:
            function_ref = self.function_ref

        sql_template: None | str | Unset
        if isinstance(self.sql_template, Unset):
            sql_template = UNSET
        else:
            sql_template = self.sql_template

        api_config: dict[str, Any] | None | Unset
        if isinstance(self.api_config, Unset):
            api_config = UNSET
        elif isinstance(self.api_config, FormulaUpdateApiConfigType0):
            api_config = self.api_config.to_dict()
        else:
            api_config = self.api_config

        input_schema: dict[str, Any] | None | Unset
        if isinstance(self.input_schema, Unset):
            input_schema = UNSET
        elif isinstance(self.input_schema, FormulaUpdateInputSchemaType0):
            input_schema = self.input_schema.to_dict()
        else:
            input_schema = self.input_schema

        output_schema: dict[str, Any] | None | Unset
        if isinstance(self.output_schema, Unset):
            output_schema = UNSET
        elif isinstance(self.output_schema, FormulaUpdateOutputSchemaType0):
            output_schema = self.output_schema.to_dict()
        else:
            output_schema = self.output_schema

        domain_tags: list[str] | None | Unset
        if isinstance(self.domain_tags, Unset):
            domain_tags = UNSET
        elif isinstance(self.domain_tags, list):
            domain_tags = self.domain_tags

        else:
            domain_tags = self.domain_tags

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if executor_type is not UNSET:
            field_dict["executor_type"] = executor_type
        if module_ref is not UNSET:
            field_dict["module_ref"] = module_ref
        if function_ref is not UNSET:
            field_dict["function_ref"] = function_ref
        if sql_template is not UNSET:
            field_dict["sql_template"] = sql_template
        if api_config is not UNSET:
            field_dict["api_config"] = api_config
        if input_schema is not UNSET:
            field_dict["input_schema"] = input_schema
        if output_schema is not UNSET:
            field_dict["output_schema"] = output_schema
        if domain_tags is not UNSET:
            field_dict["domain_tags"] = domain_tags
        if category is not UNSET:
            field_dict["category"] = category
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.formula_update_api_config_type_0 import FormulaUpdateApiConfigType0  # noqa: PLC0415
        from ..models.formula_update_input_schema_type_0 import FormulaUpdateInputSchemaType0  # noqa: PLC0415
        from ..models.formula_update_output_schema_type_0 import FormulaUpdateOutputSchemaType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_executor_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        executor_type = _parse_executor_type(d.pop("executor_type", UNSET))

        def _parse_module_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        module_ref = _parse_module_ref(d.pop("module_ref", UNSET))

        def _parse_function_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        function_ref = _parse_function_ref(d.pop("function_ref", UNSET))

        def _parse_sql_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sql_template = _parse_sql_template(d.pop("sql_template", UNSET))

        def _parse_api_config(data: object) -> FormulaUpdateApiConfigType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                api_config_type_0 = FormulaUpdateApiConfigType0.from_dict(data)

                return api_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FormulaUpdateApiConfigType0 | None | Unset, data)

        api_config = _parse_api_config(d.pop("api_config", UNSET))

        def _parse_input_schema(data: object) -> FormulaUpdateInputSchemaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_schema_type_0 = FormulaUpdateInputSchemaType0.from_dict(data)

                return input_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FormulaUpdateInputSchemaType0 | None | Unset, data)

        input_schema = _parse_input_schema(d.pop("input_schema", UNSET))

        def _parse_output_schema(data: object) -> FormulaUpdateOutputSchemaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                output_schema_type_0 = FormulaUpdateOutputSchemaType0.from_dict(data)

                return output_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FormulaUpdateOutputSchemaType0 | None | Unset, data)

        output_schema = _parse_output_schema(d.pop("output_schema", UNSET))

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

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        formula_update = cls(
            display_name=display_name,
            description=description,
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
            version=version,
        )

        formula_update.additional_properties = d
        return formula_update

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
